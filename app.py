from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render the homepage using the 'index.html' template
    return render_template('index.html')

# Start the Flask web server when the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)