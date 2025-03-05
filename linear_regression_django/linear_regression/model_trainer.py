# linear_regression/model_trainer.py
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# Generate some sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 8, 18, 32, 50])  # More complex pattern than linear

# Apply polynomial transformation
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train a polynomial regression model
model = LinearRegression()
model.fit(X_poly, y)

# Save the model and the transformer
joblib.dump(model, 'model.pkl')
joblib.dump(poly, 'transformer.pkl')
