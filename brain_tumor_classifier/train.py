from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow.keras.optimizers import Adam
from brain_tumor_classifier.data_loader import load_data
from brain_tumor_classifier.model import create_model
import numpy as np

def run_pipeline():
    X, y = load_data('data/brain_tumor_dataset')
    X = X / 255.0
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = create_model()
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=10, validation_split=0.2)

    preds = (model.predict(X_test) > 0.5).astype("int32")
    print(classification_report(y_test, preds))
