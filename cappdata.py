def get_path(component):
    import os
    repopath = os.path.abspath(os.path.join(os.getcwd(),
                                            os.pardir,
                                            os.pardir,
                                            component))
    return repopath


def apps_list():
    apps = ['catfish', 'gigolo', 'mousepad', 'parole', 'ristretto',
            'xfburn', 'xfce4-dict', 'xfce4-mixer', 'xfce4-notifyd',
            'xfce4-panel-profiles', 'xfce4-screensaver',
            'xfce4-screenshooter', 'xfce4-taskmanager', 'xfce4-terminal',
            'xfce4-volumed-pulse', 'xfdashboard', 'xfmpc']
    return apps


def bindings_list():
    bindings = ['thunarx-python', 'xfce4-vala']
    return bindings


def core_list():
    core = ['exo', 'garcon', 'libxfce4ui', 'libxfce4util',
            'thunar', 'thunar-volman', 'tumbler', 'xfce4-appfinder',
            'xfce4-dev-tools', 'xfce4-panel', 'xfce4-power-manager',
            'xfce4-session', 'xfce4-settings', 'xfconf', 'xfdesktop', 'xfwm4']
    return core


def panel_plugins_list():
    panel_plugins = ['xfce4-battery-plugin', 'xfce4-calculator-plugin',
                     'xfce4-clipman-plugin', 'xfce4-cpufreq-plugin',
                     'xfce4-cpugraph-plugin', 'xfce4-datetime-plugin',
                     'xfce4-diskperf-plugin', 'xfce4-docklike-plugin',
                     'xfce4-embed-plugin', 'xfce4-eyes-plugin',
                     'xfce4-fsguard-plugin', 'xfce4-genmon-plugin',
                     'xfce4-indicator-plugin', 'xfce4-mailwatch-plugin',
                     'xfce4-mount-plugin', 'xfce4-mpc-plugin',
                     'xfce4-netload-plugin', 'xfce4-notes-plugin',
                     'xfce4-places-plugin',  'xfce4-pulseaudio-plugin',
                     'xfce4-sample-plugin', 'xfce4-sensors-plugin',
                     'xfce4-smartbookmark-plugin',
                     'xfce4-statusnotifier-plugin', 'xfce4-stopwatch-plugin',
                     'xfce4-systemload-plugin', 'xfce4-time-out-plugin',
                     'xfce4-timer-plugin', 'xfce4-verve-plugin',
                     'xfce4-wavelan-plugin', 'xfce4-weather-plugin',
                     'xfce4-whiskermenu-plugin', 'xfce4-xkb-plugin']
    return panel_plugins


def thunar_plugins_list():
    thunar_plugins = ['thunar-archive-plugin', 'thunar-media-tags-plugin',
                      'thunar-shares-plugin', 'thunar-vcs-plugin']
    return thunar_plugins


def www_list():
    www = ['archive.xfce.org', 'blog.xfce.org', 'cdn.xfce.org',
           'forum.xfce.org', 'moka', 'wiki.xfce.org', 'www.xfce.org']
    return www


def query_yes_no(question, default="yes"):
    import sys
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes": "yes", "y": "yes", "ye": "yes",
             "no": "no", "n": "no"}
    if default is None:
        prompt = " [(Y)es/(N)o] "
    elif default == "yes":
        prompt = " ([Y]es/[N]o) "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
