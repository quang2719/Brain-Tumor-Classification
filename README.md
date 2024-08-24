# 🧠 Brain Tumor Classification

<div align="center">
<a href="https://raw.githubusercontent.com/quang2719/Brain-Tumor-Classification/main/IMG_readme_file/new_background_icon.ico" target="_blank">
<img src="https://raw.githubusercontent.com/quang2719/Brain-Tumor-Classification/main/IMG_readme_file/new_background_icon.ico" alt="My background" style="max-width: 300px;">
</a>
</div>

## 📝 Project Description

This repository contains Jupyter Notebooks exploring brain tumor classification using various deep learning techniques.

## Notebooks 📓
*I recommend running notebook nb1_training_original_model first as it contains specific instructions for the other notebooks.*
* **nb0_predict_new_img.ipynb** 🚀: Use this notebook to run predictions on new, unseen samples.
* **nb1_training_original_model.ipynb** 🥇: The initial notebook with the core model implementation. This will be continuously updated and serves as a guide to the other notebooks.
* **nb2_optimization_model.ipynb** 🏋️‍♀️: Explores techniques like regularization to address overfitting issues in the baseline model.
* **nb3_compare_with_other_model.ipynb** 🆚: Compares the performance of our model against established neural networks like LeNet-5, AlexNet, and MobileNet.
* **nb4_using_trainsfer_learning.ipynb** 🔄: Leverages transfer learning to fine-tune the VGG16 network on our brain tumor dataset.

**Note:** The number of notebooks may change in the future as the project evolves and incorporates feedback from my supervisor. Please refer to the individual notebooks for detailed information about each experiment.

## 📁 Dataset

The dataset used in this project was provided by my teacher, Mr. Hinh.

## 🏗️ Project Structure

### 🧪 Model Testing

Users can test new data using the stored models. Open the `predict_new_img.ipynb` notebook, and load either:

- **`BrainTumor_v1.keras`**: The original model.
- **`BrainTumor_v2.keras`**: The optimized model.
- **`BrainTumor_v3.keras`**: The transfer learning model.

To test, simply change the value in the `load_model()` method between these two models.

## 📊 Results

* **First Model**: 86.75% accuracy (overfitting)
* **Second Model**: 94.5% accuracy (optimized)

## 🛠️ Contact
[![Facebook](https://img.shields.io/badge/Facebook-blue?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/qq2719/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/quang-nv-ptit/)

