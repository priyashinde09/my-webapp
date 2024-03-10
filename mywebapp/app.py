from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, World! Wel-come to the Python Application.'
    return 'priyanka..'

# Run the application
if __name__ == '__main__':
    app.run('0.0.0.0')
