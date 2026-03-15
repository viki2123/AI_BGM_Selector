import requests
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv("JAMENDO_CLIENT_ID")

def fetch_music(query):
    # Jamendo v3.0 Tracks endpoint
    url = "https://api.jamendo.com/v3.0/tracks/"
    
    params = {
        'client_id': CLIENT_ID,
        'format': 'json',
        'limit': 5,
        'search': query,       # Your AI keywords go here
        'include': 'musicinfo', # Gives us genre/mood data
        'audioformat': 'mp32'  # Standard MP3 format
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            # Jamendo returns results in a 'results' list
            return data.get('results', [])
        else:
            print(f"Jamendo Error: {response.status_code}")
            return []
    except Exception as e:
        print(f"Connection Error: {e}")
        return []