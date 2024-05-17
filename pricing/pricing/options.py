import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from operator import add,mul

class Payoffs:
    def __init__(self, pay_name: str):
        self.pay_name = pay_name
        pass
    #### make a funcion that lets you specify a few parameters and calculates the payoff 
        # S = stock underlying # K = strike price # Price = premium paid for option

    def long_call(self, S, K, Price):
        # Long Call Payoff = max(Stock Price - Strike Price, 0)     # If we are long a call, we would only elect to call if the current stock price is greater than     # the strike price on our option     
        P = list(map(lambda x: max(x - K, 0) - Price, S))
        return P

    def long_put(self, S, K, Price):
        # Long Put Payoff = max(Strike Price - Stock Price, 0)     # If we are long a call, we would only elect to call if the current stock price is less than     # the strike price on our option     
        P = list(map(lambda x: max(K - x,0) - Price, S))
        return P
    
    def short_call(self, S, K, Price):
        # Payoff a shortcall is just the inverse of the payoff of a long call     
        P = self.long_call(S, K, Price)
        return [-1.0*p for p in P]

    def short_put(self, S,K, Price):
        # Payoff a short put is just the inverse of the payoff of a long put 
        P = self.long_put(S,K, Price)
        return [-1.0*p for p in P]
        
    def binary_call(self, S, K, Price):
        # Payoff of a binary call is either:     # 1. Strike if current price > strike     # 2. 0     
        P = list(map(lambda x:  K - Price if x > K else 0 - Price, S))
        return P

    def binary_put(self, S,K, Price):
        # Payoff of a binary call is either:     # 1. Strike if current price < strike     # 2. 0     
        P = list(map(lambda x:  K - Price if x < K else 0 - Price, S))
        return P  
         
    def run(self):
        
        plt.style.use('ggplot')
        plt.rcParams['xtick.labelsize'] = 10
        plt.rcParams['ytick.labelsize'] = 10
        plt.rcParams['figure.titlesize'] = 15
        plt.rcParams['figure.titleweight'] = 'medium'
        plt.rcParams['lines.linewidth'] = 2
      
        S = [t/5 for t in range(0,1000)] # Define some series of stock-prices 
        fig, ax = plt.subplots(nrows=3, ncols=2, sharex=True, sharey=True, figsize = (20,10))
        fig.suptitle('Payoffs / Profits', fontsize=20, fontweight='bold')
        fig.text(0.5, 0.04, 'Stock/Underlying Price ($)', ha='center', fontsize=14, fontweight='bold')
        fig.text(0.08, 0.5, 'Option Payoff ($)', va='center', rotation='vertical', fontsize=14, fontweight='bold')


        lc_P = self.long_call(S,100, 10)
        lp_P = self.long_put(S,100, 10)
        plt.subplot(321)
        plt.plot(S, lc_P, 'r')
        plt.plot(S, lp_P, 'b')
        plt.legend(["Long Call", "Long Put"])


        bc_P = self.binary_call(S,100, 10)
        bp_P = self.binary_put(S,100, 10)
        plt.subplot(322)
        plt.plot(S, bc_P, 'b')
        plt.plot(S, bp_P, 'r')
        plt.legend(["Binary Call", "Binary Put"])

        T2 = self.long_call(S, 120, 10)
        T4 = self.long_put(S,100, 10)
        plt.subplot(323)
        plt.plot(S,T2, 'r')
        plt.plot(S, T4, 'b')
        plt.legend(["Long Call", "Long Put"])


        sc_P = self.short_call(S,100, 10)
        sp_P = self.short_put(S,100, 10)
        plt.subplot(324)
        plt.plot(S, sc_P, 'r')
        plt.plot(S, sp_P, 'b')
        plt.legend(["Short Call", "Short Put"])
        
      #  https://www.fidelity.com/learning-center/investment-products/options/options-strategy-guide/bull-call-spread

        sc0_P = self.long_call(S,90, 10)
        sc1_P =  self.short_call(S,100, 10)
        sc1_P = list( map (lambda x : x * 2 , sc1_P))
        sc2_P = self.long_call(S,120, 10)
        plt.subplot(325)
        plt.plot(S, sc0_P, 'r')
        plt.plot(S, sc1_P, 'g')
        plt.plot(S, sc2_P, 'b')

        plt.plot(S, list( map (add, sc1_P , map (add,sc0_P, sc2_P))), 'y')

        plt.legend(["Long Call", "Short Call", "LC-Butterfly"])


        sc0_P = self.long_call(S,100, 10)
        sc1_P = self.short_call(S,150, 10)
        plt.subplot(326)
        plt.plot(S, sc0_P, 'r')
        plt.plot(S, sc1_P, 'b')
        plt.plot(S, list( map (add, sc1_P , sc0_P)), 'y')

        plt.legend(["Long Call", "Short Call", "Call Spread"])

        plt.show()