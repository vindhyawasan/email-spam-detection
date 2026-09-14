# 📧 Spam Email Detection using Machine Learning

A Machine Learning-based web application that detects whether an email is **Spam** or **Not Spam (Ham)** based on its subject and content.

The project uses **TF-IDF Vectorization** to convert email text into numerical features and **Multinomial Naive Bayes** to classify the email.

## 🚀 Features

* 📩 Enter email subject and content
* 🧹 Text preprocessing
* 🔢 TF-IDF text vectorization
* 🤖 Multinomial Naive Bayes classification
* ✅ Spam / Not Spam prediction
* 📊 Model evaluation
* 🌐 Django web interface
* ⚡ Real-time prediction

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Django
* TF-IDF
* Multinomial Naive Bayes
* HTML
* CSS
* Git & GitHub

## 🧠 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Remove Message ID & Date
   ↓
Handle Missing Values
   ↓
Subject + Message
   ↓
Text Preprocessing
   ↓
Train/Test Split
   ↓
TF-IDF Vectorization
   ↓
Multinomial Naive Bayes
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation
```

## 📊 Model Performance

The trained Multinomial Naive Bayes model achieved approximately:

**99% Accuracy**

Classification results:

| Class | Precision | Recall | F1-Score |
| ----- | --------- | ------ | -------- |
| Ham   | 0.98      | 0.99   | 0.99     |
| Spam  | 0.99      | 0.98   | 0.99     |

## 📂 Project Structure

```text
emailpro/
│
├── manage.py
│
├── emailapp/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── to_model/
│   │   ├── spam_model.pkl
│   │   └── tfidf_vectorizer.pkl
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
│
└── requirements.txt
```

## 🔄 How It Works

1. The user enters an email **subject and content**.
2. Django receives the submitted email.
3. The subject and content are combined into a single text input.
4. The text is cleaned using preprocessing techniques.
5. The saved TF-IDF vectorizer converts the text into numerical features.
6. The saved Naive Bayes model analyzes the features.
7. The application predicts whether the email is **Spam** or **Not Spam**.
8. The prediction is displayed on the webpage.

## 🧪 Example

### Spam Email

**Subject:**

```text
Congratulations! You Won a Prize
```

**Content:**

```text
Congratulations! You have won ₹50,000. Claim your prize immediately by clicking the link below. This offer expires today.
```

**Prediction:**

```text
🔴 Spam Email
```

### Not Spam Email

**Subject:**

```text
Team Meeting Tomorrow
```

**Content:**

```text
Hi team, our meeting is scheduled for tomorrow at 10 AM. Please bring the project report and presentation.
```

**Prediction:**

```text
🟢 Not Spam
```

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Go to the project directory:

```bash
cd emailpro
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 📦 Required Libraries

Example `requirements.txt`:

```text
Django
pandas
scikit-learn
joblib
```

## 📌 Future Improvements

* Add email history
* Add user authentication
* Store predictions in MySQL
* Improve text preprocessing
* Compare multiple ML algorithms
* Add probability/confidence score
* Deploy the application online

## 👨‍💻 Author

**Vindhywasan Singh**

B.Tech Computer Science Engineering

GitHub: Add your GitHub profile link here

LinkedIn: Add your LinkedIn profile link here

---

⭐ If you find this project useful, consider giving it a star!
