import cv2
import pytesseract
from gtts import gTTS
import pygame
from io import BytesIO

pygame.mixer.init()

def text_to_speech_from_video():
    video = cv2.VideoCapture("https://192.168.63.88:8080/video")
    video.set(3, 640)
    video.set(4, 480)

    while True:
        ret, frame = video.read()
        if not ret:
            print("Error: Failed to read frame. Exiting...")
            break

        data = pytesseract.image_to_data(frame, output_type=pytesseract.Output.DICT)
        if 'text' in data and data['text']:
            text = ' '.join(data['text'])
            tts = gTTS(text=text, lang='en', slow=False)
            fp = BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            pygame.mixer.music.load(fp)
            pygame.mixer.music.play()

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    pygame.quit()

text_to_speech_from_video()
