
from datetime import datetime, timedelta
import random
from django.core.signing import Signer, BadSignature
from django.utils.html import format_html


# this function is used to generate clicking link which will be used in anothe function before 'send_email'.
# Please check settings to set gmail account from where email will be sent.
def fp_email_generate(name):
    current_time = datetime.now().strftime("%H:%M:%S")
    h, m, s =  map(int, current_time.split(':'))
    t_s = h*3600 + m*60 + s
    t_s = str(t_s)
    random_number = random.choices('123456790',k=4)
    random_number = ''.join(random_number)
    v_c = t_s + random_number
    signer = Signer()
    encrypted_value = signer.sign(v_c)
    fp_encrypted_value = signer.sign(v_c).split(":")[1]
    # decrypted_value = signer.unsign(encrypted_value)


    link = f"<p>Congratulations {name} ! You can reset your password as your email address had registered before </p><a href='http://127.0.0.1:8000/reset_password/"+fp_encrypted_value+"' target='_blank'>Click to reset your password</a>"
    formatted_link = format_html(link)
    return fp_encrypted_value,formatted_link