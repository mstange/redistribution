from redist import *
import cplex


def find_optimal_redistribution(problem):
    """Solve the transfer problem and return a RedistributionSupply object that contains the solution."""

    variant_indices = range(len(problem.variants))

    lp = cplex.Cplex()
    lp.objective.set_sense(lp.objective.sense.maximize)

    # Add variables for transfer between supplies and demands.

    def var_supply_to_demand(supply, demand):
        return "supply %d to demand %d" % (supply.index, demand.index)

    for supply in problem.supplies:
        lp.variables.add(names=[var_supply_to_demand(supply, demand) for demand in problem.demands],
                         lb=[0 for demand in problem.demands],
                         ub=[1 for demand in problem.demands],
                         types=[lp.variables.type.integer for demand in problem.demands],
                         obj=[supply.weight + demand.weight for demand in problem.demands])

    # Add conditions for: Every supply must be transfered to only one demand (or to none).

    lp.linear_constraints.add(
        lin_expr=[
            cplex.SparsePair(
                ind=[var_supply_to_demand(supply, demand) for demand in problem.demands],
                val=[1                                    for demand in problem.demands])
            for supply in problem.supplies],
        senses=["L" for supply in problem.supplies],
        rhs=[1 for supply in problem.supplies])

    # Add conditions for: Every demand may only be supplied by demand.allowed_number_of_supplies() supplies.

    lp.linear_constraints.add(
        lin_expr=[
            cplex.SparsePair(
                ind=[var_supply_to_demand(supply, demand) for supply in problem.supplies],
                val=[1                                    for supply in problem.supplies])
            for demand in problem.demands],
        senses=["L" for demand in problem.demands],
        rhs=[demand.allowed_number_of_supplies() for demand in problem.demands])

    # Add variables and conditions for avoiding overflow.

    def var_overflow_for_demand_variant(demand, k):
        return "overflow for demand %d on variant %d" % (demand.index, k)

    for demand in problem.demands:

        # Add variables for overflow of variants per demand.

        lp.variables.add(names=[var_overflow_for_demand_variant(demand, k) for k in variant_indices],
                         lb=[0 for k in variant_indices],
                         ub=[demand.allowed_overflow_per_variant() for k in variant_indices],
                         types=[lp.variables.type.integer for k in variant_indices])

        # Add conditions for overflow of variants per demand.

        lp.linear_constraints.add(
            lin_expr=[
                cplex.SparsePair(
                    ind=[var_supply_to_demand(supply, demand) for supply in problem.supplies] + [var_overflow_for_demand_variant(demand, k)],
                    val=[supply.supply_of_variant[k]          for supply in problem.supplies] + [-1])
                for k in variant_indices],
            senses=["L" for k in variant_indices],
            rhs=[demand.demand_of_variant[k] for k in variant_indices])

        if demand.allowed_total_overflow() is not None:

            # Add condition for: Only demand.allowed_total_overflow() variants may be overflowed on this demand.

            lp.linear_constraints.add(
                lin_expr=[cplex.SparsePair(
                    ind=[var_overflow_for_demand_variant(demand, k) for k in variant_indices],
                    val=[1                                          for k in variant_indices])],
                senses=["L"],
                rhs=[demand.allowed_total_overflow()])

    lp.solve()

    return RedistributionSolution(problem, lp.solution.get_values(), lp.solution.get_objective_value())
