"""
Renders main page of lotto buster
"""
import sys
import os
from flask import Flask, request, jsonify, render_template

cur_dir = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(cur_dir)
if parent_directory not in sys.path:
    sys.path.insert(0, parent_directory)

import compare_numbers


app = Flask(__name__)


@app.route("/LottoBuster", methods=["GET"])
def main_page():
    """
    Page explaining what the lotto buster does
    """
    return render_template("main_page.html")


@app.route("/LottoBuster/run", methods=["GET"])
def lotto_buster_get():
    """
    displays main page
    """
    return render_template("runner_page.html")


results = {
        "wins": 0,
        "plays": 0,
    }


@app.route("/LottoBuster/run", methods=["PUT"])
def lotto_buster_put():
    """
    Checks wins and loses then returns new page with wins,
    loses.
    """
    # todo make actions to count losses and wins
    numbers = {"number1": 0, "number2": 0, "number3": 0, "number4": 0,
               "number5": 0}
    request_data = request.get_json()

    for key, value in request_data.items():
        numbers[key] = value

    res = compare_numbers(numbers.values())
    results["wins"] = res[0]
    results["plays"] = res[1]
    return render_template("result_display.html", results=results)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
