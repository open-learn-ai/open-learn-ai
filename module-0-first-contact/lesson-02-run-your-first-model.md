# Lesson 2: Run Your First Model

**Time**: 45 minutes | **Type**: Hands-On | **Outcome**: LLM running on your machine

---

## Goal

By the end of this lesson, you'll have a large language model running locally. No API keys. No cloud. Your machine, your model.

---

## Option A: Ollama (Easiest)

Ollama packages everything for you. If you just want to get running fast, start here.

### Install

**Mac**:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Linux**:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows**:
Download from [ollama.ai](https://ollama.ai)

### Run Your First Model

```bash
# Download and run Llama 2 (7B parameters, ~4GB)
ollama run llama2

# You're now chatting with an LLM!
>>> What is the capital of France?
The capital of France is Paris...
```

### Try Different Models

```bash
# Smaller, faster
ollama run phi

# Code-specialized
ollama run codellama

# More capable (needs more RAM)
ollama run llama2:13b
```

### Use from Python

```python
import requests

def chat(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt, "stream": False}
    )
    return response.json()["response"]

print(chat("Explain recursion in one sentence."))
```

---

## Option B: llama.cpp (More Control)

For understanding what's actually happening under the hood.

### Install

```bash
# Clone the repo
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

# Build (Mac/Linux)
make

# Build with GPU support (if you have NVIDIA)
make LLAMA_CUBLAS=1
```

### Download a Model

Models come in GGUF format (quantized for efficient inference).

```bash
# Download a small model (~2GB)
# Visit huggingface.co and search for GGUF models
# Example: TheBloke/Llama-2-7B-GGUF

wget https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf
```

### Run It

```bash
./main -m llama-2-7b.Q4_K_M.gguf -p "The meaning of life is" -n 100
```

**Flags**:
- `-m`: Model file
- `-p`: Prompt
- `-n`: Max tokens to generate
- `-t`: Number of threads (try your CPU core count)

### Interactive Mode

```bash
./main -m llama-2-7b.Q4_K_M.gguf --interactive-first
```

---

## Option C: Hugging Face Transformers (Most Flexible)

For when you want to inspect everything.

### Install

```bash
pip install transformers torch accelerate
```

### Run

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Generate
prompt = "What is machine learning?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### See Inside

```python
# How many parameters?
total_params = sum(p.numel() for p in model.parameters())
print(f"Parameters: {total_params:,}")  # ~1.1 billion

# What's the vocabulary size?
print(f"Vocabulary: {tokenizer.vocab_size:,} tokens")

# Inspect a layer
print(model.model.layers[0])  # First transformer layer
```

---

## Understanding What's Happening

When you run inference, here's the flow:

```
Your Text → Tokenizer → Token IDs → Model → Logits → Sample → Token ID → Detokenizer → Text
```

1. **Tokenize**: "Hello world" → [15496, 995]
2. **Embed**: Token IDs → Vectors
3. **Transform**: Vectors flow through layers
4. **Predict**: Output probabilities for next token
5. **Sample**: Pick next token (with some randomness)
6. **Repeat**: Add token, predict again

### Measure Performance

```python
import time

start = time.time()
outputs = model.generate(**inputs, max_new_tokens=100)
elapsed = time.time() - start

tokens_generated = len(outputs[0]) - len(inputs["input_ids"][0])
print(f"Speed: {tokens_generated / elapsed:.1f} tokens/second")
```

Typical speeds:
- CPU: 5-20 tokens/second
- GPU: 50-200+ tokens/second
- Apple Silicon: 30-100 tokens/second

---

## Hardware Requirements

| Model Size | RAM Needed | Good For |
|------------|------------|----------|
| 1-3B | 4GB | Learning, experiments |
| 7B | 8GB | General use |
| 13B | 16GB | Better quality |
| 30B+ | 32GB+ | Production quality |

**Don't have enough RAM?** Use quantized models:
- Q4_K_M: ~4 bits per parameter (decent quality, 1/4 the size)
- Q8_0: ~8 bits per parameter (good quality, 1/2 the size)

---

## Troubleshooting

### "Out of memory"
- Try a smaller model
- Use quantized version (Q4_K_M)
- Close other applications

### "Slow generation"
- Check you're using GPU if available
- Try llama.cpp (often faster than Python)
- Reduce context length

### "Weird outputs"
- Try different temperature (lower = more deterministic)
- Check prompt formatting
- Some models need specific templates

---

## Checkpoint

You should now have:
- [ ] A model running locally
- [ ] Generated some text
- [ ] Measured tokens/second
- [ ] Tried at least 2 different prompts

---

## Exercise

Complete [Exercise 1: Run inference and measure tokens/second](exercises/exercise-01-inference.py)

---

## Next

→ [Lesson 3: How Training Works](lesson-03-how-training-works.md)
