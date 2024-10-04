from flask import Flask, send_file, render_template
from flask_cors import CORS
import os

# Create instance of Flask class
app = Flask(__name__)
CORS(app) # enable CORS (Cross-Origin Resource Sharing) for all routes

# Route decorator indicates which route should trigger function home()py
@app.route('/')
def home():
    return "<p>Welcome to SMeshboard's Flask backend server!</p>"

@app.get('/get-data')
def send_data():
    # data = {"message": render_template('show_data.html')}
    data_path = os.path.join(app.root_path, 'static', '4004_pmsa003i.csv')
    filepath = {"filepath" : data_path}
    return send_file(data_path, mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)