# Fatigue Detection using Hybrid Deep Learning Models
Using the capability of deep learning-based object detectors for robust fatigue detection, this solution uses real-time facial monitoring to detect indicators of drowsiness. Object detection plays an important role when determining fatigue indicators. Three models will be used and compared to one another
## Dataset and Preprocessing
The UTA-RLDD dataset, composed of RGB video recordings, features 60 participants categorized into three states: alert, low vigilance, and drowsy. To streamline the training process, only the alert and drowsy videos are utilized, excluding those labeled as low vigilant.
## Model
<b> YOLOv11 <strong>: YOLOv11 improves multiscale object detection by including an upgraded Feature Pyramid Network (FPN) that efficiently leverages features at different scales, allowing for exact object detection across varying sizes by exploiting numerous feature map resolutions
