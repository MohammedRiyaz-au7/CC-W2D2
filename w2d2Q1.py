S1 = int(input("enter marks in subject 1:"))
S2 = int(input("enter marks in subject 2:"))
S3 = int(input("enter marks in subject 3:"))
S4 = int(input("enter marks in subject 4:"))
S5 = int(input("enter marks in subject 5:"))
Perc = (S1 + S2 + S3 + S4 + S5) / 5
print("the perc value is ", Perc)
if Perc >= 90:
    print("the grade is A")
elif Perc >= 70 and Perc < 90:
    print("the grade is B")
elif Perc >= 50 and Perc < 70:
    print("the grade is C")
elif Perc >= 30 and Perc < 50:
    print("the grade is D")
else:
    print("the grade is E")
