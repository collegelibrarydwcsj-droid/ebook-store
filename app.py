# app.py
# This is the "brain" of your website. It runs on the server,
# decides what page to show, and hands the book info to the page.
#
# We are using a tool called Flask. Think of Flask as a helper that
# makes it easy to build a website with Python.

# --- 1. Bring in the tools we need ---
from flask import Flask, render_template

# --- 2. Create the app ---
app = Flask(__name__)

# --- 3. The name of your site (shown at the top of the page) ---
SITE_TITLE = "Divine Word College of San Jose E-Resources"

# --- 4. Your books ---
# Still typed in by hand for now. Later these come from your database.
# Each book now also has a "cover_color". Since we don't have real
# cover images yet, we draw a colored rectangle with the title on it.
# When you add real cover images later, we'll swap this out.
books = [
    {"title": "How to Sell Ebooks", "author": "Juan dela Cruz", "price": 199, "cover_color": "#1b3a6b"},
    {"title": "Cooking for Beginners", "author": "Maria Santos", "price": 149, "cover_color": "#274d8a"},
    {"title": "Learn Python Fast", "author": "Jose Rizal", "price": 249, "cover_color": "#16294d"},
    {"title": "World History Basics", "author": "Andres Bonifacio", "price": 179, "cover_color": "#2f5aa0"},
    {"title": "Intro to Accounting", "author": "Apolinario Mabini", "price": 209, "cover_color": "#1b3a6b"},
    {"title": "English Grammar Guide", "author": "Gabriela Silang", "price": 159, "cover_color": "#274d8a"},
]

# --- 5. The home page ---
@app.route("/")
def home():
    # We hand the title and the book list to the page.
    return render_template("index.html", site_title=SITE_TITLE, books=books)

# --- 6. Start the website ---
if __name__ == "__main__":
    app.run(debug=True)
