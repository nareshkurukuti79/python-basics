################################ Twilio ############################

from twilio.rest import Client


account_sid = "werwer"  # SampleOnly

auth_token = "kwjerkljwelrkjwer"  # SampleOnly

client = Client(account_sid, auth_token)

client.messages.create(
    to="...",
    from_="+1212323232323",
    body="Hey There This is sent from AFG-PY"
)
