from dotenv import load_dotenv
import os
import openai
from prompts import CATEGORIZATION_PROMPT, SYSTEM_PROMPT

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

def read_bullets_from_file(filename):
    with open(filename, 'r') as file:
        # Read lines and remove empty ones
        return [line.strip() for line in file.readlines() if line.strip()]

def categorize_bullets(bullets):
    prompt = CATEGORIZATION_PROMPT.format('\n'.join(bullets))
    
    response = openai.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )
    
    print(response.choices[0].message.content)

# Read from input.txt and process
bullets = read_bullets_from_file('input.txt')
categorize_bullets(bullets)