import unittest
from unittest.mock import patch
from yolobytetrackcamera import start_video_tracking

class TestVideoTracking(unittest.TestCase):
    @patch('yolobytetrackcamera.model_choose')
    def test_invalid_selected_model(self, mock_model_choose):
        selected_model = 6
        video_path = "video-ending.mp4"
        conf = 0.3
        iou = 0.5
        tracker = "bytetrack.yaml"

        mock_model_choose.side_effect = ValueError("Invalid model number")

        with self.assertRaises(ValueError):
            start_video_tracking(selected_model, video_path, conf=conf, iou=iou, tracker=tracker)

if __name__ == '__main__':
    unittest.main()