# app.py
# This is the "brain" of your website. It runs on the server,
# decides what page to show, and hands the book info to the page.
#
# We are using a tool called Flask. Think of Flask as a helper that
# makes it easy to build a website with Python.

# --- 1. Bring in the tools we need ---
# "Flask" builds the website. "render_template" lets us show an HTML page.
from flask import Flask, render_template

# --- 2. Create the app ---
# This line creates your website. We'll call it "app" from now on.
app = Flask(__name__)

# --- 3. Your books ---
# For now, the books are just typed in here by hand (this is the
# "hardcoded" part we talked about). Later, these will come from a
# real database that you fill using your admin panel.
#
# Each book is a little bundle of info: a title, an author, and a price.
books = [
    {"title": "How to Sell Ebooks", "author": "Juan dela Cruz", "price": 199},
    {"title": "Cooking for Beginners", "author": "Maria Santos", "price": 149},
    {"title": "Learn Python Fast", "author": "Jose Rizal", "price": 249},
]

# --- 4. The home page ---
# This says: "when someone visits the main page of the website ('/'),
# run the function below."
@app.route("/")
def home():
    # We hand our list of books to the HTML page called "index.html".
    # The page will loop through them and show each one.
    return render_template("index.html", books=books)

# --- 5. Start the website ---
# This line actually turns the website on when you run this file.
# debug=True means it will show helpful error messages while you learn.
if __name__ == "__main__":
    app.run(debug=True)
