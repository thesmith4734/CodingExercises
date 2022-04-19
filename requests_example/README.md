# Sample Requests Project
## Leverage

Write a program that allows a user to specify certain parameters, then leverage the api endpoints here: https://developers.coinbase.com/api/v2#data-endpoints to provide and return the data per the requirements below. Yuo can choose who you want to collect and manage user inputs.
* Allow the user to specify a currency code and return the full currency name for that code.
* Allow the user to specify a currency, then get data for all currencies and their exchange rate relative to that specified currency and output this data to a csv
    * Should have at least the columns: currency, currency_code, exchange_rate
    * csv file name should follow the format {currency-code}currency_exchange_output_{timestamp}.csv
* Allow the user to specify buy, sell or spot, as well as a currency pair and return the specified price for the given currency pair


#### Bonus
* For a given base currency find and return the currency and rate with the highest or lowest exchange rate (specified by user)
* For a given base currency find and return the currency and price which will yield the highest or lowest buy/sell/spot price (specified by user)
