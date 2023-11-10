import requests

endpoint = "https://api.assembly.ai.com/v2/transcript"

json = {
    "audio_url": "https://www.youtube.com/watch?v=8q2q_820Sx4",
    "sumamrization": True,
    "summary_type": "bullets" # paragraph, headline, gist
}

headers = {
    "authorization": "", # Your API Key
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)
print(response.json)


# Reference: 
# https://www.assemblyai.com/blog/automatically-summarize-audio-and-video-files-at-scale-with-ai/