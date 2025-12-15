"""
Exercise 1: Run Inference and Measure Performance

OBJECTIVE:
- Successfully run inference on a local LLM
- Measure and understand tokens/second
- Experiment with different generation parameters

TIME: ~30 minutes

PREREQUISITES:
- Ollama installed OR
- Hugging Face transformers installed

INSTRUCTIONS:
Complete each TODO section. Run the tests at the bottom to verify.
"""

import time
from typing import Optional

# =============================================================================
# PART 1: Basic Inference
# =============================================================================

def run_inference_ollama(prompt: str, model: str = "llama2") -> str:
    """
    Run inference using Ollama's API.

    TODO: Implement this function
    - Make a POST request to http://localhost:11434/api/generate
    - Send the prompt and model name
    - Return the generated text

    Hint: Use the requests library
    """
    import requests

    # YOUR CODE HERE
    # response = requests.post(...)
    # return response.json()["response"]

    raise NotImplementedError("Complete this function!")


def run_inference_transformers(prompt: str, model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0") -> str:
    """
    Run inference using Hugging Face Transformers.

    TODO: Implement this function
    - Load the tokenizer and model
    - Tokenize the prompt
    - Generate output tokens
    - Decode and return the text

    Hint: See lesson-02 for example code
    """
    # YOUR CODE HERE
    raise NotImplementedError("Complete this function!")


# =============================================================================
# PART 2: Measure Performance
# =============================================================================

def measure_tokens_per_second(
    generate_fn,
    prompt: str,
    max_tokens: int = 50,
    num_runs: int = 3
) -> dict:
    """
    Measure the tokens/second of a generation function.

    TODO: Implement this function
    - Call generate_fn multiple times
    - Measure the time taken
    - Count tokens generated (approximate by splitting on spaces, or use tokenizer)
    - Return average tokens/second

    Returns:
        dict with keys: 'avg_tokens_per_second', 'total_tokens', 'total_time'
    """
    # YOUR CODE HERE
    #
    # times = []
    # token_counts = []
    #
    # for _ in range(num_runs):
    #     start = time.time()
    #     output = generate_fn(prompt)
    #     elapsed = time.time() - start
    #     ...
    #
    # return {
    #     'avg_tokens_per_second': ...,
    #     'total_tokens': ...,
    #     'total_time': ...
    # }

    raise NotImplementedError("Complete this function!")


# =============================================================================
# PART 3: Experiment with Parameters
# =============================================================================

def compare_temperatures(prompt: str, temperatures: list = [0.1, 0.7, 1.0, 1.5]) -> dict:
    """
    Generate text at different temperatures and observe the difference.

    Temperature controls randomness:
    - Low (0.1): Very deterministic, repetitive
    - Medium (0.7): Balanced creativity
    - High (1.5): Very random, potentially incoherent

    TODO: Implement this function
    - Generate text at each temperature
    - Return a dict mapping temperature -> generated text

    Note: You'll need to modify your inference function to accept temperature
    """
    # YOUR CODE HERE
    raise NotImplementedError("Complete this function!")


# =============================================================================
# PART 4: Reflection Questions
# =============================================================================

"""
After completing the exercises, answer these questions in comments:

Q1: What tokens/second did you achieve? How does this compare to reading speed?
    (Humans read ~250 words/minute ≈ 4 words/second)

YOUR ANSWER:


Q2: How did temperature affect the outputs? Which temperature would you use for:
    - Writing code?
    - Creative writing?
    - Answering factual questions?

YOUR ANSWER:


Q3: What happens if you give the model a very long prompt? Does speed change?

YOUR ANSWER:

"""


# =============================================================================
# TESTS - Run these to verify your implementation
# =============================================================================

def test_inference():
    """Test that inference runs and returns non-empty string."""
    # Uncomment the one you implemented:

    # result = run_inference_ollama("Say 'hello' and nothing else.")
    # result = run_inference_transformers("Say 'hello' and nothing else.")

    # assert isinstance(result, str)
    # assert len(result) > 0
    # print("✓ Inference test passed")
    print("⚠ Uncomment test after implementing inference function")


def test_performance_measurement():
    """Test that performance measurement returns valid metrics."""
    # def dummy_generate(prompt):
    #     time.sleep(0.1)  # Simulate generation
    #     return "This is a test output with some tokens"
    #
    # metrics = measure_tokens_per_second(dummy_generate, "test", max_tokens=10, num_runs=2)
    #
    # assert 'avg_tokens_per_second' in metrics
    # assert 'total_tokens' in metrics
    # assert 'total_time' in metrics
    # assert metrics['avg_tokens_per_second'] > 0
    # print("✓ Performance measurement test passed")
    print("⚠ Uncomment test after implementing measure function")


def test_temperature_comparison():
    """Test that temperature comparison returns results for all temperatures."""
    # results = compare_temperatures("Once upon a time", temperatures=[0.1, 1.0])
    #
    # assert 0.1 in results
    # assert 1.0 in results
    # assert results[0.1] != results[1.0]  # Should be different (usually)
    # print("✓ Temperature comparison test passed")
    print("⚠ Uncomment test after implementing temperature function")


if __name__ == "__main__":
    print("Running Exercise 1 Tests...")
    print("-" * 40)
    test_inference()
    test_performance_measurement()
    test_temperature_comparison()
    print("-" * 40)
    print("Complete the TODOs and uncomment tests to verify!")
