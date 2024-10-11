'''' '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    '''endpoint for rendoring page'''
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detector():
    '''endpoint for getting emotion analysis of text'''
    text_to_analyze = request.args.get("textToAnalyze")

    responce = emotion_detector(text_to_analyze)

    if responce['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"""For the given statement, the system response is 'anger': {responce['anger']}, 'disgust': {responce['disgust']}, 'fear': {responce['fear']}, 'joy': {responce['joy']} and 'sadness': {responce['sadness']}. The dominant emotion is {responce['dominant_emotion']}."""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
