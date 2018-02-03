from flask import Flask, render_template, request, redirect, url_for
import models
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/blog')
def blog():
    posts = models.session.query(models.Post).all()
    return render_template("blog.html", posts=posts)

@app.route('/article/<int:post_id>')
def article(post_id):
    blogpost = models.session.query(models.Post).filter_by(id=post_id).one()
    return render_template('article.html', blogpost=blogpost)

@app.route('/addpost')
def addpost():
    return render_template("addpost.html")

@app.route('/post', methods=['POST'])
def post():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['blogpost']
    post = models.Post()
    post.title = title
    post.subtitle = subtitle
    post.author = author
    post.content = content
    models.session.add(post)
    models.session.commit()
    time.sleep(2)
    return redirect(url_for('blog'))

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/pricing')
def pricing():
    return render_template("pricing.html")



if __name__ == '__main__':
    app.run(debug=True)
