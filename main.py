import numpy
from flask import Flask, render_template, request
import cv2
from gtts import gTTS
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
app = Flask(__name__)

@app.route("/")
def upload():
    return render_template('upload.html')


@app.route("/", methods=["GET", "POST"])
def success():
    if request.method == 'POST':
        img = request.files['img'].read()
        Image = numpy.fromstring(img, numpy.uint8)
        images= cv2.imdecode(Image, cv2.IMREAD_COLOR)
        text= pytesseract.image_to_string(images)
        result = gTTS(text=text, lang='en', slow=False)
        result.save("result.mp3")
        os.system("result.mp3")
    return render_template('success.html',text=text)


if __name__ == "__main__":
    app.run(debug=True)