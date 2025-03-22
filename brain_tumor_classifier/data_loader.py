import os
import cv2
import numpy as np

def load_data(dataset_path, img_size=(128, 128)):
    X, y = [], []
    for label in ['yes', 'no']:
        folder = os.path.join(dataset_path, label)
        for img in os.listdir(folder):
            img_path = os.path.join(folder, img)
            img_arr = cv2.imread(img_path)
            if img_arr is None:
                continue
            img_arr = cv2.resize(img_arr, img_size)
            X.append(img_arr)
            y.append(1 if label == 'yes' else 0)
    return np.array(X), np.array(y)
