from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        test_joy_result = emotion_detector('I am glad this happened')
        self.assertEqual(test_joy_result['dominant_emotion'], 'joy')

        test_anger_result = emotion_detector('I am really mad about this')
        self.assertEqual(test_anger_result['dominant_emotion'], 'anger')

        test_disgust_result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(test_disgust_result['dominant_emotion'], 'disgust')

        test_sadness_result = emotion_detector('I am so sad about this')
        self.assertEqual(test_sadness_result['dominant_emotion'], 'sadness')

        test_fear_result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(test_fear_result['dominant_emotion'], 'fear')

unittest.main()