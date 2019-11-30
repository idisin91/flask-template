# -*- coding: utf-8 -*-
from app.api import bp
from flask import request, jsonify
def as_json(f):
    def apply(*args, **kwargs):
        res = f(*args, **kwargs)
        if isinstance(res, dict):
            res = jsonify(res)
        return res
    return apply

@bp.route('/process', methods=["GET", "POST"])
def index():
    key = request.args.get("key")
    if request.method == "GET":
        return jsonify({"key": f"{key} GET"})
    else:
        return jsonify({"key": f"{key} POST"})