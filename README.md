# Bitcoin-Trends
This repository was created to house my submission for the Duke Fuqua MSQM Winter Data Competition. 

Historical Bitcoin data was acquired from Yahoo Finance: https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD.

Five years of daily Bitcoin adjusted close price data was used as the primary source of information. The daily volume was also retained in the dataset. Many additional columns were calculated using the closing price

# Data Dictionary

* `Date` = The date the `Adj Close` was recorded.
* `Adj Close` = The adjusted closing price of Bitcoin to USD for the given date. 
* `Volume` = The transaction volume of Bitcoin.
* `Close_-1` = The closing price of the previous day.
* `Delta` = The daily percentage difference in price `(today - yesterday) / yesterday`.
* `Close_-1_Delta` = The `Delta` value for the previous day.
* `Delta_Class_Numeric` = Classifier based on the `Close_-1_Delta` values.
    * 1 = `Close_-1_Delta >= 0.02`
    * -1 = `Close_-1_Delta <= 0.02`
    * 0 = All else
* `Gain_Run` = Binary indicator that is equal to 1 if the last three days (inclusive of the target row) of `Close_-1_Delta` are positive. Meaning, this is flagged if there are three consecutive days of gains leading into the given row's date.
* `Gain_Loss` = Binary indicator that is equal to 1 if the last three days (inclusive of the target row) of `Close_-1_Delta` are negative. Meaning, this is flagged if there are three consecutive days of losses leading into the given row's date.
* `7-Day_Delta_AVG` = Rolling average of the previous seven days (inclusive of today) values of `Close_-1_Delta`. This value shows the average change in price for the seven days leading up to the target row's date. Also available for 30-day average.
* `7-Day_High` = The max value of `Close_-1` over the previous seven days (inclusive of today). Also available for 30 and 365 day highs.
* `7-Day_Low` = The min value of `Close_-1` over the previous seven days (inclusive of today). Also available for 30 and 365 day lows.
* `Diff_from_7-Day_High` = This value shows the percentage difference between the previous day's price and the `7-Day_High`. Calculated as: `Close_-1 - 7-Day_High / 7-Day_High`.
* `Diff_from_7-Day_Low` = This value shows the percentage difference between the previous day's price and the `7-Day_Low`. Calculated as: `Close_-1 - 7-Day_Low / 7-Day_Low`.
* `7-Day_AVG_Price` = Rolling average of the previous seven days (inclusive of today) values of `Close_-1`. This value shows the average price for the seven days leading up to the target row's date. Also available for 30/50/100-day averages.
* `7-Day_AG_to_30-Day_AVG` = The percentage difference between the 7-day and 30-day average prices. Calculated as `(7-Day_AVG_Price - 30-Day_AVG_Price) / 30-Day_AVG_Price`. This is also available as `30-Day_AG_to_50-Day_AVG` and `50-Day_AG_to_100-Day_AVG`.
* `7_to_30_5-Day_AVG` = The 5-day rolling average of `7-Day_AG_to_30-Day_AVG`. This is also available as `30_to_50_5-Day_AVG` and `50_to_100_5-Day_AVG`.
