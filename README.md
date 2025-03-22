# Lab 4 - Part 2: Brain Tumor Detection Using CNN

## 📊 Overview
This project is part of the Parallel and Distributed Computing course (DSAI 3202), Lab 4 Part 2. It applies a Convolutional Neural Network (CNN) to detect the presence of brain tumors from MRI scans.

## 📂 Dataset
- **Folder**: `data/brain_tumor_dataset`
- **Subfolders**:
  - `yes/`: Images with brain tumors
  - `no/`: Images without brain tumors

## 📁 Project Structure
```
/Parallel-and-Distributed-Computing-
|
|➜ brain_tumor_classifier/
|   |➜ __init__.py
|   |➜ train.py              # Contains the main pipeline and training logic
|   |➜ model.py              # CNN model definition
|   |➜ data_loader.py        # Data loading and preprocessing
|
|➜ data/
|   |➜ brain_tumor_dataset/   # Contains 'yes' and 'no' folders
|
|➜ main.py                  # Entry point to run the entire pipeline
|
|➜ README.md
|➜ requirements.txt
```

## 🎨 Model Summary
- **Architecture**: CNN (Sequential)
- **Layers**: Conv2D, MaxPooling2D, Flatten, Dense
- **Loss Function**: Binary Crossentropy
- **Optimizer**: Adam
- **Metrics**: Accuracy
- **Epochs**: 10

## 📊 Training & Evaluation Output
```
Epoch 1/10  - val_accuracy: 0.7024
Epoch 5/10  - val_accuracy: 0.7651
Epoch 10/10 - val_accuracy: 0.7651

              precision    recall  f1-score   support
           0       0.73      0.62      0.67        26
           1       0.78      0.86      0.81        51

    accuracy                           0.76        77
   macro avg       0.76      0.74      0.74        77
weighted avg       0.76      0.76      0.76        77
```

## 🔍 Interpretation
- The model achieved **76% accuracy** in detecting brain tumors.
- It performs better at detecting positive (tumor-present) cases.
- False negatives are low, which is desirable in medical imaging.

## 🚀 Future Improvements
- Add **data augmentation** to reduce overfitting.
- Use **pre-trained models** like VGG16 or ResNet.
- Tune hyperparameters (learning rate, batch size).
- Add **early stopping** and model checkpointing.



🙌 Project by Aamir Ahmed | DSAI 3202

