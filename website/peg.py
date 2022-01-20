from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Peg
from . import db

peg = Blueprint('pegrequest', __name__)


@peg.route('/pegrequest', methods=['POST', 'GET'])
@login_required
def peg1():
    if request.method == 'POST':
        project_info = request.form.get('Project_info')
        manager = request.form.get('Manager')
        if not (project_info != "" and manager != ""):
            flash('Something went wrong!', category='error')
        else:
            # print(project_info, manager)
            users = User.query.order_by(User.id)
            for user in users:
                if user.first_name == manager:
                    if user.role == 'manager':
                        new_peg = Peg(data="empty",
                                      status="pending",
                                      user_id=user.id,
                                      receiver_user_id=current_user.id,
                                      project_info=project_info,
                                      type="sent")
                        db.session.add(new_peg)
                        db.session.commit()
                        flash('Peg successfully sent!', category='success')
                    else:
                        flash('User {} is not a manager!'.format(manager), category='error')
                else:
                    flash('User {} not found!'.format(manager), category='error')
    return render_template('pegrequest.html', user=current_user)
