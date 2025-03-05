# Django Linear Regression Project

This is a simple Django project that implements a linear regression model to make predictions based on input data. The project allows users to input data, run a prediction using a trained model, and view the prediction results.

## Features

- User can input values and get predictions from the linear regression model.
- Displays prediction history (input values, predicted values, and the date of prediction).
- Clean and simple user interface using Django templates.

## Project Structure

```
/linear_regression_django
├── manage.py
├── linear_regression_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── linear_regression_app/
│       ├── __init__.py
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       └── templates/
│           └── index.html
└── requirements.txt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/linear-regression-django.git
cd linear-regression-django
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

5. Run the Django development server:
```bash
python manage.py runserver
```

6. Open your browser and go to http://127.0.0.1:8000/ to view the application.

## Usage

- Input values in the form and click the **Predict** button.
- View the prediction results along with the history of previous predictions.

## Technologies Used

- Python
- Django
- Scikit-learn (for linear regression)
- HTML/CSS (for front-end)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
