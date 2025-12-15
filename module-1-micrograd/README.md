# Module 1: The Engine (micrograd)

**Time**: ~2 weeks | **Prerequisites**: Module 0, basic calculus | **Outcome**: Build autograd from scratch

---

## What You'll Build

By the end of this module, you will:
1. Understand backpropagation at an intuitive level
2. Build a fully functional autograd engine from scratch
3. Implement basic neural network components
4. Train a small neural network on a toy problem

---

## Why This Matters

Every modern AI system—GPT-4, Stable Diffusion, AlphaFold—trains using backpropagation. It's the algorithm that makes neural networks learn.

Most people treat it as a black box. You're going to build it yourself.

When you're done, PyTorch's magic won't be magic anymore. It'll be ~200 lines of code you understand completely.

---

## Lessons

| # | Lesson | Time | What You'll Learn |
|---|--------|------|-------------------|
| 1 | Derivatives and Gradients | 45 min | What gradients tell us, numerical vs analytical |
| 2 | The Chain Rule | 30 min | How gradients flow through compositions |
| 3 | Building Value | 1 hr | The core abstraction: values that track gradients |
| 4 | Automatic Differentiation | 1.5 hr | Building the backward pass |
| 5 | Neural Network Primitives | 1 hr | Neurons, layers, activation functions |
| 6 | Training Loop | 1 hr | Loss, optimization, convergence |

**Video Source**: [Karpathy - Building micrograd](https://youtube.com/watch?v=VMj-3S1tku0)

---

## Exercises

| Exercise | Time | What You'll Do |
|----------|------|----------------|
| 1 | 30 min | Numerical gradient checking |
| 2 | 45 min | Implement backward() for basic ops |
| 3 | 45 min | Add tanh, exp, pow operations |
| 4 | 30 min | Build a Neuron class |
| 5 | 45 min | Build an MLP class |
| 6 | 1 hr | Train on XOR problem |

---

## Capstone

**Build a micrograd extension and train something interesting.**

Options:
- Add new operations (softmax, batch norm, conv2d concept)
- Visualize the computation graph (graphviz)
- Train on a slightly harder problem (moons dataset, simple classification)
- Compare your gradients to PyTorch's (verify correctness)

**Requirements:**
- Extend micrograd in a meaningful way
- Train a network successfully
- Document what you learned
- Visualize something (loss curve, decision boundary, computation graph)

---

## Key Concepts

After this module, you should be able to explain:

- **Gradient**: The direction of steepest increase. We go opposite to minimize loss.
- **Chain Rule**: If y = f(g(x)), then dy/dx = dy/dg × dg/dx
- **Backpropagation**: Applying chain rule backwards through a computation graph
- **Forward Pass**: Computing the output from inputs
- **Backward Pass**: Computing gradients from output back to inputs
- **Autodiff**: Automatically computing derivatives by tracking operations

---

## Checklist

- [ ] Completed all 6 lessons
- [ ] Finished exercises 1-6
- [ ] Built and submitted capstone
- [ ] Can explain backprop without looking at notes

**Ready for Module 2?** You should be able to:
- Implement autodiff for any differentiable function
- Build and train a simple MLP
- Debug gradient issues by thinking about the chain rule

→ [Module 2: Language Models](../module-2-language-models/README.md)
