import sys
from gurobipy import GRB

# Check the model status
status_string = {
    GRB.OPTIMAL: "optimal",
    GRB.INFEASIBLE: "infeasible",
    GRB.UNBOUNDED: "unbounded",
    GRB.INF_OR_UNBD: "infeasible or unbounded",
    GRB.TIME_LIMIT: "time limit reached",
    GRB.NODE_LIMIT: "node limit reached",
    GRB.SOLUTION_LIMIT: "solution limit reached",
    GRB.INTERRUPTED: "interrupted",
    GRB.NUMERIC: "numerical issues",
    GRB.SUBOPTIMAL: "suboptimal",
    GRB.INPROGRESS: "in progress",
    GRB.USER_OBJ_LIMIT: "user objective limit reached"
}

def solve_and_print_solution(model):
    # Optimize model
    model.setParam("outputflag", 0)
    model.optimize()
    
    # Check the model status
    if model.status == GRB.OPTIMAL:
        print("Optimal solution found")
        print(f"Objective value: {model.objVal}")
        # Print the results
        for v in model.getVars():
            print(f"{v.VarName}: {abs(v.X)}")
    else:
        print(f"Model status: {status_string.get(model.status, 'unknown')}")
        sys.exit(1)