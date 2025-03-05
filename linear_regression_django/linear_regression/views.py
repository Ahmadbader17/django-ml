# linear_regression/views.py
from django.shortcuts import render
from .forms import PredictForm
from .models import Prediction
import joblib

# Load the model and transformer
model = joblib.load('model.pkl')
transformer = joblib.load('transformer.pkl')

def predict_view(request):
    prediction = None

    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            
            # Make prediction with polynomial features
            transformed_value = transformer.transform([[value]])
            prediction = model.predict(transformed_value)[0]

            # Save the input and prediction to the database
            Prediction.objects.create(input_value=value, predicted_value=prediction)

    else:
        form = PredictForm()

    # Retrieve all stored predictions
    all_predictions = Prediction.objects.all().order_by('-created_at')

    return render(request, 'linear_regression/predict.html', {
        'form': form,
        'prediction': prediction,
        'all_predictions': all_predictions
    })
