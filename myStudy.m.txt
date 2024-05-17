
pip install investpy==0.9.14
pip install -r requirements.txt

%Python_list
stock=py.investpy.get_stock_historical_data('CVX','united states','01/01/2020','01/06/2020')
%Recent
Rstock=py.investpy.get_stock_recent_data('CVX','united states')
%Countries
py.investpy.get_stock_countries()
%Retrieve all available stocks information as a pandas.DataFrame
stocks_df = py.investpy.get_stocks('united states')
%Retrieve a listing of all the available stock symbols
stocks_list = py.investpy.get_stocks_list('united states')
%instruementbyisin
search_results = py.investpy.search_stocks('isin', 'ES0113211835')

 result = investpy.get_index_historical_data('DAX','united states','01/01/2020','01/06/2020','Daily','descending')
 index=param['name'],
 country=param['country'],from_date='01/01/2001',
     to_date=today,
                                                    interval=interval,
                                                    order='descending')

pydic=Rstock.to_dict()2019-01-02   306.10   315.13  298.80   310.12  11658648      USD
    2019-01-03   307.00   309.40  297.38   300.36   6965184      USD
    2019-01-04   306.00   318.00  302.73   317.69   7394116      USD
    2019-01-07   321.72   336.74  317.75   334.96   7551225      USD
    2019-01-08   341.96   344.01  327.02   335.35   7008516      US
values(pydic)
keys(Rstock)
pydic{'Open'}
m=pydic{'Open'}
myst=struct(Rstock)
myst=struct(pydic)

stocks_list = py.investpy.get_stocks_list('united states');
nbsize=size(stocks_list,2);
matriceStocks=zeros(582,104);
k=0;
for i=1:nbsize-4000
    try
    stock=py.investpy.get_stock_historical_data(stocks_list{i},'united states','01/01/2020','01/06/2020');
    l=stock.to_dict('list');
    stockName=[stockName,stocks_list{i}];
    
        for j=1:length(l{'Open'})
        matriceStocks(j,i-k)=l{'Open'}{j};
        end

    catch
        disp("Error in stock's data: "+stocks_list{i});
        k=k+1;
    end

   % stock.to_csv('C:\Users\Rachid\Desktop\Stocks\'+stocks_list{i}+'.csv');
   
end


l=stock.to_dict('list')
l{'Open'}{1}

l=stock.to_dict()
l{'Open'}{1}

length(d{'Open'})
