from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
# Debug: Print the API key to verify it's being read
print(f"API Key found: {'Yes' if openai_api_key else 'No'}")

def read_bullets_from_file(filename):
    with open(filename, 'r') as file:
        # Read lines and remove empty ones
        return [line.strip() for line in file.readlines() if line.strip()]

def categorize_bullets(bullets):
    prompt = """Categorize each bullet point as either a PROJECT, TODO, TASK, THOUGHT, or QUOTE. 
    If it's a TODO, identify any subtasks. Format the response as JSON.
    
    Bullets:
    {}""".format('\n'.join(bullets))
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that categorizes text into PROJECTs, TODOs, TASKS, THOUGHTs, and QUOTEs."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )
    
    # Just log the response for first iteration
    print(response.choices[0].message.content)

# Read from input.txt and process
bullets = read_bullets_from_file('input.txt')
categorize_bullets(bullets)