#Number of Tables Input
input = int(input("Enter the number of Celsius temperatures to display: "))
#Table Creation
for C in range(input + 1):
#Output and Calculation
    print(C,"   ",round(9 / 5 * C + 32,1))
