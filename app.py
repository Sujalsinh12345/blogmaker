from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data to simulate a database
posts = [
    {
        'title': 'Sample Blog Post 1',
        'content': 'This is the content of the first blog post.'
    },
    {
        'title': 'Sample Blog Post 2',
        'content': 'This is the content of the second blog post.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = {'title': title, 'content': content}
        posts.append(new_post)
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Handle uploaded files here
    uploaded_files = request.files.getlist('file[]')

    # Process the uploaded files and store them as needed

    return jsonify({'message': 'Files uploaded successfully'})

if __name__ == '__main__':
    app.run(debug=True)


