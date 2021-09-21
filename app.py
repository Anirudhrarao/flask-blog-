from flask import *
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
import json
import math
import os
local_server = True
app = Flask(__name__)
app.secret_key = "annikeys"
"""app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "params['gmail-user']",
    MAIL_PASSWORD = "params['gmail-password']"
)"""
#mail = Mail(app)


with open('templates/config.json', 'r') as c:
    params = json.load(c) ['params']
app.config['UPLOAD_FOLDER'] = params['upload_location']

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String(80), nullable = False)
    phone_num = db.Column(db.String(12), nullable = False)
    msg =  db.Column(db.String(120),  nullable = False)
    date =  db.Column(db.String(12), nullable = True)
    email =  db.Column(db.String(20), nullable = False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    tittle =  db.Column(db.String(80), nullable = False)
    slug = db.Column(db.String(25), nullable = False)
    content =  db.Column(db.String(120),  nullable = False)
    tagline =  db.Column(db.String(20),  nullable = False)
    date =  db.Column(db.String(12), nullable = True)
    img_file =  db.Column(db.String(12), nullable = True)

@app.route('/')
def home():
    post = Posts.query.filter_by().all()[0:int(params['no_of_post'])]
    return render_template('index.html', params = params, post = post)  

@app.route('/about')
def about():
    return render_template('about.html', params = params)

@app.route('/dash', methods = ['GET', 'POST'])
def dashboard():
    if 'admin_user' in session and session['admin_user']  ==  params['admin']:
        return render_template('dash.html', params = params)
    if request.method == 'POST':
        adminname = request.form.get('adminname')
        adminpassword = request.form.get('adminpass')
        if adminname == params['admin'] and adminpassword == params['admin_pass']:
            session['admin_user'] = adminname
            post = Posts.query.all()
            return render_template('dash.html', params = params, post = post)
    
    return render_template('admin.html', params = params)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone_num')
        msg = request.form.get('msg')
        add_content = Contacts(name = name, phone_num =phone, msg = msg, date = datetime.now(), email = email )
        db.session.add(add_content)
        db.session.commit()
        """mail.send_message('New message from' + name, 
                            sender = email, 
                            recipients = [params['gmail-user']],
                            body =  msg + "/n" + phone)"""
        flash("Thanyou for connecting with us, we will get back to you soon", "success")
    return render_template('contact.html', params = params)

@app.route('/post/<string:post_slug>', methods = ['GET'])
def post_blog(post_slug):
    post = Posts.query.filter_by(slug = post_slug).first()
    return render_template('post.html',params = params, post = post)

@app.route('/edit/<string:sno>', methods = ['GET', 'POST'])
def editpost(sno):
    if 'admin_user' in session and session['admin_user']  ==  params['admin']:
        if request.method == "POST":
            p_tittle = request.form.get('tittle')
            p_tagline = request.form.get('tagline')
            p_slug = request.form.get('slug')
            P_content = request.form.get('content')
            p_img_file = request.form.get('image_file')
            date = datetime.now()
            if sno == '0':
                post = Posts(tittle=p_tittle, slug=p_slug, content=P_content, tagline=p_tagline, img_file=p_img_file, date = date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.tittle = p_tittle
                post.slug = p_slug
                post.content = P_content
                post.tagline = p_tagline
                post.img_file = p_img_file
                post.date = date 
                db.session.commit()
                return redirect('/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template("edit.html",params = params,post=post,sno=sno)
@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
    if 'admin_user' in session and session['admin_user']  ==  params['admin']:
        if request.method == 'POST':
            f_name = request.files['files']
            f_name.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f_name.filename)))
            return "Uploader Successfully"

@app.route('/deletes/<string:sno>', methods = ['GET', 'POST'])
def delete(sno):
    if 'admin_user' in session and session['admin_user']  ==  params['admin']:
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dash')

@app.route('/logout')
def logout():
    session.pop('admin_user')
    return redirect('/dash')

if __name__ == "__main__":
    app.run(debug=True)