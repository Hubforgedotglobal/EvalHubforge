import streamlit as st
from openai import OpenAI
from prompts import toc_prompt, matrix_prompt, tor_prompt

# Initialize OpenAI client
client = OpenAI()

st.set_page_config(page_title="Evaluation Design Copilot")

st.title("🧠 Evaluation Design Copilot")
st.caption("Generate Theory of Change, Evaluation Matrix, and ToR — free for NGOs.")

# Step 1: Project input
project_text = st.text_area("📋 Paste your project description below:", height=300)

# Step 2: Evaluation Objective
if "eval_objective" not in st.session_state:
    if st.button("🎯 Generate Evaluation Objective"):
        objective_prompt = f"""Write a clear Evaluation Objective for the following project. State what the evaluation seeks to achieve, and for whom.

Project:
{project_text}
"""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using GPT-3.5 for lower cost
            messages=[{"role": "user", "content": objective_prompt}]
        )
        eval_objective = response.choices[0].message.content
        st.session_state["eval_objective"] = eval_objective
        st.success("✅ Evaluation Objective generated.")
        st.markdown(eval_objective)

# Step 3: Select what to generate
if "eval_objective" in st.session_state:
    st.markdown("---")
    st.subheader("🛠️ Generate Evaluation Tools")

    option = st.selectbox("Choose what you want to generate:",
                          ["Theory of Change", "Evaluation Matrix", "Terms of Reference"])

    if st.button("🚀 Generate Output"):
        if option == "Theory of Change":
            prompt = toc_prompt(project_text)
        elif option == "Evaluation Matrix":
            prompt = matrix_prompt(project_text, st.session_state["eval_objective"])
        elif option == "Terms of Reference":
            prompt = tor_prompt(project_text, st.session_state["eval_objective"])

        with st.spinner("Generating using GPT-3.5 Turbo..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            output = response.choices[0].message.content
            st.markdown(output)
