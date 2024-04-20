import cv2
import time
import act_model
def gen_timestamp():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    return timestamp
def start_record_tracking(path):
    video = cv2.VideoCapture(path+".mp4")
    fourcc = cv2.VideoWriter_fourcc(*'MP4V') # Kodek beállítása (módosítható)
    fps = video.get(cv2.CAP_PROP_FPS)  # Eredeti FPS lekérdezése
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(f"{path}-with-yolobytetrackcamera-{gen_timestamp()}.mp4", fourcc, fps, (width, height))

    # Loop through the video frames
    while video.isOpened():
        # Read a frame from the video
        success, frame = video.read()

        if success:
            # Run YOLOv8 yolobytetrackcamera on the frame, persisting tracks between frames
            results = act_model.model_choose(1).track(frame, persist=True)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Tracking", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break
    # Release the video capture object and close the display window
    video.release()
    out.release()
    cv2.destroyAllWindows()