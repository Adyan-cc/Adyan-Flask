from flask import Blueprint, render_template
from flask_login import login_required, current_user

bp = Blueprint('index', __name__, url_prefix='/')


# 首页

