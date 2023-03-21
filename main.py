import streamlit as st
from function import yt_to_transcript, audiodeleter
import os

# Define the Streamlit app
def main():
    st.title("YouTube Transcript Downloader")

    video_url = st.text_input("Enter YouTube Video URL:")

    if video_url:
        go_button = st.button("Go")
        if go_button:
            try:
                file_path = yt_to_transcript(video_url)
                if os.path.exists("transcripts/"+file_path):
                    st.success("Transcript Generated!")
                    audiodeleter()
                    with open("transcripts/"+file_path, "r", encoding="utf-8") as f:
                        transcript_text = f.read()
                    st.download_button(
                        label="Download Now",
                        data=transcript_text,
                        file_name=file_path,
                        mime="text/plain",
                    )
            except Exception as e:
                st.error(f"Error: {e}")

# Run the app
if __name__ == "__main__":
    main()