from flask import Flask, render_template, request, redirect, url_for
import phonenumbers

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', valid = request.args.get('valid'))

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    entry = request.args.get('phone')
    try:
        number = phonenumbers.is_valid_number(phonenumbers.parse(entry, None))
        return redirect (f'http://api.whatsapp.com/send?phone={entry}')
    except:
        return redirect(url_for('home', valid = 0))

    

if __name__ == '__main__':
    app.run()    
