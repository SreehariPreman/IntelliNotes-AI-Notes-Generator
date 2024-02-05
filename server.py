from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import re


app = Flask(__name__)

def extract_transcript(youtube_video_url):
    video_id = youtube_video_url.split("=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = ""
    for i in transcript:
        transcript_text += " " + i["text"]
    return transcript_text

def clean_text(text):
    cleaned_text = re.sub(r'\*\*(.*?)\*\*', '', text)  # Remove bold formatting
    cleaned_text = re.sub(r'\*', '', cleaned_text)  # Remove asterisks
    return cleaned_text

def format_text_to_html(text):
    formatted_text = ""
    current_heading = None

    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue

        if line.startswith("-"):
            if current_heading:
                formatted_text += "</ul>"
            formatted_text += "<b>" + line.strip('- ') + "</b><br>"
            current_heading = line.strip('- ')
            formatted_text += "<ul>"
        elif line.startswith("    -"):
            formatted_text += "<li>" + line.strip(' -') + "</li>"
        elif line.startswith("    "):
            formatted_text += "<li>" + line.strip() + "</li>"
    
    if current_heading:
        formatted_text += "</ul>"

    return formatted_text

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@app.route('/', methods=['GET', 'POST'])
def generate_notes():
    if request.method == 'POST':
        youtube_video_url = request.form['youtube_url']
        text = extract_transcript(youtube_video_url)
        prompt = """
            your task is to provide detailed notes based on the text I'll provide. 
            Assume the role of a student and generate comprehensive notes covering the concepts mentioned in text.
            """
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt + text)
        cleaned_notes = clean_text(response.text)
        formatted_notes = format_text_to_html(cleaned_notes)
        return render_template('index.html', notes=formatted_notes)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
