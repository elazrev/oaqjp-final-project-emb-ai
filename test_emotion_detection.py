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
    def test_joy(self):
        self._run_emotion_test("joy")
    def test_anger(self):
        self._run_emotion_test("anger")
    def test_disgust(self):
        self._run_emotion_test("disgust")
    def test_sadness(self):
        self._run_emotion_test("sadness")
    def test_fear(self):
        self._run_emotion_test("fear")

    def _run_emotion_test(self, emotion_key):

        text = self.emotions_test_dict[emotion_key]
        res = emotion_detector(text)
        dominant = next(iter(res['dominant emotion']))
        print(f"\n{emotion_key.upper()} Test → Input: '{text}' → Detected: '{dominant}'")
        self.assertEqual(
            dominant,
            emotion_key,
            msg=f"Expected '{emotion_key}' but got '{dominant}' for input: '{text}'"
        )



if __name__ == '__main__':
    unittest.main()