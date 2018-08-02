

class signup:
    def adduser(self,conn,req):
        email = req.get('result').get('parameters').get('email')
        username = req.get('result').get('parameters').get('username')
        key = req.get('result').get('parameters').get('key')
        if self.check_email(conn,email):
            msg = "This email address is already Subscribed, please try different one."
            print("Response:")
            print(msg)
            return  {
            "speech": msg,
            "displayText": msg,
            "data": {},
            "contextOut": [],
            "source": "MyBank.com"
        }
        else:
            conn.signup(email,username,key)
            msg = "Your user has been added Succesfully! Please /signin to see our services."
            print("Response:")
            print(msg)
            return {
                "speech": msg,
                "displayText": msg,
                "data": {},
                "contextOut": [],
                "source": "MyBank.com"
            }

    def check_email(self,conn,email):
        return conn.checkemail(email)