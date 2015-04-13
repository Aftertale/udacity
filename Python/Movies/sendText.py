from twilio import rest

# Your Account Sid and Auth token from twilio.com/user/account
account_sid = "AC89e93074e70d83ae3622d080398a4118"
auth_token = "c3eba976ac755832a413edc7bebcd045"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Whattup???!!!",
    to="+12064467534",    # Replace with your phone number
    from_="+18656224897") # Replace with your Twilio number
print message.sid
