#!/usr/bin/env python

import urllib
import json
import os
from datetime import datetime

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

name = ['jane smith', 'sherry james', 'robert down', 'claire mcfarst']
acct = [123456, 445566, 665522, 225588]
dobs = [datetime.strptime('02 01 1959', '%m %d %Y').date(),
        datetime.strptime('09 12 1952', '%m %d %Y').date(),
        datetime.strptime('05 25 1945', '%m %d %Y').date(),
        datetime.strptime('10 05 1980', '%m %d %Y').date()]

def date_conversion(date):
    return datetime.strptime(date, '%Y-%m-%d').date()

def safe_int(n):
    if n is not None:
        return int(n)
    return n

def generate_balance(uname, udob, uacct):
    baln = [200, 500, 600, 20]
    if uname in name and udob in dobs and uacct in acct:
        if name.index(uname) == dobs.index(udob) and name.index(uname) == acct.index(uacct):
            return baln[name.index(uname)]
        else:
            return -1
    else:
        return IndexError

def generate_dues(uname, udob, uacct):
    dues = [0, 50, 10, 2.5]
    if uname in name and udob in dobs and uacct in acct:
        if name.index(uname) == dobs.index(udob) and name.index(uname) == acct.index(uacct):
            return dues[name.index(uname)]
        else:
            return -1
    else:
        return IndexError

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def makeWebhookResult(req):
    call = req.get("result").get("action")
    parameters = req.get("result").get("parameters")
    # if call == 'signin':
    #     email  = parameters.get('email')
    #     key = parameters.get('key')
    #     context = req.get('contexts')
    #     if context.get('parameters')

    acct = parameters.get("acctno")
    name = parameters.get("name")
    dobs = parameters.get("dob")

    if call == 'AcctBalance':
        balance = generate_balance(name.lower(), date_conversion(dobs), safe_int(acct))
        if balance == IndexError:
            msg = "Your record does not exist in our database, Thanks."
        if balance == -1:
            msg = "Your name, account number or DOB does not matching with each other."
        elif balance > 1:
            msg = "Your account balance is  ${}.".format(balance)
        else:
            msg = "You don't have any balance in your account."

        print("Response:")
        print(msg)
        return {
            # "fulfillmentText": msg,
            "speech": msg,
            "displayText": msg,
            "data": {},
            "contextOut": [],
            "source": "MyBank.com"
        }

    elif call == 'DuesInquiry':
        dues = generate_dues(name.lower(), date_conversion(dobs), safe_int(acct))
        if dues == IndexError:
            msg = "Your record does not exist in our database, Thanks."
        if dues == -1:
            msg = "Your name, account number or DOB does not matching with each other."
        elif dues > 1:
            msg = "Your Past dues are  ${}.".format(dues)
        else:
            msg = "You don't have any past due amount."
        print("Response:")
        print(msg)
        return {
            # "fulfillmentText": msg,
            "speech": msg,
            "displayText": msg,
            "data": {},
            "contextOut": [],
            "source": "MyBank.com"
        }

    else:
        return {}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='127.0.0.1')