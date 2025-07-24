# 🚗 Pedestrian and Vehicle Detection using Image Processing

## 📌 Project Summary
Detects vehicles (car, bus, bike) and pedestrians in real-time video streams using Python and OpenCV with Haar Cascade Classifiers.

## 🛠️ Technologies Used
- Python 3
- OpenCV
- Haar Cascades
- Background Subtraction (MOG2)

## 🔍 Object Categories
- Cars
- Buses
- Bikes
- Pedestrians

## 🧪 How it Works
- Convert video frames to grayscale
- Apply Haar cascade classifiers to detect objects
- Use `detectMultiScale` to locate and draw boxes

## ▶️ Run It
```bash
pip install opencv-python
python object_detection.py
```

## 📸 Sample Output
Rectangles around detected objects like:
- Green: Car
- Red: Bike
- Blue: Bus
- Yellow: Pedestrian