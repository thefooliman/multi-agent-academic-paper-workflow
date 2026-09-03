# Humanizer Pattern Catalog (English)

What the polishing agent flags and fixes. Each entry names a habit that makes
prose read as machine-written, explains why, and gives a concrete rewrite.

Severity: 🔴 fix in standard mode · 🟡 fix in radical mode · 🟢 optional in
radical mode. Fix rhythm first, it moves the needle more than any vocabulary
change, then the 🔴 items, then the rest.

The rule of thumb that keeps you from over-correcting: a phrase followed by a
citation, a number, or a test statistic is normal academic writing, not a tell.

---

## Keep, don't flag

These are legitimate. Strip them and the text gets worse.

- "Notably", "Importantly", "In contrast", "Specifically" as transitions.
- Attribution with a source: "Prior work has shown that … (Smith 2020; Li 2023)".
- Technical register: "significant at the 1% level", "robust to", "identification
  strategy", "point estimate".
- Evidence-tied hedges: "suggests", "is consistent with", "may indicate",
  "appears to", "we hypothesize that".
- First-person plural "we".
- Passive voice in methods sections ("Samples were normalized…").
- An occasional rule-of-three or semicolon.
- Formal definitions, named methods and metrics, equations, symbols.

---

## Group 1 · Overclaiming and puffery

### 1.1 Inflated importance 🔴

The tell: an ordinary finding is dressed up as a landmark.

Watch for: pivotal, crucial, vital, watershed, testament, landmark, paradigm
shift, evolving landscape, far-reaching, marks a turning point, in today's
rapidly changing world.

- Before: "Carbon pricing was a watershed in the evolution of environmental
  governance, underscoring its enduring importance."
- After: "After carbon pricing, compliance costs in our sample rose 2.1% on
  average, and the effect was largest for energy-intensive firms."

### 1.2 Significance hype 🔴

The tell: the paper announces how important it is instead of what it found.

Watch for: paves the way, opens new avenues, sheds light on, of paramount
importance, bridges the gap, a step toward a new paradigm.

- Before: "This work paves the way for a new generation of tools and sheds light
  on a question of paramount importance."
- After: "This work fixes one gap in prior tools: they drift when the input
  stream shifts (Section 4)."

### 1.3 Overclaiming verbs 🔴

The tell: a verb stronger than the evidence behind it. "Prove" and "demonstrate"
belong to clean identification, not to an observational coefficient.

- Before: "This proves that the subsidy caused higher investment."
- After: "The subsidy is associated with a 6% rise in investment, though the
  design cannot separate the effect from selection."

A clean RCT or sharp RD may use direct verbs. Observational work should not.

### 1.4 Promotional adjectives 🟡

The tell: journal prose is flat by design; adjectives that sell are a giveaway.

Watch for: groundbreaking, remarkable, striking, dramatic, impressive,
cutting-edge, state-of-the-art, renowned, stunning, vibrant, rich (figurative).

- Before: "Our groundbreaking design yields remarkable evidence of a dramatic
  effect."
- After: "The difference-in-differences estimate puts the drop in new entry at
  11% (95% CI: 6%–16%)."

### 1.5 Empty intensifiers 🟡

The tell: "comprehensive", "various", "numerous" promise coverage without saying
what was done.

- Before: "We run comprehensive robustness checks using various specifications."
- After: "Four things could threaten the design; we handle each in Section 6."

### 1.6 Novelty padding 🟡

The tell: claiming novelty instead of locating the contribution.

Watch for: "novel" repeated within a section, "to the best of our knowledge",
"for the first time".

- Before: "We propose a novel framework and, to our knowledge, are the first to
  study this setting."
- After: "We study calibration when labels arrive late, a case prior offline
  work skips."

### 1.7 Unsupported "significantly" 🔴

The tell: "significantly improves" with no statistic nearby, or statistical and
economic significance blurred.

- Before: "The coefficient is highly significant, demonstrating a strong effect."
- After: "The estimate is 0.051 (s.e. 0.013), significant at 1%, but the implied
  elasticity of 0.18 is small beside the 0.4–0.7 range found in other work."

---

## Group 2 · Scaffolding and filler

### 2.1 Formulaic openers 🔴

The tell: the single most recognizable machine opening, in every language.

Watch for: "In recent years, X has attracted increasing attention", "With the
rapid development of …", "In today's globalized economy", "Despite recent
advances".

- Before: "In recent years, the digital economy has drawn growing scholarly
  attention."
- After: "From 2016 to 2021, provinces that opened free-trade zones drew 41% of
  new foreign investment. Whether the zones caused the inflow is still debated
  (Wang 2023)."

Open on a fact, a number, or a live disagreement.

### 2.2 Connective chains 🔴

The tell: every sentence or paragraph opens with Moreover / Furthermore /
Additionally.

Fix: cut the connective and relay by meaning. Open the next sentence with the
key noun of the previous one. One additive connective per paragraph, at most.

### 2.3 Rule-of-three padding 🟡

The tell: every list has exactly three items; triads of abstract nouns
("efficiency, innovation, and growth").

Fix: keep the two items you can support with evidence, cut or expand the third.
Vary list length across the paper.

### 2.4 Superficial "-ing" tails 🔴

The tell: a participle phrase bolted onto a finding to fake depth.

Watch for: sentence-final ", highlighting…", ", underscoring…", ", showcasing…",
", reflecting…", ", contributing to…".

- Before: "The coefficient holds across specifications, highlighting the
  robustness of our design and underscoring its broad relevance."
- After: "Across columns (2)–(5) the coefficient holds between 0.041 and 0.048."

### 2.5 Generic contributions 🔴

The tell: the conclusion restates the abstract and gestures at "policymakers and
practitioners".

- Before: "This study fills an important gap and offers valuable insights for
  policy."
- After: "Unlike earlier work, our design separates the supply- from the
  demand-side response; the upshot is that a subsidy aimed only at construction
  would leave about half the enrollment gain on the table."

### 2.6 Citation dumping 🟡

The tell: five-plus references bracketed after a bland claim, none engaged.

- Before: "Many studies look at spillovers (A and B 1999; C 2004; D 2010; …)."
- After: "Evidence on spillovers is split: some studies find negative effects,
  others find gains only through supplier links, and our data lets us separate
  the two."

Cite the one or two works that matter and say why.

### 2.7 Echo-chamber conclusion 🔴

The tell: the conclusion repeats the abstract with the same vocabulary, then
adds generic "limitations and future research".

Fix: the conclusion has to add something new: a question this design cannot
answer, a policy margin the estimates can't reach, the dataset that would settle
it. Limitations must be this paper's ("our eight-year sample cannot pick up
long-run effects"), not generic ones.

### 2.8 Vague attribution 🔴

The tell: claims handed to nobody.

Watch for: "Studies have shown", "Research suggests", "Experts argue", "It is
widely believed", with no source attached.

- Before: "Studies have shown that financial constraints limit innovation."
- After: "Cash-strapped firms file fewer patents; the evidence is surveyed in
  one line of work, and a recent study finds that grants lift patenting among
  constrained applicants."

### 2.9 Stock sections 🔴

The tell: a section titled "Challenges and Legacy" or "Future Outlook" that
restates vague claims instead of adding facts.

- Before: "Despite its growth, the district grapples with the usual urban
  pressures, from traffic to water supply. Despite these pressures, it keeps
  expanding."
- After: "The district has chronic traffic and water shortages."

Add dates or public actions only when the source provides them.

### 2.10 Roadmap preview 🔴

The tell: "This paper is organized as follows: Section 2 describes…, Section 3
reviews…, Section 4 discusses…" with rigid parallel phrasing.

Fix: drop it, or name what each section actually contributes. A specific roadmap
("the next section separates supply from demand effects") is fine; a mechanical
list is not.

### 2.11 Definitional repetition 🟡

The tell: glossing the term's own name ("the word 'rebound' is apt, because…",
"By 'decentralization' we mean…"). AI does this more than humans.

Fix: cut the gloss, or fold the definition into the argument instead of
announcing it.

---

## Group 3 · Word and grammar habits

### 3.1 AI vocabulary 🟡

The tell: words whose frequency spiked after 2023, especially in clusters.

Watch for: delve, intricate, interplay, tapestry, landscape (abstract), realm,
pivotal, crucial, foster, leverage (verb), showcase, underscore (verb), garner,
seamless, enhancing, enduring, quietly, valuable, testament, align with.

Fix: use the plain word, examine, complex, interaction, setting, important,
encourage, use, show. One instance is fine; a cluster is not.

### 3.2 Copula avoidance 🟢

The tell: reaching for "serves as" / "represents" where "is" would do.

- Before: "The 2015 tax change serves as an ideal natural experiment."
- After: "The 2015 tax change is a plausible natural experiment: assignment
  followed a formula and firms could not game their eligibility."

### 3.3 Negative parallelism 🟡

The tell: "not only X, but Y", "this is not just X, it's Y".

- Before: "The reform not only lowered entry costs but also reshaped the
  competitive landscape."
- After: "The reform lowered entry costs. Competitive pressure shows up only in
  downstream markets (Table 6)."

### 3.4 Synonym cycling 🟡

The tell: rotating labels for one thing, firms/enterprises/companies/
organizations, effect/impact/influence. Academic writing fixes one term and
repeats it. Pick one, define it, stick to it.

### 3.5 False ranges 🟢

The tell: "from X to Y" where X and Y are not on a scale.

- Before: "Our findings bear on questions from tax design to rural credit."
- After: Name the two audiences and one sentence each on why.

### 3.6 Hedging miscalibration 🔴

Two failures. Stacked hedges: "may potentially suggest the possibility that X
could contribute to…" becomes "suggests that X may raise…". Missing hedges: an
observational finding stated as causal fact.

One hedge per claim, chosen by design strength. Never zero for observational
claims, never three.

### 3.7 Word-choice tells 🟡

| Machine habit | Academic norm |
|---|---|
| "linked to" | "associated with" |
| "via" | "through" |
| "yielded" (results) | "produced", "provided" |
| "Beyond X, …" (transition) | "In addition to X, …" |
| non-locative "where" | "with", or a new sentence |

### 3.8 Passive voice, judgment call

General humanizers over-strip passive. In academic text it is fine when the actor
does not matter ("Samples were normalized to total protein"). Use active voice
only when it clarifies who acted.

---

## Group 4 · Typography

### 4.1 Em and en dashes 🔴

Final output should contain no em dashes or en dashes used as punctuation,
unless the author's sample uses them. Replace with a period, comma, colon,
parentheses, or a rewritten sentence. Also check spaced dashes and double
hyphens. Search the text for the characters before delivering.

### 4.2 Curly quotes

Use straight quotes in source files; model output often carries curly ones.

### 4.3 Title case

Sentence case in headings ("Robustness checks", not "Robustness Checks"), unless
the venue says otherwise.

### 4.4 Bold, mini-headings, emoji

No bolding without a reason; no vertical lists where every item opens with a bold
label and colon; no decorative emoji.

### 4.5 Hyphen pairs

Keep the hyphen before a noun ("a high-quality report"), drop it after ("the
report is high quality"). Watch for third-party, cross-functional, data-driven,
long-term, real-time, end-to-end.

---

## Group 5 · Filler and rhetoric

### 5.1 Filler phrases

"In order to achieve this" becomes "To achieve this". "Due to the fact that"
becomes "Because". "At this point in time" becomes "Now". "It is important to
note that the data shows" becomes "The data shows".

### 5.2 Qualifier pile-up

"to be fair", "it's also possible", "could potentially", "might arguably". Keep a
qualifier only when the source supports it and the meaning needs it.

### 5.3 Pseudo-depth

"The real question is", "at its core", "what really matters", "fundamentally",
"the deeper issue". State the point directly.

### 5.4 Announcing the next point

"Let's dive in", "here's what you need to know", "now let's look at", "without
further ado". Remove the announcement, not just its formal tone.

### 5.5 Heading echo

A heading followed by a sentence that only restates the heading. Cut the
restatement.

### 5.6 Forced punchlines

One short sentence can land emphasis; a row of fragments reads forced. Replace
with the specific claim.

### 5.7 Formulaic sayings

"X is the Y of Z", "X becomes a trap", "the language of", "the currency of".
Replace with the concrete claim.

### 5.8 Fake-candid openings

"Honestly?", "Look", "Here's the thing", "Let's be honest" as standalone hooks.
State the point.

### 5.9 Answering objections no one raised

"This isn't mainly about", "I'm not arguing that", "To be clear", "Don't get me
wrong". Remove only the unsupported defense; keep a named objection.

### 5.10 Rejecting fake alternatives

"A tempting approach would be", "One might be tempted to", "You might think…
but". Remove the straw option and state the real constraint.

### 5.11 Generic positive endings

End on the last concrete fact, not vague optimism ("The future looks bright…").
If the source states real plans, use those.

---

## Group 6 · Chatbot residue

### 6.1 Chatbot text

"I hope this helps", "Of course!", "Certainly!", "Would you like…", "let me know".
Strip greetings, offers, and closings from text that should stand alone.

### 6.2 Knowledge-limit disclaimers

"as of [date]", "up to my training update", "details are limited", "based on
available information", "likely [grew up/studied]". State what the source does
not show, or cut the sentence. Do not pass a guess off as fact.

### 6.3 Overly agreeable tone

"Great question! You're absolutely right…". Drop the praise and state the point.

---

## Rhythm, the highest-leverage fix 🔴

Uniform sentence length is the signature AI text and human text share least.
Detection: five-plus consecutive sentences of 20–30 words, low length variance
across a paragraph.

Fix: per ~200 words, force one short sentence (≤8 words) and one long one (≥40
words). Short sentences open questions or land conclusions ("The data say
otherwise."); long ones carry the evidence. Vary paragraph length too.

---

## Group 7 · Missing human texture (add, don't just strip)

Removing tells is only half the job. Text that is merely "clean" still reads as
AI: too even, too neutral, too smooth. A real researcher's prose is lumpy. Check
for these and add them back where they fit.

### 7.1 Mechanical causal connectors 🔴

AI marks every causal link explicitly; humans often leave the link implied.

Watch for dense therefore, thus, consequently, so that, because, taken together.
If a paragraph strings several, cut some and let the logic carry.

- Before: "Prices rose, therefore demand fell. Consequently firms cut output,
  so that supply shrank further."
- After: "Prices rose and demand fell. Firms cut output; supply shrank further."

### 7.2 Uniform paragraph arc 🔴

AI writes every paragraph the same way: a topic-sentence opener, a middle, and a
summary or transition closer. Humans do not.

Fix: vary where the point lands. Some paragraphs end abruptly on the evidence;
some open with the conclusion. Break the three-part rhythm.

### 7.3 Safe verbs 🔴

AI reaches for neutral verbs where a human would pick a sharper one.

Watch for is, are, remains, concludes, raises, matters, underperform — used where
undermine, erode, dwarf, propel, gut, unwind would carry more weight. Swap in a
vivid verb when it is accurate.

### 7.4 Abstract-noun subjects 🟡

AI likes "The mechanism", "That last possibility", "The subsequent literature",
"Projections" as sentence subjects. Vary the subject; lead with the actor or the
finding sometimes.

### 7.5 Missing subjective adverbs 🟡

AI avoids the words that mark a thinking person: arguably, admittedly,
strikingly, curiously, tellingly. Where the writer's judgment calls for one, use
it. Their absence is itself a tell.

### 7.6 "we" only in declarations 🟡

AI tends to use "we" in a set-piece ("We do not attempt to settle the debate")
rather than inside the reasoning ("we chose X over Y because…"). Move "we" into
the argument.

### 7.7 Irregular voice and rhythm 🟡

AI alternates active/passive and short/long too evenly. Humans are lumpy: several
short declaratives, then one long digression. Vary the pattern deliberately. Add
an occasional fragment, aside, or parenthetical.

### 7.8 Repeated parallel structures 🟡

AI writes "this is the direct effect … this is the indirect effect … this is the
economy-wide effect". Humans vary the phrasing. Keep one parallel set for real
emphasis; otherwise rewrite.

### 7.9 Stock academic set-phrases 🟢

Watch for polished clichés that read "textbook but anonymous": looming
exhaustion, run against intuition, unsettle policy design, at first glance,
lends support to. They are not wrong; they are just not yours. Replace with a
phrase specific to your argument.

---

## Group 8 · Content humanness (argue, don't survey)

Style rules fix how a paper sounds; this group fixes what it does. The deepest
tell in the test output was not a word choice. It was that the text surveyed the
debate without taking a side. A real researcher argues.

### 8.1 Take a position 🔴

Do not just report that "views differ" or "the evidence is mixed". State what you
think and defend it. A thesis, not a summary.

- Before: "The literature offers competing explanations for the rebound effect."
- After: "The economy-wide rebound is the one that matters for policy, and it is
  the least well measured."

### 8.2 Critique prior work 🔴

Name what a specific claim gets wrong or leaves out, rather than "some argue X,
others argue Y". Engage the strongest version of the opposing view, then say
where it breaks.

### 8.3 Make judgments 🟡

"The key flaw is…", "the more likely reading is…", "this matters because…".
Explicit evaluation, not neutral reporting.

### 8.4 Show your angle 🟡

Why this question, why this framing, what you bring to it. This is where "I
think" and "we argue" belong, inside the reasoning, not in a set-piece
declaration.

---

## False positives, do not treat any single item as proof

- Polished grammar and consistent style (editing is not AI).
- Mixed casual/formal register (field, age, or habit).
- Dry prose with none of the specific tells above.
- Formal or academic words in isolation.
- One transition word ("however") or one em dash.
- Curly quotes alone (macOS and Word auto-curl).
- A single short sentence for emphasis.
- Deliberate repeated openings for rhythm ("She came. She saw. She conquered.").
- Scope statements, legal or safety notices, real corrections.
- Real alternatives in a design argument.
- Unsourced claims (most of the web is unsourced).
- Quoted, titled, or proper-named text being discussed, not used.

Look for several patterns together. One em dash proves nothing; a handful of
stock patterns in one passage is stronger evidence.

## Human details to keep

These carry the writer's voice; keep them unless they hurt the meaning.

- Specific, unusual details (a real address, an odd quote).
- Unresolved tension ("I think this is mostly right, but it bothers me and I
  can't say exactly why.").
- Dated, era-bound references (slang, memes, in-jokes).
- Deliberate first-person choices the writer can justify.
- Variety in sentence length.
- Genuine asides or self-corrections ("(I keep wanting to say 'almost' here, but
  it really was certain.)").

---

## Chinese-manuscript appendix

For Chinese empirical papers the same logic holds, with these structural
signatures (the full ZH library can be added later):

1. Four-character formula phrases every 200 字 (综上所述 / 毋庸置疑 / 显而易见).
2. Stacked connectives (此外 / 因此 / 而且 / 在此基础上).
3. Subject avoidance (本文认为 / 相关研究表明, no named researcher).
4. Low sentence-length variance, clustered in 20–35 字.
5. Absolute conclusions (充分证明了 / 必然导致 / 毫无疑问).

Rhythm thresholds for Chinese: short sentence ≤15 字, long ≥50 字, danger zone
20–35 字. Targets: 知网 AMLC, 万方, 维普, Turnitin 中文版.
