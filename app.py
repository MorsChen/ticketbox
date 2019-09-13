from src import app
from flask import Flask, render_template, redirect, url_for


@app.route('/')
def home():
   
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
