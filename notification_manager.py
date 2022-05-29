import os
from twilio.rest import Client

ACCOUNT_SID = "###########"
AUTH_TOKEN = "##########"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = ACCOUNT_SID
        self.auth_token = AUTH_TOKEN
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, msg):
        # Account SID and Auth Token at twilio.com/console
        # Set the environment variables. See http://twil.io/secure

        message = self.client.messages \
            .create(
            body=msg,
            from_='#######',
            to='##########'
        )
