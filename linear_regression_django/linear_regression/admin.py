# linear_regression/admin.py
from django.contrib import admin
from .models import Prediction

# Register the model in the admin site
admin.site.register(Prediction)
