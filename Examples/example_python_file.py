"""
This is an example of a Python file. 

This Python file contains one function called "main".

The purpose of this function is to calculate the 
factored withdrawal resistance of SWG Assy VG Plus and
ASSY 3.0 self-tapping wood screws as per NRC Evaluation report:
CCMC 13677-R. This formula shall not apply to any other screw makes
or models.

Screw tensile strength information directly from CCMC 13677-R.

Parameters: 
    'delta': 82 for wood dry density >= 0.44, 85 otherwise
    'rho': mean wood dry density * 1000 kg/m**3 (e.g. 490 kg/m**3)
    'b_pr': 0.75 for Parallam (PSL), 1.0 otherwise
    'd_f': screw outside diameter (mm)
    'l_ef': effective embedment depth of screw in one member
    'alpha': screw insertion angle to grain (degrees)
    'K_D': load duration factor
    'K_SF': service condition factor
    
"""

from math import sin, cos, pi

def main(delta, rho, b_pr, d_f, l_ef, alpha, K_D, K_SF): 
    # As per NRC Evaluation Report: CCMC 13677-R
    # For SWG ASSY VG Plus and ASSY 3.0 Self-tapping wood screws
    
    ## Parameters
    phi = 0.9
    ## Factored screw tensile strength
    if d_f == 12: 
        P_rt = 24
    elif d_f == 10: 
        P_rt = 19.2
    elif d_f == 8:
        P_rt = 15.12
    elif d_f == 6: 
        P_rt = 9.04
    
    ## Withdrawal resistance
    alpha_rads = alpha * pi / (180)
    P_rw = phi*(0.8*delta*(b_pr*0.84*rho)**2*d_f*l_ef*10**(-3)) / (sin(alpha_rads)**2 + 4/(3)*cos(alpha_rads)**2) * K_D * K_SF
    if P_rw > P_rt: 
        P_rw = P_rt
    elif P_rw < P_rt: 
        P_rw = P_rw
    return P_rw