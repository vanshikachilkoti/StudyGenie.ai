import streamlit as st
from PIL import Image
import requests
from datetime import date

st.set_page_config(page_title="StudyGenie.ai", page_icon="📚")
st.title("📚 StudyGenie.ai – Your AI-Powered Curriculum Builder")
# Load logo
logo = Image.open("static/logo.png")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, width=200)


st.markdown("""
Welcome to **StudyGenie.ai**!  
Tell us about your learning goals, and we'll generate a personalized, weekly roadmap just for you — and email it too!
""")

with st.form("study_form"):
    topic = st.text_input("🧠 What do you want to learn?", placeholder="e.g., Data Science, Web Development")

    subtopics = st.text_input("🔍 Any specific subtopics or areas of interest?", 
                               placeholder="e.g., Python, Machine Learning, Django")

    level = st.selectbox("📚 What is your current proficiency level?", 
                         ["Beginner", "Intermediate", "Advanced"])

    goal = st.text_input("🎯 What is your learning goal?", 
                         placeholder="e.g., Crack FAANG interviews, build a project, get certified")

    hours = st.slider("⏰ How many hours can you study per week?", 1, 40, 5)

    deadline = st.date_input("📅 When do you want to complete this roadmap?", value=date.today())

    formats = st.multiselect("🧾 Preferred content types:", [
        "YouTube", "Blogs", "Official Documentation", 
        "MOOCs", "Research Papers", "GitHub Projects", 
        "Podcasts", "Forums"
    ])

    learning_style = st.selectbox("🧠 What’s your preferred learning style?", 
                                  ["Visual (videos, diagrams)", 
                                   "Auditory (talks, podcasts)", 
                                   "Hands-on (projects, coding)"])

    email = st.text_input("📩 Where should we email your personalized roadmap?")

    add_to_calendar = st.checkbox("🗓️ Add roadmap to my Google Calendar (optional)")

    submitted = st.form_submit_button("✨ Generate My Roadmap")

if submitted:
    if not topic or not email:
        st.warning("Please enter both your topic and email address.")
    else:
        with st.spinner("Generating your roadmap..."):
            try:
                res = requests.post("http://localhost:5000/generate-roadmap", json={
                    "topic": topic,
                    "subtopics": subtopics,
                    "level": level,
                    "goal": goal,
                    "hours": hours,
                    "deadline": str(deadline),
                    "formats": formats,
                    "learning_style": learning_style,
                    "email": email,
                    "add_to_calendar": add_to_calendar
                })

                if res.status_code == 200:
                    roadmap = res.json()["roadmap"]
                    st.success("✅ Roadmap generated and emailed to you!")
                    st.markdown("---")
                    st.subheader("📅 Your Personalized Study Plan:")
                    st.markdown(roadmap)
                else:
                    st.error(f"❌ Error: {res.json().get('error', 'Something went wrong')}")
            except Exception as e:
                st.error(f"❌ Request failed: {e}")
