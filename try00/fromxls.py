from redist import *
import xlrd

def from_xls_file(filename, sheet_index):
    """Parse an Excel sheet and return a RedistributionProblem."""

    sheet = xlrd.open_workbook(filename).sheet_by_index(sheet_index)

    colindex_article = 0
    colindex_weight = colindex_article + 1
    colindex_sellrate = colindex_weight + 1
    colindex_branch = colindex_sellrate + 1
    colindex_start_variants = colindex_branch + 1

    def get_variants(first_row, second_row):
        colindex = colindex_start_variants
        while first_row[colindex].ctype != xlrd.XL_CELL_EMPTY and second_row[colindex].value != "Summe":
            yield second_row[colindex].value
            colindex += 1
        raise StopIteration

    variants = list(get_variants(sheet.row(0), sheet.row(1)))

    colindex_sum = colindex_start_variants + len(variants)
    colindex_last = colindex_sum

    number_of_columns = colindex_last + 1

    colindex_start_supply = 0
    colindex_end_supply = number_of_columns
    colindex_start_demand = colindex_end_supply + 1
    colindex_end_demand = colindex_start_demand + number_of_columns

    rowindex_start_data = 2

    all_data_rows = [sheet.row(i) for i in range(rowindex_start_data, sheet.nrows)]

    supply_rows = [row[colindex_start_supply:colindex_end_supply] for row in all_data_rows
                     if row[colindex_start_supply].ctype != xlrd.XL_CELL_EMPTY]
    demand_rows = [row[colindex_start_demand:colindex_end_demand] for row in all_data_rows
                     if row[colindex_start_demand].ctype != xlrd.XL_CELL_EMPTY]

    def branches_occuring_in_rows(rows):
        branches = sorted(list(set([row[colindex_branch].value for row in rows])))
        return [RedistributionBranch(i, branches[i]) for i in range(len(branches))]

    supply_branches = branches_occuring_in_rows(supply_rows)
    demand_branches = branches_occuring_in_rows(demand_rows)

    supply_branches_by_name = dict((branch.name, branch) for branch in supply_branches)
    demand_branches_by_name = dict((branch.name, branch) for branch in demand_branches)

    def supply_or_demand_from_row(row, index, branches_by_name, RedistributionSupplyOrDemand):
        weight = float(row[colindex_weight].value)
        sellrate = float(row[colindex_sellrate].value)
        branch = branches_by_name[RedistributionBranch.make_name(row[colindex_branch].value)]
        number_per_variant = [int(row[colindex_start_variants + i].value) for i, variant in enumerate(variants)]
        number_sum = int(row[colindex_sum].value) # ignored

        return RedistributionSupplyOrDemand(index, weight, sellrate, branch, number_per_variant)

    supplies = [supply_or_demand_from_row(row, i, supply_branches_by_name, RedistributionSupply) for i, row in enumerate(supply_rows)]
    demands = [supply_or_demand_from_row(row, i, demand_branches_by_name, RedistributionDemand) for i, row in enumerate(demand_rows)]

    article = int(all_data_rows[0][colindex_article].value)

    return RedistributionProblem(article, variants, supply_branches, demand_branches, supplies, demands)
