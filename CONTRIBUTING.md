# Contributing to Open Learn AI

We're building the AI curriculum universities are too slow to create. Every contribution matters.

---

## Contribution Philosophy

### We Optimize for Incentives

Open source often burns out contributors. We don't want that. Every contribution should be:
- **Credited** - Your name, permanently attached to your work
- **Valuable to you** - Builds your portfolio, network, or career
- **Valued by us** - We actively reward high-quality contributions

### The Contributor Ladder

```
Learner → Contributor → Reviewer → Maintainer → Core Team
```

| Level | What You Do | What You Get |
|-------|-------------|--------------|
| **Learner** | Complete modules, submit capstones | Portfolio, community access |
| **Contributor** | Fix bugs, add exercises, improve docs | Credit in CONTRIBUTORS.md |
| **Reviewer** | Review student submissions & PRs | TA status, private Discord, rec letters |
| **Maintainer** | Own a module, merge PRs | Co-author status, job referrals |
| **Core Team** | Shape curriculum direction | Leadership credit, equity (if entity forms) |

---

## Types of Contributions

### 1. Content Contributions

**Exercises** (High Value)
- Hands-on coding challenges for existing lessons
- Should be completable in 15-60 minutes
- Must include solution and tests

**Lessons** (High Value)
- New content for existing modules
- Must follow our lesson template
- Requires: explanation → code → exercises → capstone tie-in

**Modules** (Very High Value)
- Entire new curriculum sections
- See BOUNTIES.md for funded module requests
- Discuss in Issues before starting

### 2. Quality Contributions

**Bug Fixes**
- Broken code, typos, unclear explanations
- Small but valued—every fix gets credited

**Improvements**
- Better explanations, additional examples
- Performance improvements to starter code
- Accessibility improvements

**Translations**
- Translate modules to other languages
- Translation leads get special credit
- See `translations/` for guidelines

### 3. Community Contributions

**Student Reviews**
- Review capstone submissions from learners
- Path to Reviewer status
- Directly helps someone learn

**Mentorship**
- Answer questions in Discord
- Run study groups
- Host office hours

**Evangelism**
- Write about the course
- Create video walkthroughs
- Share your learning journey

---

## How to Contribute

### For Code/Content

1. **Check Issues** - Look for `good first issue` or `help wanted`
2. **Claim an Issue** - Comment "I'll take this" so we don't duplicate work
3. **Fork & Branch** - Create a feature branch
4. **Follow Templates** - Use our lesson/exercise templates
5. **Submit PR** - Reference the issue, explain your changes
6. **Iterate** - Respond to feedback, refine

### For Reviews

1. **Apply for Reviewer status** - Complete at least 2 modules first
2. **Start with PR reviews** - Review code contributions
3. **Graduate to capstone reviews** - Review student submissions
4. **Earn trust** - Consistent quality = more responsibility

### For New Ideas

1. **Open a Discussion** - Share your idea for feedback
2. **Get buy-in** - Wait for maintainer approval on big changes
3. **Prototype** - Show, don't tell
4. **Submit** - Full PR with documentation

---

## Contribution Standards

### Code Quality

```python
# Good: Clear, commented, teachable
def attention(Q, K, V):
    """
    Scaled dot-product attention.

    Args:
        Q: Query matrix (batch, seq, d_k)
        K: Key matrix (batch, seq, d_k)
        V: Value matrix (batch, seq, d_v)

    Returns:
        Attention output and weights
    """
    d_k = Q.shape[-1]
    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, V), weights
```

- Code should be **readable by learners**
- Comments explain **why**, not just what
- Prioritize **clarity over cleverness**

### Exercise Quality

Every exercise needs:
- [ ] Clear learning objective
- [ ] Starter code with TODOs
- [ ] Test suite that validates solution
- [ ] Solution file (in `solutions/`)
- [ ] Estimated completion time

### Lesson Quality

Every lesson needs:
- [ ] Hook: Why should I care?
- [ ] Concept: Clear explanation with visuals
- [ ] Code: Working implementation
- [ ] Exercises: 3-5 hands-on challenges
- [ ] Capstone tie-in: How this connects to the bigger picture

---

## Getting Credit

### CONTRIBUTORS.md

All contributors are listed in `CONTRIBUTORS.md` with:
- Name and GitHub handle
- Contributions made
- Link to your profile/portfolio

### Author Attribution

For significant contributions (exercises, lessons, modules):
- Your name in the file header
- Listed as author in module README
- Mentioned in release notes

### Recommendations

Top contributors can request:
- LinkedIn recommendation from maintainers
- Letter of recommendation for jobs/grad school
- Direct intro to hiring partners

---

## Communication

### Where to Ask Questions

| Topic | Where |
|-------|-------|
| Stuck on an issue | Comment on the issue |
| General questions | Discord #contributors |
| Big ideas/proposals | GitHub Discussions |
| Sensitive matters | Email maintainers directly |

### Response Times

- **Issues/PRs**: 48 hours for initial response
- **Discord**: Usually same-day
- **Discussions**: Within a week

---

## Recognition

### Monthly Contributor Spotlight

Each month we highlight contributors who:
- Made impactful contributions
- Helped other learners
- Improved the community

Featured in: README, Discord announcement, social media

### Annual Contributors

End of year recognition for sustained contributors:
- Special badge
- Featured in year-end retrospective
- First access to new opportunities

---

## First-Time Contributors

### Good First Issues

Look for issues labeled `good first issue`:
- Typo fixes
- Small documentation improvements
- Adding test cases
- Clarifying explanations

### Your First PR Checklist

- [ ] Read this guide fully
- [ ] Set up local development environment
- [ ] Make changes on a feature branch
- [ ] Test your changes
- [ ] Write clear commit messages
- [ ] Submit PR with description
- [ ] Be patient and responsive to feedback

---

## Questions?

- **Discord**: #contributors channel
- **GitHub**: Open a Discussion
- **Email**: [maintainer email]

We want you to succeed. Ask for help.
