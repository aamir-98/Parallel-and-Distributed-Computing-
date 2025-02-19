import time
import numpy as np
import pandas as pd
from math import sqrt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from threading import Thread, Lock
from multiprocessing import Pool, cpu_count
from joblib import parallel_backend  # Ensures no conflict with multiprocessing

# Load dataset
train_path = "/home/student/Parallel-and-Distributed-Computing-/housing_price_data/train.csv"
data = pd.read_csv(train_path)

# Encode categorical features
categorical_columns = data.select_dtypes(include=['object']).columns
label_encoders = {col: LabelEncoder().fit(data[col]) for col in categorical_columns}

for col, le in label_encoders.items():
    data[col] = le.transform(data[col])

# Split into features and target
X = data.drop(columns=['SalePrice'])  
y = data['SalePrice']

# Fill missing values
imputer = SimpleImputer(strategy='mean')
X_filled = imputer.fit_transform(X)

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_filled, y, test_size=0.2, random_state=42)

# Lock for threading
lock = Lock()

# Best model tracking
best_rmse = float('inf')
best_mape = float('inf')
best_model = None
best_parameters = {}

# Function to evaluate parameters
def evaluate_params(n_estimators, max_features, max_depth, parallel=True):
    global best_rmse, best_mape, best_model, best_parameters

    rf_model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_features=max_features,
        max_depth=max_depth,
        n_jobs=cpu_count() if parallel else 1,  # Allow parallelization only when threading
        random_state=42
    )

    with parallel_backend('loky', n_jobs=cpu_count() if parallel else 1):
        rf_model.fit(X_train, y_train)

    y_val_pred = rf_model.predict(X_val)
    rmse = sqrt(mean_squared_error(y_val, y_val_pred))
    mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100

    with lock:
        print(f"Params: {n_estimators}, {max_features}, {max_depth}. RMSE: {rmse}, MAPE: {mape}%")
        if mape < best_mape:  # Prioritize lower MAPE for better generalization
            best_rmse = rmse
            best_mape = mape
            best_model = rf_model
            best_parameters = {'n_estimators': n_estimators, 'max_features': max_features, 'max_depth': max_depth}

# **Threading Version**
def train_threading():
    start_time = time.time()
    threads = []
    
    param_grid = [
        (100, 'sqrt', None), (200, 'sqrt', None), (300, 'log2', None), (400, None, None),
        (100, None, 10), (200, 'sqrt', 10), (300, 'log2', 5), (400, None, 5)
    ]  # Reduced grid for efficiency

    for params in param_grid:
        thread = Thread(target=evaluate_params, args=(*params, True))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Best Params: {best_parameters}, RMSE = {best_rmse}, MAPE: {best_mape}%")
    print(f"Threading Execution Time: {time.time() - start_time:.2f} seconds")

# Multiprocessing Version
def train_multiprocessing():
    start_time = time.time()

    param_grid = [
        (100, 'sqrt', None, False), (200, 'sqrt', None, False), (300, 'log2', None, False), (400, None, None, False),
        (100, None, 10, False), (200, 'sqrt', 10, False), (300, 'log2', 5, False), (400, None, 5, False)
    ]

    with Pool() as pool:
        pool.starmap(evaluate_params, param_grid)  # More efficient than map()

    print(f"Best Params: {best_parameters}, RMSE = {best_rmse}, MAPE: {best_mape}%")
    print(f"Multiprocessing Execution Time: {time.time() - start_time:.2f} seconds")

# Run optimized training
if __name__ == "__main__":
    train_multiprocessing()