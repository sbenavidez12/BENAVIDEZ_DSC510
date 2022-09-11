#DSC 510
#Week 2
#Programming Assignment Week 2
#Author: Stephanie Benavidez
#9/9/2022


print("      Welcome!    ")
company_name = ("Solomon Enterprises")

def calculate_total_cost(number_of_feets):
    standard_cost = 0.87
    total_cost = (number_of_feets * standard_cost)
    return total_cost

number_of_feets = int(465)
installation_cost = calculate_total_cost(number_of_feets)


# Printable Receipt Information
print("Your Receipt")
print("Company Name:",(company_name))
print("Number of feets of fiber cable:{}".format(number_of_feets))
print("Installation cost:${}".format(installation_cost))


#Change Control Log
#Change#: 2
#Change's Made: Changed formating for lines 23-24 by adding {}
#Date of Change: 9/10/2022
#Author: Stephanie Benavidez
#Changed Approved By:
#Date Moved to Production:
