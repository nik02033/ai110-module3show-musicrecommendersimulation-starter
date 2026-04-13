# Model Card: Music Recommender Simulation

## Model Name

**VibeFinder 1.0** — a small classroom recommender that ranks songs from a CSV using taste tags and a few numbers.

---

## Goal / Task

The system tries to **suggest which songs in the catalog best fit a user’s profile**. It does not predict plays or skips from real behavior. It only scores each track against things like favorite genre, mood, target energy, and valence, then returns the top matches.

---

## Data Used

There are **20 songs** in `data/songs.csv`. Each row has **genre, mood, energy, tempo (bpm), valence, danceability, and acousticness**. Genres range from pop and lofi to classical, blues, and trap, but the list is still small. Many real genres and moods are missing, so some users never get a clean genre match. **Indie pop** and **pop** are different strings, which trips up matching if we do not normalize labels.

---

## Algorithm Summary

Each song gets **points** that add up to one score. **Genre match** adds the most. **Mood match** adds a smaller chunk. **Energy** and **valence** use “closeness”: the nearer the song is to what you asked, the more points. There is a small **acoustic vs produced** bonus if the song matches that preference. After every song has a score, the program **sorts high to low** and shows the top few. A separate run can **lower genre weight and raise energy weight** to see how sensitive the list is.

---

## Observed Behavior / Biases

When someone asked for **pop**, **melancholic** mood, and **very high energy**, **Gym Hero** still won. Genre and energy mattered more than mood, and there is almost no melancholic pop in the data. So the system can **feel loud and “wrong”** even when it is following the math. That is a **filter bubble** risk: the same kind of track keeps winning if your weights favor genre and hype.

---

## Evaluation Process

I ran **`python -m src.main`** with four profiles: high-energy pop, chill lofi, deep intense rock, and an edge case (sad mood + club energy). The first three mostly matched intuition. The edge case exposed the bias above. I also ran **`--experiment-weights`** (halve genre, double energy). Top order often stayed the same, but **energy** mattered more in the printed reasons. I compared runs side by side in the terminal and wrote short notes in `reflection.md`.

---

## Intended Use and Non-Intended Use

**Intended:** Learning how recommenders turn **features + rules** into a ranked list. Demos in class, debugging scoring, and talking through tradeoffs with plain-language reasons.

**Not intended:** Real streaming products, personalized playlists for paying users, or any decision that should rely on fairness, diversity, or listening history. It does not know what you actually played, skipped, or liked.

---

## Ideas for Improvement

1. **Group similar genres** (e.g. treat indie pop like pop when the user says pop).  
2. **Penalize** big mood or valence mismatches so sad requests do not always lose to loud pop.  
3. **Force variety** in the top five (different artists or genres after the first pick).

---

## Personal Reflection

My biggest learning moment was the **adversarial profile**: the output looked silly emotionally, but the code was doing exactly what we weighted. That split between “correct math” and “good vibe” stuck with me.

**AI tools** helped me draft scoring ideas and boilerplate fast. I still had to **double-check** weights, CSV fields, and whether explanations matched the numbers—models can sound confident when the logic is wrong.

It surprised me that **adding and sorting** could still *feel* like a real recommender when the profiles matched the data. The reasons list made that illusion break in a useful way when things went off the rails.

**If I extended the project**, I would add real **skip/like** simulation or collaborative-style “users like you” on top of content scores, and a **diversity** rule so Gym Hero does not dominate every nearby profile.
