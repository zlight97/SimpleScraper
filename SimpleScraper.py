import requests

# Scraper takes headers, url, list of emails to notify, keyword to trigger an email, and a keyword to reset
# The reset is needed so the program doesn't spam you with emails. Leaving this empty will work in most cases.
class SimpleScraper:
    def __init__(self, headers: dict, url: str, emails: list, triggeredString: str, resetStr: str):
        self.url = url
        self.emails = emails
        self.trigger = triggeredString
        self.reset = resetStr
        self.ready = True
        self.headers = headers
    
    # Check is used to trigger a request to the website and parse it. This should be called externally on a delay
    def check(self):
        try:

            data = requests.get(self.url,headers=self.headers)
        except Exception as e:
            print(e)
            print(e.with_traceback)
            return 1
        #If this is done on low delay it will be extremely slow
        if self.ready:
            if self.trigger in data.text:
                self.found()
        else:
            if self.reset in data.text and not self.trigger in data.text:
                ready = True

    def found(self):
        ready = False
        self.sendEmail()

    # Email requires a valid email username and password to be found inside cred.py with the names EMAIL and PASSWORD    
    def sendEmail(self):
        import cred
        import smtplib
        from email.mime.text import MIMEText
        msg = MIMEText(self.url + " is available.")
        # msg['Subject'] = subject
        msg['From'] = cred.EMAIL
        msg['To'] = ', '.join(self.emails)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(cred.EMAIL, cred.PASSWORD)
            smtp_server.sendmail(cred.EMAIL, self.emails, msg.as_string())
