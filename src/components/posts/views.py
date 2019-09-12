from flask import Blueprint, render_template, redirect, url_for, request, flash
from src import db
from src.components.posts.forms import NewPost
from flask_login import login_required, current_user
from datetime import datetime, date
from src.models.post import Post

posts_blueprint = Blueprint('posts',
                             __name__,
                             template_folder='../../templates/posts')

@posts_blueprint.route('/newpost', methods=['POST', 'GET'])
@login_required
def newpost():
    form = NewPost()
    if request.method == 'POST':
        newpost = Post(title=form.title.data,
                        body=form.body.data,
                        created=datetime.now())
        current_user.posts.append(newpost)
        db.session.add(newpost)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template("createpost.html", form=form)


@posts_blueprint.route('/editpost/<id>', methods=['POST', 'GET'])
@login_required
def editpost(id):
    ref = request.args.get('ref')
    form = NewPost()
    post = Post.query.filter_by(id=id, author=current_user.id).first()
    if not post:
        flash('you are not allow to edit the post')
        return redirect(url_for('single_post', id = id))
    else:
        if request.method == 'POST':
            post.title = form.title.data
            post.body = form.body.data
            post.updated = datetime.now().now()
            db.session.commit()
            return redirect(url_for('single_post', id = id))
    return render_template('editpost.html', form = form, post = post)

