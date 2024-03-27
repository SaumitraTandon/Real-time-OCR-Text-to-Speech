# OCR and Text-to-Speech with OpenCV and Tesseract

This repository contains Python scripts that demonstrate various approaches to Optical Character Recognition (OCR) and text-to-speech conversion using the OpenCV library and Google's Tesseract OCR engine.

## Prerequisites

- Python 3.x
- OpenCV library
- Pytesseract library
- Google Text-to-Speech (gTTS) library
- Playsound library (for `python_2.py`)
- Pygame library (for `python_3.py`)

## Installation

1. Clone the repository:
2. Install the required dependencies:
3. Download the Tesseract OCR engine and add its path to the scripts. (e.g., `pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"`)

## Usage

### 1. python_2.py

This script uses OpenCV to read frames from a video stream, performs OCR using Pytesseract, and converts the recognized text to speech using gTTS and playsound libraries.

To run the script:
### 2. python_3.py

Similar to `python_2.py`, this script performs OCR on video frames but uses the Pygame library for text-to-speech conversion.

To run the script:
### 3. python_4.py

This script demonstrates OCR and text-to-speech functionality on static images. It provides options to detect characters, words, and perform text-to-speech conversion.

To run the script:
### 4. pythonOCR.py

This comprehensive script offers various options for OCR and text-to-speech tasks, including character detection, word detection, video feed processing, and image processing.

To run the script:
Follow the on-screen prompts to select the desired option.

## File Structure

- `python_2.py`: OCR and text-to-speech on video frames using playsound.
- `python_3.py`: OCR and text-to-speech on video frames using Pygame.
- `python_4.py`: OCR and text-to-speech on static images.
- `pythonOCR.py`: Comprehensive script with multiple OCR and text-to-speech options.
- `README.md`: This file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- The OpenCV library and its contributors.
- The Pytesseract library and its contributors.
- The Google Text-to-Speech (gTTS) library and its contributors.
- The Playsound library and its contributors.
- The Pygame library and its contributors.
- The Tesseract OCR engine and its contributors.
