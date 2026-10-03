from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>PocketSmart AI - Financial Advisor</h1><p>AI is Running!</p>"

if __name__ == '__main__':
    app.run()
