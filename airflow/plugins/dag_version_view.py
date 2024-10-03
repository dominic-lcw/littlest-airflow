import logging
import os

import subprocess
from flask_appbuilder import BaseView, expose
from flask import Blueprint, request
from typing import List

from airflow.plugins_manager import AirflowPlugin


GIT_FOLDER = os.getenv('AIRFLOW_GIT_FOLDER', '/opt/airflow/dags')

def _minimal_ext_cmd(cmd: List[str], work_dir: str) -> str:
    # construct minimal necessary command to execute a command
    # in a subprocess
    # see https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline
    error = ""
    output = ""
    try:
        completed = subprocess.Popen(
          cmd, 
          cwd = work_dir,
          shell=False,
          stdout=subprocess.PIPE, 
          stderr=subprocess.PIPE
        )
    except Exception as e:
        error = str(e)
    else:
        output, error = completed.communicate()
        output = output.decode('utf-8')
        error = error.decode('utf-8')
    
    return output, error

def get_git_version():
    try:
        output, error = _minimal_ext_cmd(["git", "rev-parse", "HEAD"], GIT_FOLDER)
    except Exception as e:
        output = ""
        error = str(e)
    return f"Git version: {output}" + (f"(Error: {error})" if error else "")



# Flask BaseView
class DagVersionView(BaseView):
    default_view = 'show'

    @expose('/')
    def show(self):
        git_version = get_git_version()
        return self.render_template('dag_version.html', git_version=git_version)

# Package
v_dag_version_view = DagVersionView()
v_appbuilder_package = {
    "name": "Test View",
    "category": "Test Plugin",
    "view": v_dag_version_view,
}

# Flask Blueprint
bp = Blueprint(
    "dag_version_view_bp", 
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/dag_version_view'
)

# Add the view to the Airflow app
def setup_dag_version_view(appbuilder):
    appbuilder.add_view(
        DagVersionView,
        "DAG Version",
        category="Admin"
    )

# # Airflow plugin definition
class DagVersionPlugin(AirflowPlugin):
    name = "dag_version_plugin"
    flask_blueprints = [bp]
    appbuilder_views = [v_appbuilder_package]

if __name__ == "__main__":
    print(get_git_version())