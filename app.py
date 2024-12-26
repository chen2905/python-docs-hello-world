from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "God Blessed, Thanks God! Please bless my family a great year 2025 from staging to production"
