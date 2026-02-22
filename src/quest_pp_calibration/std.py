import datetime
from scipy.constants import Boltzmann, convert_temperature

def pdp_std(calibrationdate,T = 25):
    """
    Calculate the Leak Rate for the leak used for PDP
    Installed before 2013,
    Used up to now (Last Update: July 2019)
    """
    LeakRate = 4.39e-6 # Pa*m**3/sec
    Deplition = 1.10 #% per month
    filldate = datetime.date(2013,1,30)
    Tfilled = 23.6 #C
    Tcoeff = 0.20 #%
    td = calibrationdate - filldate
    monthspassed = (td.days/30.)
    LR = LeakRate*(1+Tcoeff*0.01*(T-Tfilled) - Deplition*0.01*monthspassed) # Pa*m**3/sec
    LR = LR / (Boltzmann*convert_temperature(T,'C','K')) # H_2 per second
    return LR
