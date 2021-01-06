from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
import requests
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
  return render_template('profile.html', name=current_user.name)


@main.route('/members_only')
@login_required
def members():
  return render_template('members.html')

@main.route('/members_only', methods=['POST'])
@login_required
def members_post():
  rating = request.form['rating']
  flash('So have you chosen '+ rating +'. Saruman The White')
  url = "https://jsonplaceholder.typicode.com/posts"
  req = requests.get(url)
  res = json.loads(req.text)
  data = res[int(rating)-1]
  return render_template('members.html', name=current_user.name, data=data)