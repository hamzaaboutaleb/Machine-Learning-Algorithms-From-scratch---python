# Computer Vision: Comprehensive 40-Question Reference Guide

---

## Section 1: Fundamentals & Image Representation

### Q1: What is Computer Vision?
Computer Vision (CV) is a field of artificial intelligence that enables computers to extract high-level understanding, structure, and insights from digital images or videos.

### Q2: How are digital images represented in a computer?
Images are stored as 2D or 3D numerical matrices. Grayscale images are represented by a single 2D grid of pixel intensities (typically 0–255). Color images (e.g., RGB) are represented by a 3D tensor of shape $(\text{Height} \times \text{Width} \times 3)$, with one channel per color.

### Q3: What is the difference between RGB, HSV, and Grayscale color spaces?
* **RGB (Red, Green, Blue):** An additive color model primarily used for digital display.
* **HSV (Hue, Saturation, Value):** Separates color information (Hue) from intensity/brightness (Value), making it useful for color-based object segmentation.
* **Grayscale:** Represents intensity only (0 for black, 255 for white), reducing computational complexity by eliminating color channels.

### Q4: What is pixel intensity normalization, and why is it important?
Normalization scales pixel values from $[0, 255]$ to a bounded range like $[0, 1]$ or $[-1, 1]$. It prevents exploding/vanishing gradients during neural network training and speeds up numerical optimization.

### Q5: What is spatial resolution vs. color depth?
* **Spatial Resolution:** The number of pixels spanning the width and height of an image (e.g., $1920 \times 1080$).
* **Color Depth (Bit Depth):** The number of bits used to represent each pixel's color (e.g., 8-bit depth allows $2^8 = 256$ intensity levels per channel).

---

## Section 2: Image Processing & Filtering

### Q6: What is Image Convolution?
Convolution is a mathematical operation where a small matrix (kernel or filter) slides over an image to apply element-wise multiplication and summation, generating a transformed output image (feature map).

### Q7: What is the difference between high-pass and low-pass filters?
* **Low-pass filters (e.g., Gaussian, Box filter):** Pass low frequencies and attenuate high frequencies, causing image smoothing and noise reduction.
* **High-pass filters (e.g., Sobel, Laplacian):** Pass high frequencies and attenuate low frequencies, emphasizing edges and fine details.

### Q8: How does Gaussian Blur work?
Gaussian Blur applies a filter whose weights follow a 2D Gaussian distribution. It smooths images while preserving edges better than a standard uniform box filter.

### Q9: What is the Sobel Operator?
The Sobel operator calculates an approximation of the image intensity gradient to detect horizontal ($\mathbf{G}_x$) and vertical ($\mathbf{G}_y$) edges using $3 \times 3$ kernels.

### Q10: How does the Canny Edge Detector work?
Canny edge detection uses a multi-stage pipeline:
1. Noise reduction via Gaussian smoothing.
2. Gradient computation using Sobel operators.
3. Non-Maximum Suppression (NMS) to thin thick edges.
4. Double Thresholding (high/low) to classify strong, weak, or non-edges.
5. Edge tracking by hysteresis (weak edges are kept only if connected to strong edges).

### Q11: What is thresholding, and how does Otsu's binarization work?
Thresholding converts grayscale images to binary (black/white) by comparing pixel values against a cutoff. Otsu's method automatically calculates the optimal threshold by minimizing intra-class variance between foreground and background pixels.

### Q12: What are morphological operations (Erosion and Dilation)?
* **Erosion:** Removes pixels on object boundaries using a structuring element, shrinking foreground objects.
* **Dilation:** Adds pixels to object boundaries, expanding foreground objects and filling small holes.

---

## Section 3: Classical Feature Extraction & Matching

### Q13: What are image features and descriptors?
* **Keypoints (Interest Points):** Specific spatial locations in an image that are distinct (e.g., corners, blobs).
* **Descriptors:** Numerical vectors that summarize the local visual appearance around a keypoint to enable matching across images.

### Q14: What makes a corner a useful feature for vision tasks?
Corners exhibit high intensity variations in all directions, making them easily identifiable and stable under image transformations compared to flat regions or straight lines.

### Q15: What is SIFT (Scale-Invariant Feature Transform)?
SIFT extracts keypoints and descriptors that are invariant to image scale, rotation, affine transformations, and illumination changes by utilizing Difference-of-Gaussians (DoG) space.

### Q16: How does ORB (Oriented FAST and Rotated BRIEF) differ from SIFT?
ORB is an efficient, open-source alternative to SIFT. It uses FAST for fast keypoint detection and BRIEF for binary descriptor generation, adding orientation invariance to maintain performance under rotation.

### Q17: What is Histogram of Oriented Gradients (HOG)?
HOG counts occurrences of gradient orientations in localized portions of an image. It is commonly used for object detection tasks, such as pedestrian detection.

### Q18: What is the Hough Transform?
The Hough Transform is a feature extraction technique used to isolate specific shapes (such as lines, circles, or ellipses) within a binary image by voting in a parameterized parameter space.

---

## Section 4: Deep Learning & Convolutional Neural Networks (CNNs)

### Q19: What is a Convolutional Neural Network (CNN)?
A CNN is a deep learning architecture designed for spatial data. It uses learnable convolutional filters to extract local feature hierarchies automatically, reducing the parameter count compared to fully connected networks.

### Q20: What is the purpose of Pooling layers (e.g., Max Pooling, Average Pooling)?
Pooling downsamples feature maps spatially, reducing computational load and parameter count while providing translation invariance.

### Q21: What are Stride and Padding in a CNN?
* **Stride:** The step size (in pixels) by which the convolutional filter moves across the input matrix.
* **Padding:** Adding extra pixels (usually zeros) around the boundary of an image to control the spatial dimensions of the output feature map.

### Q22: How do you calculate the output spatial size of a convolutional layer?
Given input size $W$, kernel size $K$, padding $P$, and stride $S$:
$$\text{Output Size} = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1$$

### Q23: What is Receptive Field in a CNN?
The receptive field is the specific region of the input image that directly influences the activation of a particular neuron in a deeper layer of the network.

### Q24: What is Transfer Learning in Computer Vision?
Transfer Learning leverages a model pre-trained on a large dataset (e.g., ImageNet) and fine-tunes its learned feature extractors on a new, smaller domain-specific dataset.

### Q25: Why are 1x1 convolutions useful (e.g., in ResNet or Inception)?
$1 \times 1$ convolutions perform linear combinations across feature channels without altering spatial dimensions. They are used to adjust channel dimensions (dimensionality reduction or expansion) efficiently.

### Q26: What problem do Residual Connections (ResNets) solve?
Residual connections pass input identity mappings directly to deeper layers ($y = F(x) + x$), solving the vanishing gradient problem and enabling the training of extremely deep networks.

---

## Section 5: Core Computer Vision Tasks

### Q27: What is the difference between Image Classification, Object Detection, Instance Segmentation, and Panoptic Segmentation?
* **Image Classification:** Assigns a single categorical label to an entire image.
* **Object Detection:** Identifies and locates multiple objects using bounding boxes and class labels.
* **Semantic Segmentation:** Classifies every pixel in an image into a category label without distinguishing individual object instances.
* **Instance Segmentation:** Classifies every pixel into a category label and separates distinct instances of the same object class.
* **Panoptic Segmentation:** Combines Semantic and Instance segmentation to label every pixel, covering both structured foreground instances ("things") and background regions ("stuff").

### Q28: How does the YOLO (You Only Look Once) architecture work?
YOLO frames object detection as a single regression problem. It divides an image into a grid and simultaneously predicts bounding box coordinates and class probabilities in a single forward pass.

### Q29: What is Non-Maximum Suppression (NMS) in Object Detection?
NMS is a post-processing technique that filters out duplicate, overlapping bounding boxes predicting the same object by retaining only the box with the highest confidence score and dropping those with a high Intersection over Union (IoU) overlap.

### Q30: What is the U-Net architecture?
U-Net is an encoder-decoder network featuring skip connections between corresponding contracting and expanding layers. It is widely used for semantic segmentation, especially in medical imaging.

### Q31: What is Optical Flow?
Optical flow measures the pattern of apparent motion of objects, surfaces, or edges between consecutive video frames caused by relative movement between the observer and the scene.

### Q32: What is Pose Estimation?
Pose estimation detects and tracks key structural points (joints, landmarks) on human bodies, animals, or objects in 2D or 3D space.

---

## Section 6: Advanced Topics & Emerging Architectures

### Q33: What is a Vision Transformer (ViT)?
A Vision Transformer splits an image into non-overlapping patches, flattens them, embeds them linearly, and processes them using multi-head self-attention mechanisms originally designed for natural language processing.

### Q34: How do Vision Transformers differ from traditional CNNs?
* **CNNs:** Have inductive biases like translation equivariance and local locality, operating well on smaller datasets.
* **ViTs:** Lack explicit local spatial priors, relying on global self-attention. They require larger pre-training datasets to outperform CNNs but scale better.

### Q35: What is generative image modeling (e.g., GANs vs. Diffusion Models)?
* **GANs (Generative Adversarial Networks):** Use a generator network and a discriminator network in a min-max game to produce realistic synthetic images.
* **Diffusion Models:** Learn to generate images by reversing an iterative gradual noise-addition process (denoising diffusion).

### Q36: What is Neural Radiance Fields (NeRF)?
NeRF uses a fully connected deep network to represent 3D scenes as continuous volumetric functions, predicting color and density from 2D views and camera poses to render novel photorealistic viewpoints.

---

## Section 7: Evaluation Metrics & Validation

### Q37: What is Intersection over Union (IoU)?
IoU evaluates bounding box accuracy by computing the ratio of the area of overlap between the predicted bounding box ($A$) and ground truth bounding box ($B$) to the area of their union:
$$\text{IoU} = \frac{\text{Area}(A \cap B)}{\text{Area}(A \cup B)}$$

### Q38: What is Mean Average Precision (mAP) in Object Detection?
mAP evaluates object detection performance by calculating the mean of Average Precision (AP) across all classes. AP measures the area under the Precision-Recall curve computed at predefined IoU thresholds (e.g., $\text{IoU} = 0.50$).

### Q39: What is Mean IoU (mIoU) in Semantic Segmentation?
mIoU measures pixel-level overlap accuracy by calculating the average IoU score across all target semantic classes.

### Q40: What is Data Augmentation, and why is it used in Computer Vision?
Data Augmentation applies transformations (e.g., rotation, cropping, flipping, color jittering) to training images. It artificially increases dataset diversity to improve model generalization and prevent overfitting.