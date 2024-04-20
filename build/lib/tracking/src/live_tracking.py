import act_model
import cv2
def start_tracking_webcam():
    # Open the default webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        success, frame = cap.read()

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
            # Error handling (optional)
            print("Error reading webcam frame!")
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

# Futtassa a funkciót az élő kamera követéséhez
