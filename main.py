import sys

from lib import Parent, Worksheet

if __name__ == '__main__':
    # your mileage may vary
    others_days = 90
    children = 3

    if len(sys.argv) > 1:
        others_days = float(sys.argv[1])
    if len(sys.argv) > 2:
        children = int(sys.argv[2])

    her_days = others_days
    his_days = 365 - her_days

    her = Parent(
        "HerName",
        her_days,
        15 * 40 * 52 / 12,
        care_expense=0,
        insurance=0
    )

    him = Parent(
        "HisName",
        his_days,
        110 * 1000 / 12,
        care_expense=60 * 6,
        insurance=335
    )

    worksheet = Worksheet(children, him, her)
    print("\n")
    worksheet.calc_support()
    print("\n")
    worksheet.print()
