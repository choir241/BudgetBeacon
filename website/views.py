from flask import Blueprint, render_template, request, flash, jsonify

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@views.route('/finance', methods=['GET', 'POST'])
def finance():
    return render_template("finance.html")