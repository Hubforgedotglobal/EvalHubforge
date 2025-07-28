def toc_prompt(project_text):
    return f"""You are an M&E expert. Create a detailed Theory of Change. Break it into Inputs, Activities, Outputs, Outcomes, and Impact.

Project:
{project_text}

Return as markdown with clear headings."""


def matrix_prompt(project_text, eval_objective):
    return f"""Based on the project and objective, generate a 5-column Evaluation Matrix:
1. Evaluation Questions
2. Indicators
3. Data Sources
4. Methods
5. Frequency

Evaluation Objective:
{eval_objective}

Project:
{project_text}

Return as a markdown table."""


def tor_prompt(project_text, eval_objective):
    return f"""Write a Terms of Reference (ToR) for an external evaluation. Include:
- Purpose
- Scope
- Methodology
- Deliverables
- Timeline
- Roles & Responsibilities

Evaluation Objective:
{eval_objective}

Project:
{project_text}"""
