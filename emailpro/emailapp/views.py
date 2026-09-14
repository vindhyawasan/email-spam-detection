from django.shortcuts import render
import os
import re
import joblib


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


model_path = os.path.join(
    BASE_DIR,
    'emailapp',
    'to_model',
    'spam_model.pkl'
)

vectorizer_path = os.path.join(
    BASE_DIR,
    'emailapp',
    'to_model',
    'tfidf_vectorizer.pkl'
)


# Load model and vectorizer once
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def index(request):

    result = None

    if request.method == 'POST':

        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Combine subject and message
        email_content = subject + " " + message

        if email_content.strip():

            # Clean the email
            email_content_cleaned = clean_text(email_content)

            # Convert text into TF-IDF numbers
            email_content_vectorized = vectorizer.transform(
                [email_content_cleaned]
            )

            # Prediction
            prediction = model.predict(
                email_content_vectorized
            )[0]

            # Convert prediction into readable result
            if prediction == 'spam':
                result = 'Spam Email'
            else:
                result = 'Not Spam'

    return render(
        request,
        'index.html',
        {'result': result}
    )