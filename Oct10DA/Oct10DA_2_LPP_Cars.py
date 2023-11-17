""""
we want to manifacture cars of type A and B. How many cars of each type to manufacture per day?
suppose we have three resources R1, R2, R3 that are needed to manufacture these cars.
Car A needs 3 units of R1, 5 units of R2, and 1.5 units of R3
CAr B needs 4 units of R`, 6 units of R2, and 3 units of R3
Maximum availibility of resources per day is : R1 =30, R2= 60, R3= 21
Each car A sale contributes $30,000 to the profits, Car B contributes $ 45,000 to the profits
How many cars should we manufacture each day of Type A and Type B?

"""

import pulp

#Instantiate our problem class 
model = pulp.LpProblem('Profit_maximising_problem', pulp.LpMaximize)

A = pulp.LpVariable('A', lowBound=0, cat= 'Integer')
B = pulp.LpVariable('B', lowBound=0, cat= 'Integer')

#Objective function
model += 3000 * A + 4500 * B, "Profit"

#Constraints
model += 3 * A + 4 * B <= 30
model += 5 * A + 6 * B <= 60
model += 1.5 * A + 3 * B <= 21

#Just for testing - What if we want to manufacture at least 5 cars per day?
#Add another constraint
# model += A >= 5
 
#Some more constriants - One of the two below
# model += A >= B
# model += A <= B


#Solve our problem
model.solve()
pulp.LpStatus[model.status]

#Print our decision variable values
print('Production of Car A = {}'.format(A.varValue))
print('Production of Car B = {}'.format(B.varValue))

#Print our objective function value
print(pulp.value(model.objective))




















