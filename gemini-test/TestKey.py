import google.generativeai as genai

genai.configure(api_key="API-key")

try:
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Hello, Gemini! Are you working?")
    print(response.text)
except Exception as e:
    print("API key test failed: ", e)
    
    
