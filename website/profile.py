from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db

profile_blueprint = Blueprint('profile', __name__)


@profile_blueprint.route('/', methods=['POST','GET'])
@login_required
def profile():
    user = current_user
    return render_template('profile.html', user=current_user)
