# 🎥 Live Object Detection & Tracking using YOLOv8 + Streamlit

## 📌 Project Overview

This project is a real-time AI web application built using **Streamlit**, **YOLOv8 (Ultralytics)**, and **WebRTC**.

It captures live webcam video and performs real-time object detection and tracking with bounding boxes, labels, object counting, and alerts.

---

## 🚀 Features

- 🎥 Live webcam streaming in browser  
- 🤖 YOLOv8 object detection (Ultralytics)  
- 📦 Bounding box visualization  
- 🏷️ Object labeling (person, car, bottle, chair, etc.)  
- 🎯 Object tracking using ByteTrack  
- 📊 Real-time object counting  
- ⚠️ Person detection alert system  
- 🎨 Color-coded detection per class  
- 🔄 Smooth frame processing  

---

## 🧠 How It Works

1. Webcam captures live video frames  
2. Each frame is processed using YOLOv8 model  
3. Objects are detected and tracked across frames  
4. Bounding boxes and labels are drawn  
5. Output is streamed live using Streamlit WebRTC  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Streamlit WebRTC  
- Ultralytics YOLOv8  
- OpenCV  
- PyTorch  
- PyAV  
- NumPy  

---

## 📂 Project Structure

```

object-detection-app/
│
├── app.py
├── requirements.txt
├── README.md
├── yolov8n.pt

````

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/reamay526/object-detection-app
cd object-detection-app
````

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the app locally

```bash
streamlit run app.py
```

---

## 📊 Expected Output

* Live webcam feed in browser
* Real-time object detection
* Bounding boxes and labels
* Object counting display
* Person detection alert

---

## 📈 Observations

* Works best with good lighting
* Accuracy decreases in low light
* Small objects may not always be detected
* Performance depends on device hardware

---

## 🧪 Enhancements Implemented

* Object counting system
* Person detection alert system
* Color-coded bounding boxes
* Real-time tracking using ByteTrack
* Live annotation overlay

---

## ❓ Reflection

### 1. What objects were easily detected?

* Person
* Bottle
* Chair

### 2. What factors affect accuracy?

* Lighting conditions
* Camera quality
* Distance from camera
* Motion blur

---

## ⚠️ Limitations

* Requires stable internet for WebRTC
* May lag on low-end devices
* Tracking may reset during fast motion
* Performance depends on CPU/GPU

---

## 🚀 Future Improvements

* Add object filtering options
* Improve FPS performance
* Add snapshot saving feature
* Add analytics dashboard

---

## 👨‍💻 Author

Rea May M. Villanueva (BSCS 3B)

---

## 📜 License

This project is for educational purposes only.
