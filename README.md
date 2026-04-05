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

## ⚙️ Installation

```bash
pip install ultralytics opencv-python matplotlib
````

---

## ▶️ Usage

```bash
python main.py
```

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

## ⚠️ Limitations

* ❌ Difficulty detecting small objects (e.g., ball)
* ⚠️ ID switching in crowded or occluded scenes
* ⏳ Performance drops with high-density frames

---

## 🔧 Improvements Implemented

* ✔ Integrated ByteTrack for stable tracking
* ✔ Applied class filtering (person and object(ball) only)
* ✔ Added real-time player counting
* ✔ Generated time-series visualization

---

## 🔮 Feature Enhancements

* 🏀 Ball detection and tracking
* 📍 Player trajectory mapping
* 🔥 Heatmap visualization
* 📈 Advanced player analytics
* ⚡ Real-time optimization
* 📌 Deployment as notebook

---

## 📸 Results

* Annotated video frame screenshot
* Count graph (`count_plot.png`)

---

## 🙌 Acknowledgements

* Ultralytics YOLOv8
* OpenCV
* Matplotlib

---

📊 Evaluation Insight

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

