import streamlit as st
import json
import os
import base64
from datetime import datetime, timedelta

st.set_page_config(page_title="JLPT N4 Study Hub", layout="centered")
st.markdown("""
    <style>
    /* רקע האפליקציה - ורוד פסטלי חמים ורך מאוד (#fff5f7) */
    .stApp {
        background-color: #fff5f7;
        color: #4a4a4a;
        font-family: 'Comic Sans MS', 'Bubblegum Sans', 'Quicksand', sans-serif;
    }

    /* עיצוב סרגל הצד - גוון לבנדר-פסטלי רך */
    section[data-testid="stSidebar"] {
        background-color: #f3f0ff;
        color: #4a4a4a;
    }

    /* כרטיסיות ואזורים עם פינות עגולות בולטות ומסגרת פסטלית רכה */
    div[data-testid="stVerticalBlock"] > div {
        border-radius: 16px;
    }

    /* כפתורים בעיצוב Kawaii עגול וצבעוני (ורוד-בונבוניירה) */
    .stButton>button {
        background-color: #ffb7b2;
        color: #5c4033;
        border-radius: 20px;
        border: 2px solid #ff9797;
        padding: 0.6rem 1.4rem;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(255, 183, 178, 0.4);
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #ff9797;
        color: #ffffff;
        transform: scale(1.03);
    }

    /* עיצוב לשוניות (Tabs) בצורת בועות פסטליות */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #e2f0cb;
        border-radius: 12px;
        padding: 8px 18px;
        color: #3b5323;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffb7b2 !important;
        color: #5c4033 !important;
        border: 2px solid #ff9797;
    }

    /* כותרות ידידותיות ועגולות */
    h1, h2, h3 {
        color: #d46a6a;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

DATA_FILE = "data.json"
PROGRESS_FILE = "progress.json"

INTERVALS = {0: 0, 1: 1, 2: 3, 3: 7, 4: 14, 5: 30}


@st.cache_data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"grammar": [], "vocab": [], "kanji": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {"srs": {}, "correct_count": 0, "total_attempts": 0}
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_progress(progress_data):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress_data, f, ensure_ascii=False, indent=2)


def update_srs(item_id, is_correct):
    if "srs" not in st.session_state.progress:
        st.session_state.progress["srs"] = {}

    item_data = st.session_state.progress["srs"].get(item_id, {"level": 0, "next_review": ""})

    if is_correct:
        item_data["level"] = min(item_data["level"] + 1, 5)
    else:
        item_data["level"] = 0

    days_to_add = INTERVALS[item_data["level"]]
    next_date = datetime.now() + timedelta(days=days_to_add)
    item_data["next_review"] = next_date.strftime("%Y-%m-%d")

    st.session_state.progress["srs"][item_id] = item_data
    save_progress(st.session_state.progress)


# פונקציה להצגה חלקה של GIF מונפש (עוקפת את בעיית הפריים היחיד)
def display_animated_gif(gif_path, width=120, use_sidebar=False):
    if os.path.exists(gif_path):
        with open(gif_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode("utf-8")
        html_code = f'<div style="text-align: center;"><img src="data:image/gif;base64,{b64}" width="{width}"></div>'
        if use_sidebar:
            st.sidebar.markdown(html_code, unsafe_allow_html=True)
        else:
            st.markdown(html_code, unsafe_allow_html=True)


data = load_data()

if "progress" not in st.session_state:
    st.session_state.progress = load_progress()

st.sidebar.title("🏮 JLPT N4 Tracker")

# הצגת פיקאצ'ו המונפש בסרגל הצד
display_animated_gif("pikachu.gif", width=120, use_sidebar=True)

st.sidebar.markdown("""
    <div style="background-color: #fff9db; padding: 10px; border-radius: 10px; border: 2px dashed #f59f00; text-align: center; margin-top: 10px;">
        <p style="color: #d9480f; margin: 0; font-weight: bold; font-size: 14px;">⚡ ピカチュウ: 頑張ってね!</p>
        <p style="color: #495057; margin: 0; font-size: 12px;">תנו בראש היום!</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.divider()
mode = st.sidebar.radio("בחר מודול תרגול:", ["Grammar (Cloze)", "Vocabulary", "Kanji"])

total_attempts = st.session_state.progress.get("total_attempts", 0)
correct_count = st.session_state.progress.get("correct_count", 0)
accuracy = (correct_count / total_attempts * 100) if total_attempts > 0 else 0

st.sidebar.metric("אחוז דיוק כללי", f"{accuracy:.1f}%")

if st.sidebar.button("אפס התקדמות"):
    st.session_state.progress = {"srs": {}, "correct_count": 0, "total_attempts": 0}
    save_progress(st.session_state.progress)
    st.rerun()

today_str = datetime.now().strftime("%Y-%m-%d")

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if mode == "Grammar (Cloze)":
    st.title("📝 Grammar Practice")

    due_items = [
        item for item in data.get("grammar", [])
        if st.session_state.progress.get("srs", {}).get(item["id"], {}).get("next_review", today_str) <= today_str
    ]

    if not due_items:
        st.success("🎉 סיימת את כל תרגולי הדקדוק להיום! חזור מחר.")
    else:
        item = due_items[0]

        if st.session_state.last_result:
            if st.session_state.last_result['correct']:
                st.balloons()
                display_animated_gif("totoro.gif", width=140, use_sidebar=False)
                st.success("🌸 素晴らしい! נכון מאוד! 🎉")
            else:
                display_animated_gif("kirby.gif", width=140, use_sidebar=False)
                st.error(f"💦 לא מדויק. התשובה היא: {st.session_state.last_result['answer']}")
            st.write(f"**משפט מלא:** {st.session_state.last_result['full']}")

            if st.button("השאלה הבאה ➡️"):
                st.session_state.last_result = None
                st.rerun()
        else:
            st.caption(f"נקודת דקדוק: {item['grammar']}")
            st.info(f"משמעות באנגלית: {item['english']}")
            st.markdown(f"### {item['cloze_sentence']}")

            user_input = st.text_input("הקלד את התשובה (ברומאג'י, היראגאנה או קאנג'י):", key=f"g_in_{item['id']}")

            if st.button("בדוק תשובה"):
                st.session_state.progress["total_attempts"] += 1
                is_correct = (user_input.strip() == item["answer"])
                update_srs(item["id"], is_correct)

                if is_correct:
                    st.session_state.progress["correct_count"] += 1
                save_progress(st.session_state.progress)

                st.session_state.last_result = {
                    'correct': is_correct,
                    'answer': item["answer"],
                    'full': item["full_sentence"]
                }
                st.rerun()

elif mode == "Vocabulary":
    st.title("📖 Vocabulary Practice")
    due_items = [
        item for item in data.get("vocab", [])
        if st.session_state.progress.get("srs", {}).get(item["id"], {}).get("next_review", today_str) <= today_str
    ]

    if not due_items:
        st.success("🎉 סיימת את כל תרגולי אוצר המילים להיום!")
    else:
        item = due_items[0]
        st.markdown(f"## {item['word']}")

        show_meaning = st.checkbox("הצג קריאה ותרגום", key=f"v_show_{item['id']}")
        if show_meaning:
            st.write(f"**קריאה:** {item['reading']}")
            st.write(f"**משמעות:** {item['meaning']}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("זכרתי היטב", type="primary"):
                st.balloons()
                display_animated_gif("totoro.gif", width=140, use_sidebar=False)
                update_srs(item["id"], True)
                st.rerun()
        with col2:
            if st.button("לא זכרתי / טעיתי"):
                display_animated_gif("kirby.gif", width=140, use_sidebar=False)
                update_srs(item["id"], False)
                st.rerun()

elif mode == "Kanji":
    st.title("🈸 Kanji Practice")
    due_items = [
        item for item in data.get("kanji", [])
        if st.session_state.progress.get("srs", {}).get(item["id"], {}).get("next_review", today_str) <= today_str
    ]

    if not due_items:
        st.success("🎉 סיימת את כל תרגולי הקאנג'י להיום!")
    else:
        item = due_items[0]
        st.markdown(f"# {item['kanji']}")

        show_details = st.checkbox("הצג פירוט", key=f"k_show_{item['id']}")
        if show_details:
            st.write(f"**On'yomi:** {item['onyomi']}")
            st.write(f"**Kun'yomi:** {item['kunyomi']}")
            st.write(f"**משמעות:** {item['meaning']}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("זכרתי היטב", type="primary"):
                st.balloons()
                display_animated_gif("totoro.gif", width=140, use_sidebar=False)
                update_srs(item["id"], True)
                st.rerun()
        with col2:
            if st.button("לא זכרתי / טעיתי"):
                display_animated_gif("kirby.gif", width=140, use_sidebar=False)
                update_srs(item["id"], False)
                st.rerun()
