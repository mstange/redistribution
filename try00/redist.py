class RedistributionProblem:
    """Represents a stock transfer problem."""

    def __init__(self, article, variants, supply_branches, demand_branches, supplies, demands):
        self.article = article
        self.variants = variants
        self.supply_branches = supply_branches
        self.demand_branches = demand_branches
        self.supplies = supplies
        self.demands = demands


class RedistributionBranch: # Filiale

    def __init__(self, index, name):
        self.index = index
        self.name = self.make_name(name)

    @classmethod
    def make_name(cls, name):
        return "%04d" % int(name)


class RedistributionSupply:

    def __init__(self, index, weight, sellrate, branch, supply_of_variant):
        self.index = index
        self.weight = weight
        self.sellrate = sellrate
        self.branch = branch
        self.supply_of_variant = supply_of_variant


class RedistributionDemand:

    def __init__(self, index, weight, sellrate, branch, demand_of_variant):
        self.index = index
        self.weight = weight
        self.sellrate = sellrate
        self.branch = branch
        self.demand_of_variant = demand_of_variant

    def allowed_overflow_per_variant(self):
        return 1

    def allowed_total_overflow(self):
        if self.sellrate < 0.8:
            return 2
        if self.sellrate < 1:
            return 3
        return None

    def allowed_number_of_supplies(self):
        return 2


class RedistributionSolution:
    """Represents the solution of a RedistributionProblem."""

    def __init__(self, problem, solution_values, objective_value):
        self.problem = problem
        self.solution_values = solution_values
        self.objective_value = objective_value

    def is_supply_demand_path_taken(self, supply, demand):
        """Returns whether the specified supply transfers all its stock of the current article to the specified demand."""
        num_demands = len(self.problem.demands)
        return self.solution_values[supply.index * num_demands + demand.index] != 0

    def supplies_for_demand(self, demand):
        return [supply for supply in self.problem.supplies if self.is_supply_demand_path_taken(supply, demand)]

    def demands_for_supply(self, supply):
        return [demand for demand in self.problem.demands if self.is_supply_demand_path_taken(supply, demand)]
