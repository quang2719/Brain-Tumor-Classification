# 🧠 Brain Tumor Classification

<div align="center">
<a href="https://raw.githubusercontent.com/quang2719/Brain-Tumor-Classification/main/IMG_readme_file/new_background_icon.ico" target="_blank">
<img src="https://raw.githubusercontent.com/quang2719/Brain-Tumor-Classification/main/IMG_readme_file/new_background_icon.ico" alt="My background" style="max-width: 300px;">
</a>
</div>

## 📝 Project Description

This project aims to classify brain tumor images using Convolutional Neural Networks (CNNs). The project involves creating, training, and optimizing models to improve accuracy while addressing overfitting.

## 📁 Dataset

The dataset used in this project was provided by my teacher, Mr. Hinh.

## 🏗️ Project Structure

### 📂 Resources

- **Dataset**: MRI images of brain tumors.
- **Notebooks**: There are three Jupyter notebooks in this project.
- **Models**: Two trained models are stored in the project for testing on new data:
  - `BrainTumor_v1.keras` (Original Model)
  - `BrainTumor_v2.keras` (Optimized Model)

### 📓 Notebooks

1. **`training_original_model.ipynb`**:
   - This notebook builds, trains, and evaluates a neural network model provided by my teacher using the dataset. The model achieved 86.7% accuracy on the test set, but it suffered from overfitting.

2. **`model_comparison.ipynb`**:
   - In this notebook, the original model is compared with other well-known neural networks such as Lenet5, AlexNet, and MobileNet. The original model showed the highest accuracy on the validation set but was still overfitting with 86.7% accuracy on the test set.

3. **`optimized_model.ipynb`**:
   - This notebook contains the optimized version of the original model. Regularization techniques were applied, and the model was simplified to reduce overfitting. The optimized model achieved 94.5% accuracy on the test set.

### 🧪 Model Testing

Users can test new data using the stored models. Open the `predict_new_img.ipynb` notebook, and load either:

- **`BrainTumor_v1.keras`**: The original model.
- **`BrainTumor_v2.keras`**: The optimized model.

To test, simply change the value in the `load_model()` method between these two models.

## 📊 Results

* **First Model**: 86.75% accuracy (overfitting)
* **Second Model**: 94.5% accuracy (optimized)

## 🛠️ Dependencies

The following libraries and tools were used in this project:

* ![OpenCV](https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg) `cv2` 
* ![NumPy](https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg) `numpy`
* ![TensorFlow](https://upload.wikimedia.org/wikipedia/commons/2/2d/Tensorflow_logo.svg) `tensorflow`
* ![scikit-learn](https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg) `sklearn`
* ![Pillow](https://upload.wikimedia.org/wikipedia/commons/e/e0/Python-logo-notext.svg) `PIL` 
