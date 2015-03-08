#Mortgage calculator with additional payments 

# ask for loan amount
amount = int(input("Please enter the loan amount you are seeking without a comma: " ))

# annual percent interest
percInterest = float(input("What percent interest rate will the loan be at? " ))

# calculating monthly interest rate
monthlyInterest = percInterest/(100 * 12)

# give length of mortgage
length = float(input("How many years will the mortgage be for? " ))

# calculate total number of payments
paymentNum = length * 12

monthlyPayment = amount * ( monthlyInterest / (1 - (1 + monthlyInterest) ** (- paymentNum)))

print "Total loan = $%0.2f" % amount
print "Interest   = %0.2f%s" % (percInterest, "%")
print "Years      = %0.f" % length
print "Number of payments = %0.f" % paymentNum
print "Payment amount     = $%0.2f" % monthlyPayment
print "-"*50
print "Total cost     = $%0.2f" % (paymentNum * monthlyPayment)
print "Total interest = $%0.2f" % (paymentNum * monthlyPayment - amount)
#print "-"*50


# payments made so far
#payments = int(input("How many payments have you made so far? " ))
#remainingAmount = amount * (1 - ((1 + monthlyInterest) ** payments - 1) / ((1 + monthlyInterest) ** paymentNum - 1))
#print "The outstanding principal after %d payments is $%0.2f" % (payments, remainingAmount)
#print "At this point you have paid a total of $%0.2f" % (monthlyPayment * payments)
	