import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound

path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path

def text_to_speech_from_video():
    video = cv2.VideoCapture("https://192.168.63.88:8080/video")
    video.set(3, 640)  # Set width
    video.set(4, 480)   # Set height

    while True:
        ret, frame = video.read()
        if not ret:
            print("Error: Failed to read frame. Exiting...")
            break

        # Resize the frame for better OCR performance
        resized_frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

        data = pytesseract.image_to_data(resized_frame, output_type=pytesseract.Output.DICT)
        if 'text' in data and data['text']:
            text = ' '.join(data['text'])
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save("temp.mp3")
            playsound("temp.mp3")

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

text_to_speech_from_video()

