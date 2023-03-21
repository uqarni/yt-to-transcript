def yt_to_transcript(yt_url):

    from pytube import YouTube
    import openai 
    from pydub import AudioSegment #haven't used yet
    import os
    import random

    yt = YouTube(yt_url)
    random_hex = hex(random.randrange(16**8))[2:].upper().zfill(8)
    audiofilename = "audio-" + random_hex + ".mp3"
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio_stream.download(output_path='audiofiles/', filename=audiofilename)

    audio_file= open("audiofiles/"+audiofilename, "rb")
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    transcript = openai.Audio.transcribe("whisper-1", audio_file, response_format = "text")

    transcriptfilename = "transcript-"+random_hex+".txt"
    with open("transcripts/"+transcriptfilename, 'w') as file:
        file.write(transcript)
    
    return transcriptfilename


def audiodeleter():
    import os
    
    folder_path = "audiofiles"
    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the path is a file and not a directory
        if os.path.isfile(file_path):
            # Remove the file
            os.remove(file_path)