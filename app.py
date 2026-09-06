# ==========================================
# SECTION 1: IMPORTS
# ==========================================
import streamlit as st
import datetime
import os
import random
from typing import Dict, Any
 
import database

# ==========================================
# SECTION 2: APP INITIALIZATION
# (DB setup + Streamlit page config)
# ==========================================

database.init_db()
 
st.set_page_config(
    page_title="CET- Anonymous Confessions",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ==========================================
# SECTION 3: STYLING
# Loads external CSS file
# ==========================================
def load_css():
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
 
load_css()
# ==========================================
# SECTION 4: SESSION STATE INITIALIZATION
# (Persists login status & liked posts across reruns)
# ==========================================
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "liked_confessions" not in st.session_state:
    st.session_state["liked_confessions"] = set()

# ==========================================
# SECTION 5: STATIC DATA / CONSTANTS
# (Categories, moods, anonymous persona pool)
# ==========================================

CATEGORIES = [
    "General",
    "Deep Secret",
    "Crush & Romance",
    "College & Campus",
    "Funny & Wild",
    "Late Night Thoughts",
    "Regret & Vent",
    "Wholesome"
]
 
CATEGORY_ICONS = {
    "General": "📢",
    "Deep Secret": "🤫",
    "Crush & Romance": "💘",
    "College & Campus": "🎓",
    "Funny & Wild": "😂",
    "Late Night Thoughts": "💭",
    "Regret & Vent": "💔",
    "Wholesome": "🌟"
}
 
CATEGORY_PILL_CLASS = {
    "Deep Secret": "pill-secret",
    "Crush & Romance": "pill-crush",
    "College & Campus": "pill-college",
    "Funny & Wild": "pill-funny",
    "Late Night Thoughts": "pill-thoughts",
    "Regret & Vent": "pill-regret",
    "Wholesome": "pill-wholesome",
    "General": "pill-general"
}
 
MOODS = [
    ("🤫", "Shh / Secretive"),
    ("💘", "In Love / Crush"),
    ("😂", "Wild / Hilarious"),
    ("💭", "Reflective / Pensive"),
    ("💔", "Heartbroken / Venting"),
    ("🍕", "Random / Casual"),
    ("😈", "Chaotic / Mischievous"),
    ("🥺", "Vulnerable / Emotional")
]
 
ANONYMOUS_PERSONAS = [
    "Spiderman", "Phantom", "Shadow", "Shaji Papan", "Incognito",
    "hulk", "Pink Panther", "Echo", "MaskedSoul",
    "Cipher", "Minnal Murali", "Batman", "StarlightSeeker"
]
 
 
# ==========================================
# SECTION 6: HELPER FUNCTIONS
# (Formatting utilities used by the feed)
# ==========================================


# ==========================================
# SECTION 7: SIDEBAR — AUTHENTICATION & NAVIGATION
# (Login / Signup forms + anonymity guarantee note)
# ==========================================

# ==========================================
# SECTION 8: MAIN CONTENT — HERO HEADER
# (Top banner with title/subtitle/anonymity badge)
# ==========================================
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">CET Confessions</div>
        <div class="hero-subtitle">
            Unburden your mind. Share your untold thoughts, deep secrets, crazy campus stories, or unspoken crushes completely anonymously.
        </div>
        <div class="anonymity-badge">
            <span>🛡️</span> Zero-Knowledge Anonymity Guaranteed • No Admin Tracking
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
 
 

# ==========================================
# SECTION 9: STATS BAR
# (Total confessions / likes / users / top category)
# ==========================================


# ==========================================
# SECTION 10: CONFESSION SUBMISSION FORM
# (Only visible/usable when logged in)
# ==========================================


