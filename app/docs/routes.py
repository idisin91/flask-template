# -*- coding: utf-8 -*-
from app.docs import bp
from flask import render_template

@bp.route('/', methods=["GET"])
def index():
    return render_template('docs/index.html')