CATEGORIZATION_PROMPT = """You are analyzing a large collection of personal/professional notes. Please provide your analysis in JSON format.

1. Initial Classification:
   - Is this an actionable item or reference material?
   - Are there multiple distinct ideas? (Split if: new emoji, new checkbox, topic shift, audience change)
   - What's the primary intent? (Project/Task/Reference/Idea/Goal)

2. For each distinct idea, analyze efficiently:
   - Quick Stats:
      * Urgency: NOW/SOON/LATER/REFERENCE
      * Complexity: SIMPLE/MEDIUM/COMPLEX
      * Dependencies: STANDALONE/NEEDS-PREREQUISITES
   
   - Project Context:
      * Domain: Tech/Business/Creative/Marketing/Research/Personal/Content/Social/Other
      * Nature: Development/Design/Analysis/Planning/Content/Growth/Other
      * Required Resources: ["key tools", "platforms", "skills needed"]
   
   - Implementation:
      * Estimated Timeline: "duration"
      * Key Risks: ["major concerns"]
      * Next Actions: ["immediate next steps"]

3. Pattern Recognition:
   - Related to previous notes? Link by theme/project
   - Part of larger initiative?
   - Recurring theme?

Format your response as a JSON object with the following structure:
{{
    "items": [
        {{
            "originalText": "full text",
            "ideas": [
                {{
                    "text": "distinct idea",
                    "quickStats": {{
                        "urgency": "level",
                        "complexity": "level",
                        "dependencies": "type"
                    }},
                    "context": {{
                        "domain": "type",
                        "nature": "type",
                        "resources": []
                    }},
                    "execution": {{
                        "timeline": "estimate",
                        "risks": [],
                        "nextActions": []
                    }},
                    "patterns": {{
                        "relatedThemes": [],
                        "initiative": "name if part of larger project"
                    }}
                }}
            ]
        }}
    ]
}}

Notes to analyze:
{}"""

SYSTEM_PROMPT = "You are an efficient note analysis system that quickly identifies patterns, separates distinct ideas, and provides actionable insights across large collections of notes. You will respond in JSON format following the specified structure."