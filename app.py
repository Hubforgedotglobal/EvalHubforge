import streamlit as st
import openai
import os
from prompts import toc_prompt, matrix_prompt, tor_prompt

st.set_page_config(page_title="Evaluation Design Copilot")

st.title("🧠 Evaluation Design Copilot")
st.caption("Build ToC, Evaluation Matrix, and ToR — free for NGOs and change-makers.")

project_text = st.text_area("Paste your project description here 👇", height=300)

if "eval_objective" not in st.session_state:
    if st.button("Generate Evaluation Objective"):
        prompt = f"""Write a clear Evaluation Objective based on this project. State what the evaluation seeks to achieve and for whom.

Project:
{project_text}"""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        eval_objective = response["choices"][0]["message"]["content"]
        st.session_state["eval_objective"] = eval_objective
        st.success("Evaluation Objective generated.")
        st.markdown(eval_objective)

if "eval_objective" in st.session_state:
    option = st.selectbox("Choose what to generate:", ["Theory of Change", "Evaluation Matrix", "Terms of Reference"])

    if st.button("Generate"):
        if option == "Theory of Change":
            prompt = toc_prompt(project_text)
        elif option == "Evaluation Matrix":
            prompt = matrix_prompt(project_text, st.session_state["eval_objective"])
        elif option == "Terms of Reference":
            prompt = tor_prompt(project_text, st.session_state["eval_objective"])

        with st.spinner("Generating..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown(response["choices"][0]["message"]["content"])
