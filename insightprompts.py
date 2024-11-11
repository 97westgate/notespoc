INSIGHT_PROMPT = """Analyze the collection of categorized notes and provide strategic insights. Please provide your analysis in JSON format.

Consider:
1. Pattern Analysis:
   - Recurring themes or project types
   - Most common categories
   - Domains that appear frequently
   - Time investment patterns

2. Strategic Insights:
   - High-impact opportunities
   - Resource bottlenecks
   - Quick wins vs long-term investments
   - Potential synergies between projects
   - Underutilized areas or missed opportunities

3. Recommendations:
   - Priority adjustments
   - Resource allocation suggestions
   - Skill development needs
   - Strategic pivots or focus areas

Format your response as a JSON object with the following structure:
{{
    "patterns": {{
        "dominantThemes": ["list of main themes"],
        "frequentCategories": ["most common categories"],
        "timeDistribution": "analysis of time allocation",
        "domainFocus": "primary domain focus areas"
    }},
    "insights": {{
        "highImpactOpportunities": [
            {{
                "description": "opportunity description",
                "rationale": "why this matters",
                "potentialValue": "expected impact"
            }}
        ],
        "resourceBottlenecks": [
            {{
                "area": "bottleneck area",
                "impact": "how it affects progress",
                "solution": "potential resolution"
            }}
        ],
        "quickWins": ["immediately actionable items"],
        "synergies": ["potential project combinations"]
    }},
    "recommendations": {{
        "priorities": ["priority adjustments"],
        "resources": ["resource allocation suggestions"],
        "skills": ["skill development needs"],
        "strategy": ["strategic direction suggestions"]
    }}
}}

Notes to analyze:
{}"""

INSIGHT_SYSTEM_PROMPT = "You are a strategic advisor that analyzes patterns in projects and tasks to provide actionable insights and recommendations. You will respond in JSON format following the specified structure." 