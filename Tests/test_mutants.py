# Tests/test_mutants.py
import os
import sys
import pickle
import pytest

# Add the project directory to the Python path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_path)

from Polynomial import Polynomial
from MutationOperators import MutationOperators
from Tests.PolyTest import (
    test_init,
    test_str,
    test_add,
    test_sub,
    test_mul,
    test_first_degree_polynomial,
    test_second_degree_polynomial,
    test_third_degree_polynomial,
)

def apply_and_save_mutation(mutant_name, original_poly, mutation_func):
    mutated_poly = mutation_func(original_poly)
    mutant_filename = os.path.join(project_path, f"{mutant_name}.pkl")
    with open(mutant_filename, "wb") as file:
        pickle.dump(mutated_poly, file)

def test_mutants():
    original_polynomial = Polynomial([3, 0, 2])

    # Apply change_coefficient mutation
    apply_and_save_mutation("mutant_change_coefficient", original_polynomial, MutationOperators.change_coefficient)

    # Apply introduce_redundant_code mutation
    apply_and_save_mutation("mutant_introduce_redundant_code", original_polynomial, MutationOperators.introduce_redundant_code)

    # Apply modify_arithmetic_operation mutation
    apply_and_save_mutation("mutant_modify_arithmetic_operation", original_polynomial, MutationOperators.modify_arithmetic_operation)

    # Run tests for mutants
    for i in range(1, 4):  # Run tests on 3 mutants as an example
        print(f"Running tests for Mutant {i}")
        mutant_filename = os.path.join(project_path, f"Mutants/mutant_change_coefficient_{i}.pkl")  # Adjust the filename here
        assert os.path.exists(mutant_filename), f"Mutant file {mutant_filename} not found."
        with open(mutant_filename, "rb") as file:
            mutant = pickle.load(file)
        test_init(mutant)
        test_str(mutant)
        test_add(mutant)
        test_sub(mutant)
        test_mul(mutant)
        test_first_degree_polynomial(mutant)
        test_second_degree_polynomial(mutant)
        test_third_degree_polynomial(mutant)

if __name__ == "__main__":
    pytest.main()
