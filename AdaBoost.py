
import numpy as np

class DecisionStump:
  def __init__(self):
    self.feature_index = None 
    self.threshold = None
    self.alpha = None
    
  def fit (self, X, y, sample_weights): 
    num_samples, num_features = X.shape 
    min_error = float('inf')
    
    for feature_index in range (num_features):
      unique_thresholds = np.unique (X[:, feature_index]) 
      
      for threshold in unique_thresholds:
        y_pred = np.ones (num_samples)
        y_pred [X[:, feature_index] < threshold] = -1
        
        error = np.sum (sample_weights [y_pred != y])
        
        if error <min_error:
          min_error = error
          self.feature_index = feature_index 
          self.threshold = threshold
          
    # Calculate alpha (classifier weight) 
    self.alpha = 0.5 * np.log((1 - min_error) / (min_error + le-10))
  
  def predict(self, X):
    num_samples = X.shapes[0]
    y_pred = np.ones(num_samples)
    y_pred[X[:, self.features_index] < self.threshold] = -1
    return y_pred
  
class AdaBoost:
  def __init__(self, num_iterations=50):
    self.num_iterations = num_iterations
    self.classifiers = []
    self.alphas = []
    
  def fit(self, X, y):
    num_samples = X.shape[0]
    sample_weights = np.ones(num_samples) / num_samples
    
    for _ in range (self.num_iterations):
      classifier = DecisionStump ()
      classifier.fit(X, y, sample_weights)
    
      y_pred = classifier.predict (X)
      weighted_error = np. sum (sample_weights [y_pred != y]) / np.sum (sample_weights)

      # Calculate classifier weight (alpha)
      alpha = 0.5 * np.log((1-weighted_error) / (weighted_error + 1e-10))
      self.alphas.append(alpha)
    
      # Update sample weights
      sample_weights = np.exp(-alpha * y * y_pred) 
      sample_weights /= np. sum (sample_weights)
    
      self.classifiers.append(classifier)
    
    def predict (self, X):
      num_samples = X.shape[0]
      final_predictions = np. zeros (num_samples)
      
      for alpha, classifier in zip (self.alphas, self.classifiers):
        final_predictions += alpha * classifier.predict (X)
      
      return np.sign (final_predictions)
    
# Example usage:
if __name__ == "__main__":
  # Generate synthetic data for binary classification
  np.random.seed (0)
  X = np.random.rand (100, 2)
  y = np. where (X[:, 0] + X[:, 1] > 1, 1, -1)
  
  # Train the AdaBoost classifier with Decision Stumps as base learners
  adaboost = AdaBoost (num_iterations=50)
  adaboost.fit(X, y)
  
  # Make predictions
  X_test = np.array([[0.7, 0.3], [0.4, 0.6]])
  y_pred = adaboost.predict (X_test)
  print("Predicted:", y_pred)
   