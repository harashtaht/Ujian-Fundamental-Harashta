###--------No 1----------###

# def calculate_years(principal, interest, tax, desired):
#     year = 0
#     while principal < desired:
#         principal = (principal + ((principal*interest)-((principal*interest*tax))))
#         year = year + 1

#     return print('Years required = ', year)

# calculate_years(1000, 0.05, 0.18, 1100)
# calculate_years(1200, 0.17, 0.05, 2000)
# calculate_years(1500, 0.07, 0.6, 5000)


###--------No 2----------###

a = 89237

def remainder(num):
    looper = (len(str(num))-1)
    nuremain = [num]
    for i in range(looper,0,-1):
        nr0 = num%(10**(i))
        nuremain.append(nr0)
    return nuremain

ToBeDivided = (remainder(a))
# [89237, 9237, 237, 37, 7]

def expandedForm (num):
    looper = (len(str(num))-1)
    k = 0
    nudigit = []
    for i in range(looper,0,-1):
        nd = (ToBeDivided[k]//10**i)*(10**i)
        nudigit.append(nd)
        k += 1
    return nudigit

expandedForm(ToBeDivided)