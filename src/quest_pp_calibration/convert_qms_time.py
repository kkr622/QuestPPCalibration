import datetime, time
import numpy as np

def t2s(t):
    """
    Convert a time string of the Qulee format,
    '000:00:00.625' -> 'hhh:mm:ss.ms' to time in seconds.
    E.g '000:00:00.625' to 0.625 (s)
    
    Parameters
    ----------
    t: string
        Qulee time stamp string

    Returns
    -------
    t: datetime.timedelta
        datetime timedelta in seconds
    """

    ms = t.split(".")[1]
    hh = int(t.split(".")[0].split(":")[0])
    mm = t.split(".")[0].split(":")[1]
    ss = t.split(".")[0].split(":")[2]
    hoffset = 0
    if int(t.split(".")[0].split(":")[0]) > 23:
        hoffset = hh // 24
        tt = "0%d:%s:%s" % (hh - hoffset * 24, mm, ss)
    else:
        tt = "0%d:%s:%s" % (hh, mm, ss)
    x = time.strptime(tt, "0%H:%M:%S")
    return (
        datetime.timedelta(hours=hoffset * 24 + x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
        + float(ms) * 1e-3
    )


def t2sa(ta):
    """
    Convert an array of Qulee time stamp strings to array of datetime.timedelta in seconds.
    Just calls :func:`~akalab.qulee.t2s` in a loop.

    Parameters
    ----------
    ta: array-like
        array of time-strings from Qulee QMS
    
    Returns
    -------
    timearray: numpy.array
        numpy array with datetime.timedelta in seconds
    """

    return np.array([t2s(tt) for tt in ta])