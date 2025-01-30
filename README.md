Vibe Checker

Vibe Checker is a web application that analyzes the "vibes" of your text using NLTK for natural language processing. The app generates a pie chart based on the vibe of the text and displays it to the user.

Features:
Vibe Analysis: Analyzes text and categorizes vibes as Positive, Negative, or Neutral.
Pie Chart: Displays a pie chart representing the vibe distribution (Positive, Neutral, Negative).
User-Friendly Interface: Built with HTML, CSS, and JavaScript for smooth interaction.
Technologies Used:
Backend: Python with Flask web framework
Natural Language Processing: NLTK (VADER Sentiment Analyzer)
Data Visualization: Matplotlib for pie chart generation
Frontend: HTML, CSS, and JavaScript
How to Run Locally:
Clone this repository:

1) download 
git clone https://github.com/syedyazdan101/vibe-checker.git

2) open the vibe_checker file
use "cd vibe_checker" in the terminal


3)Install the required dependencies:
"pip intall Flask nltk matplotlib"

if you recieve an error saying that vader lexicon is not avalible run the code below 

"import nltk
nltk.download('vader_lexicon')"

4) to run the app use
"python app.py"


Usage:
1)Enter text in the provided textarea.
2)Click Analyze to check the vibes of the text.
3)View the vibe chart
