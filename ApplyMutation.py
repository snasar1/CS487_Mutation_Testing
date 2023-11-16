# ApplyMutation.py
import os
from Polynomial import Polynomial
from MutationOperators import MutationOperators

def apply_mutations(original_polynomial):
    # Use an absolute path for the Mutants directory
    mutants_dir = os.path.join(os.path.dirname(__file__), 'Mutants')
    os.makedirs(mutants_dir, exist_ok=True)

    # Create mutants using different mutation operators
    mutant_1 = MutationOperators.change_coefficient(original_polynomial)
    mutant_2 = MutationOperators.introduce_redundant_code(original_polynomial)
    mutant_3 = MutationOperators.modify_arithmetic_operation(original_polynomial)

    # Print some information for debugging
    print(f"Mutant 1 coefficients:\n{mutant_1.coefficients}")
    print(f"Mutant 2 coefficients:\n{mutant_2.coefficients}")
    print(f"Mutant 3 coefficients:\n{mutant_3.coefficients}")

    # Save mutants to separate files
    with open(os.path.join(mutants_dir, 'mutant_1.py'), 'w') as file:
        file.write("# Coefficients: " + str(mutant_1.coefficients))

    with open(os.path.join(mutants_dir, 'mutant_2.py'), 'w') as file:
        file.write("# Coefficients: " + str(mutant_2.coefficients))

    with open(os.path.join(mutants_dir, 'mutant_3.py'), 'w') as file:
        file.write("# Coefficients: " + str(mutant_3.coefficients))

if __name__ == "__main__":
    # Assuming you already have the original polynomial object
    original_polynomial = Polynomial([3, 0, 2])

    # Apply mutations and save mutants
    apply_mutations(original_polynomial)
