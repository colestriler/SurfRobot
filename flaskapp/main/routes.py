from flask import render_template, request, Blueprint, flash, redirect, url_for


main = Blueprint('main', __name__)

# @main.route('/', methods=['GET', 'POST'])
# #@main.route('/home', methods=['GET', 'POST'])
# def home():
#     pass
