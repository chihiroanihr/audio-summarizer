'''
# Creating summarized chapters from podcasts

The Auto Chapters model summarizes audio data over time into chapters.
Chapters makes it easy for users to navigate and find specific information.
Each chapter contains the following:

- Summary
- One-line gist
- Headline
- Start and end timestamps

You'll send the auto_chapters parameter in your request, and then use chapters property from the response.
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

# Create a TranscriptionConfig with auto_chapter set to True.
config = aai.TranscriptionConfig(auto_chapters=True)

# Create a Transcriber object and pass in the configuration.
transcriber = aai.Transcriber(config=config)

# Pass the URL or file path to Transcriber.transcribe(). 
transcript = transcriber.transcribe(FILE_URL)

# You can access the chapter results from the chapters attribute in the transcript.
if transcript.error:
    print(transcript.error)
else:
    transcript_texts = []
    for chapter in transcript.chapters:
        # print(f"Chapter Start Time: {chapter.start}\
        #     \nChapter End Time: {chapter.end}\
        #     \nChapter Gist: {chapter.gist}\
        #     \nChapter Headline: {chapter.headline}\
        #     \nChapter Summary: {chapter.summary}\
        #     \n")
        transcript_text = f"Chapter Start Time: {chapter.start}\
            \nChapter End Time: {chapter.end}\
            \nChapter Gist: {chapter.gist}\
            \nChapter Headline: {chapter.headline}\
            \nChapter Summary: {chapter.summary}\
            \n"
        transcript_texts.append(transcript_text)
    write_result('\n'.join(transcript_texts))

'''
Your automatic chapters are located in the chapters key of the API response.
Each entry contains:
    - A summary of the chapter
    - A one-line gist
    - A chapter headline
    - Start and end timestamps.
'''


# Reference:
# https://www.assemblyai.com/docs/guides/creating-summarized-chapters-from-podcasts