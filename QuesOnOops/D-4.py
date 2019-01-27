# Question D4: WAP to input the sales made by a salesman in every month of a given year and
# find out the total, average, maximum and minimum sales.

sales ={'jan':1,'feb':2,'mrch':5,'aprl':6,'may':7,'june':8,'july':4,'aug':5,'sep':7,'oct':5,'nov':9,'dec':6}

for val in sales:
    add = sum(sales.values())
    avg = add/12
print(add)
print(avg)