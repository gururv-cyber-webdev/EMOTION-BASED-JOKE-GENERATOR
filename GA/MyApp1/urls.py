from django.urls import path
from .views import emotion_detection_view, detect_emotion

urlpatterns = [
    path('emotion_detection/', emotion_detection_view, name='emotion_detection'),
    path('detect_emotion/', detect_emotion, name='detect_emotion'),
]
