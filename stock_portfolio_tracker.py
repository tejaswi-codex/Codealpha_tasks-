# hard-coded dictionary for stock prices
stock_prices = {
    "HAL": 4500,
    "BEL": 320,
    "TCS": 3900,
    "INFY": 1500
}

print("STOCK PORTFOLIO TRACKER")

# taking stock name from user
stock_name = input("\nEnter stock name: ").upper()

# checking stock availability
if stock_name in stock_prices:

    # taking quantity from user
    quantity = int(input("Enter quantity: "))

    # calculating total investment
    total_investment = stock_prices[stock_name] * quantity

    # displaying result
    print("\nStock Price:", stock_prices[stock_name])
    print("Quantity:", quantity)
    print("Total Investment Value:", total_investment)

    # saving result in text file
    file = open("portfolio.txt", "w")

    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("Stock Name: " + stock_name + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Investment Value: " + str(total_investment))

    file.close()

    print("\nData saved in portfolio.txt")

else:
    print("Stock not found")
