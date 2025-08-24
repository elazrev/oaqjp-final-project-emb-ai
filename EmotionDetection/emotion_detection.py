import requests

def emotion_detector(text_to_analyse: str):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        emotions = result['emotionPredictions'][0]['emotion']
        sorted_emotions = sorted(emotions.items(), key=lambda item: item[1], reverse=True)
        dominant_emotion_name, dominant_emotion_score = sorted_emotions[0]

        ans_format = {
            "text": text_to_analyse,
            "emotions": emotions,
            "dominant emotion": {dominant_emotion_name: dominant_emotion_score}
        }

        return ans_format

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}




if __name__ == "__main__":
    print(emotion_detector("I am happy"))
    print(emotion_detector("I love this new technology"))
    print(emotion_detector("I hate cucumbers"))
    print(emotion_detector("I love my dog"))
    