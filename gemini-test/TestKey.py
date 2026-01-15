import google.generativeai as genai

genai.configure(api_key="AIzaSyAsdsXmXpPceesmZ9eVloTM6z9Y2qenQlY")

try:
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Hello, Gemini! Are you working?")
    print(response.text)
except Exception as e:
    print("API key test failed: ", e)
    
    