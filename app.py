from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


# This class represents a blog post with a title and content
class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    

@app.route('/home')  # Change the endpoint name to something unique
def home():
    # Your home route logic goes here
    return render_template('home.html')

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        return redirect(url_for('home'))  # Use the correct endpoint name
    return render_template('create_post.html')

# Add your other routes and configurations here

if __name__ == '__main__':
    app.run(debug=True)