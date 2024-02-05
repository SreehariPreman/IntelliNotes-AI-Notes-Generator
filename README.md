# summarize-tube
This web application allows users to generate notes or summaries based on the transcript of a YouTube video. The user simply needs to enter the URL of the YouTube video, and the application will extract the transcript, generate notes from it, and display the result.

## Features

- **Transcript Extraction**: Extracts the transcript of a YouTube video using the YouTube Transcript API.
- **Notes Generation**: Generates notes or summaries based on the extracted transcript using artificial intelligence techniques.
- **Material Design**: Provides a user-friendly interface with a Material Design-inspired layout and appearance.

## Usage

To use the application, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Obtain a GOOGLE API KEY from the Google Cloud Console.
4. Set your GOOGLE API KEY as an environment variable named `GOOGLE_API_KEY`.
5. Run the Flask application using `python app.py`.
6. Open your web browser and navigate to `http://localhost:5000`.
7. Enter the URL of a YouTube video in the input field and click "Generate Notes".
8. Wait for the notes to be generated. A loader animation will be displayed during this process.
9. Once the notes are generated, they will be displayed on the screen.

## Dependencies

- Flask
- python-dotenv
- youtube-transcript-api
- google-generativeai

