# Transcribe audio with Assembly AI

### This is a command-line application that utilizes the free version of the [**Assembly AI API**](https://www.assemblyai.com/docs).

This app transcribes any audio files into texts. There are 4 types of transcribe methods:

1.  **Transcribe** an video/audio file.

    - You can also enable **Speaker Diarization** to detect speakers in an video/audio file.

2.  Generating **subtitles** for video/audio file.

    You can export your completed transcripts in SRT or VTT format, which can be used for subtitles and closed captions in videos.

    - **SRT (SubRip Text)** files are commonly used to store subtitles for videos.
      The format is plain text, and it contains the timing information for each subtitle along with the subtitle text itself.
    - **WEBVTT (Web Video Text Tracks)**, which is a standard format for displaying timed text tracks (such as subtitles or captions)
      within HTML5 video.

3.  Identifying **highlights** in video/audio files

    The Key Phrases model identifies significant words and phrases in your transcript and lets you to extract the most important concepts or highlights from your audio or video file.

4.  Creating **summarized chapters** from podcasts

    The Auto Chapters model summarizes audio data over time into chapters. Chapters makes it easy for users to navigate and find specific information.

    Each chapter contains the following:

    - Summary
    - One-line gist
    - Headline
    - Start and end timestamps

#### [Assembly AI - Home page](https://www.assemblyai.com/)

#### [Assembly AI - Documentation](https://www.assemblyai.com/docs)

#### [Assembly AI - Dashboard (Log in required)](https://www.assemblyai.com/app)

You can also try their playground website (upload your audio / video file).

#### [**Assembly AI - Playground**](https://www.assemblyai.com/playground/source)

## Requirements

- [Python](https://www.python.org/) installed
- API Key from [Assembly AI](https://www.assemblyai.com/app)

## Packages

### Create Virtual Environment

#### Unix/MacOS

```shell
python3 -m venv env
```

#### Windows

```shell
py -m venv env
```

### Activate Virtual Environment

#### Unix/MacOS

```shell
source env/bin/activate
```

#### Windows

```shell
.\env\Scripts\activate
```

### Install Packages

#### Unix/MacOS

```shell
python3 -m pip install -r requirements.txt
```

#### Windows

```shell
py -m pip install -r requirements.txt
```

### Export Current Environment Config File

#### Unix/MacOS

```shell
python3 -m pip freeze > requirements.txt
```

#### Windows

```shell
py -m pip freeze > requirements.txt
```

#### [Source Website](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
