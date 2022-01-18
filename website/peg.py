from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db

peg = Blueprint('pegrequest', __name__)


@peg.route('/pegrequest', methods=['POST', 'GET'])
@login_required
def peg1():
    return render_template('pegrequest.html', user=current_user)
