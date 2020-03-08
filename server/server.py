from flask import Flask
from flask_cors import CORS
import json
import hackernews

app = Flask(__name__)
CORS(app)


@app.route('/')
def get_news():
    articles = hackernews.main()
    return json.dumps(articles, sort_keys=True)
