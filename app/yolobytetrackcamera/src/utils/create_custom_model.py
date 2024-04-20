from ultralytics import YOLO
from roboflow import Roboflow

rf = Roboflow(api_key="kLYx9ha9722jBsrfr8p7")
project = rf.workspace("pothole-dataset-kwweo").project("bp-pothole-detection-project")
version = project.version(2)

model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights
results = model.train(data='coco8.yaml', epochs=10, imgsz=640)