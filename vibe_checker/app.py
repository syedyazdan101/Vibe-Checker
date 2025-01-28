import os
import matplotlib
matplotlib.use('Agg')

# Ensure the static directory exists
if not os.path.exists('static'):
    os.makedirs('static')
from flask import Flask, request, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route("/", methods=["GET", "POST"])
def index():
    print("Request received")
    sentiment = None
    chart_path = None

    if request.method == "POST":
        # Get the input text from the form
        input_text = request.form.get("text")

        if input_text:
            # Perform sentiment analysis using VADER
            sentiment_scores = sia.polarity_scores(input_text)

            # Generate a pie chart based on the sentiment scores
            labels = ['Positive', 'Neutral', 'Negative']
            sizes = [sentiment_scores['pos'], sentiment_scores['neu'], sentiment_scores['neg']]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')

            # Save the chart to the static folder
            chart_path = "static/sentiment_chart.png"
            plt.savefig(chart_path)
            plt.close()

            # Determine overall sentiment
            if sentiment_scores['compound'] >= 0.05:
                sentiment = "Positive"
            elif sentiment_scores['compound'] <= -0.05:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

    return render_template("index.html", sentiment=sentiment, chart_path=chart_path)

if __name__ == "__main__":
    app.run(debug=True)