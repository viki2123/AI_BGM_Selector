import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
# We use the latest 2026 Gemini 3 Flash for fast, cheap reasoning
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_script_for_music(script_text):
    """
    Analyzes the script and returns 3-4 perfect search keywords.
    """
    prompt = f"""
    You are an expert video editor for Instagram Reels. 
    Analyze the following script and provide exactly 3 keywords that describe the 
    ideal background music mood, genre, or vibe. 
    
    Script: "{script_text}"
    
    Respond ONLY with the keywords separated by commas. 
    Example: cinematic, inspiring, piano
    
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt
        )
        # We clean the response to make sure it's just the tags
        keywords = response.text.strip().replace(" ", "")
        return keywords
    except Exception as e:
        print(f"AI Error: {e}")
        return "lofi, chill, background" # Fallback if AI fails