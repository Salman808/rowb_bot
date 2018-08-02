from connector import conn
class signin:
    def login(self,conn,req):
        email = req.get('result').get('parameters').get('email')
        key = req.get('result').get('parameters').get('key')
        if self.check_user(conn,email,key):
            msg = "You have been successfully login! Please let me know if you want:" \
                  "" \
                  "/checkcoin - to check your coins." \
                  "/newoffers - to see new offers." \
                  "/settings - if you want to change something."
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
            msg = "Your email or secret key is not valid, please /signin again." \
                  "or" \
                  "If you are new here please /signup here." \
                  "Thanks!"

            print("Response:")
            print(msg)
            return {
                "speech": msg,
                "displayText": msg,
                "source": "MyBank.com"
            }

    def check_user(self,c,email,key):
        return c.signin(email,key)