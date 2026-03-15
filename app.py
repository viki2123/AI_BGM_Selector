# import streamlit as st
# from utils.ai_logic import analyze_script_for_music
# from utils.music_api import fetch_music

# st.set_page_config(page_title="Smart BGM Finder", page_icon="🎬")

# st.title("🎬 Smart Reel Music Matcher")
# st.caption("AI-powered music selection for your content")

# script = st.text_area("What is your Reel about?", height=150, 
#                       placeholder="Paste your script or describe the video vibe here...")

# if st.button("Generate Music Recommendations", type="primary"):
#     if script:
#         with st.status("AI is reading your script...", expanded=True) as status:
#             # Step 1: Get keywords from Gemini
#             st.write("Determining the mood...")
#             keywords = analyze_script_for_music(script)
#             st.write(f"Vibe detected: **{keywords}**")
            
#             # Step 2: Search Pixabay
#             st.write("Searching Pixabay library...")
#             music_results = fetch_music(keywords)
#             status.update(label="Matching complete!", state="complete", expanded=False)

#         if music_results:
#             st.subheader(f"🎵 Top Matches for: {keywords}")
#             for track in music_results:
#                 # Create a nice UI card for each track
#                 with st.container(border=True):
#                     col1, col2 = st.columns([3, 1])
#                     with col1:
#                         # Show the track title (often found in 'tags') and duration
#                         st.write(f"**Vibe:** {track.get('tags', 'Background Music')}")
#                         st.write(f"👤 Artist: {track.get('user')}")
                        
#                         # Pixabay provides a preview URL for music tracks
#                         preview_url = track.get('previewURL')
#                         if preview_url:
#                             st.audio(preview_url)
                    
#                     with col2:
#                         # Link to the actual Pixabay music page for download
#                         st.link_button("Download", track.get('pageURL'), use_container_width=True)
#         else:
#             st.error("Couldn't find music. Try simplifying your script.")
#     else:
#         st.warning("Please enter some text first!")


import streamlit as st
from utils.ai_logic import analyze_script_for_music
from utils.music_api import fetch_music

st.set_page_config(page_title="Smart BGM Finder", page_icon="🎬")

st.title("🎬 Smart Reel Music Matcher")
st.caption("AI-powered music selection via Jamendo")

script = st.text_area("What is your Reel about?", height=150, 
                      placeholder="Paste your script or describe the video vibe here...")

if st.button("Generate Music Recommendations", type="primary"):
    if script:
        with st.status("AI is reading your script...", expanded=True) as status:
            # Step 1: Get keywords from Gemini
            st.write("Determining the mood...")
            keywords = analyze_script_for_music(script)
            st.write(f"Vibe detected: **{keywords}**")
            
            # Step 2: Search Jamendo
            st.write("Searching Jamendo library...")
            music_results = fetch_music(keywords)
            status.update(label="Matching complete!", state="complete", expanded=False)

        if music_results:
            st.subheader(f"🎵 Top Matches for: {keywords}")
            for track in music_results:
                # Create a nice UI card for each Jamendo track
                with st.container(border=True):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        # Jamendo uses 'name' for the song title and 'artist_name'
                        st.write(f"**Track:** {track.get('name', 'Unknown Title')}")
                        st.write(f"👤 Artist: {track.get('artist_name', 'Unknown Artist')}")
                        
                        # Jamendo provides a direct MP3 link in the 'audio' field
                        audio_url = track.get('audio')
                        if audio_url:
                            st.audio(audio_url)
                    
                    with col2:
                        # Jamendo uses 'shareurl' for the public track page
                        st.link_button("View Track", track.get('shareurl'), use_container_width=True)
        else:
            st.error("No music found on Jamendo for these keywords. Try a different script!")
    else:
        st.warning("Please enter some text first!")