from act_model import model_choose

def create_custom_model(selected_model, *args, **kwargs):
    model = model_choose(selected_model)
    model = model.load('yolov8n.pt')
    data = kwargs.get('data', 'coco8.yaml')
    epochs = kwargs.get('epochs', 10)
    imgsz = kwargs.get('imgsz', 640)
    training_params = {}
    results = model.train(data=data, epochs=epochs, imgsz=imgsz, **training_params)
    return results

create_custom_model(1, epochs=15, imgsz=320, lr=0.0001)