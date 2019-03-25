import pandas as pd
from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

df = pd.read_csv('csco-daily.csv', index_col=0)

print(df)
