import QuantLib as ql

# Set up the QuantLib date and calendar
valuation_date = ql.Date(25, 8, 2023)
ql.Settings.instance().evaluationDate = valuation_date
calendar = ql.NullCalendar()

# Define the curve rates (these are just example rates)
index_rate = 0.025  # GC_USD_MAIN_INDEX rate
floating_rate = 0.018  # SOFR rate
spread = 0.001  # Spread over the rates
notional = 1000000  # Notional amount

# Set up the interest rate curves
index_curve = ql.FlatForward(valuation_date, ql.QuoteHandle(ql.SimpleQuote(index_rate)), ql.Actual360())
floating_curve = ql.FlatForward(valuation_date, ql.QuoteHandle(ql.SimpleQuote(floating_rate)), ql.Actual360())

# Create the index and floating legs of the TRS
index = ql.USDLibor(ql.Period("1M"), ql.YieldTermStructureHandle(index_curve))
index_leg = ql.IborLeg([1], index)

floating_leg = ql.FixedRateLeg([1], calendar, [notional], [floating_rate])

# Create the Total Return Swap instrument
trs = ql.TotalReturnSwap(ql.TotalReturnSwap.Payer, notional, index_leg, floating_leg, spread)

# Calculate the fair value of the TRS
engine = ql.DiscountingSwapEngine(ql.YieldTermStructureHandle(index_curve))
trs.setPricingEngine(engine)
fair_value = trs.fairRate()

print("Fair Value:", fair_value)
