from flask import Flask
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/api/get-data')
def getConsolidatedData():
    data = pd.read_table('./Output/consolidated_output.csv', sep=',|\|', engine='python')
    json_data = data.to_json(orient='split')
    parsed_data = json.loads(json_data)
    return(json.dumps(parsed_data))
