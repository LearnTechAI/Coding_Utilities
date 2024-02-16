import numpy as np

class LogisticRegression():
  
  def  __init__ (self,lr,n_iter):
    self.lr=lr
    self.n_iter=n_iter
    self.weights=None
    self.bias=None
    
  def sigmoid (self,z):
    return 1 / (1 + np.exp(-z))
  
  def fit_model (self, X,y):
    n_samples,n_features = X.shape
    
    #weight bias initialization 
    self.weights = np.random.rand(n_features)
    self.bias=0
    
    # start training iterations
    for _ in range (self.n_iter):
      linear_output = np.dot( X, self.weights) + self.bias 
      y_pred = self.sigmoid(linear_output)
      
      #compute gradient
      delw = (1/n_samples) * np.dot(X.T, (y_pred-y)) 
      delb = (1/n_samples) * np.sum(y_pred-y)
      
      #update weights and bias 
      self.weights = self.weights-self.lr*delw 
      self.bias = self.bias-self.lr*delb
      
  def predict_class (self,X):
    linear_output = np.dot(X, self.weights) + self.bias 
    y_pred = self.sigmoid(linear_output)
    y_pred_class = [1 if i>0.5 else 0 for i in y_pred]
    return y_pred_class