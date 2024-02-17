import os
import shutil


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
    shutil.copy(os.path.join(os.getcwd(), 'RequestManager/thumbnail.png'), workspace_dir)


def load_workspace_list(home):
    workspace_list = os.listdir(home)
    workspace_list.sort()
    thumbnail_list = []
    for workspace_dir in workspace_list:
        thumbnail_list.append(os.path.isfile(os.path.join(home, workspace_dir, 'thumbnail.png')))
    return workspace_list, thumbnail_list


def rename_space(home, org_name, new_name):
    os.rename(os.path.join(home, org_name), os.path.join(home, new_name))


def delete_space(home, workspace_name):
    shutil.rmtree(os.path.join(home, workspace_name), ignore_errors=True)
