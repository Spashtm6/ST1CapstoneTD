# *******************************************
# Author: Tyler Jones (u3214218)
# Assessment: ST1 Capstone Project
# Date: 30/4/2023
# ********************************************
from flask import Flask, Blueprint, render_template, redirect, url_for, request
from werkzeug.middleware.proxy_fix import ProxyFix
import sys
from argparse import ArgumentParser
from cvd_model import *

appweb = Blueprint('hello', __name__)

@appweb.route('/')
def home():
    return render_template("index.html")

@appweb.route('/send', methods=['POST'])
def send(predict=predict):
    if request.method == 'POST':
        customer_credit_score = request.form['credit_score']
        customer_country = request.form['country']
        customer_gender = request.form['gender']
        customer_age = request.form['age']
        customer_tenure = request.form['tenure']
        customer_balance = request.form['balance']
        customer_products_number = request.form['products_number']
        customer_credit_card = request.form['credit_card']
        customer_active_member = request.form['active_member']
        customer_estimated_salary = request.form['estimated_salary']
        customer_churn = request.form['churn']

        if customer_country == "France":
            customer_country = 0
        elif customer_country == "Spain":
            customer_country = 1
        else:
            customer_country = 2

        if customer_gender == "Male":
            customer_gender = 0
        else:
            customer_gender = 1

        if customer_credit_card == "Yes":
            customer_credit_card = 1
        else:
            customer_credit_card = 0

        if customer_active_member == "yes":
            customer_active_member = 1
        else:
            customer_active_member = 0

        if customer_churn == "Yes":
            customer_churn = 1
        else:
            customer_churn = 0


        # Accuracy of Model
        model.fit(x_train, y_train) #<-- this line
        acc = model.score(x_train, y_train)

        predict_real = model.predict([[customer_credit_score,customer_country,customer_gender,customer_age,
                                       customer_tenure,customer_balance,customer_products_number,
                                       customer_credit_card,customer_active_member,customer_estimated_salary]])

        if(predict_real == [0]):
            predict = "The result returned with " + str(round(acc,2)*100)  + "% accuracy and you have a lower chance of getting heart disease"
        else:
            predict = "The result returned with " + str(round(acc,2)*100) + "% accuracy and you have a higher chance of getting heart disease"


        return render_template('index.html', predict=predict)

    else:
        return render_template('index.html', predict=predict)



@appweb.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':

    # arg parser for the standard anaconda-project options
    parser = ArgumentParser(prog="home",
                            description="Simple Flask Application")
    parser.add_argument('--anaconda-project-host', action='append', default=[],
                        help='Hostname to allow in requests')
    parser.add_argument('--anaconda-project-port', action='store', default=8086, type=int,
                        help='Port to listen on')
    parser.add_argument('--anaconda-project-iframe-hosts',
                        action='append',
                        help='Space-separated hosts which can embed us in an iframe per our Content-Security-Policy')
    parser.add_argument('--anaconda-project-no-browser', action='store_true',
                        default=False,
                        help='Disable opening in a browser')
    parser.add_argument('--anaconda-project-use-xheaders',
                        action='store_true',
                        default=False,
                        help='Trust X-headers from reverse proxy')
    parser.add_argument('--anaconda-project-url-prefix', action='store', default='',
                        help='Prefix in front of urls')
    parser.add_argument('--anaconda-project-address',
                        action='store',
                        #default='0.0.0.0',
                        help='IP address the application should listen on.')

    args = parser.parse_args()

    app = Flask(__name__)
    app.register_blueprint(appweb, url_prefix = args.anaconda_project_url_prefix)

    app.config['PREFERRED_URL_SCHEME'] = 'https'

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=args.anaconda_project_address, port=args.anaconda_project_port)
