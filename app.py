import os
from dotenv import load_dotenv
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

youtube_video_url ="https://www.youtube.com/watch?v=YrSUxgiwoFk&ab_channel=GPBEducation"


def extract_transcript(youtube_video_url):
    video_id = youtube_video_url.split("=")[1]

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    transcript_text = ""
    for i in transcript:
        transcript_text += " " + i["text"]

    return transcript_text


text = extract_transcript(youtube_video_url)
prompt = """
    your task is to provide detailed notes based on the text I'll provide. 
    Assume the role of a student and generate comprehensive notes covering the concepts mentioned in text.
    """

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(prompt + text)
print(response.text)