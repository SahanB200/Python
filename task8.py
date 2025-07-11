price = float(input("Enter the price: "))
discount = 0

if price > 1000 :
    discount = price * (10/100)
    fprice = price - discount
    print(f"Discount is 10% \nFinal price is {fprice}")

elif price > 500 and price <1000:
    discount = price * (5/100)
    fprice = price - discount
    print(f"Discount is 5% \nFinal price is {fprice}")

else :
    print(f"No discount. Final price is {price}")