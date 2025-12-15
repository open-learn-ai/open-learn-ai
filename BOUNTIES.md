# Bounties

High-value contributions with explicit rewards. Claim an issue, deliver quality work, get rewarded.

---

## How Bounties Work

### Claiming a Bounty

1. **Comment on the issue**: "I'd like to claim this bounty"
2. **Wait for approval**: Maintainer assigns you within 24h
3. **Provide timeline**: When will you deliver?
4. **Deliver**: Submit PR meeting acceptance criteria
5. **Get rewarded**: Payout on merge

### Bounty Types

| Type | Symbol | Meaning |
|------|--------|---------|
| Cash | `$` | USD paid via GitHub Sponsors/PayPal/crypto |
| Credit | `CR` | Featured credit (author status, CONTRIBUTORS.md) |
| Network | `NET` | Intro to hiring partners, private Discord |
| Letter | `LTR` | Recommendation letter from maintainers |

---

## Open Bounties

### Tier 1: Foundation ($500+ value)

#### `[BOUNTY-001]` Module 5: Fine-Tuning Deep Dive
**Reward**: $500 + CR + NET

Create comprehensive module on fine-tuning open models:
- LoRA/QLoRA explanation and implementation
- Dataset preparation for fine-tuning
- Training loop with proper evaluation
- 5+ exercises with solutions
- Capstone: Fine-tune a model for specific task

**Acceptance Criteria**:
- [ ] Lesson content (3000+ words)
- [ ] Working code, tested on Llama 2 7B or similar
- [ ] Exercises with test suites
- [ ] Runs on single consumer GPU (24GB or less)
- [ ] Peer-reviewed by 2 maintainers

**Status**: OPEN
**Deadline**: Rolling
**Claim**: [Open an issue to claim](https://github.com/open-learn-ai/open-learn-ai/issues/new)

---

#### `[BOUNTY-002]` Module 5: RAG from Scratch
**Reward**: $400 + CR + NET

Build RAG system without frameworks:
- Vector embeddings explanation
- Implement simple vector store
- Chunking strategies
- Retrieval + generation pipeline
- 4+ exercises

**Acceptance Criteria**:
- [ ] No LangChain/LlamaIndex (educational, from scratch)
- [ ] Working end-to-end demo
- [ ] Exercises test understanding, not just copy-paste
- [ ] Documentation explains tradeoffs

**Status**: OPEN
**Claim**: [Open an issue to claim](https://github.com/open-learn-ai/open-learn-ai/issues/new)

---

#### `[BOUNTY-003]` Module 5: Deployment & Inference
**Reward**: $400 + CR + NET

Production deployment guide:
- Quantization (GGUF, AWQ, GPTQ)
- Inference servers (vLLM, TGI, llama.cpp)
- API design for LLM applications
- Cost optimization strategies
- Capstone: Deploy model that handles real traffic

**Acceptance Criteria**:
- [ ] Covers at least 3 deployment options
- [ ] Benchmarks included
- [ ] Works with free tier cloud options
- [ ] Security considerations documented

**Status**: OPEN
**Claim**: [Open an issue to claim](https://github.com/open-learn-ai/open-learn-ai/issues/new)

---

### Tier 2: Enhancement ($100-300 value)

#### `[BOUNTY-010]` Exercise Set: Attention Mechanism
**Reward**: $200 + CR

Create 5 progressive exercises for attention:
1. Implement basic attention (no mask)
2. Add causal masking
3. Multi-head attention
4. Scaled dot-product optimization
5. Flash attention conceptual (explain, not implement)

**Requirements**:
- Starter code with clear TODOs
- Test suites for each
- Solutions in `solutions/`
- Estimated times per exercise

**Status**: OPEN
**Claim**: [Open an issue to claim](https://github.com/open-learn-ai/open-learn-ai/issues/new)

---

#### `[BOUNTY-011]` Exercise Set: Backpropagation
**Reward**: $200 + CR

5 exercises building on micrograd:
1. Implement tanh backward pass
2. Add division operation
3. Build small MLP from scratch
4. Train on XOR problem
5. Visualize computation graph

**Status**: OPEN
**Claim**: [Open an issue to claim](https://github.com/open-learn-ai/open-learn-ai/issues/new)

---

#### `[BOUNTY-012]` Visualization Suite
**Reward**: $150 + CR

Interactive visualizations for:
- Attention patterns
- Token embeddings (PCA/t-SNE)
- Training loss curves
- Gradient flow

**Requirements**:
- Works in Jupyter notebooks
- Minimal dependencies
- Clear documentation

**Status**: OPEN
**Claim**: [Open an issue to claim](https://github.com/open-learn-ai/open-learn-ai/issues/new)

---

### Tier 3: Quality & Community ($50-100 value)

#### `[BOUNTY-020]` Code Review: All Module Exercises
**Reward**: $100 + CR + LTR

Comprehensive review of existing exercises:
- Test all solutions work
- Verify instructions are clear
- Check estimated times are accurate
- Document any issues found
- Submit fixes for issues

**Status**: OPEN
**Claim**: [Open an issue to claim](https://github.com/open-learn-ai/open-learn-ai/issues/new)

---

#### `[BOUNTY-021]` Video Walkthrough: Module 1
**Reward**: $100 + CR + NET

Create video content for micrograd module:
- 20-30 min walkthrough
- Screen recording with narration
- Cover common stumbling points
- Post to YouTube (we'll feature)

**Status**: OPEN
**Claim**: [Open an issue to claim](https://github.com/open-learn-ai/open-learn-ai/issues/new)

---

#### `[BOUNTY-022]` Translation: Spanish
**Reward**: $50/module + CR (Translation Lead status)

Translate modules to Spanish:
- All lesson content
- Exercise instructions
- README files

**Requirements**:
- Native or fluent speaker
- Consistent terminology
- Technical accuracy maintained

**Status**: OPEN (all modules)
**Claim**: [Open an issue to claim](https://github.com/open-learn-ai/open-learn-ai/issues/new)

---

### Tier 4: Quick Wins ($10-50 value)

#### `[BOUNTY-030]` Typo/Bug Bounty
**Reward**: $10 per valid fix + CR

Find and fix:
- Typos in documentation
- Broken code examples
- Incorrect explanations
- Dead links

**Limit**: 5 per person per month
**Status**: ALWAYS OPEN

---

#### `[BOUNTY-031]` Test Coverage
**Reward**: $25 per exercise test suite + CR

Add test coverage for exercises missing tests:
- Unit tests for solutions
- Edge case coverage
- Clear failure messages

**Status**: OPEN
**Claim**: Check `needs-tests` label

---

## Non-Cash Bounties

### Network Access Bounties

These earn you access to our private network:

| Contribution | Reward |
|--------------|--------|
| Review 10 student capstones | Private Discord + direct maintainer access |
| Complete all modules + excellent capstone | Intro to 3 hiring partners of your choice |
| Create 1 full module | Featured in newsletter + job board priority |
| Mentor 5 students to completion | Letter of recommendation |

### Career Bounties

| Contribution | Reward |
|--------------|--------|
| First 20 contributors | "Founding Contributor" badge (permanent) |
| Module author | Co-author on any papers about this project |
| Core team member | Advisory role if entity forms, equity consideration |

---

## Bounty Rules

### Claiming
- One bounty per person at a time (prevents hoarding)
- If no progress in 2 weeks, bounty returns to pool
- Partial work = partial credit (we're fair)

### Quality
- Must meet acceptance criteria
- Must pass review by 2 maintainers
- Revisions may be requested

### Payment
- Cash bounties paid within 7 days of merge
- Payment via GitHub Sponsors, PayPal, or crypto (your choice)
- Non-cash rewards fulfilled within 30 days

### Disputes
- Maintainers have final say on acceptance
- We err on the side of paying contributors
- Reach out privately if concerns

---

## Propose a Bounty

Think something should be bounties?

1. Open an issue with `[BOUNTY PROPOSAL]` prefix
2. Describe the work needed
3. Suggest appropriate reward tier
4. We'll review and add to this list if approved

---

## Funding

Bounties are funded by:
- Maintainer personal funds (initial)
- GitHub Sponsors
- Corporate sponsors (see PARTNERS.md)
- Community donations

**Want to fund a bounty?** Contact maintainers.

---

## Current Bounty Pool

| Source | Amount | Status |
|--------|--------|--------|
| Initial seed | $2,000 | Active |
| Community donations | $0 | Accepting |
| Corporate sponsors | $0 | Seeking |

*Updated: December 2025*
