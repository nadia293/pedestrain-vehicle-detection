import cv2

# Load Haar cascade classifiers
car_cascade = cv2.CascadeClassifier('cascades/haarcascade_car.xml')
bus_cascade = cv2.CascadeClassifier('cascades/haarcascade_bus.xml')
bike_cascade = cv2.CascadeClassifier('cascades/haarcascade_two_wheeler.xml')
pedestrian_cascade = cv2.CascadeClassifier('cascades/haarcascade_fullbody.xml')

cap = cv2.VideoCapture(0)  # Use 0 for webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 3)
    buses = bus_cascade.detectMultiScale(gray, 1.1, 3)
    bikes = bike_cascade.detectMultiScale(gray, 1.1, 3)
    pedestrians = pedestrian_cascade.detectMultiScale(gray, 1.1, 3)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Car', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    for (x, y, w, h) in buses:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Bus', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    for (x, y, w, h) in bikes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, 'Bike', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        cv2.putText(frame, 'Pedestrian', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)

    cv2.imshow('Object Detection', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()