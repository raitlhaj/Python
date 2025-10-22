import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from operator import add,mul
from math import exp
from enum import Enum

    
class models:
    def __init__(self, pay_name: str):
        self.pay_name = pay_name
        pass

    def spot_price_bs(S0, r, sig, t):
        #St = St( u*dt + sig * dBt)
        #prices follow a geometric motion Wt 
        #Under a risk neutral probablity the prices are martingles ( Q equiv to P) , Girsanov : Wt = Bt + ( u-r)t/sig
        # St = St( r*dt + sig * dWt)
        
        Z = np.random.normal(0, 1, 1)
        return S0 * exp((r-sig**2/2)*t +  sig*Z*t)
    
    def option_price_bs(S0, K, r, sig, t, option_type='call'):
        
        from scipy.stats import norm
        d1 = (np.log(S0/K) + (r + 0.5 * sig**2) * t) / (sig * np.sqrt(t))
        d2 = d1 - sig * np.sqrt(t)
        
        if option_type == 'call':
            price = S0 * norm.cdf(d1) - K * np.exp(-r * t) * norm.cdf(d2)
        elif option_type == 'put':
            price = K * np.exp(-r * t) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
        else:
            raise ValueError("option_type must be 'call' or 'put'")
        
        return price
    
    