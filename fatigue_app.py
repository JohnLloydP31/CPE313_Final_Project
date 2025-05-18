import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
import tempfile
import os
from io import BytesIO

st.title("Fatigue Detection using YOLOv11")

# Load the YOLO model
model = YOLO("best.pt")  # update path as needed

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(BytesIO(uploaded_file.read())).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Detect button
    if st.button("Detect"):
        # Convert PIL image to NumPy array and BGR for OpenCV
        img_array = np.array(image)
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # Save to a temporary file for YOLOv8
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_file:
            cv2.imwrite(tmp_file.name, img_bgr)
            results = model(tmp_file.name)
            annotated_frame = results[0].plot()

        st.image(annotated_frame, caption="Detected Image", use_container_width=True)
