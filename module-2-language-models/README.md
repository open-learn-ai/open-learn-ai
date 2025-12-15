# Module 2: Language Models

**Time**: ~3 weeks | **Prerequisites**: Module 1 | **Outcome**: Build GPT from scratch

---

## What You'll Build

By the end of this module, you will:
1. Understand how language models work at every level
2. Build progressively more sophisticated models (bigram → MLP → Transformer)
3. Train models that generate coherent text
4. Implement the full Transformer architecture from scratch

---

## The Journey

We start simple and add complexity only when needed:

```
Bigram → MLP → RNN (concept) → Attention → Transformer → GPT
```

Each step teaches you why the next innovation was necessary.

---

## Lessons

### Part A: Foundations (makemore)

| # | Lesson | Time | What You'll Build |
|---|--------|------|-------------------|
| 1 | Bigram Language Model | 1.5 hr | Predict next character from counts |
| 2 | Neural Network Approach | 1.5 hr | Same task, but learned |
| 3 | MLP Language Model | 2 hr | Use context window |
| 4 | Batch Normalization | 1 hr | Training stability |
| 5 | Wavenet Architecture | 1.5 hr | Hierarchical processing |

**Video Source**: [Karpathy - makemore series](https://youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)

### Part B: Transformers (nanoGPT)

| # | Lesson | Time | What You'll Build |
|---|--------|------|-------------------|
| 6 | Self-Attention | 2 hr | The core mechanism |
| 7 | Multi-Head Attention | 1.5 hr | Parallel attention heads |
| 8 | Transformer Block | 1.5 hr | Attention + feedforward |
| 9 | Full GPT | 2 hr | Stack it all together |
| 10 | Training GPT | 2 hr | Generate Shakespeare |

**Video Source**: [Karpathy - Let's Build GPT](https://youtube.com/watch?v=kCc8FmEb1nY)

---

## Exercises

### Part A Exercises
| Exercise | Time | Task |
|----------|------|------|
| 1 | 45 min | Build bigram model, sample names |
| 2 | 1 hr | Implement neural bigram with cross-entropy |
| 3 | 1 hr | Add context window, tune embedding size |
| 4 | 45 min | Add batch norm, compare training curves |

### Part B Exercises
| Exercise | Time | Task |
|----------|------|------|
| 5 | 1.5 hr | Implement single-head attention |
| 6 | 1 hr | Extend to multi-head |
| 7 | 1.5 hr | Build full transformer block |
| 8 | 2 hr | Train on Shakespeare, generate text |

---

## Capstone

**Train a language model on data you care about.**

Ideas:
- Song lyrics → generate new songs in an artist's style
- Code → generate code snippets
- Recipes → generate new recipes
- Game dialogue → generate NPC conversations
- Your own writing → generate text in your style

**Requirements:**
- Collect and preprocess a dataset (1MB+ of text)
- Train a character-level or small token-level model
- Generate samples and evaluate quality
- Experiment with hyperparameters, document what works
- Deploy somewhere others can try it (optional but impressive)

---

## Key Concepts

After this module, you should understand:

- **Language Model**: Probability distribution over sequences
- **Autoregressive**: Generate one token at a time, feed back into input
- **Embedding**: Dense vector representation of discrete tokens
- **Attention**: Dynamic weighting based on content similarity
- **Self-Attention**: Tokens attend to other tokens in the same sequence
- **Transformer**: Attention + feedforward + residuals + layer norm
- **Positional Encoding**: How the model knows token order

---

## Checklist

- [ ] Completed all 10 lessons
- [ ] Finished exercises 1-8
- [ ] Built and submitted capstone
- [ ] Can whiteboard the transformer architecture

**Ready for Module 3?** You should be able to:
- Implement attention from scratch
- Train a GPT on custom data
- Explain why attention beats RNNs for long sequences

→ [Module 3: Tokenization](../module-3-tokenization/README.md)
