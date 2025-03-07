import streamlit as st
import openai

# Configure OpenAI API Key
# openai.api_key = "your_openai_api_key"
from openai import OpenAI

client = OpenAI(
  api_key= "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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);


# Streamlit UI
st.title("🎙️ AI InterviewMate - Practice Your Interviews")
st.write("Your AI-powered mock interview assistant. Type your answers below, and AI will provide feedback.")

# User inputs job role
job_role = st.text_input("Enter the job role you're interviewing for (e.g., Software Engineer, Data Analyst):")

# Generate an interview question
if st.button("Start Interview"):
    prompt = f"Generate a tough behavioral interview question for a {job_role}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    question = response["choices"][0]["message"]["content"]
    st.session_state["question"] = question
    st.write(f"**Question:** {question}")

# User submits an answer
if "question" in st.session_state:
    user_answer = st.text_area("Your Answer:")
    
    if st.button("Get AI Feedback"):
        feedback_prompt = f"Evaluate this answer for a {job_role} interview. Provide constructive feedback, improvement areas, and a score out of 10:\n\n{user_answer}"
        feedback_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": feedback_prompt}]
        )
        feedback = feedback_response["choices"][0]["message"]["content"]
        st.write("### 📢 AI Feedback:")
        st.write(feedback)
