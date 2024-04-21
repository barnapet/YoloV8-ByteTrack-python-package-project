import cv2
import time
import argparse
from .utils.act_model import model_choose

def gen_timestamp():
    """Generates a timestamp string in YYYY-MM-DD_HH-MM-SS format."""
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    return timestamp

def start_record_tracking(selected_model, source_path, target_path):
    """
    Record tracking video with object detection annotations.

    Parameters:
        selected_model (int): The index of the selected YOLO model from 1 between 5.
        source_path (str): The path to the source video file (without extension).
        target_path (str): The path to save the output video file.

    Returns:
        None
    """
    try:
        model = model_choose(selected_model)
        video = cv2.VideoCapture(source_path + ".mp4")
        if not video.isOpened():
            raise Exception(f"Error opening video file: {source_path}.mp4")
        fps = video.get(cv2.CAP_PROP_FPS)
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        output_filename = f"{target_path}-with-yolobytetrackcamera-{gen_timestamp()}.mp4"
        out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

        while video.isOpened():
            success, frame = video.read()
            if success:
                try:
                    results = model.track(frame, persist=True)
                    annotated_frame = results[0].plot()
                    cv2.imshow("YOLOv8 Tracking", annotated_frame)
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break
                except Exception as e:
                    print(f"Error processing frame: {e}")
            else:
                print("Error reading video")
                break

    except Exception as e:
        print(f"General error: {e}")
    finally:
        video.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8-ByteTrack Record Tracking")
    parser.add_argument("model", type=int, choices=[1, 2, 3, 4, 5],
                        help="The index of the selected YOLO model from 1 to 5")
    parser.add_argument("source_path", type=str,
                        help="The path to the source video file (without extension)")
    parser.add_argument("target_path", type=str,
                        help="The path to save the output video file")
    args = parser.parse_args()
    start_record_tracking(args.model, args.source_path, args.target_path)