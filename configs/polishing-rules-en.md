# Polishing Rules (Operational)

Operating rules for the polishing agent. They tie together the pattern catalog,
the claim-evidence discipline, the scoring rubric, and the section strategies.

Reference files:

- `humanizer-patterns-en.md`: what to remove
- `claim-evidence-discipline.md`: the rigor layer
- `scoring-rubric.md`: the convergence measure
- `section-strategies.md`: per-section intensity

## Core principle

Academic prose already has the right voice: neutral, precise, third-person
plural, each claim backed by evidence. The job is to strip the machine tells
without making it casual, and to hold the line that every claim earns its number
or citation and no verb overreaches its evidence.

## What does not help (don't do these)

1. Swapping synonyms. Detectors read n-gram patterns, not individual words, so
   trading "important" for "crucial" changes nothing.
2. Inverting clauses. Flipping "Because A, B" into "B, because A" keeps the same
   template.
3. Running the text through another model to "rewrite" it. You just replace one
   model's fingerprint with another, and paraphrase tools usually raise the score.
4. Planting typos or stiff grammar to seem human. Reviewers notice, and current
   detectors are not fooled.

## Hard protections

- Leave every number, coefficient, standard error, p-value, sample size,
  equation, variable name, and citation untouched.
- Never invent data, results, citations, or a "surprise finding" for flavor.
- Never change what the paper claims, only how it says it.
- Don't over-correct: ordinary academic phrasing is not a tell unless it is
  stacked or citation-free.

## Process (both modes)

1. Read the text and any writing sample; note the document type.
2. Audit without editing: list each tell with its location and fix, and each
   claim's evidence status.
3. Rewrite: same structure and content, tells removed, overclaims matched to
   evidence, legitimate hedging kept.
4. Report: cleaned text plus a short change log (what was removed, what was
   softened or given an evidence pointer).

## Intensity tiers

### Standard

- Fix rhythm first, then the 🔴 items.
- Keep the author's natural voice; don't casualize.
- The five-dimension score is optional feedback, not a gate.

### Radical

- Fix 🔴🟡🟢.
- Run the six-step loop: intake → audit → claim-evidence check → rewrite →
  self-score → cold-reader recheck.
- Apply section strategies; rewrite abstract, intro, lit review, discussion,
  and conclusion hardest.
- Enforce rhythm hard (one ≤8-word and one ≥40-word sentence per ~200 words; no
  run of 5+ mid-length).
- Zero em dashes in the final output (search before delivering).
- Pass at a weighted score of 42; below 35, rewrite rather than patch.
- Cold-reader recheck before delivering: fluency, fidelity (every number/name/
  year/citation unchanged), consistency (one voice, no seams).

## Voice matching

If the author hands you a sample of their own writing, read it first: sentence
length, word choice, openings, punctuation, transitions, where they hedge. Match
those habits and don't replace casual words with formal ones or scrub deliberate
quirks. The sample overrides the generic rules (if it uses em dashes, keep them
at about the same rate instead of banning them). With no sample, default to
clean, venue-appropriate prose, not a casual opinionated voice.

## Academic integrity

The goal is to return human-written and AI-assisted text to the language
distribution of a real researcher, not to help fully AI-generated work evade
disclosure. Integrity outranks detection scores. No rewrite may touch the claims,
data, or citations, and when a claim lacks evidence the fix is to flag it, not
hide it.
