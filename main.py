import os
import sys
import assemblyai as aai
from writeToFile import write_result

# Replace with your API token
API_KEY = os.environ["API_ASSEMBLY-AI"]

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"


def setup_api(api_key):
    aai.settings.api_key = api_key

def transcribe_audio(file_url, enable_speaker_diarization=False):
    config = aai.TranscriptionConfig(speaker_labels=enable_speaker_diarization)
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(file_url)

    if transcript.error:
        print(transcript.error)
    else:
        if enable_speaker_diarization:
            speaker_texts = []
            if enable_speaker_diarization:
                for utterance in transcript.utterances:
                    # print(f"Speaker {utterance.speaker}: {utterance.text}")
                    speaker_text = f"Speaker {utterance.speaker}: {utterance.text}"
                    speaker_texts.append(speaker_text)
            write_result('\n'.join(speaker_texts))
        else:
            write_result(transcript.text)

def generate_subtitles(file_url, subtitle_format):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_url)

    if transcript.error:
        print(transcript.error)
    else:
        if subtitle_format == '3':
            write_result(transcript.export_subtitles_srt())
        else:
            write_result(transcript.export_subtitles_vtt())

def extract_highlights(file_url):
    config = aai.TranscriptionConfig(auto_highlights=True)
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(file_url)

    if transcript.error:
        print(transcript.error)
    else:
        highlight_texts = []
        for result in transcript.auto_highlights.results:
            # print(f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}, Timestamps: {result.timestamps}")
            highlight_text = f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}, Timestamps: {result.timestamps}"
            highlight_texts.append(highlight_text)
        write_result('\n'.join(highlight_texts))

def extract_chapters(file_url):
    config = aai.TranscriptionConfig(auto_chapters=True)
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(file_url)

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

def main():
    setup_api(API_KEY)
    
    while True:
        user_input = input(
            "\n"
            "[1] Default Transcribe\n"
            "[2] Speaker Diarization\n"
            "[3] Generate Subtitles (SRT)\n"
            "[4] Generate Subtitles (VTT)\n"
            "[5] Extract Highlights\n"
            "[6] Extract Chapters\n"
            "Enter your choice ([q] to quit): "
        )

        if user_input == 'q':
            sys.exit()
        elif user_input == '1':
            transcribe_audio(FILE_URL)
        elif user_input == '2':
            transcribe_audio(FILE_URL, enable_speaker_diarization=True)
        elif user_input in ('3', '4'):
            generate_subtitles(FILE_URL, user_input)
        elif user_input == '5':
            extract_highlights(FILE_URL)
        elif user_input == '6':
            extract_chapters(FILE_URL)
        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()
