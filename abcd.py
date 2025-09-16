from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    data = request.get_json()
    text = data.get('text')
    language = data.get('language', 'en')

    if not text:
        return "Please provide text to convert.", 400

    try:
        tts = gTTS(text=text, lang=language, slow=False)
        audio_file = "output.mp3"
        tts.save(audio_file)
        return send_file(audio_file, mimetype="audio/mp3", as_attachment=True, download_name="speech.mp3")
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
