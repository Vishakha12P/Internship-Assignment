import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile

st.title("⚽ Player Detection & Tracking")

uploaded_file = st.file_uploader("Upload a video")

if uploaded_file is not None:
    # Save uploaded video temporarily
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(tfile.name)

    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.track(
            frame,
            persist=True,
            classes=[0],
            conf=0.3,
            tracker="bytetrack.yaml"
        )

        annotated = results[0].plot()
        stframe.image(annotated, channels="BGR")

    cap.release()