from twilio.rest import Client
import time

# Informações da sua conta Twilio
account_sid = 'SEU_ACCOUNT_SID'  # Substitua pelo seu Account SID
auth_token = 'SEU_AUTH_TOKEN'      # Substitua pelo seu Auth Token
twilio_number = 'SEU_NUMERO_TWILIO'  # Substitua pelo seu número Twilio

# Número do destinatário
to_number = 'NUMERO_DESTINATARIO'  # Substitua pelo número do destinatário

# Cria um cliente Twilio
client = Client(account_sid, auth_token)

# Mensagem a ser enviada
message_body = "Esta é uma mensagem de teste enviada pelo Twilio!"

# Envia SMS
def send_sms(message_body, to_number):
    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_number,
            to=to_number
        )
        print(f"Mensagem enviada: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Enviar poucos SMS
for i in range(5):  # Envia 5 SMS
    send_sms(message_body, to_number)
    time.sleep(2)  # Espera 2 segundos entre os envios
 
