"""Flask server for emotion detection."""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Returns greeting message."""
    return jsonify(message="Hello world"), 200

@app.route('/emotionDetector', methods=["GET"])
def api_emotion_detector():
    """Analyzes emotions from user input text."""
    text = request.args.get('textToAnalyze', '')
    res = emotion_detector(text)

    if res['dominant_emotion'] is None:
        return jsonify(message="Invalid text! Please try again!"), 400

    return f"""<p>
    For the given statement, the system response is <br>
    'anger': {res['anger']}, <br>
    'disgust': {res['disgust']}, <br>
    'fear': {res['fear']}, <br>
    'joy': {res['joy']}<br> 
    and 'sadness': {res['sadness']}.<br> 
    The dominant emotion is <b>{res['dominant_emotion']}</b>.
    </p>""", 200

if __name__ == "__main__":
    app.run(debug=True)
    