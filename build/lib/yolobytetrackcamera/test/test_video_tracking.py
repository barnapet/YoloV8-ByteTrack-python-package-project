import unittest
from unittest.mock import patch
from yolobytetrackcamera import start_video_tracking, TrackingConfig

class TestVideoTracking(unittest.TestCase):
    @patch('yolobytetrackcamera.model_choose')
    def test_start_video_tracking_default_config(self, mock_model_choose):
        # Mock model_choose behavior (replace with specific behavior for your model)
        mock_model_choose.return_value.track.return_value = "tracking_results"  # Simulate tracking results

        # Define test arguments
        selected_model = 2
        video_path = "test_video.mp4"

        # Test with default configuration
        results = start_video_tracking(selected_model, video_path)

        # Assert model_choose is called with correct arguments
        mock_model_choose.assert_called_once_with(selected_model, source=video_path, show=True,
                                                  conf=0.3, iou=0.5, tracker="bytetrack.yaml")

        # Assert returned results
        self.assertEqual(results, "tracking_results")  # Adjust based on your model's output

    def test_start_video_tracking_custom_config(self, mock_model_choose):
        # Mock model_choose behavior (same as before)
        mock_model_choose.return_value.track.return_value = "tracking_results"

        # Define test arguments
        selected_model = 3
        video_path = "another_video.mp4"
        custom_config = TrackingConfig(conf=0.7, iou=0.8, tracker="custom_tracker.yaml")

        # Test with custom configuration
        results = start_video_tracking(selected_model, video_path, custom_config)

        # Assert model_choose is called with arguments from custom config
        mock_model_choose.assert_called_once_with(selected_model, source=video_path, show=True,
                                                  conf=custom_config.conf, iou=custom_config.iou,
                                                  tracker=custom_config.tracker)

        # Assert returned results
        self.assertEqual(results, "tracking_results")  # Adjust based on your model's output

if __name__ == '__main__':
    unittest.main()