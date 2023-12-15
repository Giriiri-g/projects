def readcsv():
    file = input("Enter file path/name :")
    fin = open(file)
    csvreader = csv.reader(fin)
    format_brakets = "{:<10}"
    for row in csvreader:
        l = len(row)
        print(format_brakets*l.format(row))
        
