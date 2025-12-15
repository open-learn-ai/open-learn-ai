# Module 0: First Contact

**Time**: ~1 week | **Prerequisites**: Basic Python | **Outcome**: Running AI on your machine

---

## What You'll Build

By the end of this module, you will:
1. Run a large language model locally on your own machine
2. Understand what an LLM actually is (two files!)
3. Build your first AI-powered application
4. Have a mental model for how this all works

---

## Why Start Here?

Most courses start with math. We start with magic.

You're going to run a model that can write poetry, explain code, and answer questions—on your laptop. Then we'll pull back the curtain and show you what's actually happening.

The goal: **Get hooked first, understand later.**

---

## Lessons

| # | Lesson | Time | What You'll Do |
|---|--------|------|----------------|
| 1 | [What is an LLM?](lesson-01-what-is-an-llm.md) | 30 min | Mental model for language models |
| 2 | [Run Your First Model](lesson-02-run-your-first-model.md) | 45 min | Download and run Llama locally |
| 3 | [How Training Works](lesson-03-how-training-works.md) | 30 min | Compression, prediction, emergence |
| 4 | [The Assistant Transformation](lesson-04-assistant-transformation.md) | 30 min | Pre-training vs fine-tuning |
| 5 | [Build Something](lesson-05-build-something.md) | 2 hrs | Your first AI application |

---

## Exercises

- [Exercise 1: Run inference and measure tokens/second](exercises/exercise-01-inference.py)
- [Exercise 2: Compare different model sizes](exercises/exercise-02-model-sizes.py)
- [Exercise 3: Prompt engineering basics](exercises/exercise-03-prompting.py)
- [Exercise 4: Build a simple chatbot](exercises/exercise-04-chatbot.py)

---

## Capstone

**Build an AI-powered tool that solves a real problem for you.**

Examples:
- A study assistant that quizzes you on your notes
- A code explainer for a language you're learning
- A writing helper for a specific style/purpose
- A data analyzer for a dataset you care about

**Requirements:**
- Uses local model (no API calls)
- Solves a problem YOU actually have
- Has a simple interface (CLI or basic web)
- Documented: What it does, how to run it, what you learned

Submit via PR to `capstones/module-0/[your-github-handle]/`

---

## Resources

**Video Source**: [Intro to Large Language Models - Andrej Karpathy](https://youtube.com/watch?v=zjkBMFhNj_g)

**Supplementary**:
- [Llama.cpp](https://github.com/ggerganov/llama.cpp) - Run models locally
- [Ollama](https://ollama.ai) - Easiest way to get started
- [Hugging Face](https://huggingface.co) - Model hub

---

## Checklist

- [ ] Completed all 5 lessons
- [ ] Finished exercises 1-4
- [ ] Built and submitted capstone
- [ ] Helped at least one other learner in Discord

**Ready for Module 1?** You should be able to:
- Explain what an LLM is to a friend (two files!)
- Run inference locally
- Articulate the difference between pre-training and fine-tuning
- Have built something that works

→ [Module 1: The Engine (micrograd)](../module-1-micrograd/README.md)
