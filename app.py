from __future__ import annotations

from io import BytesIO
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
import streamlit as st

from data_service import ALL_ASSETS, HISTORY_WINDOWS, MARKET_UNIVERSES, download_prices, prepare_returns
from style import MOUNTAIN_CSS


st.set_page_config(page_title="Volatility Characteristics Laboratory", page_icon="▲", layout="wide")
st.markdown(MOUNTAIN_CSS, unsafe_allow_html=True)

GOLD, BLUE, SKY, GREEN, RED, MUTED = "#FFD700", "#1a4480", "#ADD8E6", "#35c96f", "#ff4b5c", "#b8c7dc"
PLOT = dict(
    paper_bgcolor="#112240", plot_bgcolor="#112240", font_color="#e6f1ff",
    font_family="Source Sans 3", margin=dict(l=40, r=24, t=60, b=40),
    xaxis=dict(gridcolor="rgba(136,146,176,.15)"),
    yaxis=dict(gridcolor="rgba(136,146,176,.15)"),
    hoverlabel=dict(bgcolor="#0a192f"),
)


@st.cache_data(ttl=3600, show_spinner=False)
def cached_prices(ticker: str, years: int | None):
    return download_prices(ticker, years)


def acf(values, max_lag=30):
    x = np.asarray(pd.Series(values).dropna(), dtype=float)
    x = x - x.mean()
    denom = np.dot(x, x)
    return np.array([np.dot(x[k:], x[:-k]) / denom for k in range(1, min(max_lag, len(x) - 2) + 1)])


def annual_factor(frequency):
    return {"Daily": 252, "Weekly": 52, "Monthly": 12}[frequency]


def realised_vol(returns, window, factor):
    return returns.rolling(window).std() * np.sqrt(factor)


def metric_table(series, factor):
    rows = []
    for name in series:
        r = series[name].dropna()
        if len(r) < 30:
            continue
        rows.append({
            "Market": name, "Observations": len(r), "Annualised volatility (%)": r.std() * np.sqrt(factor),
            "Skewness": stats.skew(r, bias=False), "Excess kurtosis": stats.kurtosis(r, fisher=True, bias=False),
            "Worst return (%)": r.min(), "Best return (%)": r.max(),
            "Tail events > 3σ": int((np.abs((r-r.mean())/r.std()) > 3).sum()),
        })
    return pd.DataFrame(rows)


def callout(title, body):
    st.markdown(f'<div class="insight"><b style="color:{GOLD}">{title}</b><br>{body}</div>', unsafe_allow_html=True)


st.markdown('''
<div class="mp-header"><div class="mp-logo">▲</div><div><div class="mp-name">THE MOUNTAIN PATH ACADEMY</div>
<div class="mp-tag">Finance · Risk · Analytics — Practitioner-led education</div></div></div>
<div class="mp-hero"><span class="eyebrow">MARKET VOLATILITY LEARNING LAB</span>
<h1>Volatility has <em>character</em></h1>
<p>Explore the empirical features of volatility using up to 20 years of actual global index, currency,
commodity, rate and risk-market data. Each tab turns one important volatility characteristic into an observable fact.</p></div>
''', unsafe_allow_html=True)

with st.sidebar:
    st.header("Data laboratory")
    universe = st.selectbox("Primary market group", list(MARKET_UNIVERSES))
    primary = st.selectbox("Primary instrument", list(MARKET_UNIVERSES[universe]))
    history_label = st.segmented_control("History requested", list(HISTORY_WINDOWS), default="20 Years")
    frequency = st.selectbox("Return frequency", ["Daily", "Weekly", "Monthly"])
    rolling = st.slider("Rolling window", 10, 126, 21, help="21 daily observations are approximately one trading month.")
    comparison_defaults = ["S&P 500", "NIFTY 50", "EUR/USD", "Gold", "WTI Crude", "CBOE VIX"]
    comparisons = st.multiselect("Cross-market comparison", list(ALL_ASSETS),
                                 default=[x for x in comparison_defaults if x != primary], max_selections=7)
    run = st.button("Build volatility laboratory", type="primary", width="stretch")
    st.caption("Market information is downloaded from a public data interface and may be delayed. Long histories differ by instrument.")

if "run_lab" not in st.session_state:
    st.session_state.run_lab = False
if run:
    st.session_state.run_lab = True
if not st.session_state.run_lab:
    st.info("Select a primary market and choose **Build volatility laboratory**.")
    st.stop()

years = HISTORY_WINDOWS[history_label]
selected = list(dict.fromkeys([primary] + comparisons))
closes, returns_map, failures = {}, {}, {}
with st.spinner(f"Building {history_label.lower()} of market evidence across {len(selected)} instruments…"):
    for name in selected:
        try:
            px = cached_prices(ALL_ASSETS[name], years)
            c, r = prepare_returns(px, frequency)
            if len(r) < 60:
                raise ValueError(f"only {len(r)} usable returns")
            closes[name], returns_map[name] = c, r
        except Exception as exc:
            failures[name] = str(exc)

if primary not in returns_map:
    st.error(f"The primary series could not be loaded: {failures.get(primary, 'unknown data error')}")
    st.stop()

returns_df = pd.concat(returns_map, axis=1).sort_index()
close_df = pd.concat(closes, axis=1).sort_index()
r = returns_map[primary]
c = closes[primary]
factor = annual_factor(frequency)
rv = realised_vol(r, rolling, factor)
requested = history_label.lower()
available_years = (r.index.max() - r.index.min()).days / 365.25

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Actual history", f"{available_years:.1f} years", help=f"Requested: {requested}")
m2.metric("Observations", f"{len(r):,}")
m3.metric("Annualised volatility", f"{r.std()*np.sqrt(factor):.2f}%")
m4.metric("Excess kurtosis", f"{stats.kurtosis(r, fisher=True, bias=False):.2f}")
m5.metric("Largest absolute move", f"{r.abs().max():.2f}%")
st.caption(f"{primary} · {r.index.min():%d %b %Y} to {r.index.max():%d %b %Y} · {frequency.lower()} log returns · Requested {requested}")
if failures:
    st.warning("Some comparison series were unavailable: " + "; ".join(f"{k} ({v})" for k, v in failures.items()))

tabs = st.tabs([
    "1 · Time Variation", "2 · Clustering", "3 · Persistence", "4 · Mean Reversion",
    "5 · Fat Tails", "6 · Asymmetry", "7 · Cross-Market Dynamics"
])

with tabs[0]:
    st.subheader("Volatility is not constant")
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=.055,
                        row_heights=[.38, .27, .35], subplot_titles=("Market level", "Log returns (%)", f"Rolling {rolling}-period annualised volatility"))
    fig.add_trace(go.Scatter(x=c.index, y=c, line=dict(color=GOLD, width=2), name="Level"), 1, 1)
    fig.add_trace(go.Bar(x=r.index, y=r, marker_color=np.where(r >= 0, GREEN, RED), name="Return"), 2, 1)
    fig.add_trace(go.Scatter(x=rv.index, y=rv, fill="tozeroy", line=dict(color=SKY, width=2), name="Realised volatility"), 3, 1)
    fig.update_layout(height=800, hovermode="x unified", showlegend=False, **PLOT)
    st.plotly_chart(fig, width="stretch")
    q10, q90 = rv.quantile([.1, .9])
    callout("Evidence in this sample", f"Rolling volatility ranges from {rv.min():.1f}% to {rv.max():.1f}%. The calm/turbulent 10th and 90th-percentile thresholds are {q10:.1f}% and {q90:.1f}%—a single constant volatility number hides this variation.")
    st.latex(r"\widehat\sigma_{t,m}=\sqrt{A}\;\operatorname{StdDev}(r_{t-m+1},\ldots,r_t)")

with tabs[1]:
    st.subheader("Volatility clustering: large moves follow large moves")
    abs_acf, sq_acf = acf(r.abs()), acf(r**2)
    lags = np.arange(1, len(abs_acf)+1)
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Absolute returns through time", "Dependence in squared returns"))
    fig.add_trace(go.Scatter(x=r.index, y=r.abs(), line=dict(color=GOLD, width=1), name="|return|"), 1, 1)
    fig.add_trace(go.Bar(x=lags, y=sq_acf, marker_color=np.where(sq_acf >= 0, SKY, RED), name="ACF"), 1, 2)
    bound = 1.96 / np.sqrt(len(r))
    fig.add_hline(y=bound, line_dash="dash", line_color=MUTED, row=1, col=2)
    fig.add_hline(y=-bound, line_dash="dash", line_color=MUTED, row=1, col=2)
    fig.update_layout(height=470, showlegend=False, **PLOT)
    fig.update_xaxes(title_text="Lag", row=1, col=2); fig.update_yaxes(title_text="Autocorrelation", row=1, col=2)
    st.plotly_chart(fig, width="stretch")
    callout("How to read it", f"Lag-1 autocorrelation of squared returns is {sq_acf[0]:.3f}. Bars beyond ±{bound:.3f} indicate statistically visible clustering: the size of yesterday's move contains information about future risk.")
    st.latex(r"\operatorname{Corr}(r_t^2,r_{t-k}^2)>0\quad\text{for several lags }k")

with tabs[2]:
    st.subheader("Persistence: volatility shocks decay slowly")
    max_lag = min(60, max(10, len(r)//20))
    a = acf(r**2, max_lag)
    positive = np.clip(a, 1e-6, None)
    valid = np.where(a > 0)[0]
    decay = np.nan
    if len(valid) >= 5:
        slope = np.polyfit(valid[:min(20, len(valid))] + 1, np.log(positive[valid[:min(20, len(valid))]]), 1)[0]
        decay = -np.log(2)/slope if slope < 0 else np.nan
    fig = go.Figure(go.Bar(x=np.arange(1, len(a)+1), y=a, marker_color=GOLD))
    fig.update_layout(title="Squared-return autocorrelation decay", height=430, xaxis_title="Lag", yaxis_title="Autocorrelation", **PLOT)
    st.plotly_chart(fig, width="stretch")
    c1, c2, c3 = st.columns(3)
    c1.metric("Lag-1 dependence", f"{a[0]:.3f}")
    c2.metric("Sum of first 20 ACFs", f"{a[:20].sum():.2f}")
    c3.metric("Indicative half-life", f"{decay:.1f} periods" if np.isfinite(decay) else "Not stable")
    callout("Economic meaning", "Persistence does not mean returns are predictable. It means the magnitude of risk changes gradually, so a crisis can influence risk estimates long after the original price shock.")

with tabs[3]:
    st.subheader("Mean reversion: turbulent and calm regimes do not last forever")
    long_run = r.std()*np.sqrt(factor)
    smooth = rv.ewm(span=max(rolling, 20), min_periods=rolling).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=rv.index, y=rv, name="Rolling volatility", line=dict(color=SKY, width=1.5)))
    fig.add_trace(go.Scatter(x=smooth.index, y=smooth, name="Smoothed path", line=dict(color=GOLD, width=3)))
    fig.add_hline(y=long_run, line_dash="dash", line_color=GREEN, annotation_text="Full-sample anchor")
    fig.update_layout(title="Volatility moves around a long-run anchor", height=480, yaxis_title="Annualised volatility (%)", **PLOT)
    st.plotly_chart(fig, width="stretch")
    high = rv > rv.quantile(.9)
    episodes = []
    for dt in rv[high].index:
        future = rv.loc[dt:].iloc[1:1+max(rolling*4, 20)]
        hit = future[future <= long_run]
        if len(hit): episodes.append((hit.index[0]-dt).days)
    median_days = np.median(episodes) if episodes else np.nan
    callout("Sample evidence", f"The long-run volatility anchor is {long_run:.1f}%. After top-decile volatility observations, the median observed calendar time to return below that anchor is {median_days:.0f} days." if np.isfinite(median_days) else "The selected sample does not contain enough completed high-volatility episodes for a stable reversion estimate.")

with tabs[4]:
    st.subheader("Fat tails: extreme returns occur too often for a Normal curve")
    z = (r-r.mean())/r.std()
    x = np.linspace(-5, 5, 400)
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Standardised return distribution", "Normal Q–Q plot"))
    fig.add_trace(go.Histogram(x=z, histnorm="probability density", nbinsx=70, marker_color=GOLD, opacity=.75, name="Observed"), 1, 1)
    fig.add_trace(go.Scatter(x=x, y=stats.norm.pdf(x), line=dict(color=SKY, width=3), name="Normal"), 1, 1)
    osm, osr = stats.probplot(z, dist="norm", fit=False)
    fig.add_trace(go.Scatter(x=osm, y=osr, mode="markers", marker=dict(color=GOLD, size=4), name="Observed quantiles"), 1, 2)
    lo, hi = min(osm), max(osm)
    fig.add_trace(go.Scatter(x=[lo,hi], y=[lo,hi], line=dict(color=SKY, dash="dash"), name="Normal line"), 1, 2)
    fig.update_layout(height=480, **PLOT)
    st.plotly_chart(fig, width="stretch")
    actual = int((z.abs() > 3).sum()); expected = len(z)*2*(1-stats.norm.cdf(3))
    c1,c2,c3=st.columns(3); c1.metric("Skewness",f"{stats.skew(r,bias=False):.2f}"); c2.metric("Excess kurtosis",f"{stats.kurtosis(r,fisher=True,bias=False):.2f}"); c3.metric("Observed > |3σ|",f"{actual} vs {expected:.1f} Normal")
    callout("Risk implication", "When tails are fat, Normal-distribution VaR and confidence intervals can understate the frequency of extreme outcomes. The Q–Q plot makes the tail departure visible.")

with tabs[5]:
    st.subheader("Asymmetry: downside shocks can carry a different volatility response")
    next_abs = r.abs().shift(-1)
    bins = pd.qcut(r.abs(), 5, duplicates="drop")
    asym = pd.DataFrame({"shock":r,"next_abs":next_abs,"bin":bins}).dropna()
    grp = asym.groupby(["bin", asym.shock.lt(0)], observed=True).next_abs.mean().unstack()
    labels=[f"Q{i+1}" for i in range(len(grp))]
    fig=go.Figure()
    fig.add_trace(go.Bar(x=labels,y=grp.get(False),name="After positive shock",marker_color=GREEN))
    fig.add_trace(go.Bar(x=labels,y=grp.get(True),name="After negative shock",marker_color=RED))
    fig.update_layout(title="Average next-period absolute return by prior-shock size",barmode="group",height=450,xaxis_title="Prior absolute-return quintile",yaxis_title="Next absolute return (%)",**PLOT)
    st.plotly_chart(fig,width="stretch")
    neg=next_abs[r<0].mean(); pos=next_abs[r>=0].mean(); ratio=neg/pos if pos else np.nan
    callout("Evidence in this sample",f"The next-period absolute move averages {neg:.3f}% after negative returns and {pos:.3f}% after positive returns—a downside/upside response ratio of {ratio:.2f}×. This unconditional comparison is descriptive, not a causal test.")

with tabs[6]:
    st.subheader("Cross-market dynamics: volatility can move together")
    if returns_df.shape[1] < 2:
        st.info("Select at least one comparison market in the sidebar.")
    else:
        common = returns_df.dropna(how="all")
        vol_panel = common.rolling(rolling).std()*np.sqrt(factor)
        norm_vol = vol_panel.divide(vol_panel.median())
        fig=go.Figure()
        palette=[GOLD,SKY,GREEN,RED,"#c792ea","#ff9f43","#4dd0e1","#f78fb3"]
        for i,name in enumerate(norm_vol):
            fig.add_trace(go.Scatter(x=norm_vol.index,y=norm_vol[name],name=name,line=dict(color=palette[i%len(palette)],width=2 if name==primary else 1.35)))
        fig.add_hline(y=1,line_dash="dash",line_color=MUTED)
        fig.update_layout(title="Rolling volatility relative to each market's median",height=500,yaxis_title="Volatility / own median",hovermode="x unified",**PLOT)
        st.plotly_chart(fig,width="stretch")
        corr=common.corr(min_periods=60)
        heat=go.Figure(go.Heatmap(z=corr.values,x=corr.columns,y=corr.index,zmin=-1,zmax=1,zmid=0,colorscale=[[0,"#e41d3d"],[.5,"#f4f6fa"],[1,"#1a4480"]],text=np.round(corr.values,2),texttemplate="%{text}"))
        heat.update_layout(title="Full-sample return correlation",height=max(430,70*len(corr)),**PLOT)
        st.plotly_chart(heat,width="stretch")
        st.dataframe(metric_table(common,factor).style.format({"Annualised volatility (%)":"{:.2f}","Skewness":"{:.2f}","Excess kurtosis":"{:.2f}","Worst return (%)":"{:.2f}","Best return (%)":"{:.2f}"}),hide_index=True,width="stretch")
        callout("Teaching point","Volatility co-movement and return correlation answer different questions. Markets may become turbulent together even when the directions of their returns differ.")

with st.expander("Definitions, formulas and interpretation guide", expanded=False):
    st.markdown("""
    **Return:** continuously compounded percentage change, `100 × ln(Pₜ/Pₜ₋₁)`.  
    **Realised volatility:** rolling sample standard deviation of returns, annualised by √252, √52 or √12.  
    **Clustering:** serial dependence in absolute or squared returns.  
    **Persistence:** slow decay of that dependence after a volatility shock.  
    **Mean reversion:** movement of volatility toward a long-run range after unusually calm or turbulent periods.  
    **Fat tails:** more extreme standardised returns than predicted by the Normal distribution.  
    **Asymmetry:** different subsequent volatility following negative and positive returns.  
    **Cross-market dynamics:** co-movement in return direction, volatility level or both.
    """)


def build_download():
    out=BytesIO()
    with pd.ExcelWriter(out,engine="xlsxwriter") as writer:
        close_df.to_excel(writer,sheet_name="Market Levels")
        returns_df.to_excel(writer,sheet_name="Log Returns")
        metric_table(returns_df,factor).to_excel(writer,sheet_name="Summary Statistics",index=False)
        wb=writer.book
        for ws in writer.sheets.values():
            ws.freeze_panes(1,1); ws.set_column(0,0,14); ws.set_column(1,20,18)
            ws.set_row(0,22,wb.add_format({"bold":True,"bg_color":"#1A4480","font_color":"#FFFFFF"}))
    return out.getvalue()

st.download_button("Download the market evidence workbook",build_download(),"Volatility_Characteristics_Laboratory.xlsx","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",width="stretch")
st.markdown('''<div class="mp-footer"><b>The Mountain Path Academy</b> · Finance · Risk · Analytics<br>
Prof. V. Ravichandran · <a href="https://themountainpathacademy.com">Website</a> ·
<a href="https://www.linkedin.com/in/trichyravis">LinkedIn</a><br>
<small>Educational use only. Data may be delayed, revised or unavailable and must not be treated as investment advice.</small></div>''',unsafe_allow_html=True)
