# Fatigue Detection using Hybrid Deep Learning Models
Using the capability of deep learning-based object detectors for robust fatigue detection, this solution uses real-time facial monitoring to detect indicators of drowsiness. Object detection plays an important role when determining fatigue indicators. Three models will be used and compared to one another.
## Dataset and Preprocessing
The UTA-RLDD dataset, composed of RGB video recordings, features 60 participants categorized into three states: alert, low vigilance, and drowsy. To streamline the training process, only the alert and drowsy videos are utilized, excluding those labeled as low vigilant.
## Models
<b> YOLOv11:</b> YOLOv11 improves multiscale object detection by including an upgraded Feature Pyramid Network (FPN) that efficiently leverages features at different scales, allowing for exact object detection across varying sizes by exploiting numerous feature map resolutions.
<b>RetinaNet:</b> RetinaNet is a single-stage object detection model with the ResNet50 architecture as its backbone. It uses a Feature Pyramid Network (FPN) to overcome disappearing gradients and class imbalance, making it useful for aerial picture analysis and feature extraction.
<b>RT-DETR:</b> RT-DETR is a real-time target detection model that uses the attention mechanism. It includes a backbone network and a hybrid encoder with an auxiliary prediction head to improve detection performance.  Figure 5 shows the summary of the architecture of RT-DETR.
## Metrics
For object detection the main focus for the metric is mAP. The highest mAP result will be used to deploy in streamlit.

