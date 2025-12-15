# Module 4: Training GPT-2

**Time**: ~2 weeks | **Prerequisites**: Modules 1-3 | **Outcome**: Reproduce GPT-2 124M

---

## What You'll Build

By the end of this module, you will:
1. Train a real language model from scratch (not toy-sized)
2. Match GPT-2 124M performance
3. Understand distributed training and optimization
4. Know what it takes to train production models

---

## Why This Matters

You've built toy models. Now you'll train a real one.

GPT-2 124M was cutting-edge in 2019. Today, you can reproduce it in ~1 hour for ~$10 on cloud compute. This is the bridge between "I understand the concepts" and "I can train real models."

---

## Lessons

| # | Lesson | Time | What You'll Learn |
|---|--------|------|-------------------|
| 1 | GPT-2 Architecture Deep Dive | 1.5 hr | Every layer, every parameter |
| 2 | Data Pipeline | 1.5 hr | Loading, batching, streaming |
| 3 | Optimization at Scale | 2 hr | AdamW, learning rate schedules, gradient clipping |
| 4 | Training Loop | 2 hr | Forward, backward, update, logging |
| 5 | Distributed Training | 1.5 hr | Data parallel, gradient accumulation |
| 6 | Evaluation | 1 hr | Validation loss, perplexity, generation quality |
| 7 | The Full Run | 2 hr | Put it together, train to convergence |

**Video Source**: [Karpathy - Reproducing GPT-2](https://youtube.com/watch?v=l8pRSuU81PU)

---

## Exercises

| Exercise | Time | Task |
|----------|------|------|
| 1 | 1 hr | Load GPT-2 weights from HuggingFace, inspect architecture |
| 2 | 1.5 hr | Implement GPT-2 architecture matching HF exactly |
| 3 | 1 hr | Build efficient data loader with streaming |
| 4 | 1.5 hr | Implement training loop with proper optimizer |
| 5 | 2 hr | Train on small dataset, verify learning |
| 6 | 1 hr | Add logging, checkpointing, evaluation |
| 7 | 2+ hr | Full training run, match GPT-2 validation loss |

---

## Compute Options

You'll need GPU access for this module. Options:

| Option | Cost | Notes |
|--------|------|-------|
| **Google Colab Pro** | $10/month | Good for experiments, limited for full runs |
| **Lambda Labs** | ~$1/hr | Cheap GPUs, pay per use |
| **RunPod** | ~$0.50/hr | Very cheap, community GPUs |
| **Vast.ai** | ~$0.30/hr | Cheapest, variable quality |
| **Your own GPU** | Free | RTX 3090/4090 works great |

Full GPT-2 124M training: ~1 hour on A100, ~$10

---

## Capstone

**Train GPT-2 on custom data and analyze the results.**

Requirements:
- Reproduce GPT-2 124M baseline (match validation loss)
- Train on your own dataset (or continue pre-training on specific domain)
- Document: training curves, compute used, samples generated
- Analysis: What did it learn? What does it struggle with?

Bonus:
- Try different hyperparameters, document what matters
- Implement a training optimization (mixed precision, gradient checkpointing)
- Compare your model to the original GPT-2 qualitatively

---

## Key Concepts

- **Pre-training**: Training on massive text data for general capability
- **Validation Loss**: How well the model predicts held-out data
- **Perplexity**: Exponential of loss, interpretable as "confusion"
- **Learning Rate Schedule**: Warmup, cosine decay
- **Gradient Accumulation**: Simulate large batches with limited memory
- **Mixed Precision**: FP16/BF16 training for speed

---

## What You'll Learn About Scale

| Parameter | GPT-2 124M | What It Teaches |
|-----------|------------|-----------------|
| Parameters | 124M | Small by 2025 standards, still useful |
| Layers | 12 | Depth matters |
| Heads | 12 | Multi-head attention scales |
| Embedding | 768 | Wider = more capacity |
| Context | 1024 | Longer = more memory, slower |
| Training tokens | ~10B | Data matters enormously |

---

## Checklist

- [ ] Completed all 7 lessons
- [ ] Finished exercises 1-7
- [ ] Successfully trained to match GPT-2 124M
- [ ] Built and submitted capstone
- [ ] Can explain the full training pipeline

**Ready for Module 5?** You should be able to:
- Train GPT-scale models from scratch
- Debug training runs (loss curves, gradient issues)
- Make informed decisions about hyperparameters

→ [Module 5: Modern Stack](../module-5-modern-stack/README.md)
