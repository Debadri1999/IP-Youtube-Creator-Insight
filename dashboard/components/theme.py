from __future__ import annotations

import streamlit as st


APP_THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700;800&display=swap');

/* Creator Insights (Youtube-Optmization) design DNA — extended for full IP V5 surface area */
:root {
    --yt-red: #FF0000;
    --yt-red-dark: #CC0000;
    --yt-bg: #0F0F23;
    --yt-bg-alt: #1A1A2E;
    --yt-surface: #16213E;
    --yt-accent: #00D4FF;
    --yt-success: #00E676;
    --yt-warning: #FFB300;
    --yt-text: #FFFFFF;
    --yt-text-muted: #B0B0B0;

    --app-canvas: var(--yt-bg);
    --app-bg: var(--yt-bg);
    --app-bg-alt: var(--yt-bg-alt);
    --app-surface-1: rgba(22, 33, 62, 0.55);
    --app-surface-2: rgba(22, 33, 62, 0.92);
    --app-border: rgba(255, 255, 255, 0.08);
    --app-border-focus: rgba(0, 212, 255, 0.55);
    --app-text: var(--yt-text);
    --app-text-secondary: var(--yt-text-muted);
    --app-text-tertiary: #8b8ba8;
    --app-accent: var(--yt-accent);
    --app-accent-2: var(--yt-red);
    --app-success: var(--yt-success);
    --app-warning: var(--yt-warning);
    --app-radius-lg: 18px;
    --app-radius-md: 16px;
    --app-radius-pill: 999px;
    --app-control-height: 46px;
    --app-page-width: 1200px;
    --app-command-width: 1000px;
    --app-section-width: 1120px;
    --app-font-display: "Inter", system-ui, sans-serif;
    --app-font-body: "Inter", system-ui, sans-serif;
    --app-font-mono: "IBM Plex Mono", ui-monospace, monospace;
}

html, body, [data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, #1A1A2E 0%, #0F0F23 40%, #000000 100%) !important;
    color: var(--yt-text);
    font-family: var(--app-font-body);
    font-size: 15px;
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
}

/* Thin top accent (default Streamlit decoration is tall) */
[data-testid="stDecoration"] {
    height: 2px !important;
    min-height: 2px !important;
    max-height: 2px !important;
    background-image: none !important;
    background: linear-gradient(90deg, rgba(255,0,0,0.85), rgba(0,212,255,0.85)) !important;
}

/*
 * Compact Deploy / menu bar — only light touches. Do not override child layout
 * (flex on stHeader > div breaks Streamlit 1.5x internals and can block scroll/clicks).
 */
[data-testid="stHeader"] {
    background: rgba(15, 15, 35, 0.92) !important;
    backdrop-filter: blur(14px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    min-height: 2.5rem !important;
    padding: 0.25rem 0.65rem !important;
}
[data-testid="stToolbar"] {
    padding-top: 0.1rem !important;
    padding-bottom: 0.1rem !important;
}

/*
 * Main column: enough top padding so the first markdown hero clears the fixed header
 * (Streamlit 1.5x) and is not visually clipped at the viewport edge.
 */
section[data-testid="stMain"] > div {
    padding-top: 0.85rem !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0F0F23 0%, #1A1A2E 50%, #0F0F23 100%) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.06);
}

[data-testid="stSidebarCollapsedControl"] button,
[data-testid="collapsedControl"] button {
    background: rgba(22, 33, 62, 0.9) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 999px !important;
    color: var(--yt-text) !important;
}

.block-container {
    max-width: var(--app-page-width) !important;
    padding-top: 2.35rem !important;
    padding-bottom: 2.75rem;
    padding-left: 1.25rem !important;
    padding-right: 1.25rem !important;
}

::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.16);
    border-radius: 4px;
}

/* Product hero — gradient headline (line-height + padding avoid background-clip glyph crop) */
.yt-app-hero-shell {
    overflow: visible !important;
    padding-top: 0.35rem;
    margin-top: 0;
}

div[data-testid="stMarkdownContainer"]:has(.yt-page-title) {
    overflow: visible !important;
}

.yt-page-title {
    font-family: var(--app-font-display);
    font-size: clamp(1.85rem, 2.8vw, 2.35rem);
    font-weight: 800;
    margin: 0 0 0.5rem 0;
    line-height: 1.22 !important;
    letter-spacing: -0.03em;
    padding: 0.5em 0 0.15em 0 !important;
    display: block;
    overflow: visible !important;
    position: relative;
    background: linear-gradient(90deg, #FFFFFF 0%, #FF0000 48%, #00D4FF 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    -webkit-box-decoration-break: clone;
    box-decoration-break: clone;
}

.fade-in:has(.yt-page-title) {
    overflow: visible !important;
}

@supports not (-webkit-background-clip: text) {
    .yt-page-title {
        -webkit-text-fill-color: unset;
        color: #FFFFFF;
    }
}

.yt-page-subtitle {
    color: var(--yt-text-muted);
    font-size: 15px;
    margin-bottom: 0.35rem;
    max-width: 820px;
    font-weight: 500;
    line-height: 1.55;
}

.app-hero-kicker {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #00D4FF;
    margin-bottom: 0.35rem;
}

.app-hero-blurb {
    margin: 0;
    font-size: 14px;
    line-height: 1.6;
    color: #c8c8d8;
    max-width: 820px;
}

.yt-section-header {
    font-family: var(--app-font-display);
    font-size: 1.35rem;
    font-weight: 600;
    margin-top: 1.65rem;
    margin-bottom: 0.4rem;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--yt-text);
}

.yt-section-underline {
    width: 72px;
    height: 3px;
    border-radius: 999px;
    background: linear-gradient(90deg, #FF0000, #00D4FF);
    margin-bottom: 1.1rem;
}

.metric-row {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 1.25rem;
}

.metric-card {
    flex: 1 1 160px;
    padding: 0.9rem 1rem;
    border-radius: var(--app-radius-md);
    background: radial-gradient(circle at top left, rgba(255,255,255,0.08) 0%, rgba(22,33,62,0.9) 35%, rgba(10,10,25,0.95) 100%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 14px 35px rgba(0, 0, 0, 0.55);
    backdrop-filter: blur(10px);
    transition: transform 0.15s ease-out, box-shadow 0.15s ease-out, border-color 0.15s;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 18px 45px rgba(0, 0, 0, 0.75);
    border-color: rgba(255, 0, 0, 0.55);
}

.metric-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--yt-text-muted);
    margin-bottom: 0.2rem;
    font-weight: 600;
}

.metric-value {
    font-family: var(--app-font-display);
    font-size: 1.75rem;
    font-weight: 700;
    line-height: 1.1;
    color: var(--yt-text);
}

.metric-delta.positive { color: var(--yt-success); }
.metric-delta.negative { color: #FF6090; }

.styled-dataframe thead tr th {
    background: linear-gradient(90deg, rgba(255,0,0,0.85), rgba(12,12,32,0.95)) !important;
    color: #FFFFFF !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15) !important;
    font-family: var(--app-font-display);
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

.styled-dataframe tbody tr:nth-child(odd) { background-color: rgba(255, 255, 255, 0.015); }
.styled-dataframe tbody tr:nth-child(even) { background-color: rgba(255, 255, 255, 0.03); }

.stButton > button,
.stFormSubmitButton > button {
    min-height: var(--app-control-height) !important;
    border-radius: 999px !important;
    padding: 0.5rem 1.2rem !important;
    font-family: var(--app-font-display) !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    transition: transform 0.12s ease-out, box-shadow 0.12s ease-out, filter 0.15s;
}

button[kind="primary"],
.stButton > button[kind="primary"],
.stFormSubmitButton > button[kind="primary"] {
    background: linear-gradient(90deg, #FF0000, #CC0000) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6) !important;
}

button[kind="primary"]:hover,
.stButton > button[kind="primary"]:hover,
.stFormSubmitButton > button[kind="primary"]:hover {
    transform: translateY(-1px) scale(1.01);
    filter: brightness(1.05);
    box-shadow: 0 14px 30px rgba(0, 0, 0, 0.8) !important;
}

.stButton > button:not([kind="primary"]),
.stFormSubmitButton > button:not([kind="primary"]),
button[kind="secondary"],
button[kind="secondaryFormSubmit"] {
    background: rgba(15, 15, 35, 0.85) !important;
    color: var(--yt-text) !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.45) !important;
}

.stButton > button:not([kind="primary"]):hover,
.stFormSubmitButton > button:not([kind="primary"]):hover {
    border-color: rgba(0, 212, 255, 0.35) !important;
}

.stButton > button:focus-visible,
.stFormSubmitButton > button:focus-visible {
    outline: none !important;
    box-shadow: 0 0 0 2px rgba(0, 212, 255, 0.45) !important;
}

.stTextInput > div > div > input,
.stTextArea textarea,
.stSelectbox > div > div,
.stDateInput > div > div,
.stSlider > div > div,
[data-baseweb="select"] > div,
[data-baseweb="input"] > div {
    background-color: rgba(15, 15, 35, 0.95) !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    color: var(--yt-text) !important;
    min-height: var(--app-control-height) !important;
}

.stTextInput > div > div:focus-within,
.stSelectbox > div > div:focus-within,
[data-baseweb="select"] > div:focus-within,
[data-baseweb="input"] > div:focus-within {
    border-color: var(--yt-accent) !important;
    box-shadow: 0 0 0 1px rgba(0, 212, 255, 0.45) !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #747494 !important;
}

[data-testid="stSegmentedControl"] {
    width: 100%;
    background: rgba(15, 15, 35, 0.75) !important;
    border-radius: 14px !important;
    padding: 5px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}
[data-testid="stSegmentedControl"] [data-baseweb="button-group"],
[data-testid="stSegmentedControl"] [role="radiogroup"] {
    width: 100%;
    display: flex !important;
}
[data-testid="stSegmentedControl"] [data-baseweb="button-group"] > *,
[data-testid="stSegmentedControl"] [role="radiogroup"] > * { flex: 1 1 0 !important; }
[data-testid="stSegmentedControl"] button,
[data-testid="stSegmentedControl"] [role="radio"] {
    min-height: var(--app-control-height) !important;
    width: 100% !important;
    justify-content: center !important;
    border-radius: 10px !important;
    color: var(--yt-text-muted) !important;
}
[data-testid="stSegmentedControl"] [aria-checked="true"],
[data-testid="stSegmentedControl"] [data-selected="true"] {
    background: linear-gradient(90deg, rgba(255,0,0,0.35), rgba(0,212,255,0.28)) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
}

.stToggle label, .stCheckbox label, .stRadio label, .stSelectbox label,
.stDateInput label, .stTextInput label, .stSlider label, .stNumberInput label {
    color: var(--yt-text-muted) !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 0.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}
.stTabs [data-baseweb="tab"] p {
    font-size: 14px;
    font-weight: 500;
    color: var(--yt-text-muted);
}
[aria-selected="true"] p { color: var(--yt-text) !important; font-weight: 600 !important; }

[data-testid="stExpander"] {
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: var(--app-radius-md) !important;
    background: rgba(15, 15, 35, 0.5) !important;
}
[data-testid="stExpander"] summary {
    font-family: var(--app-font-display);
    font-size: 13px;
    font-weight: 600;
    color: var(--yt-text-muted);
}

.yt-card {
    border-radius: var(--app-radius-lg);
    padding: 1.1rem 1.25rem;
    background: radial-gradient(circle at top left, rgba(255,255,255,0.06) 0%, rgba(22,33,62,0.96) 40%, rgba(6,6,20,0.98) 100%);
    border: 1px solid rgba(255, 255, 255, 0.09);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(12px);
    margin-bottom: 1.15rem;
    animation: fadeIn 0.35s ease-out;
}

.yt-callout-info {
    border-radius: var(--app-radius-md);
    padding: 1.05rem 1.2rem;
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.08) 0%, rgba(15, 15, 35, 0.92) 100%);
    border: 1px solid rgba(0, 212, 255, 0.22);
    border-left: 3px solid #00D4FF;
    color: #d0d0e0;
    margin-bottom: 1rem;
    line-height: 1.6;
    font-size: 14px;
}
.yt-callout-info strong { color: #FFFFFF; }
.yt-callout-info code {
    background: rgba(0, 0, 0, 0.35);
    color: #00D4FF;
    padding: 0.15rem 0.45rem;
    border-radius: 6px;
    font-family: var(--app-font-mono);
    font-size: 12px;
}

.yt-callout-recommend {
    border-radius: var(--app-radius-md);
    padding: 1.15rem 1.25rem;
    background: linear-gradient(135deg, rgba(255, 0, 0, 0.1) 0%, rgba(15, 15, 35, 0.94) 100%);
    border: 1px solid rgba(255, 0, 0, 0.28);
    box-shadow: 0 12px 40px rgba(255, 0, 0, 0.06);
    color: #e8e8f0;
    margin-bottom: 1.25rem;
    line-height: 1.6;
}
.yt-callout-recommend h4 {
    margin: 0 0 0.55rem;
    font-family: var(--app-font-display);
    color: #FF6B6B;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
}
.yt-callout-recommend ul {
    margin: 0;
    padding-left: 1.2rem;
    font-size: 14px;
    color: #e0e0ec;
    line-height: 1.62;
}
.yt-callout-recommend ul li { margin-bottom: 0.4rem; }

.yt-summary-panel {
    border-radius: var(--app-radius-lg);
    padding: 1.25rem 1.4rem;
    background: radial-gradient(circle at top left, rgba(255,255,255,0.05) 0%, rgba(22,33,62,0.9) 50%, rgba(10,10,25,0.95) 100%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.55);
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.yt-summary-panel::before {
    content: "";
    position: absolute;
    top: 0; left: 0; width: 4px; height: 100%;
    background: linear-gradient(180deg, #FF0000, #00D4FF);
    border-radius: 4px 0 0 4px;
}
.yt-summary-panel h3 {
    margin: 0 0 0.75rem;
    padding-left: 0.5rem;
    font-family: var(--app-font-display);
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #00D4FF;
}

.strategy-summary-list {
    margin: 0;
    padding-left: 1.5rem;
    color: #d0d0e0;
    font-size: 14px;
    line-height: 1.65;
}
.strategy-summary-list li { margin-bottom: 0.45rem; }
.strategy-summary-list strong { color: #FFFFFF; font-weight: 600; }
.strategy-summary-list em { color: #B0B0B0; font-style: normal; }

.app-section-shell { max-width: var(--app-section-width); margin: 0 auto 2rem; }
.app-command-shell { max-width: var(--app-command-width); margin: 0 auto 2rem; }
.app-section-title {
    font-family: var(--app-font-display);
    font-size: 1.6rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    color: var(--yt-text);
    margin-bottom: 0.25rem;
}
.app-section-copy {
    color: var(--yt-text-muted);
    font-size: 14px;
    line-height: 1.6;
    max-width: 720px;
}
.app-subsection-label {
    font-size: 10px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #8b8ba8;
    font-weight: 600;
    margin: 0.25rem 0 0.65rem;
}

.app-meta-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.4rem 0.75rem;
    border-radius: var(--app-radius-pill);
    background: rgba(22, 33, 62, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: var(--yt-text-muted);
    font-size: 12px;
}
.app-meta-pill strong { color: var(--yt-text); }
.app-meta-pill--state {
    background: rgba(0, 212, 255, 0.1);
    border-color: rgba(0, 212, 255, 0.28);
}

.keyword-chip {
    display: inline-flex;
    align-items: center;
    padding: 0.1rem 0.6rem;
    border-radius: 999px;
    margin: 0.12rem;
    font-size: 12px;
    font-weight: 500;
    background: linear-gradient(90deg, rgba(255,0,0,0.25), rgba(0,212,255,0.25));
    border: 1px solid rgba(255, 255, 255, 0.16);
    color: var(--yt-text);
    white-space: nowrap;
}

.thumb-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
    margin-top: 0.75rem;
}
.thumb-card {
    border-radius: 16px;
    overflow: hidden;
    background: #050511;
    border: 1px solid rgba(255, 255, 255, 0.18);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.85);
    transition: transform 0.16s ease-out, box-shadow 0.16s ease-out;
}
.thumb-card:hover {
    transform: translateY(-3px) scale(1.01);
    box-shadow: 0 18px 42px rgba(0, 0, 0, 0.95);
}
.thumb-card img { width: 100%; display: block; }
.thumb-card-footer {
    padding: 0.4rem 0.6rem 0.6rem;
    font-size: 12px;
    color: var(--yt-text-muted);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.metric-icon { display: none !important; }

div[data-testid="stCaption"] { color: #8b8ba8 !important; }

div[data-testid="stMarkdownContainer"] h1 { color: var(--yt-text); font-weight: 800; }
div[data-testid="stMarkdownContainer"] h2,
div[data-testid="stMarkdownContainer"] h3 { color: #e8e8f0; font-weight: 700; }

.fade-in {
    animation: fadeIn 0.4s ease-out;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
"""


def inject_shared_theme() -> None:
    st.markdown(APP_THEME_CSS, unsafe_allow_html=True)
