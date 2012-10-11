# coding=utf-8

import fromxls
import solving


def print_redistribution_solution(solution):
    """Prints a description of the solution."""

    problem = solution.problem

    print "\n-----------------\n"
    print "Resultat:\n"

    for demand in problem.demands:
        supplying = solution.supplies_for_demand(demand)
        if supplying:
            print "Filiale " + demand.branch.name + " wird beliefert von folgenden Filialen:", \
                  ", ".join([supply.branch.name for supply in supplying])
        else:
            print "Filiale " + demand.branch.name + " wird nicht beliefert."
        overflowed_variants = [variant for k, variant in enumerate(problem.variants)
                                 if sum([supply.supply_of_variant[k] for supply in supplying]) > demand.demand_of_variant[k]]
        if overflowed_variants:
            print "  Dabei werden folgende Varianten überbeliefert:", u", ".join(overflowed_variants)

    undemanded_supplies = [supply for supply in problem.supplies if not solution.demands_for_supply(supply)]
    if undemanded_supplies:
        print "Folgende Versorgerfilialen haben keine Abnehmer gefunden:", \
               ", ".join([supply.branch.name for supply in undemanded_supplies])
    else:
        print "Alle Versorgerfilialen wurden komplett abgenommen."

    print "Zielfunktionswert:", solution.objective_value


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    sheet_index = int(sys.argv[2])
    print "Importiere Excel-Datei %s (Seite %d)..." % (filename, sheet_index)
    problem = fromxls.from_xls_file(filename, sheet_index)
    print "Löse Problem für Artikel %d mit %d Versorgern und %d Abnehmern..." % \
        (problem.article, len(problem.supplies), len(problem.demands))
    optimal_redistribution = solving.find_optimal_redistribution(problem)
    print_redistribution_solution(optimal_redistribution)
