import argparse
from .utils.act_model import model_choose

def start_video_tracking(selected_model, path, conf=0.3, iou=0.5, tracker="bytetrack.yaml"):
    """
    Start object tracking on a video file.

    .This function performs object detection and tracking on a video file specified by `path`.
    If a `config` object is provided, it will be used to configure the tracking parameters.
    Otherwise, default parameters will be used.

    Parameters:
        selected_model (int): The index of the selected YOLO model from 1 between 5.
        path (str): The path to the input video file.
        conf (float, optional): The confidence threshold for object detection. Defaults to 0.3.
        iou (float, optional): The IoU threshold for object tracking. Defaults to 0.5.
        tracker (str, optional): The name or path of the tracker configuration file. Defaults to "bytetrack.yaml".

    Returns:
        dict: A dictionary containing tracking results.
    """
    model = model_choose(selected_model)
    try:
        model.track(source=path, show=True, conf=conf, iou=iou, tracker=tracker)
    except Exception as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8-ByteTrack Video Tracking")
    parser.add_argument("model", type=int, choices=[1, 2, 3, 4, 5],
                        help="The index of the selected YOLO model from 1 to 5")
    parser.add_argument("path", type=str, help="The path to the input video file")
    parser.add_argument("--conf", type=float, default=0.3,
                        help="The confidence threshold for object detection")
    parser.add_argument("--iou", type=float, default=0.5,
                        help="The IoU threshold for object tracking")
    parser.add_argument("--tracker", type=str, default="bytetrack.yaml",
                        help="The name or path of the tracker configuration file")
    args = parser.parse_args()
    start_video_tracking(args.model, args.path, conf=args.conf, iou=args.iou, tracker=args.tracker)
