import streamlit as st
import cv2
import numpy as np
from tracking import find_eucledian_dist
import tempfile
import os

# Create tracker object
tracker = find_eucledian_dist()

# Streamlit app setup
st.set_page_config(page_title="🚗 Vehicle Detection & Tracking", layout="wide")

# Header Section with Emojis
st.markdown(
    """
    <div style="background-color:#1e81b0; padding:10px; border-radius:10px">
        <h1 style="color:white; text-align:center;">🚗 Vehicle Detection & Tracking System 🛣️</h1>
        <p style="color:white; text-align:center;">Upload a video and track vehicles with unique IDs!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar for file upload
st.sidebar.title("🎥 Upload Video")
st.sidebar.info("Supported formats: MP4, AVI, MOV. Max size: 250MB.")
uploaded_file = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save video to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_file.write(uploaded_file.read())
    temp_file_path = temp_file.name

    # Load video using OpenCV
    cap = cv2.VideoCapture(temp_file_path)

    # Object detection from a stable camera
    object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

    # Create layout: Two columns for video and mask
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎥 Original Video with Tracking")
        stframe = st.empty()

    with col2:
        st.markdown("### ⚫ Background Subtraction (Mask)")
        mask_frame = st.empty()

    st.markdown("---")  # Divider line

    # Process video frame by frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        height, width, _ = frame.shape
        roi = frame[340:720, 500:800]

        # 1. Object Detection
        mask = object_detector.apply(roi)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        detections = []

        for cnt in contours:
            # Calculate area and remove small elements
            area = cv2.contourArea(cnt)
            if area > 100:
                x, y, w, h = cv2.boundingRect(cnt)
                detections.append([x, y, w, h])

        # 2. Object Tracking
        boxes_ids = tracker.update(detections)
        for box_id in boxes_ids:
            x, y, w, h, id = box_id
            cv2.putText(roi, f"{id}", (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Display the video frame with ROI
        result_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(result_frame, channels="RGB", use_column_width=True)

        # Display the mask frame
        mask_colored = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
        mask_frame.image(mask_colored, channels="RGB", use_column_width=True)

    cap.release()
    os.remove(temp_file_path)  # Delete temporary file after processing
    st.success("✅ Video processing complete!")
else:
    st.warning("⚠️ Please upload a video file to start tracking.")
