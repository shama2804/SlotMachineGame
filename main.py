import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#REELS
ROWS = 3
COLS = 3

#SYMBOLS
symbol_count = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
symbol_value = {
    "A": 5,  
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """
    Checks for winning lines in the slot machine and calculates total winnings.

    Parameters:
    columns (list): 2D list representing the slot machine grid (list of columns).
    lines (int): Number of lines the player has chosen to bet on.
    bet (int): Amount the player has bet per line.
    values (dict): Dictionary mapping symbols to their payout values.

    Returns:
    int: Total winnings based on the number of winning lines.
    """
    winnings = 0  # Initialize total winnings to zero
    winning_lines = []

    # Iterate over each line the player is betting on (rows in the grid)
    for line in range(lines):
        symbol = columns[0][line]  # Get the first symbol in the current row (line)

        # Check if all symbols in the same row (across columns) match the first symbol
        for column in columns:
            symbol_to_check = column[line] # Get the symbol from the current column at this row
            if symbol != symbol_to_check:  # If any symbol doesn't match, it's not a winning line
                break
        else:
            winnings += values[symbol] * bet  # Add winnings based on symbol value and bet amont
            winning_lines.append(line +1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    """
    Generates a randomized set of symbols for the slot machine.

    Parameters:
    rows (int): Number of rows in the slot machine grid.
    cols (int): Number of columns in the slot machine grid.
    symbols (dict): Dictionary where keys are symbol names (e.g., "A", "B") 
                    and values represent their frequency in the reels.

    Returns:
    list: A randomly generated 2D list representing the slot machine spin.
    """

    # List to store all possible symbols based on their defined frequency
    all_symbols = []
    # Iterate through the dictionary of symbols
    for symbol, symbol_count in symbols.items():
        # Append the symbol 'symbol_count' times to the all_symbols list
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    # Loop through each column
    for _ in range(cols):
        column = []  # Initialize an empty list for the current column
        current_symbols = all_symbols[:] # Make a copy of the all_symbols list to randomly select from (so it doesn't get modified globally)
        
         # Loop through each row
        for _ in range(rows):
            # Randomly choose a symbol from the current_symbols list
            value = random.choice(current_symbols)
            current_symbols.remove(value) # Remove the random chosen symbol from the current_symbol 
            column.append(value) # Append the chosen symbol to the current column

        columns.append(column) # Append the complete column to the columns list

    return columns


def print_slot_machine(columns):
    # Transposing and printing the slot machine grid
    for row in range(len(columns[0])): # Iterate over each row
        for i, column in  enumerate(columns): # Iterate through each column
            if i != len(columns) -1:
                print(column[row], end= " | ") # Print each symbol in the row, with a " | " separator between columns
            else:
                print(column[row],end="")

        print()


def deposit(): # For collecting user input that gets the deposit from the user
    while True: # To continue it untill we break it
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): # Should be a digit
            amount = int(amount) # Conver the amount from string to integer as it would accept it as string
            if amount > 0: # Amout should be greater than 0
                break
            else:
                print("Amout must be greater than 0")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" +str(MAX_LINES) +")?")
        if lines.isdigit(): # Should be a digit
            lines = int(lines) # Conver the lines from string to integer as it would accept it as string
            if 1 <= lines <= MAX_LINES: # lines should be greater than or equal to 1 and less than or equal to MAX_VALUE
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True: 
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): # Should be a digit
            amount = int(amount) # Conver the amount from string to integer as it would accept it as string
            if MIN_BET <= amount <= MAX_BET: # Amout should be greater than MIN_BET and less than MAX_BET
                break
            else:
                print(f"Amout must be in between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")
    return amount

def spin(balance):

    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        # There are cases when the person tries to bet more than the amount of balance he has
        if total_bet > balance:
            print(f"You do not have enough balance to continue with the bet. Your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to : ${total_bet}.")

    slot = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        user_input = input("Press enter to play. (q to quit)")
        if user_input == 'q':
            break
        balance += spin(balance)

main()
