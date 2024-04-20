# YOLOV8-ByteTrack Camera Package

This Python package utilizes the Ultralytics library, specifically the YOLOv8 object detection and ByteTrack tracking algorithms.

## Installation

You can install the package via pip:

```bash
pip install yolobytetrackcamera
```
Alternatively, if pip installation is not available, you can download the package from the [Releases](link_to_releases_page) page. The package includes two files for installation:

- `yolobytetrackcamera-0.1.tar.gz`
- `yolobytetrackcamera-0.1-py3-none-any.whl`

You can use these files for installation using the following command:
## Usage

### live_tracking

The `live_tracking` method initiates an immediate object detection and tracking process using the primary camera on the device with visual display.

```python
from yolobytetrackcamera import start_tracking_webcam

start_tracking_webcam(1)
```
Where:
- `[model_index]` (int): The index of the selected YOLO model from 1 to 5.

Press 'q' to quit the tracking loop and close the window.

The model index should be between 1 and 5, corresponding to the available YOLOv8 models.

| YOLOv8 Type | Number |
|-------------|--------|
| yolov8n     |   1    |
| yolov8s     |   2    |
| yolov8m     |   3    |
| yolov8l     |   4    |
| yolov8x     |   5    |

### record_tracking

The `record_tracking` method captures a video from a source and records a new video on the device with the object detection and tracking annotations.

```python
from yolobytetrackcamera import start_record_tracking

start_record_tracking(selected_model=1, source_path="input_video_path", target_path="output_video_path")
```
Where:
- `selected_model` (int): The index of the selected YOLO model from 1 to 5.
- `source_path` (str): The path to the input video file (without extension).
- `target_path` (str): The path to save the output video file.

### video_tracking

The `video_tracking` method performs a quick analysis with object detection and tracking annotations on a video file, displaying the results on the device where it is executed.

```python
from yolobytetrackcamera import start_video_tracking

start_video_tracking(selected_model=1, source_path="input_video_path", target_path="output_video_path", conf=0.3, iou=0.5, tracker="custom_tracker.yaml")
```
Where:
- `[model_index]` (int): The index of the selected YOLO model from 1 to 5.
- `[video_path]` (str): The path to the input video file.
- `--conf` (float, optional): The confidence threshold for object detection. Defaults to 0.3.
- `--iou` (float, optional): The IoU threshold for object tracking. Defaults to 0.5.
- `--tracker` (str, optional): The name or path of the tracker configuration file. Defaults to "bytetrack.yaml".

Parameters:
- `model_index` (int): The index of the selected YOLO model from 1 to 5.
- `video_path` (str): The path to the input video file.
- `conf` (float, optional): The confidence threshold for object detection. Defaults to 0.3.
- `iou` (float, optional): The IoU threshold for object tracking. Defaults to 0.5.
- `tracker` (str, optional): The name or path of the tracker configuration file. Defaults to "bytetrack.yaml".

Notes:
- Ensure the video file exists at the specified path.
- The script will display the annotated video frames with bounding boxes.
- Press 'q' to quit the tracking loop.

## Acknowledgments

This package relies on the Ultralytics and Open-CV library for its object detection and tracking functionalities.

## System Requirements

Ensure you have the following installed:

- Python 3.x
- OpenCV
- YOLOv8-ByteTrack Camera package

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
