from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# -------------------------------
# Load YOLO model
# -------------------------------
model = YOLO("yolov8n.pt")

# -------------------------------
# Load video
# -------------------------------
cap = cv2.VideoCapture("football-video-dataset.mp4")

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# -------------------------------
# Get video properties
# -------------------------------
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30

# -------------------------------
# Output video writer
# -------------------------------
out = cv2.VideoWriter(
    "annotated_output.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

# -------------------------------
# Object count over time storage
# -------------------------------
frame_counts = []
frame_number = 0

# -------------------------------
# Main loop
# -------------------------------
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_number += 1

    # -------------------------------
    # Tracking
    # -------------------------------
    results = model.track(
        frame,
        persist=True,
        classes=[0],
        conf=0.3,
        tracker="bytetrack.yaml"
    )

    annotated_frame = results[0].plot()

    # -------------------------------
    # Object count
    # -------------------------------
    if results[0].boxes.id is not None:
        ids = results[0].boxes.id.cpu().numpy()
        count = len(set(ids))
    else:
        count = 0

    frame_counts.append(count)

    # Show count on video
    cv2.putText(
        annotated_frame,
        f"Count: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # -------------------------------
    # Display + Save
    # -------------------------------
    cv2.imshow("Tracking", annotated_frame)
    out.write(annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# -------------------------------
# Release resources
# -------------------------------
cap.release()
out.release()
cv2.destroyAllWindows()

print("✅ Output saved as annotated_output.mp4")

# -------------------------------
# Plot Object Count Over Time
# -------------------------------
plt.plot(frame_counts)
plt.title("Object Count Over Time")
plt.xlabel("Frame Number")
plt.ylabel("Number of Players")
plt.savefig("count_plot.png")  # saves graph
plt.show()