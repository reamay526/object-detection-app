# 📷 Live Object Detection & Tracing (YOLOv8 + Streamlit)

## 🧠 Project Overview

This project is a real-time object detection and tracking web application built using **Streamlit** and **YOLOv8 (Ultralytics)**. It uses a webcam to detect everyday objects such as people, phones, and bottles, and displays bounding boxes and labels directly on the video feed.

This activity demonstrates how Artificial Intelligence and Computer Vision can be applied in real-world scenarios.

---

## 🎯 Objectives

By completing this project, the following concepts were learned:

* Basics of real-time computer vision
* How AI models process video frames
* Deployment of AI models in a web application
* Object tracking across multiple frames

---

## ⚙️ Features

* 📷 Live webcam streaming in browser
* 🧠 Real-time object detection using YOLOv8
* 🟩 Bounding boxes and labels on detected objects
* 🔄 Object tracking across frames (using YOLO tracking)
* 📊 Object counting system
* 🚨 Alert system for detecting a person

---

## 🖥️ System Output

### 1. Functional Web App Interface

* Displays title: **Live Object Detection & Tracing**
* Shows live webcam feed inside browser

### 2. Live Camera Detection

* Detects objects in real-time
* Displays bounding boxes
* Shows labels such as:

  * person
  * cell phone
  * bottle

### 3. Object Tracking Behavior

* Moving objects are tracked continuously
* Objects maintain identity across frames (smooth tracking)

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

### Libraries Used

* streamlit
* opencv-python
* ultralytics
* numpy
* torch
* torchvision

---

## ▶️ How to Run

```bash
streamlit run app.py
```

---

## 📊 Observation Report

### Detected Objects

* Person
* Cell phone
* Bottle
* Chair
* Laptop

### Detection Accuracy

* High accuracy in good lighting conditions
* Reduced accuracy in low-light environments
* Backlighting can affect detection performance

### Performance

* Smooth tracking under normal conditions
* Slight lag when detecting multiple objects

---

## 📸 Screenshots / Outputs

(Add your screenshots here)

Examples to include:

* Person detection
* Multiple objects detected
* Moving object tracking
* Low-light detection
* Alert system (PERSON DETECTED)

---

## 🧠 Reflection

### What objects were easily detected?

Objects like **person, phone, and bottle** were easily detected because they are commonly trained in the YOLOv8 dataset.

### What factors affect detection accuracy?

* Lighting conditions
* Object size and distance
* Camera quality
* Occlusion (objects being blocked)

---

## 🚀 Enhancements Implemented

* ✅ Object counting (number of detected objects)
* ✅ Alert system (PERSON DETECTED)


---

## 🔗 Submission Links

* 🌐 Live Streamlit App: *(Add your deployed link here)*
* 💻 GitHub Repository: *(Your repo link)*
* 📄 Document Report: *(Google Docs link)*

---

## 👨‍💻 Author

REA MAY M. VILLANUEVA (BSCS 3B)
