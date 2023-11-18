# Mutation Testing

## Overview

Welcome to the CS487 Mutation Testing Project! This Python project focuses on polynomial operations and incorporates mutation testing to evaluate the effectiveness of the test suite.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Mutation Testing](#mutation-testing)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/snasar1/CS487_Mutation_Testing.git
    cd CS487_Mutation_Testing
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

- Run the main polynomial operations script:

    ```bash
    python PolynomialOperations.py
    ```

- Explore and modify the polynomial codebase in the `Polynomial.py` file.

## Project Structure

- `Polynomial.py`: Contains the implementation of the Polynomial class and associated operations.
- `Tests/`: Directory for test scripts and mutants testing.
- `MutationOperators.py`: Defines mutation operators used in testing.
- `ApplyMutation.py` and `applymutations.py`: Scripts for applying mutations and saving mutant files.
- `requirements.txt`: Lists project dependencies.

## Mutation Testing

Mutation testing is performed on the polynomial codebase to assess the test suite's effectiveness. Three mutation operators are applied:
1. `change_coefficient`: Mutates polynomial coefficients.
2. `introduce_redundant_code`: Introduces redundant code.
3. `modify_arithmetic_operation`: Alters arithmetic operations.

## Tests

Run tests using pytest:

```bash
pytest Tests/
```

