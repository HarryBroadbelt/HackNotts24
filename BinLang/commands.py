grammar = {
    '1': 'start',
    '0': 'end',
    '00': '+',
    '01': '-',
    '10': '*',
    '11': '/',
    '000': '=',
    '001': '!=',
    '010' : 'if',
    '011' : 'else',
    '100' : '>',
    '101' : '<',
    '110' : '>=',
    '111' : '<=',
    '1000' : '==',
    '1001' : 'print'

}   

commands = {
    1 : "print(x)",
    2 : "x > y:",
    3 : "x < y:",
    4 : "x >= y:",
    5 : "x <= y:",
    6 : "x == y:",
    8 : "else:",
    9 : "  ", #tab
    10 : "print(y)",
    11 : "x = int(input())",
    12 : "y = int(input())",
    13 : "if",
    14 : "elif",
    15 : "x = y",
    16 : "y = x",
    17 : "print(z)",
    18 : "z = int(input())",
    19 : "x > z",
    20 : "y > z",
    21 : "x >= z",
    22 : "y >= z",
    23 : "x <= z",
    24 : "y <= z",
    25 : "x == z",
    26 : "y == z",
    27 : "x < z",
    28 : "y < z",
    
}