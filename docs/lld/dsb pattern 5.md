Perfect timing, Amar.
Binary Search is **one of the top-3 most important FAANG patterns**, and Google/Meta interviewers expect you to **recognize it even when it’s completely hidden**.

I’ll teach this **exactly the way strong Google/Meta candidates internalize it** — not as an algorithm, but as a **thinking framework**.

---

# Pattern 5: Binary Search

## (Classic + Answer Space) — FAANG Mastery Guide

---

## 0️⃣ Interviewer Expectation (Read this first)

> **Binary Search ≠ “search in sorted array”**

For Google/Meta:

* Binary Search = **monotonic decision problem**
* You are not searching an element — you are **searching a boundary**
* Often:

  * Array is not explicitly sorted
  * You are searching an **answer**, not an index
  * Problem looks like DP / Greedy / Math at first glance

If you master this, you unlock **30–40% of Medium + Hard problems**.

---

## 1️⃣ Binary Search Thinking Model (FAANG Mental Model)

Interviewers expect you to think like this:

```
1. Can I define a search space?
2. Is there a monotonic property?
3. Can I answer YES/NO for a given mid?
4. What boundary am I looking for?
```

If all 4 are YES → Binary Search.

---

## 2️⃣ Two Faces of Binary Search

### A. Classic Binary Search

> Search in a **sorted structure**

Examples:

* Search element
* First / last occurrence
* Lower bound / upper bound
* Rotated sorted array
* Nearly sorted array

### B. Answer Space Binary Search (MOST IMPORTANT)

> Search over **possible answers**, not array indices

Examples:

* Minimum feasible value
* Maximum possible capacity
* Kth smallest / largest
* Minimum time / days / speed
* Optimize something

💡 **90% FAANG binary search questions are Answer Space**

---

## 3️⃣ Monotonic Property (Heart of Binary Search)

Binary Search works ONLY when this exists:

```
False False False True True True
```

OR

```
True True True False False
```

That’s it.

### Examples:

* Can finish in X days? → YES/NO
* Is capacity C sufficient? → YES/NO
* Can we place K items with distance D? → YES/NO

If answer changes only once → Binary Search applicable.

---

## 4️⃣ Classic Binary Search — Deep Understanding

### Template (Index-based)

```java
while (low <= high) {
    mid = low + (high - low) / 2;
    if (condition(mid)) {
        answer = mid;        // optional
        high = mid - 1;      // move left
    } else {
        low = mid + 1;       // move right
    }
}
```

### What Interviewers Test Here

* Overflow-safe mid
* Boundary handling
* Infinite loop avoidance
* Off-by-one correctness
* Clear invariant explanation

---

## 5️⃣ Classic Variants You MUST Master

### 1. First occurrence

### 2. Last occurrence

### 3. Lower bound (>= target)

### 4. Upper bound (> target)

### 5. Rotated sorted array

### 6. Binary search on answer in sorted matrix

💡 If you can’t explain **why `high = mid - 1`**, you’re not ready.

---

## 6️⃣ Answer Space Binary Search (Google Favorite)

### Core Idea

Instead of:

```
Search index
```

You do:

```
Search range of possible answers
```

### General Template

```java
low = min_possible_answer
high = max_possible_answer

while (low <= high) {
    mid = low + (high - low) / 2;
    if (isValid(mid)) {
        answer = mid;
        high = mid - 1;   // try better
    } else {
        low = mid + 1;
    }
}
```

---

## 7️⃣ How to Identify Answer Space Binary Search

Interviewers hide it under:

* "Minimum"
* "Maximum"
* "Optimize"
* "Capacity"
* "Kth"
* "At least"
* "At most"
* "Within X days"
* "Smallest possible"

🚨 **If problem asks for optimal value → THINK BINARY SEARCH**

---

## 8️⃣ How to Find Search Space (Critical Skill)

| Problem Type | low         | high         |
| ------------ | ----------- | ------------ |
| Min capacity | max(weight) | sum(weight)  |
| Kth smallest | min value   | max value    |
| Min time     | 1           | max time     |
| Distance     | 0           | max distance |

Interviewers expect you to **justify bounds logically**.

---

## 9️⃣ isValid(mid) — Where You Win or Lose

This function:

* Must be **O(n)** or better
* Must be **monotonic**
* Usually greedy
* Never changes search direction randomly

Explain this clearly → interviewer confidence ↑↑

---

## 🔟 Typical Mistakes (Instant Reject Signals)

❌ Binary search without monotonic proof
❌ Wrong boundaries
❌ Infinite loops
❌ Confusing index search with answer search
❌ Overcomplicated isValid
❌ Not explaining why mid works

---

## 1️⃣1️⃣ Medium & Hard FAANG-Level Problems (Try First)

### Medium

1. Capacity To Ship Packages Within D Days
2. Koko Eating Bananas
3. Find Minimum in Rotated Sorted Array
4. Search in Rotated Sorted Array

### Hard

5. Median of Two Sorted Arrays
6. Split Array Largest Sum

⛔ **Do NOT jump to solution yet**
Try to identify:

* Search space
* Monotonic condition
* isValid logic

---

## 1️⃣2️⃣ Interviewer Cross-Questions You Must Answer

Be ready to explain:

* Why binary search works here?
* What is the monotonic property?
* Why this low and high?
* What happens if constraints increase?
* Time complexity?
* Can we optimize isValid?
* Edge cases?

---

## 1️⃣3️⃣ Binary Search Master Checklist

You are FAANG-ready when you can:

✔ Identify binary search in disguised problems
✔ Explain monotonicity clearly
✔ Write correct template without bugs
✔ Derive bounds logically
✔ Handle off-by-one confidently
✔ Solve hard optimization problems

---

## Next Step (Very Important)

I suggest this order:
1️⃣ Solve **2 classic + 2 answer-space** problems alone
2️⃣ Then I’ll:

* Walk through **full solutions**
* Show **Google-style explanation**
* Teach **pattern variants & traps**

👉 **Say “Start Solutions”** when ready
or
👉 Ask for **Binary Search problem breakdown Google vs Meta style**
