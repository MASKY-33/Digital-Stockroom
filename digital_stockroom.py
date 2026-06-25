## Digital Stockroom


stockroom = {
    "laptops" : 9,
    "monitors" : 4,
    "phones" : 15
}

stocking = stockroom["phones"]
print(stocking)


stockroom["watches"] = 25

stockroom["monitors"] = 10

print(stockroom)


desktop_usage = "keyboards "

if desktop_usage in stockroom:
    keyboards = stockroom[desktop_usage]
    print(keyboards)
else:
    print("Product not in stock!")
