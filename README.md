# 🎯 Multi-Object Detection & Tracking in Sports Video

![Python](https://img.shields.io/badge/Python-3.x-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📌 Overview
This project implements a **computer vision pipeline** to detect and track multiple players in a sports video using **YOLOv8**.

Each detected player is assigned a **unique tracking ID**, enabling consistent tracking across frames.  
The system also performs **temporal analysis** by plotting the number of detected players over time.

---
🎥 Demo Video
<p align="center"> <a href="https://drive.google.com/file/d/1r1gbTvPkZ4iJl9fLBvdvbsPDzrrsD77L/view?usp=sharing"> <img src="https://img.shields.io/badge/▶️ Watch%20Demo%20Video-blue?style=for-the-badge" alt="Watch Demo Video"> </a> </p>

## 🚀 Key Features
- 🔍 Real-time player detection using YOLOv8  
- 🧠 Multi-object tracking with persistent IDs (ByteTrack)  
- 🎯 Live player count displayed on video  
- 📊 Time-series analysis of object count  
- 🎥 Annotated output video generation  

---

## 🛠️ Tech Stack

| Technology     | Purpose                          |
|----------------|----------------------------------|
| Python         | Core programming language        |
| OpenCV         | Video processing                |
| YOLOv8         | Object detection                |
| ByteTrack      | Object tracking                |
| Matplotlib     | Data visualization             |

---

## 📂 Project Structure

```

project/
│── main.py
│── football-video-dataset.mp4
│── annotated_output.mp4
│── count_plot.png

````

---

## ⚙️ Installation Steps
Clone the Repository
* git clone https://github.com/your-username/your-repo-name.git
* cd your-repo-name
  
Create Virtual Environment (Recommended)
* python -m venv venv
  
Activate Environment
* Windows:venv\Scripts\activate
* Mac/Linux:source venv/bin/activate

Install Dependencies
* pip install -r requirements.txt

---

## 📦 Dependencies

Main libraries used:

* ultralytics (YOLOv8)
* opencv-python
* numpy
* torch
* matplotlib (optional for visualization)

Install manually if needed:

```bash
pip install ultralytics opencv-python matplotlib
````

---

## ▶️ Usage

```bash
python main.py
```

---

## 🧠 Pipeline Workflow

1. Load input video using OpenCV
2. Process frames sequentially
3. Detect players using YOLOv8
4. Track players using ByteTrack
5. Assign unique IDs
6. Count players per frame
7. Store results for analysis
8. Generate visualization graph
9. Save annotated video

---

## ▶️ How to Run Pipeline

Run the detection + tracking pipeline:

from ultralytics import YOLO

model = YOLO("yolov8l.pt")

results = model.track(
    source="Dataset_videos/video_1.mp4",
    save=True
)

---

## 📌 Assumptions Taken

* Input videos are clear and not heavily blurred
* Objects of interest (players/targets) are visible in frame
* Camera is mostly stationary or has slow movement
* Pretrained YOLO model is sufficient (no full custom retraining assumed)

---

## ⚠️ Limitations

* ❌ Difficulty detecting small objects (e.g., ball)
* ⚠️ ID switching in crowded or occluded scenes
* ⏳ Performance drops with high-density frames

---


## 🧠 Model / Tracker Choice

🔍 Model Used:
* YOLOv8 (You Only Look Once v8)
* 
Why YOLOv8?
* Real-time performance
* High accuracy on small + large objects
* Easy integration with tracking pipelines
* Pretrained weights available
  
🎯 Tracker Used:
* ByteTrack (default in YOLOv8 tracking)
* Why ByteTrack?
* Maintains identity consistency even during occlusions
* Works well in crowded scenes
* Lightweight and fast

---

## 🔮 Feature Enhancements

* 🏀 Ball detection and tracking
* 📍 Player trajectory mapping
* 🔥 Heatmap visualization
* 📈 Advanced player analytics
* ⚡ Real-time optimization
* 📌 Deployment as notebook

---
## 🎥 Output

### 1️⃣ Annotated Video

* Bounding boxes around players
* Unique tracking IDs
* Real-time player count

📁 Output file: `annotated_output.mp4`

---

### 2️⃣ Player Count Over Time

* Graph showing number of detected players per frame

📁 Output file: `count_plot.png`
## 📸 Results

* Annotated video frame screenshot
* Count graph (`count_plot.png`)

---

## 🙌 Acknowledgements

* Ultralytics YOLOv8
* OpenCV
* Matplotlib

---

## 📊 Evaluation Insight

The system was evaluated visually by checking ID consistency across frames and tracking stability during occlusion and fast motion scenarios.
Performance was assessed based on detection accuracy, tracking continuity, and smoothness of ID assignment.

---

## 📄 License

This project is intended for **educational and learning purposes**.

---

## 👨‍💻 Author

**Vishakha Rajak**
B.Tech Computer Science | Machine Learning Enthusiast

---

```

