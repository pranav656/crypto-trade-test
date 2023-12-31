import logging

from bfxapi import Client
from bfxapi.types import Candle, TradingPairTrade
from bfxapi.websocket.subscriptions import Candles, Trades

bfx = Client()

# the line below is a decorator, indicating that the following function
# should be executed when the event candles_update_occurs 
@bfx.wss.on("candles_update")
def on_candles_update(_sub: Candles, candle: Candle):
    # Example New candle: Candle(mts=1704018960000, open=42752, close=42752, high=42752, low=42752, volume=0.00153076)
    # Timestamp, Open price, close price, High price, low price, volume of asset traded
    print(f"New candle: {candle}")


@bfx.wss.on("open")
async def on_open():
    # using print statements for now, use asynchronous logging  library
    # in the future
    print("WebSocket connection opened")
    # this line awaits the subscription to the "candles" channel
    await bfx.wss.subscribe("candles", key="trade:1m:tTESTBTC:TESTUSD")
    print("Subscribed to candles channel for 1-minute intervals")

bfx.wss.run()