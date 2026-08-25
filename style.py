MOUNTAIN_CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;800&family=Source+Sans+3:wght@300;400;500;600;700&display=swap');
:root{--gold:#FFD700;--blue:#003366;--mid:#004d80;--card:#112240;--bg:#0a192f;--txt:#f4f8ff;--muted:#b8c7dc;--green:#35c96f;--red:#ff4b5c;--border:rgba(255,215,0,.18)}
.stApp{background:var(--bg);color:var(--txt);font-family:'Source Sans 3',sans-serif}
html,body,[class*="css"]{font-family:'Source Sans 3',sans-serif}
h1,h2,h3{font-family:'Playfair Display',Georgia,serif!important;color:var(--txt)!important}
[data-testid="stSidebar"]{background:#0d2040;border-right:1px solid var(--border)}
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label,[data-testid="stSidebar"] p,
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] *{color:var(--txt)!important;opacity:1!important}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p{color:var(--muted)!important;line-height:1.55}
/* White sidebar controls require dark text; generic sidebar-wide white text made them unreadable. */
[data-testid="stSidebar"] div[data-baseweb="select"]>div,
[data-testid="stSidebar"] div[data-baseweb="input"]>div,
[data-testid="stSidebar"] [data-testid="stNumberInput"]>div>div{background:#f8fbff!important;border-color:#d6e1ef!important}
[data-testid="stSidebar"] div[data-baseweb="select"] span,
[data-testid="stSidebar"] div[data-baseweb="select"]>div *,
[data-testid="stSidebar"] div[data-baseweb="select"] input,
[data-testid="stSidebar"] div[data-baseweb="input"] input,
[data-testid="stSidebar"] [data-testid="stNumberInput"] input{color:#0a2445!important;-webkit-text-fill-color:#0a2445!important;opacity:1!important;font-weight:650!important}
[data-testid="stSidebar"] div[data-baseweb="select"] svg,
[data-testid="stSidebar"] [data-testid="stNumberInput"] button svg{fill:#0a2445!important;color:#0a2445!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button{background:#f3f7fc!important;border-color:#c9d5e5!important;color:#17385f!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button *{color:#17385f!important;opacity:1!important;font-weight:700!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button[aria-pressed="true"]{background:#FFD700!important;border-color:#FFD700!important}
[data-testid="stSidebar"] [data-testid="stSegmentedControl"] button[aria-pressed="true"] *{color:#0a192f!important}
[data-testid="stSidebar"] [data-testid="stRadio"] label *{color:var(--txt)!important;opacity:1!important}
[data-testid="stSidebar"] [role="slider"]{background:#ff4b5c!important}
.block-container{max-width:1240px;padding-top:1.1rem;padding-bottom:3rem}
.mp-header{background:#1a4480;border-bottom:3px solid #e41d3d;padding:15px 22px;border-radius:6px 6px 0 0;display:flex;align-items:center;gap:14px}
.mp-logo{font-size:32px;color:white}.mp-name{font-weight:700;color:white;font-size:18px}.mp-tag{color:#cfe8ff;font-size:12px;letter-spacing:.4px}
.mp-hero{background:var(--card);border:1px solid var(--border);padding:28px 32px;margin:0 0 18px;border-radius:0 0 6px 6px}
.eyebrow{display:inline-block;background:var(--gold);color:var(--bg);font-weight:800;font-size:12px;padding:4px 12px;border-radius:3px;letter-spacing:.08em}.mp-hero h1{font-size:2.25rem;margin:.8rem 0 .4rem}.mp-hero em{font-style:normal;color:var(--gold)}.mp-hero p{color:var(--muted);max-width:850px}
[data-testid="stMetric"]{background:var(--card);border:1px solid var(--border);border-radius:6px;padding:14px}[data-testid="stMetricLabel"]{color:var(--muted)}[data-testid="stMetricValue"]{color:var(--gold);font-family:'Playfair Display'}
[data-testid="stTabs"] button{color:var(--muted)!important;font-weight:700;opacity:1!important}[data-testid="stTabs"] button *{color:inherit!important;opacity:1!important}[data-testid="stTabs"] button:hover{color:#fff!important}[data-testid="stTabs"] button[aria-selected="true"]{color:var(--gold)!important;border-bottom-color:var(--gold)}
.stButton>button,.stDownloadButton>button{background:var(--gold);color:var(--bg);font-weight:800;border:0;border-radius:6px}.stButton>button:hover,.stDownloadButton>button:hover{color:var(--bg);border:0;box-shadow:0 4px 14px rgba(255,215,0,.25)}
/* Keep expander headers dark and readable in closed, open, focus and hover states. */
div[data-testid="stExpander"]{background:var(--card)!important;border:1px solid rgba(255,215,0,.22)!important;border-radius:6px;overflow:hidden}
div[data-testid="stExpander"] details,div[data-testid="stExpander"] summary{background:var(--card)!important;color:var(--txt)!important}
div[data-testid="stExpander"] summary:hover,div[data-testid="stExpander"] details[open]>summary{background:#173158!important;color:var(--gold)!important}
div[data-testid="stExpander"] summary *,div[data-testid="stExpander"] summary svg{color:inherit!important;fill:currentColor!important;opacity:1!important}
div[data-testid="stExpander"] [data-testid="stExpanderDetails"]{background:var(--card)!important;color:var(--txt)!important;padding-top:.65rem}
div[data-testid="stExpander"] [data-testid="stMarkdownContainer"],div[data-testid="stExpander"] p,div[data-testid="stExpander"] li{color:var(--txt)!important;white-space:normal!important;overflow-wrap:anywhere!important;word-break:normal!important;line-height:1.65!important}
[data-testid="stMain"] [data-testid="stMarkdownContainer"] p,[data-testid="stMain"] [data-testid="stMarkdownContainer"] li{color:var(--txt)}
[data-testid="stMain"] [data-testid="stCaptionContainer"] p{color:var(--muted)!important}
[data-testid="stAlert"] p,[data-testid="stAlert"] li{color:inherit!important}
.formula{background:rgba(255,215,0,.04);border-left:4px solid var(--gold);padding:10px 16px;border-radius:4px;margin:8px 0}.insight{background:var(--card);border:1px solid var(--border);padding:15px;border-radius:6px;color:var(--txt)}
.method-flow{display:flex;flex-direction:column;align-items:center;max-width:920px;margin:1rem auto 1.5rem}.method-node{width:100%;background:var(--card);border:1px solid rgba(255,215,0,.28);border-left:5px solid var(--gold);border-radius:7px;padding:13px 18px;color:var(--txt);box-shadow:0 5px 18px rgba(0,0,0,.12)}.method-node b{color:var(--gold);font-family:'Playfair Display',Georgia,serif;font-size:1.03rem}.method-node span{display:block;color:var(--muted);margin-top:3px;line-height:1.5}.method-arrow{color:var(--gold);font-size:1.5rem;line-height:1.05;padding:3px}.method-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:12px 0}.method-card{background:var(--card);border:1px solid var(--border);border-radius:6px;padding:16px;color:var(--txt)}.method-card h4{color:var(--gold);margin:0 0 7px;font-family:'Playfair Display',Georgia,serif}.method-card p{color:var(--txt)!important;margin:0;line-height:1.55}@media(max-width:720px){.method-grid{grid-template-columns:1fr}}
.mp-footer{margin-top:28px;background:#1a4480;border-top:3px solid #e41d3d;padding:20px;border-radius:6px;color:#cfe8ff;font-size:12px}.mp-footer a{color:var(--gold);text-decoration:none}
</style>
"""
