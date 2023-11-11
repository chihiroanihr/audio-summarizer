'''
# Transcribing an audio file

Start by making sure the `assemblyai` package is installed.
If not, you can install it by running the following command:
pip install -U assemblyai

Note: Some macOS users may need to use `pip3` instead of `pip`.
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

# Transcribe audio function
def transcribe_audio(enable_speaker_diarization=False):
    config = None
    
    # Enable the Speaker diarization model to detect who said what.
    if enable_speaker_diarization:
        config = aai.TranscriptionConfig(speaker_labels=True)
    
    # Create a new Transcriber and configure it to use your API key.
    transcriber = aai.Transcriber()
    
    # Submit an audio file for transcription
    transcript = transcriber.transcribe(FILE_URL, config)
    
    # YouTube URLs are not supported. If you want to transcribe a YouTube video, you need to download the audio first.
    # You can also transcribe a local file by passing in a file path
    # FILE_URL = './path/to/file.mp3'
    
    if transcript.error:
         print(transcript.error)
    else:
        if enable_speaker_diarization:
            # In addition to the full transcript, you now have access to utterances from each speaker.
            speaker_texts = []
            if enable_speaker_diarization:
                for utterance in transcript.utterances:
                    # print(f"Speaker {utterance.speaker}: {utterance.text}")
                    speaker_text = f"Speaker {utterance.speaker}: {utterance.text}"
                    speaker_texts.append(speaker_text)
            write_result('\n'.join(speaker_texts))
        else:
            write_result(transcript.text)
            # print(transcript.text)

# User Input
while True:
    user_input = input(
        "\n"
        "[1] Default Transcribe\n"
        "[2] Speaker Diarization\n"
        "Enter your number ([q] to quit): "
    )
    if user_input == 'q':
        sys.exit()
    elif user_input == '1':
        transcribe_audio()
    elif user_input == '2':
        transcribe_audio(enable_speaker_diarization=True)
    else:
        print("Please enter a valid option.")


# Reference:
# https://www.assemblyai.com/docs/getting-started/transcribe-an-audio-file