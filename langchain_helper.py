import os
import ast
import requests
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
def call_gemini(prompt: str):
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()

    # Print the raw response to debug structure
    # print("Raw API response:\n", data)

    return data['candidates'][0]['content']['parts'][0]['text']

    
def generate_restaurant_menu_with_name_and_item(cuisine: str):
    # Step 1: Restaurant name
    prompt_name = f"Suggest one fancy name for a {cuisine} restaurant. "
    "Return only the name. No explanations, no context, no quotes, no brackets, nothing else."
    "Return only the name. Do not include any description."
    restaurant_name = call_gemini(prompt_name)
    # print("restaurant name is \n",restaurant_name)

    # Step 2: Menu items
    prompt_items = (
        f"List 5-10 menu items for the restaurant named '{restaurant_name}' which is a {cuisine} restaurant.\n"
        "Return ONLY the dish names, one per line. Include local language and English in brackets.\n"
        "Do NOT include any introductions, explanations, numbers, bullets, or context.\n"
        "Do NOT write phrases like 'Here are the items' or 'Okay'.\n"
        "Do NOT add anything other than the dish names.\n"
        "Do NOT include more than 12 items and atlest include 10 items always.\n"
    )

    raw_menu_items = call_gemini(prompt_items)
    menu_item=raw_menu_items.split('\n')[:10]
    # print("menu items are \n",menu_item)

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_item
    }
if __name__ == "__main__":
    result = generate_restaurant_menu_with_name_and_item("indian")
    print(result)
