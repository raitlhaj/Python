from underlyings.stock import Stock
from underlyings.index import Index
import pandas as pd

class Basket:
    
    def __init__(self, references : list[str], weights: list[float]):
        self.references =  references
        self.weights =  weights
        
    def get_quotes(self, start_date: str, end_date: str):
      
      incremented_quotes = 0.0
      
      if len(self.references) != len(self.weights) :
        print("the number of basket ticker & weigths should have the same length !")
        return
        
      for i in range(len(self.references)):
            try:
                stock_quotes = Stock(self.references[i]).get_quotes(start_date = start_date, end_date = end_date)
                incremented_quotes += stock_quotes.apply(lambda x: x * self.weights[i]).values
                
            except:
                index_quotes = Index(self.references[i]).get_quotes(start_date = start_date, end_date = end_date)
                incremented_quotes = index_quotes.apply(lambda x: x * self.weights[i]).values
       
      incremented_quotes = pd.DataFrame(incremented_quotes,columns=["Basket"])
      return incremented_quotes.astype('float64')

    