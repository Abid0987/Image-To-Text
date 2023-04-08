from flask import Flask, render_template, request
import cv2
import pytesseract
import numpy as np

# Now you can use the NumPy library by referring to it as "np"
my_array = np.array([1, 2, 3, 4])


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded image from the HTML form
    image = request.files['image']

    # Preprocess the image using OpenCV
    img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Extract text using pytesseract
    text = pytesseract.image_to_string(gray)

    return render_template('result.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
