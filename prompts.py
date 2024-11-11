CATEGORIZATION_PROMPT = """Analyze and categorize each bullet point as follows:
1. Category: Either PROJECT, INTENTION, TODO, TASK, THOUGHT, or QUOTE
2. Project Type (if applicable):
   - Domain: Tech/Business/Creative/Research/Personal/Other
   - Nature: Development/Design/Analysis/Planning/Documentation/Infrastructure/Process/Other
   - Stack: Infer relevant technologies, tools, or methodologies needed
3. Impact Level: HIGH, MEDIUM, or LOW based on:
   - Potential value to stakeholders
   - Scope of influence
   - Long-term effects
   - Strategic importance
4. Impact Reasoning: Brief explanation of why this impact level was chosen
5. Time Estimation:
   - Duration: Estimated time to complete (e.g., "2 hours", "3 days", "2 weeks", "1 month")
   - Confidence: HIGH/MEDIUM/LOW confidence in this estimate
   - Rationale: Brief explanation of the time estimate
6. If it's a TODO, list any subtasks

Format the response as JSON with structure:
{{
    "items": [
        {{
            "text": "original bullet",
            "category": "category",
            "projectType": {{
                "domain": "domain type",
                "nature": "project nature",
                "stack": ["inferred technologies or methodologies"]
            }},
            "impact": {{
                "level": "HIGH/MEDIUM/LOW",
                "reasoning": "brief explanation"
            }},
            "timeEstimate": {{
                "duration": "estimated time",
                "confidence": "HIGH/MEDIUM/LOW",
                "rationale": "brief explanation"
            }},
            "subtasks": [] // only for TODOs
        }}
    ]
}}

Bullets:
{}"""

SYSTEM_PROMPT = "You are an analytical assistant that evaluates text to identify project types, required technologies, strategic importance, and provides realistic time estimations based on common development and business project timelines."