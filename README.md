# 🚗 **Vehicle Detection and Tracking System** 🛣️

Welcome to the **Vehicle Detection and Tracking System**! This project allows you to detect and track vehicles in uploaded videos using computer vision techniques. Vehicles are assigned unique IDs, and their movement is tracked throughout the video.

---

## ✨ **Features**
- **🎥 Video Upload**: Upload videos up to 250MB in size (supports `.mp4`, `.avi`, and `.mov` formats).
- **🔍 Vehicle Detection**: Detect vehicles in the video using background subtraction and contour detection.
- **🆔 Vehicle Tracking**: Assign unique IDs to each detected vehicle for consistent tracking.
- **⚫ Background Subtraction Preview**: View the black-and-white mask (background subtraction process) alongside the original video.
- **🚀 Real-Time Processing**: Watch the results frame-by-frame as the video is processed.

---

## 🛠️ **Technologies and Libraries Used**

### **Python Libraries**
- **Streamlit**: For building the web interface.
- **OpenCV**: For image processing and object detection.
- **NumPy**: For numerical operations and array manipulation.

### **OpenCV Functions**
- **`cv2.VideoCapture`**: To read video files.
- **`cv2.createBackgroundSubtractorMOG2`**: To apply background subtraction for detecting objects.
- **`cv2.findContours`**: To find the contours of detected objects.
- **`cv2.contourArea`**: To filter out small, irrelevant objects.
- **`cv2.boundingRect`**: To create bounding boxes around detected objects.
- **`cv2.putText`**: To display vehicle IDs on the video frames.
- **`cv2.rectangle`**: To draw bounding boxes around detected objects.

---
## 🎨 **Screenshots**
### **Split-Screen View**
- **Left**: Original video with bounding boxes and IDs.
- **Right**: Black-and-white mask showing the background subtraction process.

*(Add a screenshot here showing both views for better visualization)*

---

## 🚀 **Future Enhancements**
- Add a download option for the processed video.
- Incorporate advanced object detection models like YOLO or SSD for more robust detection.
- Allow region-of-interest customization within the app.

---

## 💡 **Contributions**
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

---

## 🙌 **Acknowledgments**
Inspired by real-world traffic monitoring systems and vehicle analytics tools. Special thanks to the OpenCV community for their powerful tools and resources.

---

## 📧 **Contact**
For any queries or suggestions, feel free to reach out:  
📧 Email: [massnaveen1002@gmail.com](mailto:massnaveen1002@gmail.com)  
🌐 GitHub: [Naveen Kumar](https://github.com/Naveen035)

## 🔗 **LinkedIn Post**  
Check out the LinkedIn post about this project: [LinkedIn Post](https://www.linkedin.com/posts/naveen-kumar1002_vehicle-detection-and-tracking-system-activity-7264175943844257792-InUI?utm_source=share&utm_medium=member_desktop)
