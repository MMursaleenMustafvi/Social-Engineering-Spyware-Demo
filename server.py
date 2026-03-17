from flask import Flask, request, send_file
import time
import tempfile

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_drive_service():

    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)


drive_service = get_drive_service()


def index():
    return send_file("index.html")


def static_files(filename):
    return send_file(filename)


def upload():

    video = request.files.get("video")

    print("Video received:", video)

    if not video:
        return "No video"

    filename = str(int(time.time())) + "_video.webm"

    temp = tempfile.NamedTemporaryFile(delete=False)
    video.save(temp.name)

    media = MediaFileUpload(temp.name, mimetype='video/webm')

    file = drive_service.files().create(
        media_body=media,
        body={'name': filename},
        fields='id'
    ).execute()

    print("Uploaded File ID:", file.get("id"))

    return "uploaded"


app.add_url_rule("/", "index", index)
app.add_url_rule("/upload", "upload", upload, methods=["POST"])
app.add_url_rule("/<path:filename>", "static_files", static_files)

if __name__ == "__main__":
    app.run(port=3000)