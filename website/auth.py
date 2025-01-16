from flask import Blueprint, render_template, request, flash, jsonify

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def home():
    return render_template("login.html")


@auth.route('/signup', methods=['GET', 'POST'])
def finance():
    return render_template("signup.html")