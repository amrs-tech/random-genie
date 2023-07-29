from flask import Flask, render_template, request
import random
from config import Config

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def generate():
  """
  Home backend to manage home page
  and the form submission from home
  """
  template_name = "index.html"
  if str(request.method).lower() == 'post':  
    length = request.form.get('length','0')
    length = int(length) if length else 0
    custom_string_inp = request.form.get('custom','')
    type_ = request.form.get('type','')
    print('types:',type_)
    if len(custom_string_inp) == 0 and (length < 5 or length > 32):
      error_out = "!- Length exceeded or incorrect -!"
      print(error_out)
      return render_template(template_name, output=error_out)
    random_string = generate_string(length, 
                                      type_=type_, 
                                      custom_string_inp=custom_string_inp)
    return render_template(template_name, output="Generated String: "+random_string)
  else:
    return render_template(template_name)

def generate_string(length, type_=None, custom_string_inp=""):
  """
  Generates a random alphanumeric string 
  including digits and special characters
  of the specified length
  """
  characters = ""
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  digits = "0123456789"
  spl_char = "!@#$%^&_;:'\",./?"
  if custom_string_inp:
    if 'alpha' == type_:
      characters = custom_string_inp
    elif 'alpha_num' == type_:
      characters = custom_string_inp + digits
    elif 'alpha_num_spl' == type_:
      characters = custom_string_inp + digits + spl_char
    length = len(characters)
  else:  
    if 'alpha' == type_:
      characters = lower_case + upper_case
    elif 'alpha_num' == type_:
      characters = lower_case + upper_case + digits
    elif 'alpha_num_spl' == type_:
      characters = lower_case + upper_case + digits + spl_char
  random_string = ""
  for _ in range(length):
    random_index = random.randrange(len(characters))
    random_string += characters[random_index]
  return random_string

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=Config.flask_debug, threaded=True)
