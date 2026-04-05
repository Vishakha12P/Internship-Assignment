from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load video
cap = cv2.VideoCapture("football-video-dataset.mp4")

# Get video properties
width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(5))

# Save output video
out = cv2.VideoWriter("annotated_output.mp4",
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Tracking
    results = model.track(frame, persist=True)

    # Draw boxes + IDs
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("Tracking", annotated_frame)

    # Save output
    out.write(annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()