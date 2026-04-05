import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import time

st.title("⚽ Player Detection (YOLOv8)")

uploaded_file = st.file_uploader("Upload a video")

if uploaded_file is not None:
    # Save uploaded video
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    # Load model
    model = YOLO("yolov8n.pt")

    # Read video
    cap = cv2.VideoCapture(tfile.name)

    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize for performance
        frame = cv2.resize(frame, (640, 480))

        # 🔥 Detection ONLY (no tracking)
        results = model(frame)

        annotated = results[0].plot()

        # Show in Streamlit
        stframe.image(annotated, channels="BGR")

        # Smooth playback
        time.sleep(0.03)

    cap.release()

    st.success("✅ Processing Complete!")