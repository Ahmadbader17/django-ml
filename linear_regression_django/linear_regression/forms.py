from django import forms

class PredictForm(forms.Form):
    value = forms.FloatField(label='Enter a number')
