#! python3
# Function that takes a list of lists of strings and displays it in a well-organised table with each column right-justified

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = []
print(colWidths)

def printTable(tableData):
    colWidths = [0] * len(tableData)
    print(colWidths)

    for col in range(len(colWidths)):
        for i in tableData[col]:
            if len(i) > colWidths[col]:
                colWidths[col] = len(i)
                print(colWidths)

    for item in range(len(tableData[0])):
        for term in range(len(colWidths)):
            print(list(zip(*tableData))[item])
        print(list(zip(*tableData))[item])
        print(list)

printTable(tableData)

