import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2:
    if (sys.argv[1].endswith(".csv")):
        try:
            data = []
            with open(sys.argv[1], 'r') as file:
                reader = csv.reader(file)
                headers = next(reader)

                for row in reader:
                    data.append(row)
            print(tabulate(data, headers, tablefmt='grid'))

        except FileNotFoundError:
            sys.exit("The file does not exist.")
    else:
        sys.exit("Not a CSV file")
else:
    sys.exit("Too many command-line arguments")
