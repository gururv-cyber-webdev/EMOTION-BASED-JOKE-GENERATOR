from django.shortcuts import render
import cv2
import base64
import numpy as np
from django.http import JsonResponse
from fer import FER
import pyjokes
from django.views.decorators.csrf import csrf_exempt
import json

# Initialize the FER model
detector = FER(mtcnn=True)

def emotion_detection_view(request):
    return render(request, 'emotion_detection.html')

@csrf_exempt
def detect_emotion(request):
    if request.method == 'POST':
        try:
            # Decode the incoming image data
            data = json.loads(request.body)
            image_data = data['image'].split(',')[1]

            # Convert base64 to numpy array
            img = np.frombuffer(base64.b64decode(image_data), np.uint8)
            frame = cv2.imdecode(img, cv2.IMREAD_COLOR)

            if frame is None:
                return JsonResponse({'error': 'Failed to decode image'}, status=400)

            # Convert the frame to RGB for emotion detection
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detect emotions in the frame
            result = detector.detect_emotions(rgb_frame)

            # Initialize default response
            emotion = "neutral"
            joke = ""

            if result:
                for face in result:
                    emotions = face["emotions"]
                    dominant_emotion = max(emotions, key=emotions.get)

                    if dominant_emotion == 'sad':
                        emotion = "sad"
                        joke = pyjokes.get_joke()

            return JsonResponse({'emotion': emotion, 'joke': joke})
        except Exception as e:
            # Return a useful error message for debugging
            return JsonResponse({'error': f'Error processing request: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
