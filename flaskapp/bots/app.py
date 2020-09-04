from flask import render_template, request, Blueprint, flash, redirect, url_for

bots = Blueprint('bots', __name__)


@bots.route('/', methods=['GET', 'POST'])
#@main.route('/home', methods=['GET', 'POST'])
def home():

    return render_template('home.html')


