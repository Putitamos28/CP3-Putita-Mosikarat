from datetime import datetime
from forex_python.converter import CurrencyRates


currency_rate = CurrencyRates()
print("--Welcome to Exchange Rate Program--")
print("PLEASE LOGIN TO PROGRAM")
username = str(input("Username : "))
password = input("Password : ")
if username == "admin" and password == "1234" :
    print("Done !")
    c = CurrencyRates()
    print("Today Exchange rate")
    result = c.get_rates('USD')
    print(result)
    print("Get conversion rate from your selected")
    def conversion():
        currency = str(input("Please select Currency : "))
        buyying_country = str(input("Please select Country :"))
        conversions = c.get_rate(currency, buyying_country)
        print(conversions)
        print("Convert amount from your selected")
    def convert():
        currency= str(input("Please select Currency : "))
        buyying_country = str(input("Please select Country :"))
        money = int(input("How many money do you get : "))
        exchange_price = c.convert(currency, buyying_country, money)
        print(exchange_price)
    def datetimecheck():
        years = int(input("YEARS : "))
        months = int(input("MONTHS : "))
        dates = int(input("DATES : "))
        select_curruncy = str(input("Currency : "))
        rate_on_date = datetime(years,months,dates, 18, 36, 28, 151012)
        currency_on_datetime = c.get_rates(select_curruncy,rate_on_date)
        print(currency_on_datetime)
    conversion()
    convert()
    datetimecheck()
else :
    print("Eror !")


