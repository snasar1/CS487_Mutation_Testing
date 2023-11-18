# MutationOperators.py
import copy
import random
import os
import pickle
from Polynomial import Polynomial

class MutationOperators:
    @staticmethod
    def change_coefficient(polynomial):
        mutated_poly = copy.deepcopy(polynomial)
        index_to_change = random.randint(0, len(mutated_poly.coefficients) - 1)
        mutated_poly.coefficients[index_to_change] += random.uniform(-1, 1)
        return mutated_poly

    @staticmethod
    def introduce_redundant_code(polynomial):
        mutated_poly = copy.deepcopy(polynomial)
        mutated_poly.coefficients.append(random.uniform(-1, 1))
        return mutated_poly

    @staticmethod
    def modify_arithmetic_operation(polynomial):
        mutated_poly = copy.deepcopy(polynomial)
        operation_to_modify = random.choice(["add", "subtract", "multiply"])
        
        if operation_to_modify == "add":
            mutated_poly.coefficients = [coef + random.uniform(-1, 1) for coef in mutated_poly.coefficients]
        elif operation_to_modify == "subtract":
            mutated_poly.coefficients = [coef - random.uniform(-1, 1) for coef in mutated_poly.coefficients]
        elif operation_to_modify == "multiply":
            mutated_poly.coefficients = [coef * random.uniform(0.5, 1.5) for coef in mutated_poly.coefficients]
        
        return mutated_poly

def apply_and_save_mutation(mutant_name, original_polynomial, mutation_function, project_path):
    mutated_polynomial = mutation_function(original_polynomial)
    mutant_filename = os.path.join(project_path, "Mutants", f"{mutant_name}.pkl")

    with open(mutant_filename, 'wb') as file:
        pickle.dump(mutated_polynomial, file)
