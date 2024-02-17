import os
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from RequestManager.workspace import workspace_set_generate


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/workspace', methods=['GET', 'POST'])
@login_required
def workspace():
    name = current_user.name
    home = current_user.home
    workspace_list = os.listdir(home)

    return render_template('workspace.html',
                           name=name,
                           workspace_list=workspace_list,
                           enabled=bool(workspace_list))


@main.route('/workspace/create_workspace', methods=['GET', 'POST'])
@login_required
def create_workspace():
    workspace_name = request.form.get('workspace_name')
    home = current_user.home
    workspace_set_generate(home, workspace_name)
    return redirect(url_for('main.workspace'))
