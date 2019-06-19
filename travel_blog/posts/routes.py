from flask import Blueprint, flash, redirect, url_for, request
from flask import render_template
from flask_login import login_required, current_user

from travel_blog.models import Post, Photo
from travel_blog import db
from .forms import PostForm, PhotoForm
from travel_blog.users.utils import save_image_file



posts = Blueprint('posts', __name__)

@posts.route('/post')
def post():
    return render_template('post.html', title='Post')


@posts.route('/post/new', methods=['GET', 'POST'])
def post_new():
    post_form = PostForm()
    photo_form = PhotoForm()

    if post_form.validate_on_submit() and photo_form.validate_on_submit():

        post = Post(
            title=post_form.title.data, 
            content=post_form.content.data, 
            user_id=current_user.id,
            )
        db.session.add(post)
        db.session.commit()

        for f in request.files.getlist('photo'):

            image_file = save_image_file(f, 'static/blog_content')
            
            photo = Photo(post_id=post.id, image=image_file)
            db.session.add(photo)
            db.session.commit()

        flash(f'Your post has been created!!!')
        return redirect(url_for('main.home'))

    return render_template('new_post.html', post_form=post_form,  photo_form=photo_form)