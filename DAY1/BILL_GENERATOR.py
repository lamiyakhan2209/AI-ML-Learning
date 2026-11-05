#BILL GENERATOR
item1 = input("Enter item1: ")
price1 = float(input("Enter price of item1: "))
quantity1 = int(input("Enter quantity of item1: "))

item2 = input("Enter item2: ")
price2 = float(input("Enter price of item2: "))
quantity2 = int(input("Enter quantity of item2: "))

item3 = input("Enter item3: ")
price3 = float(input("Enter price of item3: "))
quantity3 = int(input("Enter quantity of item3: " ))

total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3

GrandTotal = total1 + total2 + total3
gst = GrandTotal * 0.18

final_amount = GrandTotal + gst

print("----------BILL----------")

print("item1: ",item1)
print("price: ",price1)
print("quantity: ",quantity1)
print("total of item1: ",total1)
print()

print("item2: ",item2)
print("price: ",price2)
print("quantity: ",quantity2)
print("total of item2: ",total2)
print()

print("item3: ",item3)
print("price: ",price3)
print("quantity: ",quantity3)
print("total of item3: ",total3)
print()

print("Total Amount :",GrandTotal)
print("GST: ",gst)
print("Final Amount is: ",final_amount)

