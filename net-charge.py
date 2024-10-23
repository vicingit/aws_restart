# Python3.6  
# Coding: utf-8  

# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  

# Concatenate bInsulin and aInsulin to form insulin  
insulin = bInsulin + aInsulin

# Define the pKR values for the relevant amino acids
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Count the occurrences of each relevant amino acid in the insulin sequence
seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

# Initialize the pH value
pH = 0

# Loop through pH values from 0 to 14 and calculate net charge at each pH
while pH <= 14:
    # Calculate the net charge
    netCharge = (
        +(sum({x: ((seqCount[x] * (10**pKR[x])) / ((10**pH) + (10**pKR[x]))) for x in ['k', 'h', 'r']}.values()))
        - (sum({x: ((seqCount[x] * (10**pH)) / ((10**pH) + (10**pKR[x]))) for x in ['y', 'c', 'd', 'e']}.values()))
    )

    # Print the pH and corresponding net charge, formatted to two decimal places
    print('{0:.2f}'.format(pH), netCharge)

    # Increment pH by 1
    pH += 1
