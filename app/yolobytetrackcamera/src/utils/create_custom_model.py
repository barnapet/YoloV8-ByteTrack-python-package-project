from .act_model import model_choose

def create_custom_model(selected_model, *args, **kwargs):
    """
    Creates and trains a custom object detection model using Ultralytics YOLOv8.

    Args:
        selected_model (int): The index of the desired model architecture (e.g., 0 for YOLOv5s, 1 for YOLOv5m, etc.).
        *args: Additional training parameters passed as positional arguments (e.g., '--lr', 0.0001).
        **kwargs: Keyword arguments for core training parameters:
            data (str): Path to the training data configuration file (default: 'coco8.yaml').
            epochs (int): Number of training epochs (default: 10).
            imgsz (int): Input image size (default: 640).

    Returns:
        Dict: A dictionary containing training metrics and other results.
    """
    model = model_choose(selected_model)
    model = model.load('yolov8n.pt')
    data = kwargs.get('data', 'coco8.yaml')
    epochs = kwargs.get('epochs', 10)
    imgsz = kwargs.get('imgsz', 640)
    training_params = {}
    results = model.train(data=data, epochs=epochs, imgsz=imgsz, **training_params)
    return results

