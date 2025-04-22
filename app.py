from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipline import PredictionPipeline
from src.datascience import logger

model = PredictionPipeline()


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    prediction = None

    if request.method == "POST":
        try:
            features = [
                float(request.form['fixed_acidity']),
                float(request.form['volatile_acidity']),
                float(request.form['citric_acid']),
                float(request.form['residual_sugar']),
                float(request.form['chlorides']),
                float(request.form['free_sulfur_dioxide']),
                float(request.form['total_sulfur_dioxide']),
                float(request.form['density']),
                float(request.form['pH']),
                float(request.form['sulphates']),
                float(request.form['alcohol'])
            ]

            input_data = np.array([features])
            prediction = round(model.predict(input_data)[0],2)

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)