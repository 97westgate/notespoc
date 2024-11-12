NATURAL_CATEGORIZATION_PROMPT = """Analyze how this content would naturally be organized. Consider:

1. Time-based Organization:
   - Now/Soon/Later
   - Today/This Week/This Month/Someday
   - Urgent/Important/Neither (Eisenhower Matrix)

2. Energy-based Organization:
   - Quick wins (5-minute tasks)
   - Focus work (deep thinking required)
   - Creative work (needs inspiration)
   - Administrative (routine tasks)

3. Context-based Organization:
   - Location (home, office, online)
   - Tools needed (computer, phone, specific apps)
   - Mental state (focused, creative, routine)
   - Time of day (morning tasks, evening reflection)

4. Purpose-based Organization:
   - Goals (what you want to achieve)
   - Habits (regular practices)
   - Learning (things to study/understand)
   - Ideas (things to explore)
   - Reference (information to keep)

5. Natural Language Categories:
   - Let the content suggest its own groupings
   - Look for common themes or patterns
   - Consider how the user might search for this later

Please analyze the content and suggest the most natural organization method(s) for this specific set of items.

Content to analyze:
{content}
""" 