import torch
from ultralytics import YOLO, RTDETR


def experiments(model, input_path, output_path, name):
    '''
    Experiments for yolo models
    '''
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using Device: ", device)

    result = model.predict(input_path, save=True,
                           save_txt=True, project=output_path, name=name)
    res = result[0]
    classes = res.names

    # open the file to write the results
    with open(output_path + "output.txt", "a") as f:
        f.write(f"\nModel: {name}\n")
        for box in res.boxes:
            conf = round(box.conf.item() * 100, 2)
            xyxy = box.xyxy.tolist()[0]
            cls = int(box.cls.item())
            cls_name = classes.get(cls)
            f.write(f"{cls_name} {conf} {xyxy}\n")

    print("Done!")


if __name__ == "__main__":
    # input_path = "input_data/shortest.mp4"
    input_path = "input_data/images/image.png"
    output_path = "runs/detect/test3/"

    models = {
        "yolov8x": YOLO("yolov8x.pt"),
        "yolov3-sppu": YOLO("yolov3-sppu.pt"),
        "yolov3u": YOLO("yolov3u.pt"),
        "yolov5l6u": YOLO("yolov5l6u.pt"),
        "yolov8l-cls": YOLO("yolov8l-cls.pt"),
        "rtdetr-l": RTDETR("rtdetr-l.pt"),
        "yolov9e": YOLO("yolov9e.pt"),
    }
    for model_name, model_obj in models.items():
        experiments(model_obj, input_path,
                    output_path, model_name)
