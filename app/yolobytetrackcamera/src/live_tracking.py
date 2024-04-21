import cv2
import argparse
from .utils.act_model import model_choose

def start_tracking_webcam(selected_model):
    """
    Start object tracking using the webcam.

    This function initializes the webcam (index 0) and continuously captures frames from it.
    Each frame is processed using the selected YOLOv8 model for object detection and tracking.
    The annotated frames with bounding boxes are displayed in a window titled "YOLOv8 Tracking".
    Press 'q' to quit the tracking loop and close the window.

    Parameters:
        selected_model (int): The index of the selected YOLO model from 1 between 5.

    Returns:
        None
    """
    model = model_choose(selected_model)
    try:
        cap = cv2.VideoCapture(0)
        while True:
            success, frame = cap.read()
            if success:
                try:
                    results = model.track(frame, persist=True)
                    annotated_frame = results[0].plot()
                    cv2.imshow("YOLOv8-ByteTrack Live Tracking", annotated_frame)
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break
                except Exception as e:
                    print(f"Error processing frame: {e}")
            else:
                print("Error reading webcam!")
                break
    except Exception as e:
        print(f"General error: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8-ByteTrack Live Tracking")
    parser.add_argument("model", type=int, choices=[1, 2, 3, 4, 5],
                        help="The index of the selected YOLO model from 1 to 5")
    args = parser.parse_args()
    start_tracking_webcam(args.model)