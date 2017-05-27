#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    df[['Close', 'Adj Close']].plot()
    plt.show()  # Must be called to show plots

if __name__ == "__main__":
    test_run()