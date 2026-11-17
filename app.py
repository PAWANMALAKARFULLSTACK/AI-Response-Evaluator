
import streamlit as st
import csv
import os
from datetime import datetime

st.set_page_config(
    page_title="AI Response Evaluator",
    page_icon="🤖"
)

st.title("🤖 AI Response Evaluator")
st.write("Evaluate AI-generated responses.")

with st.form("evaluation_form"):

    prompt = st.text_area("Enter AI Prompt")
    response = st.text_area("Enter AI Response")

    st.subheader("Evaluate Response")

    accuracy = st.slider("Accuracy", 1, 5, 3)
    relevance = st.slider("Relevance", 1, 5, 3)
    clarity = st.slider("Clarity", 1, 5, 3)
    completeness = st.slider("Completeness", 1, 5, 3)

    feedback = st.text_area("Your Feedback")

    submit = st.form_submit_button("Evaluate")

if submit:

    if not prompt.strip() or not response.strip():
        st.error("Please enter both prompt and response.")

    else:
        scores = [
            accuracy,
            relevance,
            clarity,
            completeness
        ]

        overall = round(sum(scores) / 4, 2)

        file_exists = os.path.isfile("evaluations.csv")

        with open(
            "evaluations.csv",
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "Date", "Prompt", "Response",
                    "Accuracy", "Relevance",
                    "Clarity", "Completeness",
                    "Overall Score", "Feedback"
                ])

            writer.writerow([
                datetime.now(), prompt, response,
                accuracy, relevance, clarity,
                completeness, overall, feedback
            ])

        st.success("Evaluation Completed!")

        st.metric("Overall Score", f"{overall}/5")

        st.write("### Evaluation Summary")
        st.write("Accuracy:", accuracy, "/5")
        st.write("Relevance:", relevance, "/5")
        st.write("Clarity:", clarity, "/5")
        st.write("Completeness:", completeness, "/5")

        st.info("Evaluation saved successfully.")
