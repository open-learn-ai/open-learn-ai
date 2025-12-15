"""
Exercise 1: SOLUTIONS

Only look at this after attempting the exercise yourself!
"""

import time
import requests
from typing import Optional

# =============================================================================
# PART 1: Basic Inference - SOLUTIONS
# =============================================================================

def run_inference_ollama(prompt: str, model: str = "llama2", temperature: float = 0.7) -> str:
    """Run inference using Ollama's API."""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": 100  # max tokens
            }
        }
    )
    response.raise_for_status()
    return response.json()["response"]


def run_inference_transformers(
    prompt: str,
    model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    temperature: float = 0.7,
    max_new_tokens: int = 100
) -> str:
    """Run inference using Hugging Face Transformers."""
    from transformers import AutoModelForCausalLM, AutoTokenizer
    import torch

    # Load model and tokenizer (in practice, cache these!)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None
    )

    # Tokenize
    inputs = tokenizer(prompt, return_tensors="pt")
    if torch.cuda.is_available():
        inputs = inputs.to("cuda")

    # Generate
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            do_sample=temperature > 0,
            pad_token_id=tokenizer.eos_token_id
        )

    # Decode (only the new tokens)
    generated = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    return generated


# =============================================================================
# PART 2: Measure Performance - SOLUTION
# =============================================================================

def measure_tokens_per_second(
    generate_fn,
    prompt: str,
    max_tokens: int = 50,
    num_runs: int = 3
) -> dict:
    """Measure the tokens/second of a generation function."""
    times = []
    token_counts = []

    for i in range(num_runs):
        start = time.time()
        output = generate_fn(prompt)
        elapsed = time.time() - start

        # Approximate token count (rough: ~0.75 tokens per word for English)
        # More accurate: use tokenizer
        word_count = len(output.split())
        approx_tokens = int(word_count * 1.3)  # Rough approximation

        times.append(elapsed)
        token_counts.append(approx_tokens)

    total_time = sum(times)
    total_tokens = sum(token_counts)

    return {
        'avg_tokens_per_second': total_tokens / total_time if total_time > 0 else 0,
        'total_tokens': total_tokens,
        'total_time': total_time,
        'runs': num_runs,
        'avg_time_per_run': total_time / num_runs
    }


# =============================================================================
# PART 3: Experiment with Parameters - SOLUTION
# =============================================================================

def compare_temperatures(
    prompt: str,
    temperatures: list = [0.1, 0.7, 1.0, 1.5],
    use_ollama: bool = True
) -> dict:
    """Generate text at different temperatures and observe the difference."""
    results = {}

    for temp in temperatures:
        if use_ollama:
            output = run_inference_ollama(prompt, temperature=temp)
        else:
            output = run_inference_transformers(prompt, temperature=temp)

        results[temp] = output
        print(f"\n--- Temperature {temp} ---")
        print(output[:200] + "..." if len(output) > 200 else output)

    return results


# =============================================================================
# EXAMPLE ANSWERS TO REFLECTION QUESTIONS
# =============================================================================

"""
Q1: What tokens/second did you achieve? How does this compare to reading speed?

EXAMPLE ANSWER:
I achieved ~15 tokens/second on CPU with a 7B model, and ~80 tokens/second
on my RTX 3080 GPU. Humans read at about 4 words/second (250 wpm), and since
tokens are roughly 0.75 words, that's about 5 tokens/second. So even on CPU,
the model generates faster than we can read!


Q2: How did temperature affect the outputs?

EXAMPLE ANSWER:
- Temperature 0.1: Very repetitive, almost deterministic. Used the same phrases.
- Temperature 0.7: Good balance, creative but coherent. Best for most tasks.
- Temperature 1.0: More varied, occasionally surprising word choices.
- Temperature 1.5: Sometimes incoherent, random tangents.

I would use:
- Code: 0.1-0.3 (want deterministic, correct syntax)
- Creative writing: 0.7-1.0 (want variety)
- Factual questions: 0.1-0.5 (want accuracy)


Q3: What happens with very long prompts?

EXAMPLE ANSWER:
With longer prompts, the "time to first token" increases because the model
must process more input. However, the generation speed (tokens/second during
output) stays roughly the same. Very long prompts can also hit context limits
and cause errors or truncation.
"""


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Exercise 1 Solutions Demo")
    print("=" * 60)

    # Test basic inference
    print("\n1. Testing basic inference...")
    try:
        result = run_inference_ollama("What is 2+2? Answer in one word.")
        print(f"   Ollama result: {result.strip()}")
    except Exception as e:
        print(f"   Ollama not available: {e}")
        print("   Trying transformers...")
        try:
            result = run_inference_transformers("What is 2+2? Answer in one word.")
            print(f"   Transformers result: {result.strip()}")
        except Exception as e2:
            print(f"   Transformers also failed: {e2}")

    # Test performance measurement
    print("\n2. Measuring performance...")
    try:
        metrics = measure_tokens_per_second(
            lambda p: run_inference_ollama(p),
            "Write a short poem about coding.",
            num_runs=2
        )
        print(f"   Avg tokens/second: {metrics['avg_tokens_per_second']:.1f}")
        print(f"   Total tokens: {metrics['total_tokens']}")
        print(f"   Total time: {metrics['total_time']:.2f}s")
    except Exception as e:
        print(f"   Could not measure: {e}")

    # Test temperature comparison
    print("\n3. Comparing temperatures...")
    try:
        results = compare_temperatures(
            "The secret to happiness is",
            temperatures=[0.1, 1.0]
        )
    except Exception as e:
        print(f"   Could not compare: {e}")

    print("\n" + "=" * 60)
    print("Demo complete!")
