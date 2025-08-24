from flask import(
    Flask,
    request,
    jsonify
)
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello world"), 200

@app.route('/emotionDetector', methods=["GET"])
def api_emotion_detector():
    text = request.args['textToAnalyze']
    res = emotion_detector(text)
    return res

if __name__ == "__main__":
    app.run(debug=True)
