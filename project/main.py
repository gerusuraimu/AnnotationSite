import os
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from RequestManager.workspace import workspace_set_generate, load_workspace_list, rename_space, delete_space


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/workspace', methods=['GET', 'POST'])
@login_required
def workspace():
    name = current_user.name
    home = current_user.home
    workspace_list, thumbnail_list = load_workspace_list(home)

    return render_template('workspace.html',
                           name=name,
                           workspace_list=workspace_list,
                           thumbnail_list=thumbnail_list,
                           enabled=bool(workspace_list))


@main.route('/workspace/create_workspace', methods=['GET', 'POST'])
@login_required
def create_workspace():
    home = current_user.home
    workspace_name = request.form.get('workspace_name')
    workspace_set_generate(home, workspace_name)
    return redirect(url_for('main.workspace'))


@main.route('/workspace/rename', methods=['GET', 'POST'])
@login_required
def rename_workspace():
    home = current_user.home
    org_name = request.form['org_name']
    new_name = request.form['workspace_name']
    rename_space(home, org_name, new_name)
    return redirect(url_for('main.workspace'))


@main.route('/workspace/delete', methods=['GET', 'POST'])
@login_required
def delete_workspace():
    home = current_user.home
    workspace_name = request.form['workspace_name']
    delete_space(home, workspace_name)
    return redirect(url_for('main.workspace'))
