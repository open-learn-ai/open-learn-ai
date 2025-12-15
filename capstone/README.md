# Capstone Projects

The capstone is where everything comes together. This is your portfolio piece—the project employers will see.

---

## What Makes a Great Capstone

### 1. Solves a Real Problem
Not "I trained a model on Shakespeare" but "I built a tool that helps writers maintain consistent style across a novel."

### 2. Shows Technical Depth
Use what you learned. Don't just wrap an API—fine-tune, build RAG, implement agents, optimize inference.

### 3. Is Deployed and Accessible
A GitHub repo is good. A working demo is better. Something people can actually use is best.

### 4. Is Well Documented
- What problem does it solve?
- How do you use it?
- What technical decisions did you make and why?
- What did you learn?

### 5. Is Your Best Work
This represents you. Polish it.

---

## Capstone Timeline

| Phase | Time | What to Do |
|-------|------|------------|
| **Ideation** | 1-2 days | Pick a problem you care about |
| **Planning** | 2-3 days | Scope it, identify technical approach |
| **Building** | 1-2 weeks | Core implementation |
| **Polish** | 3-5 days | Edge cases, UX, documentation |
| **Deploy** | 1-2 days | Get it live |
| **Submit** | 1 day | PR to this repo |

---

## Submission Process

### 1. Build Your Project

Your project should live in its own GitHub repo with:
- README explaining what it does
- Clear setup instructions
- Working code
- Demo or screenshots

### 2. Create Your Submission

Fork this repo and add a folder:
```
capstones/
  [your-github-handle]/
    README.md      # Summary of your project
    LEARNINGS.md   # What you learned (optional but valuable)
```

### 3. Your README Should Include

```markdown
# [Project Name]

## Problem
What problem does this solve? Who is it for?

## Solution
How does it work? What's the technical approach?

## Demo
Link to live demo, video, or screenshots

## Repository
Link to your project repo

## Technical Highlights
- What techniques from the course did you use?
- What was challenging?
- What are you most proud of?

## What I Learned
Key insights from building this

## Future Work
What would you add with more time?
```

### 4. Submit PR

Title: `[CAPSTONE] Your Name - Project Name`

We'll review within 1 week.

---

## Example Capstones

### Research Assistant
**Problem**: Too many papers, not enough time
**Solution**: RAG system over arXiv papers in your field
**Technical**: Custom chunking for academic papers, citation-aware retrieval
**Demo**: Chat interface that answers questions with citations

### Code Reviewer
**Problem**: PRs pile up, reviews are slow
**Solution**: Fine-tuned model on your team's code review comments
**Technical**: LoRA fine-tuning on PR diff + review pairs
**Demo**: GitHub Action that auto-comments on PRs

### Study Buddy
**Problem**: Students need practice questions
**Solution**: Generate quiz questions from lecture notes
**Technical**: RAG over notes + fine-tuned question generator
**Demo**: Web app where students upload notes, get quizzes

### Domain Expert
**Problem**: Technical documentation is hard to search
**Solution**: Chatbot that knows your product's docs
**Technical**: RAG with hierarchical chunking, conversation memory
**Demo**: Embedded chat widget for documentation site

---

## Evaluation Criteria

| Criterion | Weight | What We Look For |
|-----------|--------|------------------|
| **Technical Depth** | 30% | Uses course concepts meaningfully |
| **Problem Fit** | 25% | Solves a real problem well |
| **Execution** | 25% | Works reliably, handles edge cases |
| **Documentation** | 15% | Clear, complete, helpful |
| **Polish** | 5% | Attention to detail |

---

## Getting Help

### Office Hours
Weekly office hours for capstone guidance. Bring your ideas, get feedback.

### Discord
`#capstone` channel for questions, feedback, and collaboration

### Peer Review
Post your WIP for feedback from other learners

---

## After Submission

### If Accepted
- Listed in GRADUATES.md with link to your capstone
- Access to job board and partner intros
- Eligible for showcase presentation

### If Needs Revision
- Clear feedback on what to improve
- Resubmit when ready
- No penalty for iteration

---

## FAQ

**Q: How long should my capstone take?**
A: 2-4 weeks of focused work is typical. Some do it in less, some take longer.

**Q: Can I use external APIs?**
A: Yes, but show technical depth. Don't just wrap OpenAI's API—add value.

**Q: Can I work with others?**
A: Yes, but each person needs to submit their own and explain their contribution.

**Q: What if my idea isn't original?**
A: Execution matters more than novelty. Build it well.

**Q: I'm stuck on ideas. Help?**
A: What problems do YOU face? What would make YOUR life easier? Start there.
