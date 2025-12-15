# Module 5: Modern Stack

**Time**: ~3 weeks | **Prerequisites**: Modules 0-4 | **Outcome**: Build production AI applications

---

## What You'll Build

By the end of this module, you will:
1. Fine-tune open models for specific tasks
2. Build RAG systems from scratch
3. Implement tool use and agents
4. Deploy models for real-world use

---

## Why This Matters

You understand how LLMs work. Now learn how to use them.

This module bridges "I can train models" to "I can ship AI products." These are the skills companies actually hire for.

---

## Lessons

### Part A: Fine-Tuning

| # | Lesson | Time | What You'll Learn |
|---|--------|------|-------------------|
| 1 | Fine-Tuning Fundamentals | 1.5 hr | When and why to fine-tune |
| 2 | LoRA and QLoRA | 2 hr | Parameter-efficient fine-tuning |
| 3 | Dataset Preparation | 1.5 hr | Formatting, quality, quantity |
| 4 | Training and Evaluation | 2 hr | The full fine-tuning pipeline |

### Part B: RAG (Retrieval-Augmented Generation)

| # | Lesson | Time | What You'll Learn |
|---|--------|------|-------------------|
| 5 | Embeddings Deep Dive | 1.5 hr | What embeddings capture, how to use them |
| 6 | Vector Stores | 1.5 hr | Storing and searching embeddings |
| 7 | Chunking Strategies | 1 hr | How to split documents effectively |
| 8 | RAG Pipeline | 2 hr | Retrieval → Augmentation → Generation |

### Part C: Agents and Deployment

| # | Lesson | Time | What You'll Learn |
|---|--------|------|-------------------|
| 9 | Tool Use | 1.5 hr | How LLMs use tools, function calling |
| 10 | Agent Architectures | 2 hr | ReAct, planning, memory |
| 11 | Deployment | 2 hr | Serving models, optimization, monitoring |
| 12 | Production Concerns | 1.5 hr | Cost, latency, safety, evaluation |

---

## Exercises

### Part A: Fine-Tuning
| Exercise | Time | Task |
|----------|------|------|
| 1 | 2 hr | Fine-tune Llama on custom task with LoRA |
| 2 | 1.5 hr | Compare full fine-tune vs LoRA vs QLoRA |
| 3 | 1 hr | Evaluate fine-tuned model on held-out data |

### Part B: RAG
| Exercise | Time | Task |
|----------|------|------|
| 4 | 1.5 hr | Implement embedding search from scratch |
| 5 | 1.5 hr | Build simple vector store (no frameworks) |
| 6 | 2 hr | Full RAG pipeline on your documents |

### Part C: Agents
| Exercise | Time | Task |
|----------|------|------|
| 7 | 1.5 hr | Implement tool calling |
| 8 | 2 hr | Build a simple ReAct agent |
| 9 | 1.5 hr | Deploy model with API endpoint |

---

## Capstone

**Build and deploy an AI application that solves a real problem.**

This is the big one. This capstone should be portfolio-worthy.

**Requirements:**
- Solves a real problem (not a toy demo)
- Uses techniques from this module (fine-tuning, RAG, agents, or deployment)
- Deployed and accessible (web app, API, CLI tool)
- Documented: what it does, how to use it, technical decisions
- Evaluated: metrics on performance, user feedback if possible

**Example Projects:**
- Research assistant that answers questions about a corpus of papers
- Code assistant fine-tuned on your company's codebase
- Customer support agent that uses RAG over documentation
- Personal knowledge base with semantic search
- Domain-specific chatbot (legal, medical, technical)

**What Makes a Great Capstone:**
- Clear problem statement
- Technical depth (not just API wrapper)
- Polish (works reliably, handles edge cases)
- Documentation (others can understand and use it)
- Deployed (accessible to real users)

---

## Key Concepts

### Fine-Tuning
- **Full Fine-Tuning**: Update all parameters (expensive, risky)
- **LoRA**: Low-rank adaptation, train small matrices
- **QLoRA**: Quantized LoRA, even more efficient
- **Catastrophic Forgetting**: Losing general capability when fine-tuning

### RAG
- **Embedding**: Dense vector representation of text
- **Semantic Search**: Find relevant documents by meaning
- **Chunking**: Splitting documents for retrieval
- **Context Window Management**: Fitting retrieved info into prompt

### Agents
- **Tool Use**: LLM generates structured calls to external functions
- **ReAct**: Reasoning + Acting pattern
- **Planning**: Breaking tasks into steps
- **Memory**: Maintaining state across interactions

---

## No Frameworks Challenge

For maximum learning, try building WITHOUT LangChain/LlamaIndex first.

Why?
- Understand what's actually happening
- Avoid abstraction leaks
- Debug more effectively
- Build exactly what you need

After building from scratch, you'll appreciate what frameworks do (and don't do).

---

## Checklist

- [ ] Completed all 12 lessons
- [ ] Finished exercises 1-9
- [ ] Built and deployed capstone
- [ ] Capstone is publicly accessible
- [ ] Documentation is complete

**Congratulations!** You've completed the curriculum.

→ [Submit for Graduation](../GRADUATES.md)
