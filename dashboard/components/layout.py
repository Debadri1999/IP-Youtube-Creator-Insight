"""Shared shell: page heroes and wayfinding copy aligned to the Creator Insights UX."""

from __future__ import annotations

from typing import Dict, Tuple

import streamlit as st

# (kicker, one-line value prop) — kicker is small caps; shown under the global product subtitle.
PAGE_CONTEXT: Dict[str, Tuple[str, str]] = {
    "Channel Analysis": (
        "Dataset intelligence",
        "Committed CSV benchmarks — filters, engagement, and chart-backed summaries.",
    ),
    "Channel Insights": (
        "Owned-channel depth",
        "BERTopic-ready topics, momentum views, and refresh-to-disk SQLite snapshots.",
    ),
    "Thumbnails": (
        "Creative lab",
        "Score against your dataset or generate/export thumbnails with Gemini or OpenAI.",
    ),
    "Outlier Finder": (
        "Breakout research",
        "Quota-aware scans, explainable scores, charts, and structured AI research.",
    ),
    "Ytuber": (
        "Command center",
        "Channel search, audits, AI studio, calendar — jump to Outlier Finder in one click.",
    ),
    "Tools": (
        "Media & utilities",
        "Transcription, shorts helpers, and other workflows (ffmpeg where noted).",
    ),
}


def render_page_hero(page: str) -> None:
    """Top-of-page hero: gradient product title + Purdue × Google line + page context."""
    ctx = PAGE_CONTEXT.get(page)
    if not ctx:
        return
    kicker, blurb = ctx
    st.markdown(
        f"""
        <div class="fade-in app-hero-block" style="margin-bottom:1.35rem;">
            <div class="app-hero-kicker">{kicker}</div>
            <p class="app-hero-blurb">{blurb}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
