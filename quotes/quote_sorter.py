from openai import OpenAI
from quotes_prompt import get_prompt
import os
from dotenv import load_dotenv

def sort_quotes():
    # Load environment variables
    load_dotenv()
    
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Get quotes from file
    quotes_text = get_prompt()
    
    # Process quotes
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a quote analyzer. Organize quotes into meaningful categories and identify key themes."},
            {"role": "user", "content": quotes_text}
        ]
    )
    
    # Write results
    with open('sorted.log', 'w') as f:
        f.write(response.choices[0].message.content)

if __name__ == "__main__":
    sort_quotes()