Perfect. **Linked List is a *core signal pattern*** in Google / Meta interviews because it tests **pointer thinking**, **in-place mutation**, and **edge-case discipline**.
I’ll teach it the way interviewers *expect you to think*, not just solve.

---

# **Pattern 6: Linked List**

### *(Fast–Slow Pointer + Reversal + Structural Tricks)*

---

## 1️⃣ Why Google / Meta love Linked Lists

Interviewers use Linked Lists to test:

| Skill                  | Why it matters                    |
| ---------------------- | --------------------------------- |
| Pointer manipulation   | You must reason without indexes   |
| In-place algorithms    | No extra memory                   |
| Edge-case awareness    | `null`, 1 node, 2 nodes           |
| Algorithmic maturity   | Detect cycles, reverse structures |
| Calm under constraints | Very easy to break links          |

> **If you master Linked Lists, your pointer confidence jumps massively.**

---

## 2️⃣ Mental Model (CRITICAL)

### 🔗 What a Linked List really is

```
[value | next] → [value | next] → [value | null]
```

* No random access
* Only **directional traversal**
* Once a link is broken → data is LOST

> 🔑 Rule: **Always save `next` before changing pointers**

---

## 3️⃣ Core Sub-Patterns (Interview Canon)

Google / Meta reduce **almost every LL problem** to one of these:

### A. Fast–Slow Pointer

Used when:

* Midpoint
* Cycle detection
* Palindrome
* Happy number
* K-th from end (variant)

### B. Reversal

Used when:

* Reverse list
* Reverse sublist
* Palindrome
* Reorder list
* Add numbers

### C. Dummy Node Technique

Used when:

* Head may change
* Deletions
* Merging lists

### D. Two-List Merge / Split

Used when:

* Merge sorted lists
* Partition list
* Odd–Even reordering

---

## 4️⃣ Pattern A: Fast–Slow Pointer (Tortoise–Hare)

### 🔹 Idea

```
slow → 1 step
fast → 2 steps
```

When `fast` ends → `slow` is at **middle**

---

### 🔹 Why it works (INTERVIEW INSIGHT)

Let list length = `n`

| Case | Slow lands                |
| ---- | ------------------------- |
| Odd  | Exact middle              |
| Even | First middle (important!) |

> Interviewers expect you to **know where slow stops**.

---

### 🔹 Canonical Uses

#### 1. Find Middle of Linked List

#### 2. Detect Cycle

#### 3. Find Cycle Start

#### 4. Palindrome Linked List

#### 5. Reorder List

---

### 🔹 Cycle Detection (Floyd’s Algorithm)

**Key Insight (must say aloud):**

> If a cycle exists, fast and slow **must meet**.

**Cycle start logic:**

* Distance from head to cycle start = distance from meeting point to cycle start

---

### 🔹 Interview Red Flags

❌ Not checking `fast != null && fast.next != null`
❌ Infinite loop
❌ Wrong middle for even length

---

## 5️⃣ Pattern B: Reversal (MOST IMPORTANT)

### 🔹 Core Operation

You reverse links, not values.

---

### 🔹 Iterative Reverse (Template)

```
prev = null
curr = head

while curr != null:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

return prev
```

---

### 🔹 Why Interviewers Love This

* Tests **order of operations**
* One wrong line = broken list
* Must explain pointer transitions clearly

---

### 🔹 Dry Run (say this in interview)

```
1 → 2 → 3 → null

Iteration 1:
1 → null
prev = 1
curr = 2

Iteration 2:
2 → 1 → null
prev = 2
curr = 3
```

---

## 6️⃣ Combining Fast–Slow + Reverse (Power Combo)

### 🔥 Palindrome Linked List

**Steps interviewers expect:**

1. Find middle (fast–slow)
2. Reverse second half
3. Compare halves
4. (Optional) Restore list

---

### 🔥 Reorder List

```
1 → 2 → 3 → 4 → 5
↓
1 → 5 → 2 → 4 → 3
```

Steps:

1. Find middle
2. Reverse second half
3. Merge alternately

---

## 7️⃣ Dummy Node Technique (Interview Gold)

### 🔹 Why needed?

Head may change (delete, insert)

### 🔹 Pattern

```
dummy → head
prev = dummy
```

Used in:

* Remove Nth node from end
* Merge lists
* Partition list

> Dummy node avoids **special-case hell**

---

## 8️⃣ Recognition Guide (VERY IMPORTANT)

| Problem Statement       | Pattern             |
| ----------------------- | ------------------- |
| “Find middle”           | Fast–Slow           |
| “Detect loop”           | Fast–Slow           |
| “Check palindrome”      | Fast–Slow + Reverse |
| “Reverse from m to n”   | Reversal            |
| “Remove / Insert nodes” | Dummy Node          |
| “Reorder / Alternate”   | Split + Reverse     |

---

## 9️⃣ Google / Meta Medium–Hard Problems (TRY FIRST)

### Medium

1. Middle of the Linked List
2. Linked List Cycle II
3. Remove Nth Node From End
4. Palindrome Linked List

### Hard

5. Reorder List
6. Reverse Nodes in k-Group

---

## 🔟 How Interviewers Evaluate You

They don’t care only about correctness.

They watch:

* Do you draw pointers?
* Do you state invariants?
* Do you protect `next` before change?
* Do you handle edge cases calmly?

---

## 1️⃣1️⃣ Mistakes That Kill Interviews

❌ Forgetting to store `next`
❌ Not handling `head == null`
❌ Overusing extra memory
❌ Panicking when links break

---

## 1️⃣2️⃣ Mastery Plan (Follow This)

**Day 1**

* Reverse LL
* Middle
* Cycle detection

**Day 2**

* Palindrome
* Remove Nth
* Merge lists

**Day 3**

* Reorder list
* k-Group reversal

---

## Final Interview Mindset

> “Linked List problems are not about cleverness.
> They are about **discipline, order, and pointer respect**.”

---

If you want, next I can:

* 🔥 Do **step-by-step dry runs** exactly like whiteboard interviews
* 🔥 Solve **Reorder List / k-Group** with diagram thinking
* 🔥 Give you **FAANG cross-questions + ideal answers**

Just tell me 👉 **which one next**
