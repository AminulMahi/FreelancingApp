
from datetime import datetime, timedelta
import random
from django.core.signing import Signer, BadSignature
from django.utils.html import format_html


def email_generator(name):
    current_time = datetime.now().strftime("%H:%M:%S")
    h, m, s= map(int, current_time.split(':'))
    time_sec = h*3600 + m*60 + s
    time_sec = str(time_sec)

    random_number = random.choices('123456790',k=4)
    random_number = ''.join(random_number)
    v_c = time_sec + random_number
    
    signer = Signer()
    encrypted_value = signer.sign(v_c)
    encrypted_value1 = signer.sign(v_c).split(":")[1]
    decrypted_value = signer.unsign(encrypted_value)

    link = f"<p>Congratulations Mr {name} ! For registering as a user in our doctor appointment system. To confirm the registration </p><a href='http://127.0.0.1:8000/user/email_verification/"+encrypted_value1+"' target='_blank'>please click this Activation link</a>"

    formatted_link = format_html(link)
    return encrypted_value1,formatted_link