# 🎭 Emotion-Based Joke Generator

An AI-powered Django web application that detects facial emotions in real time and responds with mood-lifting jokes to improve user experience.

---

## 📌 Project Description

* Built a Django-based web application for real-time emotion detection
* Uses OpenCV to capture facial expressions through a webcam
* Detects sadness and generates appropriate jokes automatically
* Integrates PyJokes for humor generation and NumPy for fast processing

---

## 🚀 Features

* Real-time face detection using webcam
* Emotion detection focused on identifying sadness
* Automatic joke generation to cheer up users
* Simple and user-friendly web interface
* Fast and efficient processing using NumPy
* Runs locally using Django development server

---

## 🛠️ Technologies Used

* Python
* Django
* OpenCV
* NumPy
* PyJokes
* HTML, CSS, JavaScript
* SQLite (Django default database)

---

## 📂 Project Structure

```
GA/
│── facedetection/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
│── MyApp1/
│   ├── migrations/
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── apps.py
│
│── db.sqlite3
│── manage.py
```

---

## ▶️ How to Run the Project

* Navigate to the project directory:

  ```bash
  cd GA
  ```

* Start the Django development server:

  ```bash
  python manage.py runserver
  ```

* Open the application in your browser:

  ```
  http://127.0.0.1:8000/myapp/emotion_detection/
  ```

---

## 🖥️ Output

* Webcam captures the user’s face
* Emotion detection runs in real time
* When sadness is detected, a joke is displayed in a pop-up
* Helps improve user mood through humor

---

## 📌 Use Cases

* Mental health support applications
* Stress relief and entertainment tools
* Human–computer interaction research
* Academic mini-projects and demonstrations

---

## 🔮 Future Enhancements

* Support for multiple emotions (happy, angry, surprised, etc.)
* Emotion-based motivational quotes
* Voice-based emotion recognition
* Improved UI and user experience

---
