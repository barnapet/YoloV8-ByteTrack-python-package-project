import unittest
from unittest import mock
from unittest.mock import patch
from yolobytetrackcamera import start_tracking_webcam

class TestWebcamTracking(unittest.TestCase):
    @patch('yolobytetrackcamera.model_choose')
    @patch('cv2.VideoCapture')
    @patch('cv2.waitKey')
    def test_start_tracking_webcam(self, mock_waitKey, mock_VideoCapture, mock_model_choose):
        mock_capture = mock_VideoCapture.return_value
        mock_capture.read.side_effect = [(True, "test_frame"), (True, None)]
        mock_waitKey.return_value = ord('q')
        mock_model_choose.return_value = mock.MagicMock()
        mock_model_choose.return_value.process_frame.return_value = "processed_frame"

        start_tracking_webcam(1)

        mock_VideoCapture.assert_called_once_with(0)