import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyBUjhQ3iXYiG5kScdHBCCpcmifNM6iGhPE")

def classify_user_input(user_input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Suggest me a laptop based on this request: {user_input}. Options: Office Work, Gaming, Video Editing, Art & Design, 3D Modeling."
    response = model.generate_content(prompt)
    # Print the response object to inspect its structure
    print(response)
    # Adjust based on the actual response structure
    return response.text.strip()  # Example, adjust as needed

# Call the classify_user_input function
user_input = input("Enter a laptop use case: ")
classification = classify_user_input(user_input)
print("Classification:", classification)
