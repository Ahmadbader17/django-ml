# linear_regression/models.py
from django.db import models

# Store inputs and predictions
class Prediction(models.Model):
    input_value = models.FloatField()
    predicted_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Input: {self.input_value}, Prediction: {self.predicted_value}"
