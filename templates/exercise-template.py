"""
Exercise X: [Title]

OBJECTIVE:
- [Learning objective 1]
- [Learning objective 2]
- [Learning objective 3]

TIME: ~XX minutes

PREREQUISITES:
- [Completed lesson Y]
- [Specific knowledge required]

INSTRUCTIONS:
Complete each TODO section. Run the tests at the bottom to verify.

HINTS:
- [Hint 1 without giving away the answer]
- [Hint 2]
"""

# =============================================================================
# SETUP - Run this cell first
# =============================================================================

import numpy as np
# import other dependencies

# Any setup code, data loading, etc.


# =============================================================================
# PART 1: [Concept Name]
# =============================================================================

def function_to_implement(param1, param2):
    """
    [Clear description of what this function should do]

    Args:
        param1: [Description]
        param2: [Description]

    Returns:
        [Description of return value]

    Example:
        >>> function_to_implement(x, y)
        expected_output

    TODO: Implement this function
    - [Step 1]
    - [Step 2]
    - [Step 3]
    """
    # YOUR CODE HERE
    raise NotImplementedError("Complete this function!")


# =============================================================================
# PART 2: [Next Concept]
# =============================================================================

def another_function(data):
    """
    [Description]

    TODO: Implement this function
    """
    # YOUR CODE HERE
    raise NotImplementedError("Complete this function!")


# =============================================================================
# PART 3: Putting It Together
# =============================================================================

def main_exercise():
    """
    Combine the pieces you've built.

    TODO:
    1. [Step 1]
    2. [Step 2]
    3. [Step 3]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# REFLECTION QUESTIONS
# =============================================================================

"""
After completing the exercises, answer these questions:

Q1: [Conceptual question about what they learned]

YOUR ANSWER:


Q2: [Question connecting to broader concepts]

YOUR ANSWER:


Q3: [Question about edge cases or limitations]

YOUR ANSWER:

"""


# =============================================================================
# TESTS - Do not modify
# =============================================================================

def test_part1():
    """Test function_to_implement."""
    # Test case 1
    result = function_to_implement(input1, input2)
    expected = expected_output
    assert result == expected, f"Expected {expected}, got {result}"

    # Test case 2 (edge case)
    # ...

    print("✓ Part 1 tests passed")


def test_part2():
    """Test another_function."""
    # Test cases
    print("✓ Part 2 tests passed")


def test_integration():
    """Test that everything works together."""
    # Integration test
    print("✓ Integration test passed")


def run_all_tests():
    """Run all tests."""
    print("=" * 50)
    print("Running Exercise X Tests")
    print("=" * 50)

    try:
        test_part1()
    except NotImplementedError:
        print("⚠ Part 1 not implemented yet")
    except AssertionError as e:
        print(f"✗ Part 1 failed: {e}")

    try:
        test_part2()
    except NotImplementedError:
        print("⚠ Part 2 not implemented yet")
    except AssertionError as e:
        print(f"✗ Part 2 failed: {e}")

    try:
        test_integration()
    except NotImplementedError:
        print("⚠ Integration not implemented yet")
    except AssertionError as e:
        print(f"✗ Integration failed: {e}")

    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
