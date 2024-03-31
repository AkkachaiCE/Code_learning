import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 3:
    if (sys.argv[1].endswith(".csv")) and (sys.argv[2].endswith(".csv")):
        try:
            #Reade file
            with open(sys.argv[1], 'r') as fileR:
                reader = csv.DictReader(fileR)
                #Write file
                with open(sys.argv[2], 'w', newline='') as fileW:
                    fieldnames = ['first', 'last', 'house']
                    writer = csv.DictWriter(fileW, fieldnames=fieldnames)
                    writer.writeheader()
                    #Loop to read then swap then write
                    for row in reader:
                        names = row['name'].split()
                        first, last = names[1].replace('"', '').strip(','), names[0].replace('"', '').strip(',')
                        house = row['house']
                        writer.writerow({'first': first, 'last': last, 'house': house})

        except FileNotFoundError:
            sys.exit("The file does exist.")
    else:
        sys.exit("Not a CSV file")
else:
    sys.exit("Too many command-line arguments")
