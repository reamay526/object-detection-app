import streamlit as st
from streamlit_webrtc import webrtc_streamer
from ultralytics import YOLO
import av
import cv2
import time

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

last_counts = {}
last_person_time = 0

st.title("🎥 Live Object Detection & Tracking")

st.info("⚠️ Webcam works best locally. Streamlit Cloud may limit camera access.")

run = st.checkbox("▶ Start Camera", value=True)

def video_frame_callback(frame):
    global last_counts, last_person_time

    img = frame.to_ndarray(format="bgr24")

    img = cv2.resize(img, (416, 416))

    results = model.predict(
        img,
        conf=0.3,
        verbose=False
    )

    annotated_frame = results[0].plot()

    current_counts = {}
    person_detected = False

    boxes = results[0].boxes
    if boxes is not None and len(boxes) > 0:
        for box in boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            current_counts[label] = current_counts.get(label, 0) + 1

            if label == "person":
                person_detected = True
                last_person_time = time.time()

    if current_counts:
        last_counts = current_counts

    display_person = (time.time() - last_person_time) < 1.0

    font = cv2.FONT_HERSHEY_SIMPLEX
    total_objects = sum(last_counts.values())

    cv2.putText(
        annotated_frame,
        f"Objects: {total_objects}",
        (10, 25),
        font,
        0.6,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )

    if display_person:
        person_text = "PERSON: ALERT!"
        color = (0, 0, 255)
    else:
        person_text = "PERSON: SAFE"
        color = (0, 255, 0)

    cv2.putText(
        annotated_frame,
        person_text,
        (10, 55),
        font,
        0.6,
        color,
        2,
        cv2.LINE_AA
    )

    y = 85
    for label, count in last_counts.items():
        cv2.putText(
            annotated_frame,
            f"{label}: {count}",
            (10, y),
            font,
            0.5,
            (0, 255, 0),
            1,
            cv2.LINE_AA
        )
        y += 18

    return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")

if run:
    webrtc_streamer(
        key="object-detection",
        video_frame_callback=video_frame_callback,
        async_processing=True,
        media_stream_constraints={"video": True, "audio": False},
        rtc_configuration={
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        },
    )
else:
    st.warning("Camera is stopped. Enable 'Start Camera' to run detection.")

import streamlit as st
from streamlit_webrtc import webrtc_streamer
from ultralytics import YOLO
import av
import cv2
from collections import Counter


@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

st.title("🎥 Live Object Detection & Tracing")
st.write("Point your camera at objects to identify them in real-time.")


st.sidebar.title("📊 Live Analytics")
total_box = st.sidebar.empty()
class_box = st.sidebar.empty()
alert_box = st.sidebar.empty()

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    results = model.track(
        img,
        persist=True,
        conf=0.5,
        verbose=False
    )

    annotated_frame = results[0].plot()


    boxes = results[0].boxes
    total_objects = len(boxes)

    labels = []
    for box in boxes:
        cls_id = int(box.cls[0])
        labels.append(model.names[cls_id])

    counts = Counter(labels)

    total_box.markdown(f"### Total Objects: {total_objects}")

    class_text = ""
    for obj, count in counts.items():
        class_text += f"- {obj}: {count}\n"

    class_box.markdown(f"### Object Types:\n{class_text}")


    alert = "No alerts"

    for box in boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]

        if label == "person":
            alert = "🚨 PERSON DETECTED!"

            cv2.putText(
                annotated_frame,
                "ALERT: PERSON",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )
            break

    alert_box.markdown(f"### Status: {alert}")

    return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")

webrtc_streamer(
    key="object-detection",
    video_frame_callback=video_frame_callback,
    async_processing=True,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    },
    media_stream_constraints={"video": True, "audio": False},
)