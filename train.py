from ultralytics import YOLO

model = YOLO('./pretrained_models/yolov8s.pt')

model.info()

# Train the model
# Some arbitrary values
model.train(data='./data.yaml',
            epochs=100,
            batch_size=32,
            img_size=640,
            learning_rate=0.001,
            optimizer='Adam',
            lr_scheduler='cosine')