from twilio.rest import Client 
 
account_sid = 'ACb505790b74bbf3738b7de21f52cc0361' 
auth_token = '[6935ef09075fe461ac29b7015881c2cd]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12029315659',
                              body = 'Wassup Niteesh..How are you?',
                              to ='+919967939953' 
                          ) 
 
print(message.sid)