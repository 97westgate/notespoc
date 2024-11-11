CATEGORIZATION_PROMPT = """Analyze and categorize each bullet point as follows:
1. Category: Either PROJECT, INTENTION, TODO, TASK, THOUGHT, or QUOTE
2. Impact Level: HIGH, MEDIUM, or LOW based on:
   - Potential value to stakeholders
   - Scope of influence
   - Long-term effects
   - Strategic importance
3. Impact Reasoning: Brief explanation of why this impact level was chosen
4. Time Estimation:
   - Duration: Estimated time to complete (e.g., "2 hours", "3 days", "2 weeks", "1 month")
   - Confidence: HIGH/MEDIUM/LOW confidence in this estimate
   - Rationale: Brief explanation of the time estimate
5. If it's a TODO, list any subtasks

Format the response as JSON with structure:
{{
    "items": [
        {{
            "text": "original bullet",
            "category": "category",
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

SYSTEM_PROMPT = "You are an analytical assistant that evaluates text for strategic importance, business impact, and provides realistic time estimations based on common software development and business project timelines."