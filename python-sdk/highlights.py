'''
# Identifying highlights in audio and video files

The Key Phrases model identifies significant words and phrases in your transcript and 
lets you to extract the most important concepts or highlights from your audio or video file.

You'll send the auto_highlights parameter in your request, and then use the auto_highlights_result property in the response.
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

# Create a TranscriptionConfig with auto_highlights set to True.
config = aai.TranscriptionConfig(auto_highlights=True)

# Create a Transcriber object and pass in the configuration.
transcriber = aai.Transcriber(config=config)

# Pass the URL or file path to Transcriber.transcribe(). 
transcript = transcriber.transcribe(FILE_URL)

# You can access automatic highlights from transcript.auto_highlights.results.
if transcript.error:
    print(transcript.error)
else:
    highlight_texts = []
    for result in transcript.auto_highlights.results:
        # print(f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}, Timestamps: {result.timestamps}")
        highlight_text = f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}, Timestamps: {result.timestamps}"
        highlight_texts.append(highlight_text)
    write_result('\n'.join(highlight_texts))
        
'''
The auto_highlights_result key in the response contains a list of all the highlights found in the transcription text. 
For each entry, the results include:
    - Text of the phrase or word detected (text)
    - How many times it occurred in the text (count)
    - Its relevancy score (rank)
    - A list of all the timestamps (timestamps), in milliseconds, in the audio where the phrase or word is spoken
'''


# Reference:
# https://www.assemblyai.com/docs/guides/identifying-highlights-in-audio-or-video-files