from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from . import db
from .models import User, Feedback

feedback = Blueprint('feedbackrequest', __name__)


@feedback.route('/feedbackrequest', methods=['POST', 'GET'])
@login_required
def feedback1():
    if request.method == 'POST':
        user_name = request.form.get('user')
        project_name = request.form.get('project')
        Technical_skills = request.form.get('Technical_skills')
        Communication_skills = request.form.get('Communication_skills')
        Team_work_skills = request.form.get('Team_work_skills')
        Problem_solving_skills = request.form.get('Problem_solving_skills')
        Time_management = request.form.get('Time_management')
        if user_name == "" or project_name == "":
            flash('Project or name are empty!', category='error')
        else:
            users = User.query.order_by(User.id)
            users_name = [user.first_name for user in users]
            if user_name not in users_name:
                flash('No user with this name!', category='error')
            else:
                receiver_id = [user.id for user in users if user.first_name == user_name]
                print(request.form.get('anon'))
                if request.form.get('anon') == '1':
                    user_name = "Anonymous"
                else:
                    pass
                new_feedback = Feedback(data="empty",
                                        status="pending",
                                        user_id=current_user.id,
                                        receiver_user_id=receiver_id[0],
                                        request_user_name=user_name,
                                        project_name=project_name,
                                        Technical_skills=Technical_skills,
                                        Communication_skills=Communication_skills,
                                        Team_work_skills=Team_work_skills,
                                        Problem_solving_skills=Problem_solving_skills,
                                        Time_management=Time_management)
                db.session.add(new_feedback)
                db.session.commit()
                flash('Feedback request submitted', category='success')

    return render_template('feedbackrequest.html', user=current_user)
