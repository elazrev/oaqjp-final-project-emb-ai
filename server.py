"""Flask server for emotion detection."""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def render_index_page():
    ''' This is the function to render the html interface
    '''
    return render_template('index.html')

@app.route('/emotionDetector', methods=["GET"])
def api_emotion_detector():
    """Analyzes emotions from user input text."""
    text = request.args.get('textToAnalyze', '')
    res = emotion_detector(text)
    
    if res['dominant_emotion'] == None:
        return "<b>Invalid text! Please try again!</b>", 400

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
    app.run(host="0.0.0.0", port=5000)
    