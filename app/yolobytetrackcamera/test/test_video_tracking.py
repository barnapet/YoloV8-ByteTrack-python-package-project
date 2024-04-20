import unittest
from unittest.mock import patch
from yolobytetrackcamera import start_video_tracking

class TestVideoTracking(unittest.TestCase):
    @patch('yolobytetrackcamera.model_choose')
    def test_start_video_tracking_default_params(self, mock_model_choose):
        # Mock model_choose behavior (replace with specific behavior for your model)
        mock_model_choose.return_value.track.return_value = "tracking_results"  # Simulate tracking results

        # Define test arguments
        selected_model = 2
        video_path = "video-ending.mp4"

        # Test with default parameters
        results = start_video_tracking(selected_model, video_path)

        # Assert model_choose is called with correct arguments
        mock_model_choose.assert_called_once_with(selected_model, source=video_path, show=True,
                                                  conf=0.3, iou=0.5, tracker="bytetrack.yaml")

        # Assert returned results
        self.assertEqual(results, "tracking_results")  # Adjust based on your model's output

if __name__ == '__main__':
    unittest.main()