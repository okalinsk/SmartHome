# all the imports
from flask import Flask, request, render_template, redirect, url_for, g
import display
from xbmc import Xbmc
import arduino


# create our little application :)
app = Flask(__name__)
app.config.from_object('credentials')


@app.before_request
def before_request():
    g.xbmc = Xbmc(app.config['USER'], app.config['PASSWORD'])


@app.route('/', methods=['GET', 'POST'])
def power():
    if request.method == 'POST':
        if request.form['Action'] == 'Power':
            arduino.send_power()
            display.switch_monitor_state()
        elif request.form['Action'] == 'Music':
            g.xbmc.start_music()
        return redirect(url_for('power'))
    elif request.method == 'GET':
        tv_on = display.is_display_on()
        return render_template('power.html', tv_on=tv_on)


if __name__ == '__main__':
    arduino.init()
    app.run(host='0.0.0.0')
