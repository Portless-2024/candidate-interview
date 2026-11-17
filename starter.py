"""
Portless coding interview: carrier rate shopping

Write choose_carrier(order, carriers). For one order, it returns the cheapest
carrier that can ship it and still meet the delivery promise.

The rules:
  1. A carrier can only be used if it serves the destination country, and its
     transit_days for that country is less than or equal to the order's
     promised_days.
  2. Carriers have size and weight limits. If the longest side of the box is
     over max_side_cm, or the actual weight is over max_weight_kg, that
     carrier can't take the order.
  3. Carriers charge on billable weight:
         dimensional weight = length x width x height (in cm) / dim_divisor
         billable weight    = whichever is greater: actual weight (kg) or dimensional weight
  4. Each country has a rate table of [max_kg, price_usd] brackets. A parcel is
     charged the price of the first bracket whose max_kg it doesn't exceed
     (so a parcel of exactly 1.0 kg is in the 1 kg bracket). If the billable
     weight is above the top bracket, the carrier can't take the order.
  5. Price = bracket price x (1 + fuel_surcharge_pct / 100), rounded to the
     nearest cent, with half a cent rounding up.
  6. If two carriers cost the same, pick the faster one. If they're still
     tied, pick by carrier name, alphabetically.
  7. If no carrier can take the order, say so in a way that explains why.

The data is in rate_cards.json and orders.json. You can use any language;
this stub is just a starting point.
"""
import json


def choose_carrier(order, carriers):
    raise NotImplementedError


if __name__ == "__main__":
    carriers = json.load(open("rate_cards.json"))["carriers"]
    for order in json.load(open("orders.json")):
        print(order["id"], choose_carrier(order, carriers))
