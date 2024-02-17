import os


def create_user_space(home):
    os.makedirs(home, exist_ok=False)


def workspace_set_generate(home, workspace_name):
    workspace_list = [
        'rectangle',
        'polygon',
        'images',
        'thumbnails',
        'edits'
    ]
    workspace_dir = os.path.join(home, workspace_name)
    os.makedirs(workspace_dir, exist_ok=False)
    for folder in workspace_list:
        os.makedirs(os.path.join(workspace_dir, folder), exist_ok=False)
