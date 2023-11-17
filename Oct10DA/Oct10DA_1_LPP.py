#R1: labor 2*x1 + 1*x2 + 2.5*x3 <= 60 Hours
#R2: Machine: 0.8*x1 + 0.6*x2 + 1.0*x3 <= 16 Hours
#R3: Wood : 30*x1 + 20*x2 + 30*x3 <= 400 board-feet
#Produts : chairs ($30 to profits), Tables($40), Bookcases($45)

#import all calsses of PuLP module
from pulp import *

#Crete the problem variable to contain the problem data
model = LpProblem("FurnitureProblem",LpMaximize)

#Create 3 variables tables, chairs, and bookcases

x1 = pulp.LpVariable('tables', 0, None, LpInteger)
x2 = pulp.LpVariable('chairs', 0, None, LpInteger)
x3 = pulp.LpVariable('bookcases', 0, None, LpInteger)

#Create maximize objective function
model += 40 * x1 + 30 * x2 + 45 * x3

#create three constraints
model += 2 * x1 + 1* x2 + 2.5 * x3 <= 60, "Labour"
model += 0.8 * x1 + 0.6* x2 + 1.0 * x3 <= 16, "Machine"
model += 30 * x1 + 20* x2 + 30 * x3 <= 400, "Wood"

#Try commenting the statement below and see the differnce
# model += x1 >= 1, "chairs"
# model += x3 >= 1, "bookcases"

#The problem is solved usint PuLP's choice of Solver
model.solve()

#Each of the vairable is printed with it's resolved optimum value
for v in model.variables():
    print(v.name, "=", v.varValue)