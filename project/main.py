from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/workspace', methods=['GET', 'POST'])
@login_required
def profile():
    name = current_user.name
    home = current_user.home

    # test_code
    import os
    print(home)
    workspace_list = os.listdir(home)
    print(len(workspace_list))
    # /test_code

    return render_template('workspace.html',
                           name=name,
                           workspace_list=workspace_list,
                           enabled=bool(workspace_list))
