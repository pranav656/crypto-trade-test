from simple_moving_average_strategy import SimpleMovingAverageStrategy
import pandas as pd

def test_simple_moving_average_strategy():
    # create a list and push dummy data into it
    start_price_data = {
        'Date': pd.date_range(start='2023-01-01', periods=100),
        'Close': [189 + i for i in range(100)]
    }

    # test strategy for dummy data points based on 20 point
    # moving average, sells on a dowanard trend and buys on
    # an upward trend
    df = pd.DataFrame(start_price_data)
    strategy = SimpleMovingAverageStrategy(df, 20)
    strategy.calculate_signals()

    for i in range(100):
        dummy_current_data = {
            'Date': pd.date_range(start='2023-01-01', periods=1),
            'Close': [95+i]
        }
        strategy.update_data(pd.DataFrame(dummy_current_data))
        strategy.calculate_signals()
        strategy.execute_trades()
        assert strategy.signal is not None
