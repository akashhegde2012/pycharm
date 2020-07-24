# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACb0937d3ca31dc05d95eff81e12d7d88d'
auth_token = '6ccd53e9a89881aabc38b7bb8e6cf8fe'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Today is a saturday and tomorow will be sunday",
                     from_='+19107732172',
                     to='+918762996089'
                 )

print(message.sid)