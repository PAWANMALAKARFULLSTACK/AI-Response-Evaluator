
import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="AI Response Evaluator",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Response Evaluator")
st.write("Evaluate AI-generated responses easily.")

st.subheader("Enter AI Prompt")
prompt = st.text_area("Enter your question")

st.subheader("Enter AI Response")
response = st.text_area("Enter AI response")

st.subheader("Evaluation Scores")

accuracy = st.slider("Accuracy", 1, 5, 3)
relevance = st.slider("Relevance", 1, 5, 3)
clarity = st.slider("Clarity", 1, 5, 3)
completeness = st.slider("Completeness", 1, 5, 3)

feedback = st.text_area("Feedback")

if st.button("Evaluate"):

    if not prompt.strip() or not response.strip():
        st.error("Please enter both Prompt and Response.")

    else:
        scores = [
            accuracy,
            relevance,
            clarity,
            completeness
        ]

        overall_score = sum(scores) / len(scores)

        st.success("Evaluation Completed!")

        st.metric(
            "Overall Score",
            f"{overall_score:.2f}/5"
        )

        st.write("### Evaluation Summary")
        st.write(f"Accuracy: {accuracy}/5")
        st.write(f"Relevance: {relevance}/5")
        st.write(f"Clarity: {clarity}/5")
        st.write(f"Completeness: {completeness}/5")

        st.info(feedback if feedback.strip() else "No feedback provided.")

        data = {
            "Prompt": prompt,
            "Response": response,
            "Accuracy": accuracy,
            "Relevance": relevance,
            "Clarity": clarity,
            "Completeness": completeness,
            "Overall Score": overall_score,
            "Feedback": feedback
        }

        df = pd.DataFrame([data])

        file_exists = os.path.exists("evaluations.csv")

        df.to_csv(
            "evaluations.csv",
            mode="a",
            header=not file_exists,
            index=False
        )

        st.success("Evaluation saved successfully!")
