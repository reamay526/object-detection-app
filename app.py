import streamlit as st
import cv2
from ultralytics import YOLO

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Live Object Detection & Tracing", layout="wide")
st.title("📷 Live Object Detection & Tracing")

# ---------------- LOAD MODEL ----------------
model = YOLO("yolov8n.pt")

# ---------------- CONTROLS ----------------
start = st.checkbox("▶ Start Camera")

frame_window = st.image([])

cap = cv2.VideoCapture(0)

if start:
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("❌ Camera not detected")
            break

        # ---------------- YOLO TRACKING ----------------
        results = model.track(frame, persist=True)

        annotated_frame = results[0].plot()

        # ---------------- OBJECT COUNTING ----------------
        labels = model.names
        counts = {}

        if results[0].boxes is not None:
            for box in results[0].boxes:
                cls_id = int(box.cls[0])
                name = labels[cls_id]
                counts[name] = counts.get(name, 0) + 1

        total_objects = sum(counts.values())

        # ---------------- TOP-LEFT TEXT ----------------
        cv2.putText(
            annotated_frame,
            f"Objects: {total_objects}",
            (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2,
            cv2.LINE_AA
        )

        # ---------------- PERSON ALERT ----------------
        if "person" in counts:
            cv2.putText(
                annotated_frame,
                "PERSON DETECTED!",
                (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2,
                cv2.LINE_AA
            )

        # ---------------- DISPLAY ----------------
        frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame_rgb)

