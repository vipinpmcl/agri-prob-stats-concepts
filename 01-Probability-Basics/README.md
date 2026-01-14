# Probability Basics

Learn the fundamental concepts of probability theory, essential for understanding uncertainty in agricultural decision-making and machine learning.

## Overview

Probability theory provides the mathematical framework for reasoning about uncertainty. In agriculture, we constantly deal with uncertain outcomes:
- Will it rain tomorrow?
- What's the chance of pest infestation?
- How likely is crop disease given these symptoms?
- What's the probability of achieving target yield?

This module builds your intuition for probability while keeping agricultural applications central.

## Learning Objectives

By completing this module, you will:

1. Understand sample spaces, events, and outcomes in agricultural contexts
2. Master the three axioms of probability
3. Calculate probabilities using addition and multiplication rules
4. Apply conditional probability and Bayes' theorem
5. Distinguish between independent and dependent events
6. Use probability for agricultural decision-making
7. Implement probability calculations from scratch and with SciPy

## Prerequisites

- Basic Python programming
- Arithmetic and basic algebra
- Understanding of sets (helpful but not required)
- Jupyter notebooks familiarity

## Module Structure

This module is organized into 4 progressive sections:

### 1. Fundamentals (`1_fundamentals/`)

Build intuition for probability concepts with visual, agricultural examples.

**Notebooks:**
- `01_sample_spaces_events.ipynb` - Understanding outcomes and events ✅ Ready
- `02_probability_axioms.ipynb` - The three fundamental rules ✅ Ready
- `03_conditional_probability.ipynb` - Bayes' theorem and applications ✅ Ready

**Difficulty**: Beginner
**Focus**: Intuition and visualization over proofs

### 2. From Scratch (`2_from_scratch/`)

Implement probability functions using Python to solidify understanding.

**Files:**
- `probability_functions.py` - Core probability calculators ✅ Ready
- `test_probability.ipynb` - Validation and testing ✅ Ready

**Difficulty**: Beginner to Intermediate
**Focus**: Understanding through implementation

### 3. With SciPy (`3_with_scipy/`)

Learn to use professional statistical libraries.

**Notebooks:**
- `scipy_probability.ipynb` - Using scipy.stats ✅ Ready
- `statistical_functions.ipynb` - Built-in probability tools ✅ Ready

**Difficulty**: Beginner
**Focus**: Industry-standard tools

### 4. Agricultural Application (`4_agricultural_application/`)

Apply probability concepts to real agricultural scenarios.

**Notebooks:**
- `crop_disease_probability.ipynb` - Disease diagnosis with Bayes' theorem ✅ Ready
- `weather_prediction.ipynb` - Weather event probabilities ✅ Ready
- `integrated_farming_decisions.ipynb` - Comprehensive case study ✅ Ready

**Difficulty**: Intermediate
**Focus**: Real-world problem solving

## Getting Started

### Recommended Learning Path

Work through sections sequentially:

1. Start with `1_fundamentals/01_sample_spaces_events.ipynb`
2. Complete all fundamentals notebooks
3. Implement from-scratch functions
4. Learn SciPy tools
5. Apply to agricultural problems

### Quick Start

If you're comfortable with basic probability:
1. Skim `1_fundamentals/`
2. Jump to `4_agricultural_application/`
3. Refer back to earlier sections as needed

## Key Concepts Covered

### Probability Foundations
- Sample spaces (all possible outcomes)
- Events (subsets of outcomes)
- Probability axioms (non-negativity, normalization, additivity)
- Addition rule (P(A or B))
- Multiplication rule (P(A and B))

### Conditional Probability
- P(A|B) - probability of A given B
- Bayes' theorem
- Independence vs dependence
- Law of total probability

### Agricultural Applications
- Weather event probabilities
- Crop disease diagnosis
- Yield prediction under uncertainty
- Risk assessment for farming decisions

## Why Probability Matters for ML

Machine learning models:
- **Predict probabilities**: "80% chance of disease"
- **Handle uncertainty**: Quantify confidence in predictions
- **Learn from data**: Use probabilistic frameworks (Bayesian methods)
- **Make decisions**: Choose actions based on expected outcomes

Understanding probability is fundamental to:
- Interpreting model outputs
- Choosing appropriate algorithms
- Evaluating prediction reliability
- Explaining results to stakeholders

## Agricultural Context

### Sample Problems You'll Solve

1. **Disease Diagnosis**: If 5% of crops have a disease, and a test is 90% accurate, what's the actual probability a crop with a positive test is diseased?

2. **Weather Forecasting**: Given historical data, what's the probability of rain during planting season?

3. **Yield Prediction**: What's the probability of achieving target yield given current soil and weather conditions?

4. **Risk Assessment**: Should you invest in irrigation given probability of drought?

## Expected Outcomes

### Knowledge
- Deep understanding of probability fundamentals
- Intuition for when events are independent
- Ability to apply Bayes' theorem correctly
- Understanding of probability in ML contexts

### Skills
- Calculate probabilities for real events
- Implement probability functions
- Use SciPy for statistical computing
- Make data-driven agricultural decisions
- Communicate uncertainty effectively

## Tips for Success

1. **Work Through Examples**: Don't just read - run every code cell
2. **Visualize**: Study the probability diagrams carefully
3. **Connect to Reality**: Think about how each concept applies to farming
4. **Practice**: Try the exercises at the end of each notebook
5. **Ask "Why"**: Understand the reasoning, not just formulas

## Common Pitfalls

- **Confusing P(A|B) with P(B|A)**: These are very different!
- **Assuming independence**: Most agricultural events are dependent
- **Ignoring base rates**: Critical for Bayes' theorem
- **Misinterpreting percentages**: 90% accuracy doesn't mean what you think

## Assessment

Test your understanding:

- [ ] Can you explain probability in simple terms to a farmer?
- [ ] Can you calculate conditional probabilities correctly?
- [ ] Do you understand when to use Bayes' theorem?
- [ ] Can you implement probability calculations in Python?
- [ ] Can you identify independent vs dependent events?
- [ ] Can you apply probability to agricultural decisions?

## Next Steps

After completing this module:

1. **Review**: Solidify understanding of challenging concepts
2. **Practice**: Apply probability to new agricultural datasets
3. **Extend**: Explore Monte Carlo simulation
4. **Connect**: See how probability links to Topic 02 (Random Variables)
5. **Apply**: Use probability in your own agricultural projects

## Resources

### Within This Repository
- [Root README](../README.md) - Repository overview
- [Dataset Documentation](../datasets/README.md) - Data sources

### External Resources
- [SciPy Statistics](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Khan Academy Probability](https://www.khanacademy.org/math/statistics-probability)
- [Bayesian Methods for Hackers](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)

## Status

**Current**: ✅ Complete

- ✅ Module structure created
- ✅ All fundamentals notebooks complete (3/3)
- ✅ From-scratch implementation complete (2/2)
- ✅ SciPy notebooks complete (2/2)
- ✅ Agricultural applications complete (3/3)

**Total**: 9 notebooks + 1 Python module ready for learning!

---

**Ready to start?** Open `1_fundamentals/01_sample_spaces_events.ipynb` and begin your probability journey!
