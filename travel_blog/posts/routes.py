from flask import Blueprint
from flask import render_template


posts = Blueprint('posts', __name__)

@posts.route('/post')
def post():
    return render_template('post.html', title='Post')
