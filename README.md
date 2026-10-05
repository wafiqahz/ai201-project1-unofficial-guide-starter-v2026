# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
     I picked the "campus life" corpus, which includes short posts about student life. The corresponding model can answer questions about student advice and insights on administrative tasks, specific classes, and dining and housing information. Note that my model is specific to the college campus that the corpus is sourced from, since this sort of information changes from college to college.

## Chunking Strategy for Campus Life

**Chunk size:** Keep 800 characters, i.e., one chunk per document. The 88 documents are 178-549 characters, and each post holds a topic, contextualized by its title. Although I heavily considered splitting at paragraph breaks, this would guarantee loss of context, because the title is absolutely ESSENTIAL to make sense of pronouns ("it") in the post. Keeping the chunking size 800 characters ensures that if slightly longer documents are added later, the chunker can manage the new information correctly.
**Overlap:** 0. Since we will not be chunking individual posts, there should be no need for overlap to maintain context/

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents`

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
Which dorms have students NOT shared laundry costs for?

**Answer:**

```
Based on the provided documents, Tamsin Court has in-unit washer-dryers, so laundry costs are not charged per wash/dry cycle like the other buildings (housing_tamsin_court.txt).

Sources retrieved: housing_aldridge_hall.txt, housing_calder_annexe.txt, housing_innisfree_hall.txt, housing_old_brewhouse_laundry.txt, housing_tamsin_court.txt
```

**My relevance cutoff:** 0.475, because the largest distance for an in-scope question was 0.470, and the smallest distance for an out-of-scope question was 0.477. Since my question about the gym is probably as close semantically than an out-of-scope question can get, I don't think the best distance for an out-of-scope question can get much lower. Thus, I have set my cutoff to be in the gap, but closer to the out-of-scope upper limit to allow for more leeway for in-scope questions.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| What is an advantage to declaring my major early? | Y | 0.225 |
| What CS courses have students given advice about? | Y | 0.470 |
| When do students recommend going to Verrill Street Grill? | Y | 0.324 |
| Which dorms have students NOT shared laundry costs for? | Y | 0.397 |
| Which study rooms should I book if I want to use the whiteboard? | Y | 0.354 |
| What is the capital of Mongolia? | N | 0.825 |
| How do I change the oil in a diesel engine? | N | 0.934|
| What time does the campus gym open? | N | 0.477 |
| What is the recommended dosage of ibuprofen for a headache? | N | 0.844 |
| How do I write a for loop in Rust? | N | 0.896 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**When I first ran the app.py commands in the terminal, I got the following message: "Error executing model: Error computing NN outputs." I pasted the error into Claude Code, and it explained that this is a known problem for CoreML running on some macOS versions, and told me to switch to running the model on the CPU. Thus, I made the corresponding change in line 67 of store.py.

**2.**When I ran my out-of-scope question about what time the campus gym opens, the result printed out a best distance of 0.477, which was below the then set cutoff of 0.6, but the model still didn't answer the question. I asked Claude how that was possible, and it explained that althout the cutoff gate let the question through, the model followed the prompt instructions and refused to answer a question it didn't have information on. I used Claude's explanation to modify Criteria 3 so that either the cutoff gate or the model's prompt instruction works so that the system doesn't answer out-of-scope questions.

UNIT 2
**1.**Claude Code helped me build hybrid search when I was considering that for my improvement for milestone 4. However, I decided against this improvement, since it didn't fix my missed criteria issue that I diagnosed, and Claude Code helped revert my code back to what it was before hybrid search was added.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | - | - | MET |
| 4. Chunks are a certain size | 150-550 chars | 5/5 | 5/5 | 5/5 | MET |
| 5. All parts of the model's answer comes from cited documents | 5 of 5 | 5/5 | 5/5 | 4/5 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### Sample question: What do students say is an advantage to declaring your major early? — run 1

#### Criterion 1: retrieved chunks contain the answer

Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_graduation_requirements.txt, admin_housing_lottery.txt, admin_pass_fail_option.txt

'admin_declaring_a_major.txt':
```
On the declaring a major

You declare at the end of your second semester, or later if you need to. There's no penalty for declaring late and no advantage to declaring early except that it assigns you a departmental adviser, who is generally more useful than the general one.
```

Produced by: store.py::search

#### Criterion 2: every answer names a source

Answer:According to `admin_declaring_a_major.txt`, there is no advantage to declaring early except that it assigns you a departmental adviser.

Produced by: generate.py::answer_from_chunks

#### Criterion 3: Gate stops out-of-corpus questions
| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| What time does the campus gym open? | 0.477 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |

Produced by: run_eval.py::check_out_of_scope, using gate.py::check

#### Criterion 4: Chunks are a certain size

88 chunks, 317 characters on average (shortest 178, longest 549)

Produced by: chunker.py::split_documents

#### Criterion 5: all parts of the model's answer comes from cited documents

Answer:
```
According to `admin_declaring_a_major.txt`, there is no advantage to declaring early except that it assigns you a departmental adviser.
```

'admin_declaring_a_major.txt':
```
On the declaring a major

You declare at the end of your second semester, or later if you need to. There's no penalty for declaring late and no advantage to declaring early except that it assigns you a departmental adviser, who is generally more useful than the general one.
```

All parts of the model's answer did come from the cited document.

Produced by: generate.py::answer_from_chunks

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | One of the answers in run 3 didn't include the expected answer phrase, but since the criteria only asks for 4/5 passes, it is still met. |
| 2 | Every answer names a source | MET | All questions in all runs cite at least 1 source. |
| 3 | Gate stops out-of-corpus questions | MET | This is a deterministic check, so only one run is needed. The single run resulted in the model refusing to answer all out-of-scope questions. |
| 4 | Chunks are a certain size | MET | This isn't dependent on runs, but the indexing. As discussed in UNIT 1, this chunking criteria is appropriate for the campus life corpus. |
| 5 | All parts of the model's answer comes from cited documents | MISSED | Run 3 of question 1 resulted in the model providing an incorrect answer, and this answer does not match what is said in the document the answer cites. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

     Criterion 5 was missed, due to a run of question one ("What do students say is an advantage to declaring your major early?").
     
     Stage: Generation
     In the correct document in the corpus, the answer is there is "no advantage to declaring early except that it assigns you a departmental adviser", and during the generation stage, the model missed the except clause during a run that it caught in the other two runs. Thus, the answer contradicts the document it cited, resulting in missing criteria 5. (Retrieval returned the correct document inn all 3 runs, at the same distance 0.264.) 

## The Improvement

**What I changed:** I will add the following to the prompt: "Keep any conditions or exceptions the document states ("except", "unless", "only if")."


**Why I picked it:**Since my diagnosis was a generation-stage issue, I need to fix the prompt. The new line added to the prompt directly tries to improve the issue that caused criteria 5 to be missed earlier, when the model ignored an except clause.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | - | - | MET |
| 4. Chunks are a certain size | 150-550 chars | 5/5 | 5/5 | 5/5 | MET |
| 5. All parts of the model's answer comes from cited documents | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->
     According to the test, the change to the prompt did help. During all runs, the model's answers to the "declaring an early major advantage" question does not miss the "except" clause. However, since it was only a 1-run miss during the first test, more runs should be run to ensure this issue was actually solved.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->
     Currently, all my criteria are met. However, I believe that during my testing, some of my variables like top_k and threshold were not completely fine-tuned. For example, my threshold=0.475, which is oddly specific and is based on my test of only 10 questions. These variables may not be viable for a largest set of questions, so I would write many more test questions to further understand the gap between in-scope and out-of-scope questions. This would allow me to further finetune the threshold value.

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
The chunking criteria did not feel useful, since my chunker keeps each campus life post whole. I would replace it with a criterion that tests whether keeping posts whole actually helps retrrieval. For example, "For 3 of 5 test questions, the complete answer sits in a single chunk that ranks in the top 2." I set the criteria to only 3 of 5, since the scope of some questions may be larger than a single post. However, most questions aimed at the model should be able to be answered with one post for efficiency and less inaccuracy when combining/comparing chunks.
