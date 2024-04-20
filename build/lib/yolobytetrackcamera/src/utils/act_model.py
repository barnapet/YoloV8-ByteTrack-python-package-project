from ultralytics import YOLO

def model_choose(model_type):
    list_of_models = ['yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt']

    if not 1 <= model_type <= len(list_of_models):
        raise ValueError(f"Invalid model number: {model_type}. Choose a number between 1 and {len(list_of_models)}!")

    return YOLO(list_of_models[model_type-1])
