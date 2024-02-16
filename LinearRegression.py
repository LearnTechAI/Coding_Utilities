import numpy as np
from tqdm import tqdm

class LinearRegression():
  
  def __init__(self, lr,n_iter):
    self.lr=lr          #learning rate
    self.n_iter=n_iter  #number_of_iteration_to_train
    self.weights=None
    self.bias=None
    
  def fit_model (self, X, y):
    """to train model using gradient descent""" 
    n_samples,n_features = X.shape
    print (n_samples,n_features)
    self.weights=np.random.rand (n_features)
    self.bias=0
    
    for _ in tqdm(range (self.n_iter)):
      
      # calculate y_predicted
      y_pred=np.dot (X, self.weights) +self.bias
      
      # Compute Gradients
      delw= (1/n_samples) *np.dot (X. T, (y_pred-y)) 
      delb= (1/n_samples) *np. sum (y_pred-y)

      # update weights and bias
      self.weights=self. weights-self.lr*delw
      self.bias=self.bias-self.lr*delb
    return
  
  def predict (self,X):
    return (np.dot (X, self.weights) +self.bias)