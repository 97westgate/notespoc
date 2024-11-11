CATEGORIZATION_PROMPT = """Analyze each bullet point as follows. If a bullet contains multiple distinct ideas (indicated by emojis, new sentences, or clear topic shifts), please separate and analyze them individually:

1. First, separate distinct ideas:
   - New ideas often start with emojis, bullets, or checkboxes
   - A shift in topic or audience indicates a new idea
   - Different project types or goals suggest separate items

2. Then for each distinct idea, analyze:
   - Category: Either PROJECT, INTENTION, TODO, TASK, THOUGHT, or QUOTE
   - Project Type (if applicable):
      - Domain: Tech/Business/Creative/Marketing/Research/Personal/Content/Social/Other
      - Nature: Development/Design/Analysis/Planning/Documentation/Infrastructure/Process/Content Creation/Brand Building/Community Management/Growth Hacking/Other
      - Stack: Infer relevant platforms, tools, or methodologies needed
   - Impact Level: HIGH, MEDIUM, or LOW based on:
      - Potential value to stakeholders
      - Scope of influence
      - Long-term effects
      - Strategic importance
   - Impact Reasoning: Brief explanation of why this impact level was chosen
   - Time Estimation:
      - Duration: Estimated time to complete (e.g., "2 hours", "3 days", "2 weeks", "1 month")
      - Confidence: HIGH/MEDIUM/LOW confidence in this estimate
      - Rationale: Brief explanation of the time estimate
   - If it's a TODO, list any subtasks

Format the response as JSON with structure:
{{
    "items": [
        {{
            "originalText": "full original text",
            "separatedIdeas": [
                {{
                    "text": "distinct idea 1",
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
                    "subtasks": []
                }}
            ]
        }}
    ]
}}

Bullets:
{}"""

SYSTEM_PROMPT = "You are an analytical assistant that evaluates text to identify project types across technical, creative, and marketing domains. You understand both traditional project management and modern digital/social media initiatives, providing realistic assessments based on industry standards."