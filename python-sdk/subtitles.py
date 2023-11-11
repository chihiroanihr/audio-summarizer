'''
# Generating subtitles for audios

You can export your completed transcripts in SRT or VTT format, which can be used for subtitles and closed captions in videos. 

- SRT (SubRip Text) files are commonly used to store subtitles for videos. 
  The format is plain text, and it contains the timing information for each subtitle along with the subtitle text itself.
- WEBVTT (Web Video Text Tracks), which is a standard format for displaying timed text tracks (such as subtitles or captions) 
  within HTML5 video.
'''

import os
import sys
import assemblyai as aai

# Add the parent directory of the script to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from writeToFile import write_result

# Replace with your API token
aai.settings.api_key = os.environ["API_ASSEMBLY-AI"]

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

# User Input
while True:
    user_input = input(
        "\n"
        "[1] SRT subtitles\n"
        "[2] VTT subtitles\n"
        "Enter your number ([q] to quit): "
    )
    
    if user_input == 'q':
        sys.exit()
        
    elif user_input in ('1', '2'):
        # Create a new Transcriber and configure it to use your API key.
        transcriber = aai.Transcriber()
        # Submit an audio file for transcription
        transcript = transcriber.transcribe(FILE_URL)
        
        if transcript.error:
            print(transcript.error)
        else:
            if user_input == '1':
                # Export SRT subtitles
                write_result(transcript.export_subtitles_srt())
                # print(transcript.export_subtitles_srt())
            else:
                # Export VTT subtitles
                write_result(transcript.export_subtitles_vtt())
                # print(transcript.export_subtitles_vtt())
    else:
        print("Please enter a valid option.")
        
# Reference:
# https://www.assemblyai.com/docs/guides/generating-subtitles-for-videos