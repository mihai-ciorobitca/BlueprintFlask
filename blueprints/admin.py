from flask import Blueprint, render_template

admin_blueprint = Blueprint("admin_blueprint", __name__, template_folder="templates")

@admin_blueprint.route("/admin")
def admin():
    return render_template("admin.html")

