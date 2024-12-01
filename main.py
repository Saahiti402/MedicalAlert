from twilio.rest import Client
import key

client = Client(key.account_sid, key.account_auth)

message = client.messages.create(
    body = "This is a sample message",
    from_= key.twilio_number,
    to=key.target_number
    
)
