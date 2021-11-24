from flask import Blueprint

bp = Blueprint("other", __name__, url_prefix="/other")


@bp.route("/")  # /other
def index():
    return "Hello from other"
