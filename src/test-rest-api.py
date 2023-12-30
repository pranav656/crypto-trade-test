from typing import List

from bfxapi import Client, REST_HOST
from bfxapi.types import Notification, Order
from bfxapi.types import TradingPairTrade
from bfxapi.types import Wallet

bfx = Client(
    rest_host=REST_HOST,
    api_key=YOUR_API_KEY,
    api_secret=YOUR_API_SECRET
)

# Prints a map from their symbols to the API symbols
print(bfx.rest.public.conf("pub:map:currency:sym"))

# Prints all the available exchange trading pairs
print(bfx.rest.public.conf("pub:list:pair:exchange"))

# Print wallets
wallets: List[Wallet] = bfx.rest.auth.get_wallets()

print(wallets)

# Use paper currency (TEST) for trade
notification: Notification[Order] = bfx.rest.auth.submit_order(
    type="EXCHANGE LIMIT", symbol="tTESTBTC:TESTUSD", amount=0.02, price=43000.0)

order: Order = notification.data

print(notification.status)

# get latest executed trades
t_trades: List[TradingPairTrade] = bfx.rest.public.get_t_trades(
    "tTESTBTC:TESTUSD", limit=15, sort=+1
)

print("Latest 15 trades for tBTCUSD (in ascending order):", t_trades)
