# Section-by-Section Strategies

AI traces show up differently by section, so the fix strength should differ too.
A methods section that reads "AI-flavored" is often just convention; a literature
review that reads AI-flavored is real distortion.

## Risk table

| Section | Risk | Main move | Keep |
|---|---|---|---|
| Abstract | extreme | heavy rewrite, add numbers | finding, object |
| Introduction | extreme | rebuild opening, real tension | question, contribution |
| Literature review | extreme | full rewrite, name authors | thread, disagreements |
| Hypotheses | mid | hedge, downgrade absolutes | theory, logic |
| Data | low | concrete steps | sources, window, cleaning |
| Model | low | cut filler, state reason | form, variables |
| Baseline results | mid | concretize, downgrade verbs | coefficients, significance |
| Mechanisms | mid | break total-fen-total | chain, mediator |
| Heterogeneity | mid | vary sentence length | grouping, gaps |
| Robustness | low | one check per worry | method, direction |
| Discussion | extreme | inject caution | meaning, limits |
| Conclusion | extreme | avoid echo, add new info | contribution, next |

## Per-section notes

**Abstract.** At least three concrete numbers (sample size, window, a
coefficient) and one named literature response ("consistent with Smith 2020").
Cut "深远影响 / 重要意义" filler. Order: question → method → data → finding →
mechanism → dialogue → contribution.

**Introduction.** No "近年来 / 随着…的发展" openers. Open on a fact, a number, or
a disagreement. Contributions as paragraphs naming the marginal gain over prior
work, not three numbered restatements of the abstract.

**Literature review.** Every claim gets author+year. Write the disagreement when
two camps exist. End by naming the gap concretely ("has not been systematically
tested"), not the word "gap".

**Hypotheses.** Hedge the wording ("A has a positive effect on B", not "A can
significantly promote B"). Keep "显著" out of the hypothesis; that word belongs
in results.

**Data.** One sentence per source (source + variable + window). Concrete cleaning
rules (drop ST firms, 1% winsorize, cluster by industry), not "严格清洗". State
the policy reason for the sample window if there is one.

**Model.** Write the equation, one sentence per variable, and why this estimator
(OLS/IV/DiD/PSM).

**Baseline results.** Give t-values, coefficients, CIs, not adjectives. Describe
the column-by-column sequence (no controls → add controls → stability). "与 H1
预期一致" not "证明了".

**Mechanisms.** Open with a question ("What mechanism drives the baseline
result?"). One mediator + statistic per path; report the mediation share ("this
path explains 37% of the baseline coefficient").

**Heterogeneity.** Report the ratio of group coefficients ("large-firm is 1.8×
the small-firm one"), not just directions. Say why. Interleave short sentences.

**Robustness.** Each check corresponds to one concrete worry (measurement error,
selection, reverse causality, chance). Concrete numbers; placebo tests report the
empirical distribution quantile.

**Discussion.** Engage prior literature (support, rebut, extend). Admit limits
(data, method, window). "系统检验了既有文献未处理的 X 问题", not "填补空白".

**Conclusion.** No abstract echo. Add an unresolved question + next step.
Concrete policy implications, no "完善制度 / 加强监管". Admitting a surprise or a
limit raises credibility.

## Priority when pressed

1. Abstract
2. Intro first three paragraphs
3. Conclusion
4. Literature review
5. Discussion
6. the rest

Rewrite the sections AI writes "pretty but hollow" hardest; the conservative
sections (methods, robustness) need the least.
