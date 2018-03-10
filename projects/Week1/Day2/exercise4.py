totalBillAmount = 60

qualityOfService = raw_input("How was the service?")

if qualityOfService == "good":
    print totalBillAmount * 20 / 100
elif qualityOfService == "fair":
    print totalBillAmount * 15 / 100
else:
    print totalBillAmount * 10 / 100

numberOfGuests = int(raw_input("How many ways are we splitting the bill?"))
print totalBillAmount / numberOfGuests