MOUNTAIN_CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Libre+Baskerville:wght@400;700&display=swap');
:root{--navy:#12345b;--navy-dark:#082f5b;--blue:#244f83;--teal:#167c80;--teal-dark:#105f63;--yellow:#ffd400;--paper:#ffffff;--canvas:#f2f6fb;--ink:#22354b;--muted:#66778b;--border:#d5dfeb;--green:#2d7d68;--red:#bd4b4b}
.stApp{background:radial-gradient(circle at 88% 0%,#e8f0fb 0,transparent 28%),var(--canvas);color:var(--ink);font-family:'DM Sans',sans-serif}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
h1,h2,h3{font-family:'Libre Baskerville',Georgia,serif!important;color:var(--navy-dark)!important;letter-spacing:-.02em}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#123f70 0%,#0a3159 100%);border-right:0;box-shadow:8px 0 28px rgba(8,47,91,.14)}
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label,[data-testid="stSidebar"] p,[data-testid="stSidebar"] [data-testid="stWidgetLabel"] *{color:#fffaf2!important;opacity:1!important}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p{color:#c8d9ec!important;line-height:1.55}
[data-testid="stSidebar"] div[data-baseweb="select"]>div,[data-testid="stSidebar"] div[data-baseweb="input"]>div,[data-testid="stSidebar"] [data-testid="stNumberInput"]>div>div{background:#fffdf8!important;border-color:#eadfce!important;border-radius:8px!important}
[data-testid="stSidebar"] div[data-baseweb="select"] span,[data-testid="stSidebar"] div[data-baseweb="select"]>div *,[data-testid="stSidebar"] div[data-baseweb="select"] input,[data-testid="stSidebar"] div[data-baseweb="input"] input,[data-testid="stSidebar"] [data-testid="stNumberInput"] input{color:#173a62!important;-webkit-text-fill-color:#173a62!important;opacity:1!important;font-weight:650!important}
[data-testid="stSidebar"] div[data-baseweb="select"] svg{fill:#12345b!important;color:#12345b!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button{background:#f6f9fd!important;border-color:#c6d5e6!important;color:#173a62!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button *{color:#173a62!important;opacity:1!important;font-weight:700!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button[aria-pressed="true"]{background:#ffd400!important;border-color:#ffd400!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button[aria-pressed="true"] *{color:#082f5b!important}
[data-testid="stSidebar"] [role="slider"]{background:#ffd400!important}
[data-testid="stSidebar"] div[data-baseweb="tag"]{background:#28649b!important;border:1px solid #78a8d4!important}
[data-testid="stSidebar"] div[data-baseweb="tag"] span,[data-testid="stSidebar"] div[data-baseweb="tag"] svg{color:#ffffff!important;fill:#ffffff!important}
.block-container{max-width:1280px;padding-top:1.15rem;padding-bottom:3rem}
.mp-header{background:linear-gradient(115deg,#082f5b,#184d82);border-bottom:4px solid #ffd400;padding:17px 24px;border-radius:12px 12px 0 0;display:flex;align-items:center;gap:15px;box-shadow:0 10px 26px rgba(8,47,91,.16)}
.mp-logo{font-size:34px;color:#ffd400}.mp-name{font-weight:700;color:#fff;font-size:18px;letter-spacing:.045em}.mp-tag{color:#cfe2f5;font-size:12px;letter-spacing:.35px}
.mp-hero{background:linear-gradient(130deg,#ffffff 0%,#edf4fc 100%);border:1px solid var(--border);border-top:0;padding:32px 36px;margin:0 0 22px;border-radius:0 0 12px 12px;box-shadow:0 12px 35px rgba(8,47,91,.08)}
.eyebrow{display:inline-block;background:#ffd400;color:#082f5b;font-weight:800;font-size:11px;padding:5px 12px;border-radius:99px;letter-spacing:.11em}.mp-hero h1{font-size:2.35rem;margin:.9rem 0 .5rem}.mp-hero em{font-style:normal;color:var(--blue)}.mp-hero p{color:var(--muted);max-width:900px;font-size:1.02rem;line-height:1.65}
[data-testid="stMetric"]{background:var(--paper);border:1px solid var(--border);border-top:4px solid var(--blue);border-radius:10px;padding:15px;box-shadow:0 7px 20px rgba(8,47,91,.06)}
[data-testid="stMetricLabel"]{color:var(--muted)!important;font-weight:600}[data-testid="stMetricValue"]{color:var(--navy)!important;font-family:'Libre Baskerville',Georgia,serif}
[data-testid="stTabs"]{background:#ffffff;border:1px solid #cfdae7;border-radius:12px;padding:10px 10px 0;box-shadow:0 8px 24px rgba(8,47,91,.07)}
[data-testid="stTabs"] [role="tablist"]{gap:8px!important;overflow-x:auto!important;padding:2px 2px 10px!important;border-bottom:0!important;scrollbar-width:thin}
[data-testid="stTabs"] button[role="tab"]{background:linear-gradient(145deg,#164a7b,#0c3763)!important;color:#ffffff!important;border:2px solid #285f91!important;border-radius:9px!important;min-height:48px!important;padding:10px 15px!important;font-size:.92rem!important;font-weight:800!important;letter-spacing:.01em!important;white-space:nowrap!important;opacity:1!important;box-shadow:0 4px 10px rgba(8,47,91,.16)!important;transition:transform .15s ease,box-shadow .15s ease,background .15s ease!important}
[data-testid="stTabs"] button[role="tab"] *{color:#ffffff!important;opacity:1!important;font-weight:800!important}
[data-testid="stTabs"] button[role="tab"]:hover{background:linear-gradient(145deg,#21639a,#164a7b)!important;border-color:#75a9d7!important;transform:translateY(-2px);box-shadow:0 7px 15px rgba(8,47,91,.22)!important}
[data-testid="stTabs"] button[role="tab"][aria-selected="true"]{background:#ffd400!important;color:#082f5b!important;border-color:#e4b900!important;box-shadow:0 5px 14px rgba(255,212,0,.28)!important}
[data-testid="stTabs"] button[role="tab"][aria-selected="true"] *{color:#082f5b!important;font-weight:900!important}
[data-testid="stTabs"] [data-baseweb="tab-highlight"]{display:none!important}
.stButton>button,.stDownloadButton>button,[data-testid="stBaseButton-primary"]{background:#ffd400!important;color:#082f5b!important;font-weight:800!important;border:0!important;border-radius:8px!important;box-shadow:0 5px 14px rgba(255,212,0,.22)!important}.stButton>button:hover,.stDownloadButton>button:hover,[data-testid="stBaseButton-primary"]:hover{background:#f2c900!important;color:#082f5b!important;border:0!important;box-shadow:0 7px 18px rgba(255,212,0,.3)!important}
div[data-testid="stExpander"]{background:var(--paper)!important;border:1px solid var(--border)!important;border-radius:10px;overflow:hidden;box-shadow:0 5px 16px rgba(72,54,45,.05)}
div[data-testid="stExpander"] details,div[data-testid="stExpander"] summary{background:var(--paper)!important;color:var(--ink)!important}
div[data-testid="stExpander"] summary:hover,div[data-testid="stExpander"] details[open]>summary{background:#eaf2fb!important;color:var(--navy)!important}
div[data-testid="stExpander"] summary *,div[data-testid="stExpander"] summary svg{color:inherit!important;fill:currentColor!important;opacity:1!important}
div[data-testid="stExpander"] [data-testid="stExpanderDetails"]{background:var(--paper)!important;color:var(--ink)!important;padding-top:.65rem}
div[data-testid="stExpander"] p,div[data-testid="stExpander"] li{color:var(--ink)!important;line-height:1.65!important}
[data-testid="stMain"] [data-testid="stMarkdownContainer"] p,[data-testid="stMain"] [data-testid="stMarkdownContainer"] li{color:var(--ink)}
[data-testid="stMain"] [data-testid="stCaptionContainer"] p{color:var(--muted)!important}
[data-testid="stAlert"]{border-radius:9px}[data-testid="stAlert"] p,[data-testid="stAlert"] li{color:inherit!important}
.insight{background:linear-gradient(115deg,#ffffff,#edf4fc);border:1px solid #cad9e9;border-left:5px solid #ffd400;padding:16px 18px;border-radius:9px;color:var(--ink);box-shadow:0 5px 16px rgba(8,47,91,.05)}
.mp-footer{margin-top:30px;background:#082f5b;border-top:4px solid #ffd400;padding:22px 24px;border-radius:10px;color:#e9f2fb;font-size:12px;line-height:1.7}.mp-footer a{color:#ffd400;text-decoration:none}.mp-footer small{color:#c5d7e8}
@media(max-width:720px){.mp-hero{padding:24px}.mp-hero h1{font-size:1.9rem}.block-container{padding-left:.8rem;padding-right:.8rem}}
</style>
"""
