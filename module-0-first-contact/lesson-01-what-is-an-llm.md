# Lesson 1: What is an LLM?

**Time**: 30 minutes | **Type**: Conceptual | **Video**: [Karpathy - Intro to LLMs](https://youtube.com/watch?v=zjkBMFhNj_g)

---

## The Punchline First

A large language model is **just two files**:
1. **Parameters file** - A big list of numbers (the "weights")
2. **Run file** - Code that uses those numbers to generate text

That's it. No magic servers. No mysterious cloud. Two files.

For example, Llama 2 70B:
- `parameters.bin` - 140 GB (70 billion parameters × 2 bytes each)
- `run.c` - ~500 lines of C code

You can put these on a USB drive, take them to a cabin with no internet, and have a fully functional AI that writes poetry, explains quantum physics, and helps you debug code.

---

## What's in the Parameters?

Think of the parameters as a **compressed version of the internet**.

Here's the rough process:
1. Take ~10 terabytes of internet text
2. Train a neural network to predict the next word
3. The network stores patterns in 140 GB of parameters

**Compression ratio**: ~100x (10 TB → 140 GB)

But this isn't like a zip file. It's **lossy compression**. The model doesn't memorize the internet—it learns the *patterns* and *relationships* in language.

It knows that:
- "The cat sat on the ___" → probably "mat"
- After "def fibonacci(n):" → probably Python code follows
- "The capital of France is ___" → "Paris"

All this knowledge is somehow stored in those billions of floating-point numbers.

---

## How Does It Generate Text?

The model does exactly one thing: **predict the next word**.

```
Input:  "The quick brown fox"
Output: "jumps" (97% probability)
```

To generate a whole sentence:
1. Start with your prompt
2. Predict next word
3. Add that word to the input
4. Repeat

```
"Write a poem" →
"Write a poem about" →
"Write a poem about the" →
"Write a poem about the sea" →
...
```

Each word is sampled based on probabilities. That's why you get different outputs each time—there's randomness in the sampling.

---

## The Training Process

Getting those parameters requires serious computation:

| What | Llama 2 70B |
|------|-------------|
| Training data | ~10 TB of text |
| Hardware | ~6,000 GPUs |
| Time | ~12 days |
| Cost | ~$2 million |

The model learns by trying to predict words and adjusting parameters when it's wrong. After seeing trillions of words, patterns emerge.

**Key insight**: Better prediction = more knowledge encoded

To predict "The 16th president of the United States was ___", the model must have somehow stored the fact that Lincoln was the 16th president. This knowledge emerges from the prediction objective.

---

## What We Don't Understand

Here's the weird part: **we don't really know how it works**.

We know:
- The architecture (Transformer)
- The training objective (predict next word)
- The math (attention, backpropagation)

We don't know:
- How knowledge is stored in the parameters
- Why certain prompts work better than others
- How it "reasons" (or if it does)

The model is ~100 billion parameters all interacting. We can measure that it works, but understanding *why* is an open research problem (called "interpretability" or "mechanistic interpretability").

**Analogy**: It's not like a car where we understand every part. It's more like a brain—we know it works, we can study it, but the full picture is still mysterious.

---

## Base Model vs Assistant

The raw trained model is a "base model." It's trained to predict internet text, so if you give it:

```
"What is 2+2?"
```

It might respond with:

```
"What is 2+3?
What is the capital of France?
What is..."
```

Because on the internet, questions are often followed by more questions!

To get a helpful assistant, we do **fine-tuning**:
1. Create examples of ideal Q&A conversations
2. Train the model on these examples
3. Now it responds helpfully instead of just predicting text

This is why ChatGPT answers questions instead of completing random internet text.

---

## Mental Model Summary

```
┌─────────────────────────────────────────────────────────┐
│                    TRAINING (expensive)                  │
│  Internet Text (10TB) → GPU Cluster → Parameters (140GB)│
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                    INFERENCE (cheap)                     │
│  Your Prompt → Parameters + Run Code → Generated Text   │
└─────────────────────────────────────────────────────────┘
```

- **Training**: Expensive, slow, done once
- **Inference**: Cheap, fast, done every time you use the model

---

## Key Takeaways

1. **Two files**: Parameters + code to run them
2. **Prediction machine**: All it does is predict the next word
3. **Compressed knowledge**: Internet patterns stored in weights
4. **Mysterious internals**: We don't fully understand how the knowledge is stored
5. **Base vs Assistant**: Fine-tuning transforms predictors into helpers

---

## Check Your Understanding

Before moving on, you should be able to explain:

1. What two files make up an LLM?
2. Why is training expensive but inference cheap?
3. What is the model actually doing when it generates text?
4. Why does a base model behave differently than ChatGPT?

---

## Next

→ [Lesson 2: Run Your First Model](lesson-02-run-your-first-model.md)

Let's stop talking about models and actually run one.
