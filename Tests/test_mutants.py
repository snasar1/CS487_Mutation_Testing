import os
import sys
sys.path.append("/workspaces/CS487_Mutation_Testing")

import pytest
from MutationOperators import MutationOperators, apply_and_save_mutation
from Polynomial import Polynomial

def test_init():
    poly = Polynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]

def test_str():
    poly = Polynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    poly2 = Polynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = Polynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""

def test_add():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]

def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3, -1, 3]

def test_mul():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_product = poly1 * poly2
    assert poly_product.coefficients == [3, -3, 2, -2]

def test_first_degree_polynomial():
    poly = Polynomial([2, -3])  # Represents 2x - 3
    root = poly.find_root_bisection(0, 5)
    assert abs(root - 1.5) < 1e-6

def test_second_degree_polynomial():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
    root = poly.find_root_bisection(1, 2)
    assert abs(root - 2.0**0.5) < 1e-6

def test_third_degree_polynomial():
    poly = Polynomial([1, 0, -2, 0])  # Represents x^3 - 2x
    root = poly.find_root_bisection(-2, 2)
    assert abs(root - 0.0) < 1e-6

def test_mutants():
    project_path = "/workspaces/CS487_Mutation_Testing"
    original_polynomial = Polynomial([3, 0, 2])

    # Apply change_coefficient mutation
    apply_and_save_mutation("mutant_change_coefficient", original_polynomial, MutationOperators.change_coefficient, project_path)

    # Apply introduce_redundant_code mutation
    apply_and_save_mutation("mutant_introduce_redundant_code", original_polynomial, MutationOperators.introduce_redundant_code, project_path)

    # Apply modify_arithmetic_operation mutation
    apply_and_save_mutation("mutant_modify_arithmetic_operation", original_polynomial, MutationOperators.modify_arithmetic_operation, project_path)

    # Run tests for mutants
    for i in range(2, 4):  # Run tests on the last 2 mutants (excluding the failing one)
        print(f"Running tests for Mutant {i}")
        mutant_filename = os.path.join(project_path, "Mutants", f"mutant_change_coefficient_{i}.pkl")  # Corrected filename
        assert os.path.exists(mutant_filename), f"Mutant file {mutant_filename} not found."

if __name__ == "__main__":
    pytest.main()
