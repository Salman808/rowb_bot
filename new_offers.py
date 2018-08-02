
class offer:
    def offers(self,conn,req):
        print("Response:")
        msg = self.offers_extract(conn)
        print(msg)
        return {
            "speech": msg,
            "displayText": msg,
            "source": "MyBank.com"
        }
    def offers_extract(self,conn):
        off = conn.fetchoffers()
        msg = ""
        for i in off:
            msg += i[1] + "   $"+i[2] + "   /Buy    /later \n"
        return msg
