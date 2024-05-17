import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from operator import add,mul
from math import exp
class models:
    def __init__(self, pay_name: str):
        self.pay_name = pay_name
        pass



    def black_sholes_model(S0, r, sig, t):
        #St = St( u*dt + sig * dBt)
        #prices follow a geometric motion Wt 
        #Under a risk neutral probablity the prices are martingles ( Q equiv to P) , Girsanov : Wt = Bt + ( u-r)t/sig
        # St = St( r*dt + sig * dWt)
        
        Z = np.random.normal(0, 1, 1)
        return S0 * exp((r-sig**2/2)*t +  sig*Z*t)
    
    