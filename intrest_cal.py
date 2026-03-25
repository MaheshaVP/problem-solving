#compound intrest calculator
# A = P(1+r/n)^t

p = 10000
r = 15
time = 2

ci = p * pow((1 + r/100), time)
print(f"total amount for {time} is {ci:.2f}")
