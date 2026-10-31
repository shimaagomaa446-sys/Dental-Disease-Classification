# Dental Disease Classification using Deep Learning

## Project Overview
This project aims to classify dental diseases from dental images using Deep Learning and Convolutional Neural Networks.

Three models were trained and evaluated:
- Custom CNN
- EfficientNet
- MobileNet

## Dataset Classes
The model classifies dental images into six categories:
1. Calculus
2. Caries
3. Gingivitis
4. Ulcers
5. Tooth Discoloration
6. Hypodontia

## Model Performance

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Custom CNN | 84.87% | 86.22% | 84.87% | 85.19% |
| EfficientNet | 93.59% | 93.63% | 93.59% | 93.61% |
| MobileNet | 92.29% | 92.38% | 92.29% | 92.30% |

**Best Performing Model: EfficientNet**

EfficientNet achieved the highest overall performance with 93.59% test accuracy.

## Technologies Used
- Python
- TensorFlow / Keras
- CNN
- Transfer Learning
- EfficientNet
- MobileNet
- NumPy
- Scikit-learn
- Gradio

## Deployment
A web application was developed using Gradio.

Users can upload a dental image and receive:
- Predicted dental disease class
- Prediction confidence scores




## Disclaimer
This project is developed for educational and research purposes only. It is not intended to replace professional dental examination or medical diagnosis.
