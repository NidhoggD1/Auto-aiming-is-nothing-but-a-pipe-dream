from ultralytics import YOLO

model = YOLO('./pretrained_models/yolov8s.pt')

model.info()