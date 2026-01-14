"""
Probability Functions - From Scratch Implementation

This module implements core probability functions using pure Python and NumPy.
All functions include agricultural examples in their docstrings.

Author: Agricultural ML Concepts
Purpose: Educational - Understanding probability through implementation
"""

import numpy as np
from typing import Union, List, Tuple


def calculate_probability(favorable_outcomes: Union[int, float],
                          total_outcomes: Union[int, float]) -> float:
    """
    Calculate basic probability: P(A) = favorable / total

    Parameters
    ----------
    favorable_outcomes : int or float
        Number of favorable outcomes (or count)
    total_outcomes : int or float
        Total number of possible outcomes

    Returns
    -------
    float
        Probability value between 0 and 1

    Raises
    ------
    ValueError
        If total_outcomes is 0 or negative
        If favorable_outcomes is negative
        If favorable_outcomes > total_outcomes

    Examples
    --------
    >>> # Agricultural example: Germination success
    >>> # Out of 100 seeds planted, 85 germinated
    >>> calculate_probability(85, 100)
    0.85

    >>> # Crop disease: 12 out of 80 fields affected
    >>> calculate_probability(12, 80)
    0.15
    """
    # Input validation
    if total_outcomes <= 0:
        raise ValueError(f"Total outcomes must be positive, got {total_outcomes}")

    if favorable_outcomes < 0:
        raise ValueError(f"Favorable outcomes cannot be negative, got {favorable_outcomes}")

    if favorable_outcomes > total_outcomes:
        raise ValueError(
            f"Favorable outcomes ({favorable_outcomes}) cannot exceed "
            f"total outcomes ({total_outcomes})"
        )

    return favorable_outcomes / total_outcomes


def addition_rule(p_a: float, p_b: float, p_a_and_b: float = 0) -> float:
    """
    Calculate P(A OR B) using the addition rule.

    For mutually exclusive events: P(A∪B) = P(A) + P(B)
    For non-mutually exclusive: P(A∪B) = P(A) + P(B) - P(A∩B)

    Parameters
    ----------
    p_a : float
        Probability of event A
    p_b : float
        Probability of event B
    p_a_and_b : float, optional
        Probability of both A and B (default 0 for mutually exclusive)

    Returns
    -------
    float
        Probability of A or B (or both)

    Raises
    ------
    ValueError
        If probabilities are not in [0, 1]
        If p_a_and_b > min(p_a, p_b)

    Examples
    --------
    >>> # Mutually exclusive: Weather can't be both sunny and rainy
    >>> addition_rule(0.40, 0.20)  # P(Sunny) or P(Rainy)
    0.6

    >>> # Non-mutually exclusive: Disease and pests can co-occur
    >>> addition_rule(0.25, 0.30, 0.10)  # P(Disease OR Pests)
    0.45
    """
    # Input validation
    if not (0 <= p_a <= 1):
        raise ValueError(f"P(A) must be in [0,1], got {p_a}")
    if not (0 <= p_b <= 1):
        raise ValueError(f"P(B) must be in [0,1], got {p_b}")
    if not (0 <= p_a_and_b <= 1):
        raise ValueError(f"P(A∩B) must be in [0,1], got {p_a_and_b}")

    # P(A∩B) cannot exceed either individual probability
    if p_a_and_b > min(p_a, p_b):
        raise ValueError(
            f"P(A∩B) = {p_a_and_b} cannot exceed min(P(A), P(B)) = {min(p_a, p_b)}"
        )

    result = p_a + p_b - p_a_and_b

    # Result cannot exceed 1
    if result > 1:
        raise ValueError(
            f"Invalid probabilities: P(A∪B) = {result:.4f} exceeds 1.0"
        )

    return result


def multiplication_rule(p_a: float, p_b: float,
                       independent: bool = True,
                       p_b_given_a: float = None) -> float:
    """
    Calculate P(A AND B) using the multiplication rule.

    For independent events: P(A∩B) = P(A) × P(B)
    For dependent events: P(A∩B) = P(A) × P(B|A)

    Parameters
    ----------
    p_a : float
        Probability of event A
    p_b : float
        Probability of event B (only used if independent=True)
    independent : bool, optional
        Whether events are independent (default True)
    p_b_given_a : float, optional
        P(B|A) for dependent events (required if independent=False)

    Returns
    -------
    float
        Probability of both A and B occurring

    Raises
    ------
    ValueError
        If probabilities are not in [0, 1]
        If independent=False but p_b_given_a not provided

    Examples
    --------
    >>> # Independent: Frost in two separate fields
    >>> multiplication_rule(0.15, 0.15, independent=True)
    0.0225

    >>> # Dependent: Disease and then spreading
    >>> multiplication_rule(0.30, None, independent=False, p_b_given_a=0.70)
    0.21
    """
    # Input validation
    if not (0 <= p_a <= 1):
        raise ValueError(f"P(A) must be in [0,1], got {p_a}")

    if independent:
        if not (0 <= p_b <= 1):
            raise ValueError(f"P(B) must be in [0,1], got {p_b}")
        return p_a * p_b
    else:
        if p_b_given_a is None:
            raise ValueError("For dependent events, p_b_given_a must be provided")
        if not (0 <= p_b_given_a <= 1):
            raise ValueError(f"P(B|A) must be in [0,1], got {p_b_given_a}")
        return p_a * p_b_given_a


def complement_probability(p_a: float) -> float:
    """
    Calculate P(NOT A) = 1 - P(A)

    Parameters
    ----------
    p_a : float
        Probability of event A

    Returns
    -------
    float
        Probability of A not occurring

    Raises
    ------
    ValueError
        If p_a is not in [0, 1]

    Examples
    --------
    >>> # Probability of crop success given 15% failure rate
    >>> complement_probability(0.15)
    0.85

    >>> # Probability of at least one seed germinating
    >>> # If each seed has 8% failure rate individually
    >>> p_all_fail = 0.08 ** 5  # 5 seeds
    >>> complement_probability(p_all_fail)  # At least one success
    0.9999...
    """
    if not (0 <= p_a <= 1):
        raise ValueError(f"P(A) must be in [0,1], got {p_a}")

    return 1.0 - p_a


def conditional_probability(p_a_and_b: float, p_b: float) -> float:
    """
    Calculate P(A|B) = P(A∩B) / P(B)

    Parameters
    ----------
    p_a_and_b : float
        Probability of both A and B
    p_b : float
        Probability of B

    Returns
    -------
    float
        Conditional probability of A given B

    Raises
    ------
    ValueError
        If probabilities are not in [0, 1]
        If p_b is 0 (cannot condition on impossible event)
        If p_a_and_b > p_b (invalid probabilities)

    Examples
    --------
    >>> # P(Disease | Symptoms)
    >>> # P(Disease AND Symptoms) = 0.12, P(Symptoms) = 0.30
    >>> conditional_probability(0.12, 0.30)
    0.4

    >>> # P(High Yield | Good Soil)
    >>> conditional_probability(0.35, 0.50)
    0.7
    """
    if not (0 <= p_a_and_b <= 1):
        raise ValueError(f"P(A∩B) must be in [0,1], got {p_a_and_b}")
    if not (0 <= p_b <= 1):
        raise ValueError(f"P(B) must be in [0,1], got {p_b}")

    if p_b == 0:
        raise ValueError("Cannot calculate P(A|B) when P(B) = 0")

    if p_a_and_b > p_b:
        raise ValueError(
            f"P(A∩B) = {p_a_and_b} cannot exceed P(B) = {p_b}"
        )

    return p_a_and_b / p_b


def bayes_theorem(p_b_given_a: float, p_a: float, p_b: float) -> float:
    """
    Calculate P(A|B) using Bayes' theorem: P(A|B) = P(B|A) × P(A) / P(B)

    Parameters
    ----------
    p_b_given_a : float
        Probability of B given A (likelihood)
    p_a : float
        Prior probability of A
    p_b : float
        Total probability of B (evidence)

    Returns
    -------
    float
        Posterior probability of A given B

    Raises
    ------
    ValueError
        If probabilities are not in [0, 1]
        If p_b is 0 (impossible event)

    Examples
    --------
    >>> # Disease diagnosis
    >>> # P(Positive Test | Disease) = 0.90
    >>> # P(Disease) = 0.05 (base rate)
    >>> # P(Positive Test) = 0.14 (calculated via law of total probability)
    >>> bayes_theorem(0.90, 0.05, 0.14)
    0.321...

    >>> # Crop variety identification
    >>> # P(High Yield | Variety A) = 0.80
    >>> # P(Variety A) = 0.30
    >>> # P(High Yield) = 0.65
    >>> bayes_theorem(0.80, 0.30, 0.65)
    0.369...
    """
    if not (0 <= p_b_given_a <= 1):
        raise ValueError(f"P(B|A) must be in [0,1], got {p_b_given_a}")
    if not (0 <= p_a <= 1):
        raise ValueError(f"P(A) must be in [0,1], got {p_a}")
    if not (0 <= p_b <= 1):
        raise ValueError(f"P(B) must be in [0,1], got {p_b}")

    if p_b == 0:
        raise ValueError("Cannot apply Bayes' theorem when P(B) = 0")

    numerator = p_b_given_a * p_a

    # Check if result would exceed 1
    result = numerator / p_b
    if result > 1.0001:  # Allow small numerical errors
        raise ValueError(
            f"Invalid probabilities: P(A|B) = {result:.4f} exceeds 1.0"
        )

    return min(result, 1.0)  # Cap at 1.0 for numerical stability


def law_of_total_probability(partitions: List[float],
                             conditional_probs: List[float]) -> float:
    """
    Calculate P(A) = Σ P(A|Bᵢ) × P(Bᵢ) where Bᵢ partition the sample space.

    Parameters
    ----------
    partitions : list of float
        Probabilities of each partition [P(B₁), P(B₂), ...]
        Must sum to 1.0 (complete partition)
    conditional_probs : list of float
        Conditional probabilities [P(A|B₁), P(A|B₂), ...]

    Returns
    -------
    float
        Total probability of A

    Raises
    ------
    ValueError
        If lists have different lengths
        If probabilities are not in [0, 1]
        If partitions don't sum to 1.0

    Examples
    --------
    >>> # Overall high yield probability across soil types
    >>> # Soil distribution: 30% clay, 50% loam, 20% sandy
    >>> # Yield rates: clay=60%, loam=80%, sandy=50%
    >>> partitions = [0.30, 0.50, 0.20]
    >>> conditional_probs = [0.60, 0.80, 0.50]
    >>> law_of_total_probability(partitions, conditional_probs)
    0.68

    >>> # Disease probability across seasons
    >>> # Early (60%), Late (40%)
    >>> # Disease rates: early=8%, late=20%
    >>> law_of_total_probability([0.60, 0.40], [0.08, 0.20])
    0.128
    """
    if len(partitions) != len(conditional_probs):
        raise ValueError(
            f"Partitions ({len(partitions)}) and conditional probabilities "
            f"({len(conditional_probs)}) must have same length"
        )

    # Validate all probabilities
    for i, p in enumerate(partitions):
        if not (0 <= p <= 1):
            raise ValueError(f"Partition probability {i} must be in [0,1], got {p}")

    for i, p in enumerate(conditional_probs):
        if not (0 <= p <= 1):
            raise ValueError(f"Conditional probability {i} must be in [0,1], got {p}")

    # Check if partitions sum to 1 (with tolerance for floating point)
    partition_sum = sum(partitions)
    if not np.isclose(partition_sum, 1.0, atol=1e-6):
        raise ValueError(
            f"Partitions must sum to 1.0, got {partition_sum:.6f}"
        )

    # Calculate total probability
    total_prob = sum(p_bi * p_a_given_bi
                    for p_bi, p_a_given_bi in zip(partitions, conditional_probs))

    return total_prob


def test_independence(p_a: float, p_b: float, p_a_and_b: float,
                     tolerance: float = 1e-6) -> bool:
    """
    Test if two events are independent.

    Events A and B are independent if: P(A∩B) = P(A) × P(B)

    Parameters
    ----------
    p_a : float
        Probability of event A
    p_b : float
        Probability of event B
    p_a_and_b : float
        Probability of both A and B
    tolerance : float, optional
        Tolerance for floating point comparison (default 1e-6)

    Returns
    -------
    bool
        True if events are independent, False if dependent

    Raises
    ------
    ValueError
        If probabilities are not in [0, 1]

    Examples
    --------
    >>> # Independent: Frost in two separate fields
    >>> test_independence(0.15, 0.15, 0.0225)
    True

    >>> # Dependent: Disease and symptoms
    >>> test_independence(0.10, 0.25, 0.08)
    False

    >>> # Nearly independent (within tolerance)
    >>> test_independence(0.30, 0.40, 0.1201, tolerance=0.01)
    True
    """
    if not (0 <= p_a <= 1):
        raise ValueError(f"P(A) must be in [0,1], got {p_a}")
    if not (0 <= p_b <= 1):
        raise ValueError(f"P(B) must be in [0,1], got {p_b}")
    if not (0 <= p_a_and_b <= 1):
        raise ValueError(f"P(A∩B) must be in [0,1], got {p_a_and_b}")

    expected_if_independent = p_a * p_b
    difference = abs(p_a_and_b - expected_if_independent)

    return difference < tolerance


def calculate_expected_value(outcomes: List[float],
                             probabilities: List[float]) -> float:
    """
    Calculate expected value: E[X] = Σ xᵢ × P(xᵢ)

    Parameters
    ----------
    outcomes : list of float
        Possible outcome values
    probabilities : list of float
        Probability of each outcome

    Returns
    -------
    float
        Expected value

    Raises
    ------
    ValueError
        If lists have different lengths
        If probabilities don't sum to 1.0
        If any probability is not in [0, 1]

    Examples
    --------
    >>> # Expected crop yield
    >>> # Outcomes: 50, 75, 100 bushels/acre
    >>> # Probabilities: 20%, 50%, 30%
    >>> outcomes = [50, 75, 100]
    >>> probabilities = [0.20, 0.50, 0.30]
    >>> calculate_expected_value(outcomes, probabilities)
    75.0

    >>> # Expected profit from farming decision
    >>> outcomes = [-100, 200, 500]  # Dollars
    >>> probabilities = [0.10, 0.60, 0.30]
    >>> calculate_expected_value(outcomes, probabilities)
    260.0
    """
    if len(outcomes) != len(probabilities):
        raise ValueError(
            f"Outcomes ({len(outcomes)}) and probabilities ({len(probabilities)}) "
            f"must have same length"
        )

    # Validate probabilities
    for i, p in enumerate(probabilities):
        if not (0 <= p <= 1):
            raise ValueError(f"Probability {i} must be in [0,1], got {p}")

    prob_sum = sum(probabilities)
    if not np.isclose(prob_sum, 1.0, atol=1e-6):
        raise ValueError(f"Probabilities must sum to 1.0, got {prob_sum:.6f}")

    # Calculate expected value
    expected_value = sum(x * p for x, p in zip(outcomes, probabilities))

    return expected_value


# Additional utility functions

def normalize_probabilities(values: List[float]) -> List[float]:
    """
    Normalize a list of values to sum to 1.0 (convert to probabilities).

    Parameters
    ----------
    values : list of float
        Non-negative values to normalize

    Returns
    -------
    list of float
        Normalized probabilities

    Raises
    ------
    ValueError
        If any value is negative
        If sum of values is 0

    Examples
    --------
    >>> # Convert counts to probabilities
    >>> normalize_probabilities([10, 20, 30, 40])
    [0.1, 0.2, 0.3, 0.4]

    >>> # Normalize historical frequencies
    >>> normalize_probabilities([45, 30, 20, 5])
    [0.45, 0.3, 0.2, 0.05]
    """
    if any(v < 0 for v in values):
        raise ValueError("All values must be non-negative")

    total = sum(values)
    if total == 0:
        raise ValueError("Cannot normalize: sum of values is 0")

    return [v / total for v in values]


def combine_probabilities_or(probs: List[float]) -> float:
    """
    Calculate P(A₁ OR A₂ OR ... OR Aₙ) for independent events.

    Uses complement rule: P(at least one) = 1 - P(none)

    Parameters
    ----------
    probs : list of float
        Probabilities of independent events

    Returns
    -------
    float
        Probability that at least one event occurs

    Examples
    --------
    >>> # Probability at least one seed germinates
    >>> # Each seed: 90% germination rate
    >>> combine_probabilities_or([0.90, 0.90, 0.90])
    0.999

    >>> # Probability of at least one weather problem
    >>> combine_probabilities_or([0.20, 0.15, 0.10])  # Frost, drought, flood
    0.388
    """
    for i, p in enumerate(probs):
        if not (0 <= p <= 1):
            raise ValueError(f"Probability {i} must be in [0,1], got {p}")

    # P(at least one) = 1 - P(none)
    p_none = np.prod([1 - p for p in probs])

    return 1 - p_none


if __name__ == "__main__":
    # Run simple tests if module is executed directly
    print("Testing probability_functions module...\n")

    # Test basic probability
    print("1. Basic Probability:")
    print(f"   P(germination) with 85/100 seeds: {calculate_probability(85, 100)}")

    # Test addition rule
    print("\n2. Addition Rule:")
    print(f"   P(Disease OR Pests): {addition_rule(0.25, 0.30, 0.10)}")

    # Test multiplication rule
    print("\n3. Multiplication Rule:")
    print(f"   P(Frost in both fields): {multiplication_rule(0.15, 0.15)}")

    # Test complement
    print("\n4. Complement Rule:")
    print(f"   P(Success) given 15% failure: {complement_probability(0.15)}")

    # Test conditional probability
    print("\n5. Conditional Probability:")
    print(f"   P(Disease|Symptoms): {conditional_probability(0.12, 0.30)}")

    # Test Bayes' theorem
    print("\n6. Bayes' Theorem:")
    print(f"   P(Disease|Positive Test): {bayes_theorem(0.90, 0.05, 0.14):.3f}")

    # Test law of total probability
    print("\n7. Law of Total Probability:")
    result = law_of_total_probability([0.30, 0.50, 0.20], [0.60, 0.80, 0.50])
    print(f"   Overall yield probability: {result}")

    # Test independence
    print("\n8. Independence Test:")
    print(f"   Frost events independent? {test_independence(0.15, 0.15, 0.0225)}")

    # Test expected value
    print("\n9. Expected Value:")
    ev = calculate_expected_value([50, 75, 100], [0.20, 0.50, 0.30])
    print(f"   Expected crop yield: {ev} bushels/acre")

    print("\n✓ All tests completed successfully!")
