from flask import Flask, render_template

# Create instance of Flask class
app = Flask(__name__)

# Route decorator indicates which route should trigger function home()py
@app.route('/')
def home():
    return "<p>Welcome to SMeshboard!</p>"

@app.get('/show-data')
def show_data():
    data = {"message": render_template('show_data.html')}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)