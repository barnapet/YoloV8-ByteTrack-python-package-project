import unittest
from unittest import mock
from unittest.mock import patch
from yolobytetrackcamera import start_record_tracking

class TestRecordTracking(unittest.TestCase):
    @patch('cv2.VideoCapture')
    @patch('yolobytetrackcamera.model_choose')
    def test_start_record_tracking(self, mock_model_choose, mock_VideoCapture):
        mock_capture = mock_VideoCapture.return_value
        mock_capture.get.side_effect = [30.0, 640, 480]

        def mock_track(frame, persist):
            return ["annotated_frame"]
        mock_model = mock.MagicMock()
        mock_model.track = mock_track
        mock_model_choose.return_value = mock_model
        source_path = "test_video"
        target_path = "output"

        start_record_tracking(2, source_path, target_path)

        mock_VideoCapture.assert_called_once_with(f"{source_path}.mp4")

if __name__ == '__main__':
    unittest.main()