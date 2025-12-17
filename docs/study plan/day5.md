Perfect 👍
Now we move to **Day 5–6: Trees & Recursion (MEDIUM SET)** — this is **extremely important for Google**, because they test:

* Recursive thinking
* DFS vs BFS choice
* Invariants
* Clean base cases
* Ability to explain traversal logic clearly

As requested:

* 📘 **Concepts & mental models first**
* 📘 **MEDIUM questions in detail (NO solutions initially)**
* ✅ **Solutions & deep explanations at the end**

---

# 🌳 DAY 5–6: TREES & RECURSION — CONCEPTS

## 1️⃣ Tree Basics (Must Be Automatic)

### Key Terms

* Root, leaf, height, depth
* Binary Tree vs Binary Search Tree (BST)
* Balanced vs skewed tree

### Tree Traversals

| Traversal   | Order               | Use Case               |
| ----------- | ------------------- | ---------------------- |
| Preorder    | Root → Left → Right | Copy tree, serialize   |
| Inorder     | Left → Root → Right | BST sorted order       |
| Postorder   | Left → Right → Root | Delete tree, bottom-up |
| Level Order | BFS                 | Shortest path          |

---

## 2️⃣ Recursion Mental Model (Google Favorite)

### Golden Rules

1. Define **what the function returns**
2. Base case
3. Recursive calls
4. Combine results

📌 Always explain:

> “This function returns ___ for subtree rooted at node.”

---

## 3️⃣ DFS vs BFS (When to Use)

| DFS                    | BFS                 |
| ---------------------- | ------------------- |
| Recursive              | Iterative           |
| Uses stack             | Uses queue          |
| Tree depth problems    | Level problems      |
| Lower memory sometimes | Finds shortest path |

---

## 4️⃣ Common Tree Patterns

| Pattern               | Examples         |
| --------------------- | ---------------- |
| Top-down recursion    | Path sum         |
| Bottom-up recursion   | Diameter, height |
| Divide & Conquer      | Balanced tree    |
| DFS + global variable | Max path sum     |

---

# 📘 MEDIUM PRACTICE QUESTIONS

❌ **NO SOLUTIONS YET – Attempt First**

---

## Q1️⃣ Binary Tree Level Order Traversal (BFS)

### Problem Statement

Given the root of a binary tree, return the **level order traversal** of its nodes’ values.

---

### Input

```
    3
   / \
  9  20
     / \
    15  7
```

### Output

```
[[3],[9,20],[15,7]]
```

---

### Follow-ups

1. Why BFS instead of DFS?
2. How do you track levels?
3. Time & space complexity?

---

## Q2️⃣ Maximum Depth of Binary Tree (Recursion)

### Problem Statement

Given the root of a binary tree, return its **maximum depth**.

---

### Input

```
    3
   / \
  9  20
     / \
    15  7
```

### Output

```
3
```

---

### Follow-ups

1. Why is this bottom-up?
2. Can you do it iteratively?
3. Space complexity?

---

## Q3️⃣ Diameter of Binary Tree (Bottom-Up DFS)

### Problem Statement

The **diameter** is the length of the longest path between any two nodes in a tree.

Return the diameter.

---

### Input

```
    1
   / \
  2   3
 / \
4   5
```

### Output

```
3
```

---

### Follow-ups

1. Why not compute height separately?
2. Why use a global variable?
3. Edge cases?

---

## Q4️⃣ Balanced Binary Tree

### Problem Statement

Determine if a binary tree is **height-balanced**.

---

### Definition

For every node:

```
|height(left) - height(right)| ≤ 1
```

---

### Follow-ups

1. Why naive approach is O(n²)?
2. How do you optimize?
3. What value do you return on imbalance?

---

## Q5️⃣ Lowest Common Ancestor (Binary Tree)

### Problem Statement

Given a binary tree and two nodes `p` and `q`, find their **lowest common ancestor (LCA)**.

---

### Input

```
         3
        / \
       5   1
      / \ / \
     6  2 0  8
```

LCA(5,1) = 3

---

### Follow-ups

1. Why postorder?
2. What if node doesn’t exist?
3. Difference between BT and BST LCA?

---

## Q6️⃣ Path Sum II (Top-Down DFS)

### Problem Statement

Return all root-to-leaf paths where the sum equals `targetSum`.

---

### Input

```
targetSum = 22
```

---

### Follow-ups

1. Why backtracking?
2. How do you avoid copying lists?
3. Space complexity?

---

## Q7️⃣ Binary Tree Right Side View

### Problem Statement

Return values visible when the tree is viewed from the right side.

---

### Input

```
    1
   / \
  2   3
   \   \
    5   4
```

### Output

```
[1,3,4]
```

---

### Follow-ups

1. BFS vs DFS?
2. How do you ensure rightmost node?
3. Time complexity?

---

# ✅ SOLUTIONS & IN-DEPTH EXPLANATIONS

(Only after attempting)

---

## ✅ Q1 Solution: Level Order Traversal

```java
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> res = new ArrayList<>();
    if (root == null) return res;

    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);

    while (!q.isEmpty()) {
        int size = q.size();
        List<Integer> level = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            TreeNode node = q.poll();
            level.add(node.val);
            if (node.left != null) q.offer(node.left);
            if (node.right != null) q.offer(node.right);
        }
        res.add(level);
    }
    return res;
}
```

### Explanation

* BFS processes level-by-level
* Queue size = nodes at current level

---

## ✅ Q2 Solution: Maximum Depth

```java
public int maxDepth(TreeNode root) {
    if (root == null) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
```

### Why Bottom-Up?

Depth depends on children’s depth.

---

## ✅ Q3 Solution: Diameter of Binary Tree

```java
int diameter = 0;

public int diameterOfBinaryTree(TreeNode root) {
    height(root);
    return diameter;
}

private int height(TreeNode node) {
    if (node == null) return 0;

    int left = height(node.left);
    int right = height(node.right);

    diameter = Math.max(diameter, left + right);
    return 1 + Math.max(left, right);
}
```

---

## ✅ Q4 Solution: Balanced Binary Tree

```java
public boolean isBalanced(TreeNode root) {
    return check(root) != -1;
}

private int check(TreeNode node) {
    if (node == null) return 0;

    int left = check(node.left);
    if (left == -1) return -1;

    int right = check(node.right);
    if (right == -1) return -1;

    if (Math.abs(left - right) > 1) return -1;
    return 1 + Math.max(left, right);
}
```

---

## ✅ Q5 Solution: Lowest Common Ancestor

```java
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null || root == p || root == q) return root;

    TreeNode left = lowestCommonAncestor(root.left, p, q);
    TreeNode right = lowestCommonAncestor(root.right, p, q);

    if (left != null && right != null) return root;
    return left != null ? left : right;
}
```

---

## ✅ Q6 Solution: Path Sum II

```java
public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
    List<List<Integer>> res = new ArrayList<>();
    dfs(root, targetSum, new ArrayList<>(), res);
    return res;
}

private void dfs(TreeNode node, int sum, List<Integer> path, List<List<Integer>> res) {
    if (node == null) return;

    path.add(node.val);
    if (node.left == null && node.right == null && sum == node.val) {
        res.add(new ArrayList<>(path));
    } else {
        dfs(node.left, sum - node.val, path, res);
        dfs(node.right, sum - node.val, path, res);
    }
    path.remove(path.size() - 1);
}
```

---

## ✅ Q7 Solution: Right Side View

```java
public List<Integer> rightSideView(TreeNode root) {
    List<Integer> res = new ArrayList<>();
    if (root == null) return res;

    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);

    while (!q.isEmpty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            TreeNode node = q.poll();
            if (i == size - 1) res.add(node.val);
            if (node.left != null) q.offer(node.left);
            if (node.right != null) q.offer(node.right);
        }
    }
    return res;
}
```

---

# 🎯 After Day 5–6 You Should Be Able To

* Write clean recursive solutions
* Choose BFS vs DFS confidently
* Explain tree problems clearly
* Avoid common recursion mistakes

---

## NEXT STEP?

👉 **Day 7–8: Graphs (BFS, DFS, Topo Sort, Union-Find)**
👉 **Hard Tree problems (Max Path Sum, Serialize/Deserialize)**
👉 **Google-style mock interview**

Just tell me 👍
