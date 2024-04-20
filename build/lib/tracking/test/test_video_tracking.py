import act_model

def start_video_tracking(path):
    results = act_model.model.track(source=path, show=True, conf=0.3, iou=0.5, tracker="bytetrack.yaml")
    return results