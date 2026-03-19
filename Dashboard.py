"""
Geospatial Suitability Analysis for Renewable Energy Sites
Streamlit Dashboard
Run: streamlit run dashboard.py
"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Renewable Energy Site Suitability",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Theme / CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;600;700&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #0a1628 0%, #0d2137 60%, #0a2e1f 100%);
    border-right: 1px solid #1a3a2a;
}
[data-testid="stSidebar"] * { color: #c8e6c9 !important; }
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stSelectbox label { color: #81c784 !important; font-size: 0.82rem; letter-spacing: 0.05em; text-transform: uppercase; }

h1 { font-family: 'Space Mono', monospace !important; font-size: 1.9rem !important; color: #e8f5e9 !important; }
h2, h3 { font-family: 'Space Mono', monospace !important; color: #a5d6a7 !important; }

.metric-card {
    background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #0f2027 100%);
    border: 1px solid #2e7d32;
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    text-align: center;
}
.metric-card .label { font-size: 0.78rem; color: #66bb6a; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.3rem; }
.metric-card .value { font-family: 'Space Mono', monospace; font-size: 2rem; font-weight: 700; color: #e8f5e9; }
.metric-card .delta { font-size: 0.82rem; color: #81c784; margin-top: 0.2rem; }

.section-header {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: #4caf50;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    border-bottom: 1px solid #1b5e20;
    padding-bottom: 0.4rem;
    margin-bottom: 1rem;
}

.high-badge   { background:#1b5e20; color:#a5d6a7; padding:2px 10px; border-radius:20px; font-size:0.8rem; }
.mod-badge    { background:#e65100; color:#ffccbc; padding:2px 10px; border-radius:20px; font-size:0.8rem; }
.low-badge    { background:#4a148c; color:#e1bee7; padding:2px 10px; border-radius:20px; font-size:0.8rem; }

.stPlotlyChart { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# ─── Data Loading & Feature Engineering ────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_excel("data.xlsx")

    np.random.seed(42)
    n = len(df)

    # Derive renewable energy features from terrain data
    # Solar irradiance: higher at lower slopes & elevations
    df["solar_irradiance"] = np.clip(
        7.5 - (df["slope"] / 60) * 3.0 - (df["elevation"] / 1816) * 1.5
        + np.random.normal(0, 0.3, n), 2, 8
    )

    # Wind speed: higher at greater elevations and slopes
    df["wind_speed"] = np.clip(
        3 + (df["elevation"] / 1816) * 5 + (df["slope"] / 60) * 2
        + np.random.normal(0, 0.6, n), 2, 12
    )

    # Distance to road (simulated): loam soil areas tend to be more accessible
    soil_road_offset = {"loam": -5, "clay": 0, "sand": 5}
    df["distance_to_road"] = np.clip(
        25 + df["soil_type"].map(soil_road_offset)
        + np.random.uniform(-15, 15, n), 0, 50
    )

    # Suitability score
    land_penalty = {"loam": 1.0, "clay": 0.9, "sand": 0.85}
    df["land_score"] = df["soil_type"].map(land_penalty)

    df["suitability_score"] = (
        0.30 * (df["solar_irradiance"] / 8)
        + 0.30 * (df["wind_speed"] / 12)
        + 0.20 * (1 - df["slope"] / 60)
        + 0.10 * (1 - df["distance_to_road"] / 50)
    ) * df["land_score"]

    df["suitability_score"] = df["suitability_score"].round(3)

    def classify(s):
        if s >= 0.60: return "High"
        elif s >= 0.45: return "Moderate"
        else: return "Low"

    df["suitability_class"] = df["suitability_score"].apply(classify)

    # Simulated lat/lon for geospatial map (Nigeria / West Africa region)
    df["latitude"]  = np.random.uniform(4.5, 14.0, n)
    df["longitude"] = np.random.uniform(3.0, 15.0, n)

    return df

df_full = load_data()

# ─── Sidebar Filters ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚡ Filters")
    st.markdown("---")

    suitability_filter = st.multiselect(
        "Suitability Class",
        options=["High", "Moderate", "Low"],
        default=["High", "Moderate", "Low"],
    )

    soil_filter = st.multiselect(
        "Soil Type",
        options=df_full["soil_type"].unique().tolist(),
        default=df_full["soil_type"].unique().tolist(),
    )

    elev_min, elev_max = float(df_full["elevation"].min()), float(df_full["elevation"].max())
    elev_range = st.slider("Elevation Range (m)", elev_min, elev_max, (elev_min, elev_max), step=10.0)

    slope_range = st.slider("Slope Range (°)", 0.0, 60.0, (0.0, 60.0), step=1.0)

    st.markdown("---")
    st.markdown("### Weight Tuning")
    w_solar  = st.slider("Solar Weight",    0.0, 1.0, 0.30, 0.05)
    w_wind   = st.slider("Wind Weight",     0.0, 1.0, 0.30, 0.05)
    w_slope  = st.slider("Slope Weight",    0.0, 1.0, 0.20, 0.05)
    w_road   = st.slider("Road Dist Weight",0.0, 1.0, 0.10, 0.05)

    total_w = w_solar + w_wind + w_slope + w_road
    if abs(total_w - 1.0) > 0.01:
        st.warning(f"Weights sum to {total_w:.2f}. Normalizing automatically.")

    st.markdown("---")
    st.caption("Geospatial Suitability Analysis · Renewable Energy Sites")

# ─── Apply Filters & Recompute ─────────────────────────────────────────────────
df = df_full[
    df_full["suitability_class"].isin(suitability_filter)
    & df_full["soil_type"].isin(soil_filter)
    & df_full["elevation"].between(*elev_range)
    & df_full["slope"].between(*slope_range)
].copy()

# Recompute with custom weights (normalized)
if total_w > 0:
    nw = total_w
    df["suitability_score"] = (
        (w_solar / nw)  * (df["solar_irradiance"] / 8)
        + (w_wind / nw)  * (df["wind_speed"] / 12)
        + (w_slope / nw) * (1 - df["slope"] / 60)
        + (w_road / nw)  * (1 - df["distance_to_road"] / 50)
    ) * df["land_score"]
    df["suitability_score"] = df["suitability_score"].round(3)

    def classify(s):
        if s >= 0.60: return "High"
        elif s >= 0.45: return "Moderate"
        else: return "Low"
    df["suitability_class"] = df["suitability_score"].apply(classify)

# ─── Color Palette ─────────────────────────────────────────────────────────────
CLASS_COLORS = {"High": "#4caf50", "Moderate": "#ff9800", "Low": "#9c27b0"}
SOIL_COLORS  = {"loam": "#a5d6a7", "clay": "#ffcc80", "sand": "#ce93d8"}
BG           = "#0a1628"
GRID_COL     = "#1a3a2a"
FONT_COL     = "#c8e6c9"

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor ="rgba(0,0,0,0)",
    font=dict(family="DM Sans", color=FONT_COL, size=12),
    margin=dict(t=40, b=20, l=10, r=10),
    legend=dict(bgcolor="rgba(0,0,0,0.3)", bordercolor="#2e7d32", borderwidth=1),
    xaxis=dict(gridcolor=GRID_COL, zerolinecolor=GRID_COL),
    yaxis=dict(gridcolor=GRID_COL, zerolinecolor=GRID_COL),
)

# ─── Header ────────────────────────────────────────────────────────────────────
st.markdown("# ⚡ Renewable Energy Site Suitability")
st.markdown(
    "<p style='color:#66bb6a;font-size:1rem;margin-top:-0.5rem;'>"
    "Geospatial Analysis Dashboard · Terrain × Climate × Land-Use</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# ─── KPI Row ───────────────────────────────────────────────────────────────────
total     = len(df)
high_ct   = (df["suitability_class"] == "High").sum()
mod_ct    = (df["suitability_class"] == "Moderate").sum()
low_ct    = (df["suitability_class"] == "Low").sum()
avg_score = df["suitability_score"].mean()
landslide_risk = df["landslide"].mean() * 100

kpi_cols = st.columns(5)
kpis = [
    ("Total Sites", total, "filtered"),
    ("High Suitability", high_ct, f"{high_ct/total*100:.0f}% of sites" if total else "—"),
    ("Moderate", mod_ct, f"{mod_ct/total*100:.0f}% of sites" if total else "—"),
    ("Avg Score", f"{avg_score:.3f}", "weighted composite"),
    ("Landslide Risk", f"{landslide_risk:.1f}%", "% at-risk sites"),
]
for col, (label, val, delta) in zip(kpi_cols, kpis):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="label">{label}</div>
            <div class="value">{val}</div>
            <div class="delta">{delta}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── Row 1: Map + Pie ──────────────────────────────────────────────────────────
col_map, col_pie = st.columns([2, 1])

with col_map:
    st.markdown('<div class="section-header">📍 Site Distribution Map</div>', unsafe_allow_html=True)
    fig_map = px.scatter_mapbox(
        df, lat="latitude", lon="longitude",
        color="suitability_class",
        color_discrete_map=CLASS_COLORS,
        size="suitability_score",
        size_max=14,
        hover_data={
            "elevation": ":.1f",
            "slope": ":.1f",
            "solar_irradiance": ":.2f",
            "wind_speed": ":.2f",
            "suitability_score": ":.3f",
            "soil_type": True,
            "latitude": False, "longitude": False,
        },
        mapbox_style="carto-darkmatter",
        zoom=4, height=380,
        title="",
    )
    fig_map.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color=FONT_COL),
        legend=dict(bgcolor="rgba(0,0,0,0.5)", bordercolor="#2e7d32", borderwidth=1),
        margin=dict(t=5, b=0, l=0, r=0),
    )
    st.plotly_chart(fig_map, use_container_width=True)

with col_pie:
    st.markdown('<div class="section-header">🥧 Suitability Breakdown</div>', unsafe_allow_html=True)
    class_counts = df["suitability_class"].value_counts().reset_index()
    class_counts.columns = ["class", "count"]
    fig_pie = px.pie(
        class_counts, names="class", values="count",
        color="class", color_discrete_map=CLASS_COLORS,
        hole=0.5, height=380,
    )
    fig_pie.update_traces(
        textinfo="percent+label",
        textfont=dict(color="#e8f5e9", size=13),
        marker=dict(line=dict(color=BG, width=3)),
    )
    fig_pie.update_layout(**{**PLOTLY_LAYOUT, "showlegend": False})
    st.plotly_chart(fig_pie, use_container_width=True)

# ─── Row 2: Score Distribution + Feature Influence ─────────────────────────────
col_hist, col_bar = st.columns(2)

with col_hist:
    st.markdown('<div class="section-header">📊 Suitability Score Distribution</div>', unsafe_allow_html=True)
    fig_hist = px.histogram(
        df, x="suitability_score",
        color="suitability_class",
        color_discrete_map=CLASS_COLORS,
        nbins=30, barmode="overlay",
        opacity=0.8, height=300,
    )
    fig_hist.update_layout(**PLOTLY_LAYOUT)
    fig_hist.update_xaxes(title="Suitability Score")
    fig_hist.update_yaxes(title="Site Count")
    st.plotly_chart(fig_hist, use_container_width=True)

with col_bar:
    st.markdown('<div class="section-header">🔍 Feature Influence (Correlation)</div>', unsafe_allow_html=True)
    feats = ["solar_irradiance", "wind_speed", "land_slope", "distance_to_road", "elevation", "rainfall"]
    avail = [f for f in feats if f in df.columns]
    corr  = df[avail].corrwith(df["suitability_score"]).sort_values()
    fig_corr = go.Figure(go.Bar(
        x=corr.values,
        y=corr.index,
        orientation="h",
        marker_color=[CLASS_COLORS["High"] if v > 0 else CLASS_COLORS["Low"] for v in corr.values],
        text=[f"{v:.3f}" for v in corr.values],
        textposition="outside",
        textfont=dict(color=FONT_COL),
    ))
    fig_corr.update_layout(**PLOTLY_LAYOUT, height=300)
    fig_corr.update_xaxes(title="Pearson Correlation")
    st.plotly_chart(fig_corr, use_container_width=True)

# ─── Row 3: Solar vs Wind Scatter + Soil Type Breakdown ────────────────────────
col_scatter, col_soil = st.columns(2)

with col_scatter:
    st.markdown('<div class="section-header">🌞💨 Solar vs Wind Potential</div>', unsafe_allow_html=True)
    fig_sv = px.scatter(
        df,
        x="solar_irradiance", y="wind_speed",
        color="suitability_class",
        color_discrete_map=CLASS_COLORS,
        size="suitability_score", size_max=12,
        opacity=0.75, height=320,
        hover_data=["soil_type", "elevation", "slope"],
        labels={"solar_irradiance": "Solar Irradiance (kWh/m²/day)", "wind_speed": "Wind Speed (m/s)"},
    )
    fig_sv.update_layout(**PLOTLY_LAYOUT)
    st.plotly_chart(fig_sv, use_container_width=True)

with col_soil:
    st.markdown('<div class="section-header">🌱 Suitability by Soil Type</div>', unsafe_allow_html=True)
    soil_suit = df.groupby(["soil_type", "suitability_class"]).size().reset_index(name="count")
    fig_soil = px.bar(
        soil_suit, x="soil_type", y="count",
        color="suitability_class", color_discrete_map=CLASS_COLORS,
        barmode="group", height=320,
        labels={"soil_type": "Soil Type", "count": "Site Count"},
    )
    fig_soil.update_layout(**PLOTLY_LAYOUT)
    st.plotly_chart(fig_soil, use_container_width=True)

# ─── Row 4: Correlation Heatmap + Landslide Risk ───────────────────────────────
col_heat, col_ls = st.columns(2)

with col_heat:
    st.markdown('<div class="section-header">🔥 Feature Correlation Heatmap</div>', unsafe_allow_html=True)
    num_cols = df.select_dtypes(include="number").columns.tolist()
    corr_mat  = df[num_cols].corr()
    fig_heat = go.Figure(go.Heatmap(
        z=corr_mat.values,
        x=corr_mat.columns,
        y=corr_mat.index,
        colorscale="RdYlGn",
        text=[[f"{v:.2f}" for v in row] for row in corr_mat.values],
        texttemplate="%{text}",
        showscale=True,
        zmin=-1, zmax=1,
    ))
    fig_heat.update_layout(**{**PLOTLY_LAYOUT, "height": 340})
    st.plotly_chart(fig_heat, use_container_width=True)

with col_ls:
    st.markdown('<div class="section-header">⚠️ Landslide Risk vs Suitability</div>', unsafe_allow_html=True)
    risk_suit = df.groupby("suitability_class")["landslide"].mean().reset_index()
    risk_suit.columns = ["class", "risk_rate"]
    risk_suit["risk_pct"] = (risk_suit["risk_rate"] * 100).round(1)
    fig_ls = px.bar(
        risk_suit, x="class", y="risk_pct",
        color="class", color_discrete_map=CLASS_COLORS,
        text="risk_pct", height=340,
        labels={"class": "Suitability Class", "risk_pct": "Landslide Risk (%)"},
    )
    fig_ls.update_traces(texttemplate="%{text:.1f}%", textposition="outside", textfont=dict(color=FONT_COL))
    fig_ls.update_layout(**PLOTLY_LAYOUT)
    st.plotly_chart(fig_ls, use_container_width=True)

# ─── Row 5: Box Plots ──────────────────────────────────────────────────────────
st.markdown('<div class="section-header">📦 Feature Distributions by Class</div>', unsafe_allow_html=True)

box_feat = st.selectbox("Select Feature", ["solar_irradiance", "wind_speed", "elevation", "slope", "rainfall", "distance_to_road"])
fig_box = px.box(
    df, x="suitability_class", y=box_feat,
    color="suitability_class", color_discrete_map=CLASS_COLORS,
    points="outliers", height=320,
)
fig_box.update_layout(**PLOTLY_LAYOUT)
st.plotly_chart(fig_box, use_container_width=True)

# ─── Data Table ────────────────────────────────────────────────────────────────
with st.expander("📋 View Filtered Site Data"):
    display_cols = ["elevation", "slope", "rainfall", "soil_type", "landslide",
                    "solar_irradiance", "wind_speed", "distance_to_road",
                    "suitability_score", "suitability_class"]
    avail_cols = [c for c in display_cols if c in df.columns]
    st.dataframe(
        df[avail_cols].sort_values("suitability_score", ascending=False).reset_index(drop=True),
        use_container_width=True, height=300,
    )
    csv = df[avail_cols].to_csv(index=False)
    st.download_button("⬇️ Download CSV", csv, "suitability_results.csv", "text/csv")

# ─── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#388e3c;font-size:0.8rem;'>"
    "Geospatial Suitability Analysis for Renewable Energy Sites · Built with Streamlit & Plotly</p>",
    unsafe_allow_html=True,
)