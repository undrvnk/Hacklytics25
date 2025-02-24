import google.generativeai as genai
import pandas as pd

df = pd.read_csv('data.csv', header=0)
model = genai.GenerativeModel('gemini-1.5-flash')
genai.configure(api_key="AIzaSyBUjhQ3iXYiG5kScdHBCCpcmifNM6iGhPE")

def ask_gemini(user_query):
    laptop_info = df[['brand', 'name', 'price', 'display_size', 'spec_rating', 'processor', 'CPU', 'Ram', 'ROM', 'GPU', 'OS']].to_dict(orient='records')
    prompt = (
        f"A customer asked for laptops with this request: {user_query}.\n\n"
        f"Here is the dataset containing information about laptops:\n\n{laptop_info}\n\n"
        f"Based on this dataset, provide a clear recommendation including the brand, name, price, and key specifications."
    )
    response = model.generate_content(prompt)
    return response.text.strip()

user_input = input("What do you want your laptop to be like? ")
response = ask_gemini(user_input)
print("AI Response:", response)