MOUNTAIN_CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Libre+Baskerville:wght@400;700&display=swap');
:root{--burgundy:#842d45;--burgundy-dark:#602034;--teal:#147d7a;--teal-dark:#0f5e5c;--amber:#d89a2b;--paper:#fffdf8;--canvas:#f4efe6;--ink:#263442;--muted:#687481;--border:#ddd3c4;--green:#2d7d68;--red:#bd4b4b}
.stApp{background:radial-gradient(circle at 85% 0%,#fbf3df 0,transparent 27%),var(--canvas);color:var(--ink);font-family:'DM Sans',sans-serif}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
h1,h2,h3{font-family:'Libre Baskerville',Georgia,serif!important;color:var(--burgundy-dark)!important;letter-spacing:-.02em}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#74263d 0%,#552134 100%);border-right:0;box-shadow:8px 0 28px rgba(66,40,36,.12)}
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label,[data-testid="stSidebar"] p,[data-testid="stSidebar"] [data-testid="stWidgetLabel"] *{color:#fffaf2!important;opacity:1!important}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p{color:#ead9da!important;line-height:1.55}
[data-testid="stSidebar"] div[data-baseweb="select"]>div,[data-testid="stSidebar"] div[data-baseweb="input"]>div,[data-testid="stSidebar"] [data-testid="stNumberInput"]>div>div{background:#fffdf8!important;border-color:#eadfce!important;border-radius:8px!important}
[data-testid="stSidebar"] div[data-baseweb="select"] span,[data-testid="stSidebar"] div[data-baseweb="select"]>div *,[data-testid="stSidebar"] div[data-baseweb="select"] input,[data-testid="stSidebar"] div[data-baseweb="input"] input,[data-testid="stSidebar"] [data-testid="stNumberInput"] input{color:#3a2d33!important;-webkit-text-fill-color:#3a2d33!important;opacity:1!important;font-weight:650!important}
[data-testid="stSidebar"] div[data-baseweb="select"] svg{fill:#602034!important;color:#602034!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button{background:#fff8ed!important;border-color:#e2d1bc!important;color:#5b3541!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button *{color:#5b3541!important;opacity:1!important;font-weight:700!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button[aria-pressed="true"]{background:#edba58!important;border-color:#edba58!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button[aria-pressed="true"] *{color:#452231!important}
[data-testid="stSidebar"] [role="slider"]{background:#edba58!important}
.block-container{max-width:1280px;padding-top:1.15rem;padding-bottom:3rem}
.mp-header{background:linear-gradient(115deg,#70243b,#9a3650);border-bottom:4px solid #dca23a;padding:17px 24px;border-radius:12px 12px 0 0;display:flex;align-items:center;gap:15px;box-shadow:0 10px 26px rgba(96,32,52,.15)}
.mp-logo{font-size:34px;color:#f4c76d}.mp-name{font-weight:700;color:#fff;font-size:18px;letter-spacing:.045em}.mp-tag{color:#f1dfe3;font-size:12px;letter-spacing:.35px}
.mp-hero{background:linear-gradient(130deg,#fffdf8 0%,#fbf3e4 100%);border:1px solid var(--border);border-top:0;padding:32px 36px;margin:0 0 22px;border-radius:0 0 12px 12px;box-shadow:0 12px 35px rgba(71,52,40,.08)}
.eyebrow{display:inline-block;background:#e7b552;color:#4b2933;font-weight:800;font-size:11px;padding:5px 12px;border-radius:99px;letter-spacing:.11em}.mp-hero h1{font-size:2.35rem;margin:.9rem 0 .5rem}.mp-hero em{font-style:normal;color:var(--teal)}.mp-hero p{color:var(--muted);max-width:900px;font-size:1.02rem;line-height:1.65}
[data-testid="stMetric"]{background:var(--paper);border:1px solid var(--border);border-top:4px solid var(--teal);border-radius:10px;padding:15px;box-shadow:0 7px 20px rgba(72,54,45,.06)}
[data-testid="stMetricLabel"]{color:var(--muted)!important;font-weight:600}[data-testid="stMetricValue"]{color:var(--burgundy)!important;font-family:'Libre Baskerville',Georgia,serif}
[data-testid="stTabs"]{background:rgba(255,253,248,.62);border-radius:10px;padding:5px 8px 0}
[data-testid="stTabs"] button{color:#6b5660!important;font-weight:700;opacity:1!important}[data-testid="stTabs"] button *{color:inherit!important;opacity:1!important}[data-testid="stTabs"] button:hover{color:var(--teal)!important}[data-testid="stTabs"] button[aria-selected="true"]{color:var(--burgundy)!important;border-bottom-color:var(--burgundy)!important}
.stButton>button,.stDownloadButton>button{background:var(--teal);color:#fff;font-weight:800;border:0;border-radius:8px;box-shadow:0 5px 14px rgba(20,125,122,.2)}.stButton>button:hover,.stDownloadButton>button:hover{background:var(--teal-dark);color:#fff;border:0;box-shadow:0 7px 18px rgba(20,125,122,.28)}
div[data-testid="stExpander"]{background:var(--paper)!important;border:1px solid var(--border)!important;border-radius:10px;overflow:hidden;box-shadow:0 5px 16px rgba(72,54,45,.05)}
div[data-testid="stExpander"] details,div[data-testid="stExpander"] summary{background:var(--paper)!important;color:var(--ink)!important}
div[data-testid="stExpander"] summary:hover,div[data-testid="stExpander"] details[open]>summary{background:#f9f0e3!important;color:var(--burgundy)!important}
div[data-testid="stExpander"] summary *,div[data-testid="stExpander"] summary svg{color:inherit!important;fill:currentColor!important;opacity:1!important}
div[data-testid="stExpander"] [data-testid="stExpanderDetails"]{background:var(--paper)!important;color:var(--ink)!important;padding-top:.65rem}
div[data-testid="stExpander"] p,div[data-testid="stExpander"] li{color:var(--ink)!important;line-height:1.65!important}
[data-testid="stMain"] [data-testid="stMarkdownContainer"] p,[data-testid="stMain"] [data-testid="stMarkdownContainer"] li{color:var(--ink)}
[data-testid="stMain"] [data-testid="stCaptionContainer"] p{color:var(--muted)!important}
[data-testid="stAlert"]{border-radius:9px}[data-testid="stAlert"] p,[data-testid="stAlert"] li{color:inherit!important}
.insight{background:linear-gradient(115deg,#fffdf8,#f8f1e6);border:1px solid #d9cbb9;border-left:5px solid var(--amber);padding:16px 18px;border-radius:9px;color:var(--ink);box-shadow:0 5px 16px rgba(72,54,45,.05)}
.mp-footer{margin-top:30px;background:#354957;border-top:4px solid #dca23a;padding:22px 24px;border-radius:10px;color:#e9f0f1;font-size:12px;line-height:1.7}.mp-footer a{color:#f3c86f;text-decoration:none}.mp-footer small{color:#cbd6d9}
@media(max-width:720px){.mp-hero{padding:24px}.mp-hero h1{font-size:1.9rem}.block-container{padding-left:.8rem;padding-right:.8rem}}
</style>
"""
