# Claim–Evidence Discipline

Humanizing academic prose is only half the job. The other half is making sure
every claim earns its number, figure, or citation, and that no verb is stronger
than its evidence.

## Core rule

For each empirical claim ask two things: (a) is there an anchor in the text,
such as a number, table, figure, or citation, and (b) does the verb match the
strength of that evidence.

## Verb ↔ design

- Clean identification (RCT, sharp RD, well-defended DiD): direct verbs are fine.
  "The reform reduced entry by 12%."
- Observational / correlational: "is associated with".
- Suggestive / mechanism evidence: "is consistent with".

Flag every "prove / demonstrate / establish / 充分证明 / 必然导致" whose design
can't carry it, and every "significant / 显著" with no test statistic. Never fix
the mismatch by inventing evidence; weakening the verb is the default.

## Three fixes

- **Unbacked claim → add the pointer or soften.**
  "Our method is more robust." → "Our method's error doubles under distribution
  shift, while the baseline's triples (Figure 3)."
- **Verb stronger than evidence → downgrade.**
  "This shows our method is universally better." → "On the two benchmarks we
  ran, our method matches the strongest baseline and beats the rest (Table 2)."
- **Vague magnitude → a number or range, attributed.**
  "a large improvement" → "a 4–8% gain in accuracy over the strongest baseline".
  Prefer ranges over single averages unless the averaging method is stated, and
  lead with the comparison to the strongest competitor.

## Hedging calibration

- One hedge per claim, matched to design strength.
- Never zero hedges for observational claims, never three stacked.
- Keep evidence-tied hedges ("suggests", "is consistent with", "we hypothesize").
  Turning "the results suggest X" into "the results prove X" manufactures
  overclaiming.
- Quantify vague hedging: "somewhat better, relatively robust" → "2 points
  higher, stable across five seeds".

## Citation discipline

- Cite the one or two works that matter and say why, not a bracketed dump.
- Every literature claim gets author + year.
- Write the disagreement when two camps exist.
- Do not invent references. If a detail is missing, ask or soften.

## Preserve

- Evidence-tied hedging; passive where the actor is irrelevant; first-person "we".
- Formal definitions, named methods, terms, equations, symbols.
- Real limitations and scope statements.
- The author's own supplied track record (never invent funding, results,
  partners, or letters).

## Hard protections

- Never alter numbers, coefficients, standard errors, p-values, sample sizes,
  equations, variable names, or citation contents.
- Never fabricate data, results, citations, or "surprising findings".
- Never inject errors, slang, or archaic words to game perplexity.
- Never change what the paper claims, only how it says it.

## Funding-proposal mode

A proposal is sold on vision plus feasibility, so ambition language a paper would
trim is expected here. Enforce claim ↔ feasibility instead:

- Every bold aim needs a footing: preliminary data, a prior result, a classical
  theorem, a collaborator, or staged de-risking.
- Aims should be parallel and independently valuable; the central hypothesis is
  a falsifiable commitment, not "we will explore whether…".
- Never invent preliminary results, funding, partners, or letters; flag the gap
  rather than papering over it.
