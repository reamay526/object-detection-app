import streamlit as st
from streamlit_webrtc import webrtc_streamer
from ultralytics import YOLO
import av
import cv2

# ---------------- MODEL ----------------
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# ---------------- UI ----------------
st.set_page_config(page_title="AI Object Detection", layout="centered")

st.title("🎥 YOLOv8 Real-Time Detection & Tracking")
st.caption("Optimized for Strong Detection + Stable Streamlit Cloud")

run = st.toggle("Start Camera", value=True)

# ---------------- COLORS ----------------
def get_class_color(label):
    return {
        "person": (255, 80, 80),
        "car": (80, 180, 255),
        "bottle": (80, 255, 120),
        "cell phone": (200, 80, 255),
        "chair": (255, 200, 80),
        "tv": (0, 255, 255),
    }.get(label, (200, 200, 200))

# ---------------- DRAW TEXT ----------------
def draw_text(img, text, x, y, color):
    cv2.putText(img, text, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(img, text, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, color, 1, cv2.LINE_AA)

# ---------------- CALLBACK ----------------
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # 🔥 HIGH QUALITY INPUT (IMPORTANT FIX)
    img = cv2.resize(img, (640, 640))

    # 🔥 STRONG DETECTION SETTINGS
    results = model(img, conf=0.15, iou=0.45, imgsz=640)

    frame_out = img.copy()
    counts = {}

    # ---------------- DETECTION ----------------
    if results and results[0].boxes is not None:
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            counts[label] = counts.get(label, 0) + 1

            color = get_class_color(label)

            cv2.rectangle(frame_out, (x1, y1), (x2, y2), color, 2)
            draw_text(frame_out, label.upper(), x1, y1 - 5, color)

    # ---------------- OVERLAY ----------------
    total = sum(counts.values())
    draw_text(frame_out, f"OBJECTS: {total}", 10, 20, (0, 255, 255))

    # PERSON ALERT
    if "person" in counts:
        draw_text(frame_out, "PERSON DETECTED", 10, 45, (0, 0, 255))
    else:
        draw_text(frame_out, "NO PERSON DETECTED", 10, 45, (0, 255, 0))

    # OBJECT LIST
    y = 70
    for label, count in counts.items():
        draw_text(frame_out, f"{label.upper()}: {count}", 10, y, (0, 255, 0))
        y += 18

    return av.VideoFrame.from_ndarray(frame_out, format="bgr24")

# ---------------- STREAMLIT WEBCAM ----------------
if run:
    webrtc_streamer(
        key="yolo-strong-detection",
        video_frame_callback=video_frame_callback,
        async_processing=True,   # 🔥 stability fix
        media_stream_constraints={"video": True, "audio": False},
        rtc_configuration={
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        },
    )
else:
    st.info("Camera is off")