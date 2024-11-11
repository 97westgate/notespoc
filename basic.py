from dotenv import load_dotenv
import os
import openai
from prompts import CATEGORIZATION_PROMPT, SYSTEM_PROMPT
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    filename='logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

def read_bullets_from_file(filename):
    with open(filename, 'r') as file:
        # Read lines and remove empty ones
        return [line.strip() for line in file.readlines() if line.strip()]

def categorize_bullets(bullets):
    try:
        logging.info(f"Input bullets:\n{bullets}")
        
        prompt = CATEGORIZATION_PROMPT.format('\n'.join(bullets))
        response = openai.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        logging.info(f"Response:\n{response.choices[0].message.content}")
        print(response.choices[0].message.content)
        
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        raise

# Read from input.txt and process
bullets = read_bullets_from_file('input.txt')
categorize_bullets(bullets)