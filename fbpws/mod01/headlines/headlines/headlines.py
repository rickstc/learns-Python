import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'
    }

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1>BBC Headlines</h1>
            <strong>{0}</strong> <br>
            <em>{1}</em> <br>
            <p>{2}</p>
        </body>
    </html>""".format(
        first_article.get("title"),
        first_article.get("published"),
        first_article.get("summary")
    )

if __name__ == '__main__':
    app.run(port=5000, debug=True)