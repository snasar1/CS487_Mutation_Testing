# MutationOperators.py
from Polynomial import Polynomial
import copy
import random

class MutationOperators:
    @staticmethod
    def change_coefficient(polynomial):
        # Create a deep copy of the original polynomial
        mutated_poly = copy.deepcopy(polynomial)

        # Randomly select a coefficient index to change
        index_to_change = random.randint(0, len(mutated_poly.coefficients) - 1)

        # Change the coefficient at the selected index
        mutated_poly.coefficients[index_to_change] += random.uniform(-1, 1)

        return mutated_poly

    @staticmethod
    def introduce_redundant_code(polynomial):
        # Create a deep copy of the original polynomial
        mutated_poly = copy.deepcopy(polynomial)

        # Introduce a redundant term with a random coefficient
        mutated_poly.coefficients.append(random.uniform(-1, 1))

        return mutated_poly

    @staticmethod
    def modify_arithmetic_operation(polynomial):
        # Create a deep copy of the original polynomial
        mutated_poly = copy.deepcopy(polynomial)

        # Randomly select an arithmetic operation to modify
        operation_to_modify = random.choice(["add", "subtract", "multiply"])

        # Apply the modification to the coefficients
        if operation_to_modify == "add":
            mutated_poly.coefficients = [coef + random.uniform(-1, 1) for coef in mutated_poly.coefficients]
        elif operation_to_modify == "subtract":
            mutated_poly.coefficients = [coef - random.uniform(-1, 1) for coef in mutated_poly.coefficients]
        elif operation_to_modify == "multiply":
            mutated_poly.coefficients = [coef * random.uniform(0.5, 1.5) for coef in mutated_poly.coefficients]

        return mutated_poly
