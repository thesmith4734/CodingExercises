# This Exercise is still a work in progress

=====

# Rest API lottery number exercise

Build a simple rest api leveraging the powerball_winning_numbers.csv data and respond with data in json format

* Take a date or date range as parameter and return the winning numbers for all of those dates
* Take multiplier as a parameter and return all instances with that same multiplier
* Take a set of winning numbers and return any dates which would have won any of the following categories (we will ignore the actual 'powerball' rules for this):
    * Match 4 (4 numbers are the same)
    * Match 5 (5 numbers are the same)
    * Match 6 (6 numbers are the same)
* Take a date range as parameter and find the date within that range where the sum of all winning numbers is the highest
* Take a date range as parameter and return the top 6 most frequent numbers that have appeared over that range
* Take a month + year as a parameter and return the average multiplier value for that month
