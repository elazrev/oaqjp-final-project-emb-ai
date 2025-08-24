import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    emotions_test_dict = {
        "joy": "I am glad this happened",
        "anger": "I am really mad about this",
        "disgust": "I feel disgusted just hearing about this",
        "sadness": "I am so sad about this",
        "fear": "I am really afraid that this will happen"
    }

    def test_emotion_detector(self):
        
        for expected_emotion, statement in self.emotions_test_dict.items():
            res = emotion_detector(statement)
            dominant_emotion = next(iter(res['dominant emotion']))

            self.assertEqual(
                dominant_emotion,
                expected_emotion,
                msg=f"Expected '{expected_emotion}' but got '{dominant_emotion}' for input: '{statement}'"
            )




if __name__ == '__main__':
    unittest.main()