def calculate_solution_weights(molecular_weights, solutions_needed):
    result = []
    
    for solution in solutions_needed:
        try:
            # Split the solution into chemical formula and concentration
            chemical, concentration = solution.split('-')
            concentration = float(concentration[:-1])  # Remove 'M' and convert to float
            
            # Check if the chemical exists in molecular_weights
            if chemical in molecular_weights:
                # Calculate the weight in grams
                weight = molecular_weights[chemical] * concentration
                result.append(f"{chemical}-{concentration}M-{weight:.2f}g")
            else:
                result.append("unknown")
        except (KeyError, ValueError):
            # Handle any parsing errors
            result.append("unknown")
    
    return result

# Example usage
molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}
solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']

output = calculate_solution_weights(molecular_weights, solutions_needed)
print(output)

