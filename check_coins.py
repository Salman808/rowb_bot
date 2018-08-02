
class coins:

    def coincheck(self,req):
        email = req.get('actions').get('parameters').get('email')
        key = req.get('actions').get('parameters').get('key')
        msg = "You have 50 coins."
        return {
            "speech": msg,
            "displayText": msg,
            "data": {},
            "contextOut": [],
            "source": "MyBank.com"
        }
