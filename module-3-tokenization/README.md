# Module 3: Tokenization

**Time**: ~1 week | **Prerequisites**: Module 2 | **Outcome**: Build BPE tokenizer from scratch

---

## What You'll Build

By the end of this module, you will:
1. Understand why tokenization is critical (and problematic)
2. Implement Byte Pair Encoding (BPE) from scratch
3. Build a tokenizer compatible with GPT-2
4. Debug common tokenization issues

---

## Why This Matters

Tokenization is Andrej's "least favorite part" of LLMs—and that's exactly why you need to understand it.

Many mysterious LLM behaviors trace back to tokenization:
- Why LLMs struggle with spelling
- Why simple math sometimes fails
- Why some languages work better than others
- Why "SolidGoldMagikarp" breaks ChatGPT

When you build the tokenizer yourself, these mysteries become obvious.

---

## Lessons

| # | Lesson | Time | What You'll Learn |
|---|--------|------|-------------------|
| 1 | Why Tokenization? | 30 min | Characters vs tokens, vocabulary tradeoffs |
| 2 | Byte Pair Encoding | 1.5 hr | The algorithm, step by step |
| 3 | Building a Tokenizer | 2 hr | Encode, decode, train on data |
| 4 | Special Tokens | 45 min | BOS, EOS, PAD, and why they matter |
| 5 | Tokenization Gotchas | 1 hr | Edge cases, debugging, weird behaviors |

**Video Source**: [Karpathy - Tokenization](https://youtube.com/watch?v=zduSFxRajkE)

---

## Exercises

| Exercise | Time | Task |
|----------|------|------|
| 1 | 1 hr | Implement BPE training from scratch |
| 2 | 45 min | Implement encode() and decode() |
| 3 | 30 min | Compare your tokenizer to tiktoken |
| 4 | 45 min | Analyze tokenization of different languages |
| 5 | 1 hr | Find and explain 3 "weird" tokenization behaviors |

---

## Capstone

**Analyze tokenization's impact on model behavior.**

Options:
- Compare tokenization across languages (efficiency, fairness)
- Build a visualization tool for tokenization
- Train models with different vocab sizes, measure impact
- Document tokenization "bugs" in popular models

**Requirements:**
- Original analysis or tool
- Clear documentation of findings
- Visualizations that explain the insights

---

## Key Concepts

- **Token**: The atomic unit the model sees (not characters, not words)
- **Vocabulary**: The set of all possible tokens
- **BPE**: Algorithm that iteratively merges frequent byte pairs
- **Subword**: Tokens that are parts of words
- **Encoding**: Text → token IDs
- **Decoding**: Token IDs → text

---

## Tokenization Mysteries Explained

After this module, you'll understand why:

| Behavior | Explanation |
|----------|-------------|
| LLMs can't count letters | "hello" might be 1-2 tokens, model never sees individual letters |
| Math sometimes fails | "127+677" tokenizes differently than "127+678" |
| Non-English is worse | Trained mostly on English, other languages get inefficient tokenization |
| Trailing whitespace matters | " hello" and "hello" are different tokens |
| Code has issues | Indentation tokenizes inconsistently |

---

## Checklist

- [ ] Completed all 5 lessons
- [ ] Finished exercises 1-5
- [ ] Built and submitted capstone
- [ ] Can explain BPE to someone else

**Ready for Module 4?** You should be able to:
- Implement BPE tokenizer from scratch
- Predict how text will tokenize
- Debug tokenization-related model issues

→ [Module 4: Training GPT-2](../module-4-training-gpt2/README.md)
