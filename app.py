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

st.set_page_config(page_title="Live Object Detection & Tracking", layout="centered")

st.title("🎥 Live Object Detection & Tracking")
st.caption("YOLOv8 real-time AI system")

run = st.toggle("Start Camera", value=True)

def get_class_color(label):
    return {
        "person": (255, 80, 80),
        "car": (80, 180, 255),
        "bottle": (80, 255, 120),
        "cell phone": (200, 80, 255),
        "chair": (255, 200, 80),
        "tv": (0, 255, 255),
    }.get(label, (200, 200, 200))

def draw_text(img, text, x, y, color):
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.5
    thickness = 1

    cv2.putText(img, text, (x-1, y-1), font, scale, (0, 0, 0), thickness+2, cv2.LINE_AA)
    cv2.putText(img, text, (x+1, y+1), font, scale, (0, 0, 0), thickness+2, cv2.LINE_AA)

    cv2.putText(img, text, (x, y), font, scale, color, thickness, cv2.LINE_AA)

last_results = None
last_counts = {}
last_person_time = 0
last_infer_time = 0

def video_frame_callback(frame):
    global last_results, last_counts, last_person_time, last_infer_time

    img = frame.to_ndarray(format="bgr24")
    img = cv2.resize(img, (320, 320))

    now = time.time()

    if now - last_infer_time > 0.35:
        results = model.track(
            source=img,
            persist=True,
            conf=0.4,
            tracker="bytetrack.yaml",
            verbose=False
        )
        last_results = results
        last_infer_time = now
    else:
        results = last_results

    frame_out = img.copy()
    counts = {}
    person_found = False

    if results and results[0].boxes is not None:
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            track_id = int(box.id[0]) if box.id is not None else -1

            counts[label] = counts.get(label, 0) + 1

            # 🎨 CLASS COLOR (MAIN CHANGE)
            color = get_class_color(label)

            cv2.rectangle(frame_out, (x1, y1), (x2, y2), color, 2)

            draw_text(
                frame_out,
                f"{label.upper()} ID:{track_id}",
                x1,
                y1 - 5,
                color
            )

            if label == "person":
                person_found = True

    if counts:
        last_counts = counts

    if person_found:
        last_person_time = time.time()

    draw_text(
        frame_out,
        f"OBJECTS: {sum(last_counts.values())}",
        10,
        20,
        (0, 255, 255)
    )

    if time.time() - last_person_time < 1.5:
        draw_text(
            frame_out,
            "PERSON DETECTED",
            10,
            42,
            (0, 0, 255)
        )
    else:
        draw_text(
            frame_out,
            "PERSON NOT DETECTED",
            10,
            42,
            (0, 255, 0)
        )

    y = 65
    for label, count in last_counts.items():
        draw_text(
            frame_out,
            f"{label.upper()}: {count}",
            10,
            y,
            (0, 255, 0)
        )
        y += 15

    return av.VideoFrame.from_ndarray(frame_out, format="bgr24")

if run:
    webrtc_streamer(
        key="class-color-ai",
        video_frame_callback=video_frame_callback,
        async_processing=True,
        media_stream_constraints={"video": True, "audio": False},
        rtc_configuration={
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        },
    )
else:
    st.info("Camera is off")
