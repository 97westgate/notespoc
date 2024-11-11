from dotenv import load_dotenv
import os
import openai
from largeprompts import CATEGORIZATION_PROMPT, SYSTEM_PROMPT
from insightprompts import INSIGHT_PROMPT, INSIGHT_SYSTEM_PROMPT
import logging
from datetime import datetime
import json

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
        
        # Parse the response into a Python dictionary
        categorized_data = json.loads(response.choices[0].message.content)
        logging.info(f"Response:\n{json.dumps(categorized_data, indent=2)}")
        
        return categorized_data  # Return the parsed data
        
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        raise

def analyze_insights(categorized_data):
    try:
        logging.info("Generating insights from categorized data")
        
        # Format the data for the insights prompt
        formatted_data = json.dumps(categorized_data, indent=2)
        
        response = openai.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": INSIGHT_SYSTEM_PROMPT},
                {"role": "user", "content": INSIGHT_PROMPT.format(formatted_data)}
            ],
            response_format={"type": "json_object"}
        )
        
        insights_data = json.loads(response.choices[0].message.content)
        logging.info(f"Insights generated:\n{json.dumps(insights_data, indent=2)}")
        return insights_data
        
    except Exception as e:
        logging.error(f"Error generating insights: {str(e)}")
        raise

# Main execution
bullets = read_bullets_from_file('input.txt')
categorized_data = categorize_bullets(bullets)  # Store the categorized data
insights = analyze_insights(categorized_data)   # Pass the stored data to insights

# Print both results
print("\nCategorized Data:")
print(json.dumps(categorized_data, indent=2))
print("\nInsights:")
print(json.dumps(insights, indent=2))