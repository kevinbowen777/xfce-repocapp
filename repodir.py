def repodir(component):
    if component is None:
        return 'No repository path specified'
    elif component == "apps":
        return '../../apps/'
    elif component == "bindings":
        return '../../bindings/'
    elif component == "core":
        return '../../core/'
    elif component == "panel-plugins":
        return '../../panel-plugins/'
    elif component == "thunar-plugins":
        return '../../thunar-plugins/'
    elif component == "www":
        return '../../www/'
    else:
        raise ValueError("invalid path specification: '%s'" % component)
