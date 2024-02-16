import numpy as np

class GradientBoostingRegression:
  
  def __init__(self, num_iterations=100, learning_rate=0.1):
    self.num_iterations = num_iterations
    self.learning_rate= learning_rate
    self.models = []
    
  def fit (self, X, y):
    F = np.mean (y)
    for _ in range (self.num_iterations):
      residuals = (y - F)
  
      # Train a linear regressor on the residuals (e.g., using least squares)
      weak_learner = self.train_linear_regressor (X, residuals)
      prediction = weak_learner.predict (X)
      F += self.learning_rate * prediction
      self.models.append(weak_learner)
  
  def train_linear_regressor (self, X, residuals):
    # Implement linear regression (e.g., using numpy or scikit-
    # Return_the linear regressor (e.g., coefficients)
    pass # Replace with your linear regression training code
  
  def predict (self, X):
    predictions = np. mean (X) *np. ones (X.shape[0])
    for model in self.models:
      predictions += self.learning_rate * model.predict (X)
    return predictions