import subprocess


def query_display(param):
    p = subprocess.Popen('./display.sh %s' % param, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.readlines()
    p.wait()
    return output


def is_display_on():
    result = query_display('status')
    return result[0].strip() == 'On'


def set_monitor_on():
    query_display('on')


def set_monitor_off():
    query_display('off')


def switch_monitor_state():
    if is_display_on():
        set_monitor_off()
    else:
        set_monitor_on()
