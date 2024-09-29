from flask import Flask, render_template

# Create instance of Flask class
app = Flask(__name__)

# Route decorator indicates which route should trigger function home()py
@app.route('/')
def show_data():
    # return "<p>Hello, Flask!</p>"
    return render_template('show_data.html')

if __name__ == '__main__':
    app.run(debug=True)