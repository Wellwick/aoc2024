# Parser module that can return array of tokens, coordinate data, etc.

def get_lines(day : int) -> list[list[str]]:
    if (day < 1 or day > 25):
        raise ValueError
    
    filename = "inputs/"
    if (day < 10):
        filename += "0"

    filename += str(day) + ".txt"

    with open(filename, "r") as f:
        return f.readlines()

def get_tokens(day : int, seperator : str = " ") -> list[list[str]]:
    lines = get_lines(day)
    tokens = []
    for line in lines:
        split = line.split(seperator)
        token_line = []
        for s in split:
            if s != "":
                token_line += [ s ]
        tokens += [ token_line ]

    return tokens

def get_ints(day : int, seperator : str = " ") -> list[list[int]]:
    int_tokens = []
    for line in get_tokens(day, seperator):
        int_line = []
        for token in line:
            int_line += [ int(token) ]
        
        int_tokens += [ int_line ]
    
    return int_tokens
