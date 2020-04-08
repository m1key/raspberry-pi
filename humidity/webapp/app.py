from flask import Flask
from flask import Flask, render_template

app = Flask(__name__, root_path='/home/pi/Development/raspberry-pi/humidity/webapp')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    import Humidity
    Humidity.generate_image()
    return render_template('index.html')
    #return 'Hello world'

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
