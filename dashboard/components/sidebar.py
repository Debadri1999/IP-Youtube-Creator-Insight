import streamlit as st


PAGE_OPTIONS = [
    "Channel Analysis",
    "Channel Insights",
    "Thumbnails",
    "Outlier Finder",
    "Ytuber",
    "Tools",
    "Deployment",
]

_LEGACY_PAGE_MAP = {
    "Recommendations": "Thumbnails",
}


def _normalize_page_name(value: str) -> str:
    page_name = _LEGACY_PAGE_MAP.get(str(value or "").strip(), str(value or "").strip())
    if page_name not in PAGE_OPTIONS:
        return PAGE_OPTIONS[0]
    return page_name


def render_sidebar_header() -> None:
    """Logo and label above Streamlit's built-in navigation."""
    st.markdown(
        """
        <div style="display:flex;align-items:center;gap:0.55rem;margin-bottom:0.35rem;">
            <div style="width:28px;height:20px;border-radius:6px;background:linear-gradient(135deg,#FF0000,#CC0000);display:flex;align-items:center;justify-content:center;box-shadow:0 6px 14px rgba(0,0,0,0.65);">
                <span style="font-size:14px;font-weight:800;color:#FFFFFF;">▶</span>
            </div>
            <div>
                <div style="font-weight:700;font-size:14px;letter-spacing:0.08em;text-transform:uppercase;color:#FFFFFF;">Creator Insights</div>
                <div style="font-size:11px;color:#B0B0B0;">YouTube IP V5 · Purdue × Google</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div style='margin:0.15rem 0 0.5rem;font-size:11px;color:#B0B0B0;'>Navigate</div>",
        unsafe_allow_html=True,
    )


def render_sidebar_footer() -> None:
    """Hints and attribution below the navigation menu."""
    st.markdown(
        "<hr style='border-color:rgba(255,255,255,0.10);margin:0.5rem 0 0.6rem;' />",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="font-size:11px;color:#B0B0B0;margin-bottom:0.4rem;">
            Use <code>.env</code> locally or Streamlit secrets for <code>YOUTUBE_API_KEY</code> (or <code>YOUTUBE_API_KEYS</code>),
            <code>GEMINI_API_KEY</code>, and <code>OPENAI_API_KEY</code>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="font-size:10px;color:#747494;margin-top:0.6rem;line-height:1.45;">
            <strong>Purdue University × Google</strong><br/>
            Daniels School of Business — MS BAIM Capstone<br/>
            <span style="opacity:0.85;">Repo: royayushkr/Youtube-IP-V5</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
