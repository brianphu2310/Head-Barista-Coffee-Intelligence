import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(
    page_title="LODE Bakery Cafe - Rozelle",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ESPRESSO  = "#1a0d07"
CARAMEL   = "#c9956a"
WALNUT    = "#5a3520"
CREAM     = "#f5e6d3"
LATTE     = "#8a6f5a"
PARCHMENT = "#faf4ec"

PROCESS_COLORS = {
    "Washed":     "#7aab8a",
    "Natural":    "#c9956a",
    "Honey":      "#d4a017",
    "Wet Hulled": "#8b6340",
    "Monsooned":  "#c4897a",
}

# CSS built with .format() to avoid f-string / px literal conflicts
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }
html, body, .stApp { background: PARCHMENT_; font-family: 'DM Sans', sans-serif; }
.block-container { padding: 0 !important; max-width: 100% !important; }
#MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none; }

/* MASTHEAD */
.masthead {
    background: ESPRESSO_;
    padding: 14px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.masthead-title {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 400;
    color: CREAM_;
    line-height: 1;
}
.masthead-title em { font-style: italic; color: CARAMEL_; }
.masthead-sub {
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: LATTE_;
    margin-top: 4px;
}
.masthead-right { text-align: right; }
.masthead-count {
    font-family: 'Playfair Display', serif;
    font-size: 26px;
    color: CARAMEL_;
    line-height: 1;
}
.masthead-count-label {
    font-size: 10px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: LATTE_;
}

/* ACTIVE FILTERS */
.active-filters {
    background: #f0e8dc;
    border-bottom: 1px solid #ddd2c4;
    padding: 7px 18px;
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
    min-height: 34px;
}
.af-label {
    font-size: 10px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: LATTE_;
    margin-right: 2px;
    flex-shrink: 0;
}
.af-tag {
    font-size: 10px;
    padding: 2px 8px;
    background: ESPRESSO_;
    color: CREAM_;
    border-radius: 2px;
}
.af-tag-flavor { background: WALNUT_; }
.af-none { font-size: 11px; color: LATTE_; font-style: italic; }

/* STATS */
.stat-row {
    display: flex;
    background: white;
    border-top: 1px solid #ddd2c4;
    border-bottom: 1px solid #ddd2c4;
}
.stat-cell {
    flex: 1;
    padding: 10px 0;
    text-align: center;
    border-right: 1px solid #ddd2c4;
}
.stat-cell:last-child { border-right: none; }
.stat-n {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    color: CARAMEL_;
    line-height: 1;
}
.stat-l {
    font-size: 9px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: LATTE_;
    margin-top: 2px;
}

/* RESULT CARDS */
.result-card {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 11px 18px;
    border-bottom: 1px solid #ddd2c4;
    background: white;
}
.result-card:last-child { border-bottom: none; }
.result-rank {
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    color: CARAMEL_;
    min-width: 24px;
    text-align: center;
    line-height: 1;
    flex-shrink: 0;
}
.result-body { flex: 1; min-width: 0; }
.result-name {
    font-family: 'Playfair Display', serif;
    font-size: 14px;
    font-weight: 600;
    color: ESPRESSO_;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.result-sub { font-size: 11px; color: LATTE_; margin-top: 2px; }
.result-notes {
    font-size: 11px;
    color: #7a6356;
    font-style: italic;
    margin-top: 2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.tag {
    display: inline-block;
    font-size: 10px;
    padding: 1px 6px;
    border: 1px solid #ddd2c4;
    border-radius: 2px;
    color: LATTE_;
    margin-right: 3px;
    margin-top: 3px;
}
.tag-Light  { border-color: CARAMEL_; color: CARAMEL_; }
.tag-Medium { border-color: WALNUT_;  color: WALNUT_; }
.tag-Dark   { border-color: ESPRESSO_; color: ESPRESSO_; }
.result-right { text-align: right; flex-shrink: 0; }
.result-match {
    font-family: 'Playfair Display', serif;
    font-size: 17px;
    color: CARAMEL_;
    line-height: 1;
}
.result-ml {
    font-size: 9px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: LATTE_;
}
.match-bar-wrap {
    width: 52px;
    height: 2px;
    background: #ddd2c4;
    border-radius: 1px;
    margin-top: 4px;
    margin-left: auto;
}
.match-bar-fill { height: 100%; background: CARAMEL_; border-radius: 1px; }

/* EXPANDERS */
[data-testid="stExpander"] {
    border: none !important;
    border-bottom: 1px solid #ddd2c4 !important;
    border-radius: 0 !important;
    background: white !important;
}
[data-testid="stExpander"] summary {
    background: white !important;
    padding: 10px 16px !important;
    font-size: 10px !important;
    letter-spacing: 1.8px !important;
    text-transform: uppercase !important;
    color: WALNUT_ !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
}
[data-testid="stExpander"] summary:hover {
    background: #f8f1e8 !important;
    color: ESPRESSO_ !important;
}
[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
    padding: 4px 16px 14px !important;
    background: white !important;
}
[data-testid="stExpander"] [data-testid="stMultiSelect"] > div > div {
    border: 1px solid #ddd2c4 !important;
    border-radius: 4px !important;
    background: PARCHMENT_ !important;
    font-size: 12px !important;
}
div[data-baseweb="tag"] { background: ESPRESSO_ !important; }

.options-top-label {
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 10px 16px 8px;
    border-bottom: 1px solid #2d1a10;
    background: ESPRESSO_;
    color: CARAMEL_;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
}
</style>
""".replace("PARCHMENT_", PARCHMENT).replace("ESPRESSO_", ESPRESSO).replace(
    "CARAMEL_", CARAMEL).replace("WALNUT_", WALNUT).replace(
    "CREAM_", CREAM).replace("LATTE_", LATTE)

st.markdown(CSS, unsafe_allow_html=True)

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    candidates = [
        os.path.join(os.path.dirname(__file__), "coffee_dataset.csv"),
        "/mnt/user-data/uploads/coffee_dataset.csv",
    ]
    for path in candidates:
        if os.path.exists(path):
            return pd.read_csv(path)
    st.error("coffee_dataset.csv not found. Place it in the same folder as this script.")
    st.stop()

df = load_data()

ALL_ROASTS    = sorted(df["Roast_Level"].unique())
ALL_PROCESSES = sorted(df["Processing_Method"].unique())
ALL_BREWS     = sorted(df["Brew_Method"].unique())
ALL_ACIDITIES = sorted(df["Acidity"].unique())
ALL_BODIES    = sorted(df["Body"].unique())
ALL_FLAVORS   = sorted({
    f.strip()
    for notes in df["Flavor_Notes"].dropna()
    for f in notes.split(",")
})

# ── MATCH SCORE ───────────────────────────────────────────────────────────────
def match_score(row, sel_roast, sel_brew, sel_process, sel_acidity, sel_body, sel_flavor):
    s = 0
    s += 20 if row.Roast_Level       in sel_roast   else 5
    s += 15 if row.Acidity           in sel_acidity  else 5
    s += 15 if row.Body              in sel_body     else 5
    s += 15 if row.Processing_Method in sel_process  else 3
    s += 10 if row.Brew_Method       in sel_brew     else 2
    if sel_flavor:
        hits = sum(1 for f in sel_flavor if f.lower() in str(row.Flavor_Notes).lower())
        s += min(20, hits * 7)
    else:
        s += 10
    s += max(0, ((row.Rating - 80) / 20) * 5)
    return min(100, round(s))

# ── MAP ───────────────────────────────────────────────────────────────────────
def build_map(top_df):
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lat=df["Latitude"], lon=df["Longitude"],
        mode="markers",
        marker=dict(size=4, color="#3d1f0e", opacity=0.4),
        showlegend=False, hoverinfo="skip",
    ))
    for proc, color in PROCESS_COLORS.items():
        grp = top_df[top_df["Processing_Method"] == proc]
        if grp.empty:
            continue
        sizes = ((grp["Match"] / 100) * 10 + 5).clip(5, 15)
        fig.add_trace(go.Scattergeo(
            lat=grp["Latitude"], lon=grp["Longitude"],
            mode="markers", name=proc,
            marker=dict(size=sizes, color=color, opacity=0.92,
                        line=dict(width=1, color="#f5e6d3")),
            customdata=grp[["Coffee_Name","Origin","Match","Rating",
                            "Processing_Method","Brew_Method"]].values,
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>%{customdata[1]}<br>"
                "Match: <b>%{customdata[2]}%</b> · Score: %{customdata[3]}<br>"
                "%{customdata[4]} · %{customdata[5]}<extra></extra>"
            ),
        ))
    fig.update_layout(
        geo=dict(
            showland=True, landcolor="#1e0f08",
            showocean=True, oceancolor="#0d0805",
            showcountries=True, countrycolor="#2d1a10", countrywidth=0.5,
            showcoastlines=True, coastlinecolor="#2d1a10", coastlinewidth=0.5,
            showframe=False, bgcolor="#0d0805",
            projection_type="natural earth",
            lataxis_range=[-60, 75], lonaxis_range=[-180, 180],
        ),
        paper_bgcolor="#0d0805",
        height=360,
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=True,
        legend=dict(
            orientation="h", x=0.01, y=0.02,
            bgcolor="rgba(26,13,7,0.85)", bordercolor="#2d1a10", borderwidth=1,
            font=dict(size=9, color="#c9956a", family="DM Sans"),
        ),
        hoverlabel=dict(
            bgcolor="#1a0d07", bordercolor="#c9956a",
            font=dict(size=11, color="#f5e6d3", family="DM Sans"),
        ),
    )
    return fig

# ── MASTHEAD ──────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="masthead">'
    '<div>'
    '<div class="masthead-title">LODE <em>Bakery Cafe</em></div>'
    '<div class="masthead-sub">Rozelle &middot; Sydney &middot; Coffee Finder</div>'
    '</div>'
    '<div class="masthead-right">'
    '<div class="masthead-count">' + str(len(df)) + '</div>'
    '<div class="masthead-count-label">Varieties</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)

# ── LAYOUT ───────────────────────────────────────────────────────────────────
left_col, right_col = st.columns([3, 1], gap="small")

# ── RIGHT: ACCORDION FILTERS ──────────────────────────────────────────────────
with right_col:
    st.markdown('<div class="options-top-label">&#9749; &nbsp;Filters</div>',
                unsafe_allow_html=True)

    with st.expander("Roast level", expanded=False):
        sel_roast = st.multiselect(
            "r", options=ALL_ROASTS, default=ALL_ROASTS,
            key="roast", label_visibility="collapsed",
        )
    with st.expander("Brew method", expanded=False):
        sel_brew = st.multiselect(
            "b", options=ALL_BREWS, default=ALL_BREWS,
            key="brew", label_visibility="collapsed",
        )
    with st.expander("Processing", expanded=False):
        sel_process = st.multiselect(
            "p", options=ALL_PROCESSES, default=ALL_PROCESSES,
            key="process", label_visibility="collapsed",
        )
    with st.expander("Acidity", expanded=False):
        sel_acidity = st.multiselect(
            "a", options=ALL_ACIDITIES, default=ALL_ACIDITIES,
            key="acidity", label_visibility="collapsed",
        )
    with st.expander("Body", expanded=False):
        sel_body = st.multiselect(
            "bd", options=ALL_BODIES, default=ALL_BODIES,
            key="body", label_visibility="collapsed",
        )
    with st.expander("Flavour notes", expanded=False):
        sel_flavor = st.multiselect(
            "fl", options=ALL_FLAVORS, default=[],
            key="flavor", placeholder="Any flavour...",
            label_visibility="collapsed",
        )
    with st.expander("Min score", expanded=False):
        min_score = st.slider(
            "sc",
            min_value=int(df["Rating"].min()),
            max_value=int(df["Rating"].max()),
            value=80, step=1, key="score",
            label_visibility="collapsed",
        )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    if st.button("Reset filters", use_container_width=True):
        for k in ["roast","brew","process","acidity","body","flavor","score"]:
            if k in st.session_state:
                del st.session_state[k]
        st.rerun()

# ── COMPUTE MATCHES ───────────────────────────────────────────────────────────
_roast   = sel_roast   or ALL_ROASTS
_brew    = sel_brew    or ALL_BREWS
_process = sel_process or ALL_PROCESSES
_acidity = sel_acidity or ALL_ACIDITIES
_body    = sel_body    or ALL_BODIES

scored = df[df["Rating"] >= min_score].copy()
scored["Match"] = scored.apply(
    lambda r: match_score(r, _roast, _brew, _process, _acidity, _body, sel_flavor),
    axis=1,
)
scored = scored.sort_values(["Match","Rating"], ascending=False).reset_index(drop=True)
top10 = scored.head(10)

# ── LEFT: ACTIVE FILTERS + MAP + STATS + RESULTS ─────────────────────────────
with left_col:

    # Active filter strip
    tags = []
    if set(sel_roast)   != set(ALL_ROASTS):
        tags += ['<span class="af-tag">' + v + '</span>' for v in sel_roast]
    if set(sel_brew)    != set(ALL_BREWS):
        tags += ['<span class="af-tag">' + v + '</span>' for v in sel_brew]
    if set(sel_process) != set(ALL_PROCESSES):
        tags += ['<span class="af-tag">' + v + '</span>' for v in sel_process]
    if set(sel_acidity) != set(ALL_ACIDITIES):
        tags += ['<span class="af-tag">' + v + '</span>' for v in sel_acidity]
    if set(sel_body)    != set(ALL_BODIES):
        tags += ['<span class="af-tag">' + v + '</span>' for v in sel_body]
    tags += ['<span class="af-tag af-tag-flavor">' + v + '</span>' for v in sel_flavor]
    if min_score > int(df["Rating"].min()):
        tags.append('<span class="af-tag">score &ge; ' + str(min_score) + '</span>')

    if tags:
        inner = '<span class="af-label">Active</span>' + "".join(tags)
    else:
        inner = '<span class="af-none">No filters — expand the accordions on the right to filter</span>'

    st.markdown('<div class="active-filters">' + inner + '</div>', unsafe_allow_html=True)

    # Map
    st.plotly_chart(build_map(top10), use_container_width=True, config={"displayModeBar": False})

    # Stats
    n_matches  = len(top10)
    n_origins  = top10["Origin"].nunique() if n_matches else 0
    avg_rating = round(top10["Rating"].mean()) if n_matches else 0
    top_proc   = top10["Processing_Method"].value_counts().index[0] if n_matches else "—"

    st.markdown(
        '<div class="stat-row">'
        '<div class="stat-cell"><div class="stat-n">' + str(n_matches) + '</div>'
        '<div class="stat-l">Matches</div></div>'
        '<div class="stat-cell"><div class="stat-n">' + str(n_origins) + '</div>'
        '<div class="stat-l">Origins</div></div>'
        '<div class="stat-cell"><div class="stat-n">' + str(avg_rating) + '</div>'
        '<div class="stat-l">Avg score</div></div>'
        '<div class="stat-cell"><div class="stat-n" style="font-size:13px;padding-top:4px;">' + str(top_proc) + '</div>'
        '<div class="stat-l">Top process</div></div>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Results
    RANKS = ["①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩"]

    if top10.empty:
        st.markdown(
            '<div style="padding:32px;text-align:center;font-size:13px;'
            'color:' + LATTE + ';background:white;border-top:1px solid #ddd2c4;">'
            'No matches — try broadening your filters</div>',
            unsafe_allow_html=True,
        )
    else:
        cards_html = ""
        for i, (_, row) in enumerate(top10.iterrows()):
            rank = RANKS[i] if i < len(RANKS) else str(i + 1)
            m    = int(round(float(row["Match"])))
            cards_html += (
                '<div class="result-card">'
                '<div class="result-rank">' + rank + '</div>'
                '<div class="result-body">'
                '<div class="result-name">' + str(row["Coffee_Name"]) + '</div>'
                '<div class="result-sub">' + str(row["Origin"]) + ' &middot; ' + str(row["Brew_Method"]) + '</div>'
                '<div class="result-notes">' + str(row["Flavor_Notes"]) + '</div>'
                '<span class="tag tag-' + str(row["Roast_Level"]) + '">' + str(row["Roast_Level"]) + '</span>'
                '<span class="tag">' + str(row["Processing_Method"]) + '</span>'
                '<span class="tag">' + str(row["Acidity"]) + ' acid</span>'
                '<span class="tag">' + str(row["Body"]) + ' body</span>'
                '</div>'
                '<div class="result-right">'
                '<div class="result-match">' + str(m) + '%</div>'
                '<div class="result-ml">match</div>'
                '<div class="match-bar-wrap">'
                '<div class="match-bar-fill" style="width:' + str(m) + '%"></div>'
                '</div>'
                '</div>'
                '</div>'
            )
        st.markdown(
            '<div style="background:white;border-top:1px solid #ddd2c4;">' + cards_html + '</div>',
            unsafe_allow_html=True,
        )
