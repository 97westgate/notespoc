QUOTE_SORTER_PROMPT = """You are a quote analyzer and organizer. 
Given a list of quotes, you will:
1. Check for semantic duplicates (quotes that convey the same message even if worded differently)
2. Organize quotes into meaningful categories based on their themes and messages
3. Output the analysis in a clear, markdown-formatted structure

Current quotes to analyze:
{quotes}

Please organize these quotes and format your response as markdown with:
- A "Potential Duplicates" section if any are found
- Meaningful categories with brief explanations
- Quotes listed under their respective categories (quotes can appear in multiple categories if relevant)
"""

def get_prompt(quotes_file='quotes.log'):
    with open(quotes_file, 'r') as f:
        quotes = f.read()
    
    return QUOTE_SORTER_PROMPT.format(quotes=quotes)