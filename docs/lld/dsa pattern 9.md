Perfect. **Tree DFS** is a *core FAANG pattern* — Google / Meta expect you not just to “code DFS”, but to **reason with recursion, states, and invariants**.
I’ll teach this the **exact way interviewers think**.

---

# 🌳 Pattern 10: Tree DFS — FAANG Mastery

---

## 1️⃣ What Tree DFS *Really* Is (Interview Definition)

> **Tree DFS = systematic exploration of a tree using recursion, where each recursive call solves a subproblem rooted at a node and returns meaningful information to its parent.**

Interviewers test:

* Your **recursive thinking**
* Your **ability to define return values**
* Your **control over global vs local state**
* Your **ability to convert intuition → recursion**

---

## 2️⃣ The 3 DFS Traversals (But Interview Meaning)

| Traversal | Order               | Interview Use                     |
| --------- | ------------------- | --------------------------------- |
| Preorder  | Node → Left → Right | Build paths, copy tree, serialize |
| Inorder   | Left → Node → Right | BST logic                         |
| Postorder | Left → Right → Node | Heights, balances, DP on trees    |

🔑 **90% Tree DFS interview problems use POSTORDER**

Why?

> Children compute first → parent decides.

---

## 3️⃣ The ONE Mental Model You Must Master

### Interviewer thinks like this:

> “What information does each node need from its children to solve the problem?”

That becomes your **DFS return value**.

---

## 4️⃣ The Universal Tree DFS Template (Memorize This)

```java
ReturnType dfs(TreeNode node) {
    if (node == null) {
        return BASE_VALUE;
    }

    ReturnType left = dfs(node.left);
    ReturnType right = dfs(node.right);

    // Use left + right to compute answer for current node
    ReturnType current = merge(node, left, right);

    // Optionally update global answer
    updateGlobal(current);

    return current;
}
```

🧠 **Every Tree DFS problem fits this template**

---

## 5️⃣ 5 Core Tree DFS Problem Types (FAANG MUST-KNOW)

---

### TYPE 1️⃣ Path Problems (Root → Leaf / Any Path)

Examples:

* Path Sum
* Maximum Path Sum
* Binary Tree Paths

#### Thinking Pattern

Ask:

* Is path **root to leaf**?
* Or **any node to any node**?

| Case        | State Needed      |
| ----------- | ----------------- |
| Root → Leaf | Current sum       |
| Any Path    | Max downward path |

🔑 Trick:
**Global variable for answer, return best downward path**

---

### TYPE 2️⃣ Subtree Information Problems (Postorder Kings)

Examples:

* Height of tree
* Diameter
* Balanced Binary Tree
* Largest BST in Binary Tree

#### Key Insight

Each node returns:

* Height
* Validity
* Size
* Min / Max

Example return:

```java
class Info {
    int height;
    boolean balanced;
}
```

---

### TYPE 3️⃣ Tree DP (Hard but High-Value)

Examples:

* House Robber III
* Binary Tree Cameras
* Maximum Sum Independent Set

#### Pattern

Each node returns **multiple states**

Example:

```java
int[] dfs(node) {
    // [rob, notRob]
}
```

Interviewers LOVE this pattern.

---

### TYPE 4️⃣ BST-Specific DFS

Examples:

* Validate BST
* Kth smallest
* LCA in BST

Use:

* Inorder traversal
* Range propagation (`min`, `max`)

---

### TYPE 5️⃣ Count / Aggregate Problems

Examples:

* Count good nodes
* Sum of left leaves
* Count univalue subtrees

Pattern:

* Pass context from parent
* Aggregate results upward

---

## 6️⃣ Global vs Return Value (CRITICAL INTERVIEW SKILL)

### Rule:

| Situation                      | Use    |
| ------------------------------ | ------ |
| Answer is part of subtree      | RETURN |
| Answer spans multiple subtrees | GLOBAL |

Example:

* Height → return
* Diameter → global

---

## 7️⃣ How Google/Meta Judge Tree DFS Answers

They check:

1. Do you **define return type clearly**?
2. Do you explain **what dfs returns**?
3. Do you identify **base case correctly**?
4. Do you avoid recomputation?
5. Can you **modify recursion under constraints**?

🚫 Red flags:

* Random recursion without explanation
* No clear invariant
* Using globals unnecessarily

---

## 8️⃣ Medium–Hard FAANG Problems (Try First)

### Medium

1. Path Sum II
2. Diameter of Binary Tree
3. Balanced Binary Tree
4. Binary Tree Right Side View

### Hard

5. Binary Tree Maximum Path Sum
6. House Robber III

⚠️ Do **NOT** jump to code.
First write:

* What dfs returns
* What global tracks
* Base case

---

## 9️⃣ Interview Simulation Example (Thinking First)

**Problem:** Diameter of Binary Tree

Interviewer asks:

> “What does dfs return?”

Correct answer:

> “Height of subtree rooted at this node.”

Then:

> “When do you update diameter?”

Answer:

> “At each node using leftHeight + rightHeight.”

🔥 This explanation matters more than code.

---

## 🔟 Mastery Checklist (You’re Interview-Ready When)

✔ You can define dfs return in one sentence
✔ You know when to use postorder
✔ You can solve without drawing tree
✔ You can convert brute force → DFS
✔ You can modify return type confidently

---

## Next Step (Your Learning Path)

Next patterns that **pair perfectly** with Tree DFS:

* **Pattern 11: Tree BFS**
* **Pattern 12: Binary Search Tree**
* **Pattern 13: Tree DP (Advanced)**

If you want, I can:

* Deep-dive **Tree DFS with dry runs**
* Do **one hard problem step-by-step like Google**
* Create **Tree DFS decision flowchart**

Just tell me how you want to continue 🔥
