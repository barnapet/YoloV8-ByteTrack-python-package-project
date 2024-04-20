from utils.act_model import model_choose

def start_video_tracking(path):
    results = model_choose(1).track(source=path, show=True, conf=0.3, iou=0.5, tracker="bytetrack.yaml")
    return results

start_video_tracking(r"C:\Users\barna\Downloads\video-short.mp4")