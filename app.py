#!/usr/bin/env python

import json
import os

from flask import Flask
from flask import request
from flask import make_response
from sign_in import signin
from sign_up import signup
from new_offers import offer
from check_coins import coins
from connector import conn

# Flask app should start in global layout
app = Flask(__name__)
con = conn()
print(con.cnx)


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
    if call == 'signin':
        print("Sign in Request occur...")
        return signin().login(con,req)
    elif call == 'signup':
        print("Sign up Request occur...")
        return signup().adduser(con,req)
    elif call == 'newoffer':
        print("User want to see new offers Request occur...")
        return offer().offers(con,req)
    elif call == 'checkcoins':
        print("User want to check his coins Request occur...")
        return coins().coincheck(req)
    elif call == 'settings':
        print("User want to change his settings...")
        return coins().coincheck(req)
    else:
        return {}


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='localhost')