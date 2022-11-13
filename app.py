# IMport modul yang dibutuhkan
from flask import (
    Flask,
    request,
    render_template,
)
import pickle
import numpy as np
from scipy.spatial import distance

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getInputValues():
    val = request.form['myForm']


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return 'Method Not Allowed. Ke halaman utama terlebih dahulu untuk mengakses halaman ini'

    if request.method == 'POST':
        inputValue = request.form['myForm']

        if inputValue != None:
            # Ambil nilai dari form
            values = []
            for key, value in inputValue.items():
                values.append(float(value))

        # Hitung jarak Euclidean antara nilai input dengan nilai yang ada di dataset

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
