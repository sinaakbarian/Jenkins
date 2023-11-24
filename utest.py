# test code

import unittest
import numpy as np
from main import SimpleLinearModel

def test_model_prediction(self):
      # Create a simple dataset
      X_train = np.array([[1], [2], [3]])
      y_train = np.array([2, 4, 6])

      # Instantiate the model
      model = SimpleLinearModel()

      # Fit the model
      model.fit(X_train, y_train)

      # Test the prediction
      X_test = np.array([[4]])
      prediction = model.predict(X_test)

      # Assert that the prediction is close to the expected value
      self.assertAlmostEqual(prediction[0], 8, places=2, msg="Model prediction failed for X_test=[4]")

if __name__ == '__main__':
    test_model_prediction()
