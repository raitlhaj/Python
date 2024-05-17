import QuantLib as ql

# Set up the currencies
usd_currency = ql.USDCurrency()
eur_currency = ql.EURCurrency()

# Set up the discount curves (usually obtained from market data)
usd_rate = 0.02
eur_rate = 0.01
usd_discount_curve = ql.YieldTermStructureHandle(ql.FlatForward(0, ql.NullCalendar(), ql.QuoteHandle(ql.SimpleQuote(usd_rate)), ql.Actual360()))
eur_discount_curve = ql.YieldTermStructureHandle(ql.FlatForward(0, ql.NullCalendar(), ql.QuoteHandle(ql.SimpleQuote(eur_rate)), ql.Actual360()))

# Set up the cross-currency swap details
notional = 1000000  # Notional amount
start_date = ql.Date(31, 8, 2023)
maturity_date = ql.Date(31, 8, 2028)
fixed_rate = 0.03
spread = 0.005  # Spread over the floating rate

# Create the cross-currency swap
ccy_swap = ql.CrossCcySwap(
    notional,
    start_date,
    ql.Euribor6M(eur_discount_curve),
    fixed_rate,
    ql.USDLibor6M(usd_discount_curve),
    spread,
    maturity_date
)

# Price the cross-currency swap
engine = ql.CrossCcySwapEngine(usd_discount_curve)
ccy_swap.setPricingEngine(engine)
price = ccy_swap.NPV()

print("Cross-Currency Swap Price: {:.2f}".format(price))
