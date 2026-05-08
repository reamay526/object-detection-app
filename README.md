<<<<<<< HEAD
# 🚀 Real-Time Object Detection and Tracking using AI

This project is a **Streamlit-based web application** that performs real-time object detection using a webcam and a YOLOv8 deep learning model. It detects common objects such as people, bottles, phones, and more, and displays bounding boxes with labels in real time.

---

## 📌 Features

- 🎥 Live webcam stream integration
- 🧠 AI-powered object detection using YOLOv8
- 📦 Bounding box visualization
- 🏷️ Object labeling (e.g., person, bottle, cell phone)
- 🔄 Real-time frame-by-frame processing
- 📊 Optional object counting / tracking enhancement
- ⚡ Lightweight and easy-to-run Streamlit interface

---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit 🌐  
- OpenCV 👁️  
- Ultralytics YOLOv8 🤖  
- PyTorch 🔥  
- NumPy 🔢  

---

## 📁 Project Structure

object-detection-app/

├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
├── .gitignore            # Ignored files for Git
├── README.md             # Project documentation

---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/reamay526/object-detection-app.git
cd object-detection-app

### 2. Create virtual environment (optional but recommended)
python -m venv venv

Activate:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the application
streamlit run app.py

---

## 🎯 How It Works

1. The webcam captures live video frames  
2. Each frame is processed using YOLOv8 AI model  
3. The model detects objects in real time  
4. Bounding boxes and labels are drawn on detected objects  
5. Streamlit displays the updated video feed in the browser  

---

## 📊 Observations

- Detection works best in good lighting conditions  
- Large and common objects are detected more accurately  
- Small or partially hidden objects may reduce accuracy  
- Performance depends on system hardware  

---

## ⚡ Possible Enhancements

- Object counting  
- Alert system  
- Save detected frames  
- Object tracking across frames  

---

## 🧠 Learning Outcomes

- Real-time computer vision  
- AI model deployment  
- Video frame processing  
- Streamlit web app development  

---

## 👨‍💻 Author
REA MAY M. VILLANUEVA (BSCS3B)
=======
# Live Object Detection & Tracking (YOLOv8 + Streamlit)

## Features
- Real-time webcam detection
- Object tracking
- Object counting
- Alert system (person detection)

## Run Locally
pip install -r requirements.txt
streamlit run app.py

## Tech Stack
- Python
- Streamlit
- YOLOv8
- OpenCV
>>>>>>> 8d20b3f9 (clean project (no venv))
