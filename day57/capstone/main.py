from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = 'https://api.npoint.io/d85e8d2c22bf3efc5578'


@app.route('/')
def home():
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html",posts=all_posts)

@app.route('/blog/<int:id>')
def article():
    blog_url = 'https://api.npoint.io/d85e8d2c22bf3efc5578'
    response = requests.get(blog_url)
    all_posts = response.json()
    article = all_posts['body']
    print(article)
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


