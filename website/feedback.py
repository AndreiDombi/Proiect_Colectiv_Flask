from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db

feedback = Blueprint('feedbackrequest', __name__)


@feedback.route('/feedbackrequest', methods=['POST', 'GET'])
@login_required
def feedback1():
    return render_template('feedbackrequest.html', user=current_user)