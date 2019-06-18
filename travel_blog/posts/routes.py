from flask import Blueprint, flash, redirect, url_for
from flask import render_template
from flask_login import login_required, current_user

from travel_blog.models import Post
from travel_blog import db
from .forms import PostForm
from travel_blog.users.utils import save_image_file



posts = Blueprint('posts', __name__)

@posts.route('/post')
def post():
    return render_template('post.html', title='Post')


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def post_new():
    form = PostForm()
    if form.validate_on_submit():
        image_file = save_image_file(
            form.photo.data, 
            'static/blog_content'
            )
        post = Post(
            title=form.title.data, 
            content=form.content.data, 
            user_id=current_user.id, 
            photo=image_file
            )
        db.session.add(post)
        db.session.commit()
        flash(f'Your post has been created!!!')
        return redirect(url_for('main.home'))
        
    return render_template('new_post.html', title='New Post', form=form)
