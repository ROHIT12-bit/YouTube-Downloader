from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route("/download", methods=["POST"])
def download():
    url = request.json.get("url")
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    path = stream.download()
    return jsonify({"file": path}), 200

@app.route("/")
def home():
    return "YouTube Downloader API is running!"

if __name__ == "__main__":
    app.run()
