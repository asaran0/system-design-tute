Excellent 👍
Now let’s **raise the bar**. These are **HARD / Google-level problems** for **Day 5–6 (Trees & Recursion)** and **Day 7–8 (Graphs)**.

⚠️ **Important rule (Google style)**

* Read → Think → Dry run → Code
* ❌ **No solutions first**
* ✅ **Solutions & deep explanations ONLY at the end**

---

# 🔥 HARD PRACTICE SET

## Day 5–6 (Trees & Recursion) + Day 7–8 (Graphs)

---

# 🌳 DAY 5–6: TREES & RECURSION (HARD)

---

## 🌲 Q1. Binary Tree Maximum Path Sum

### Problem

Given a non-empty binary tree, find the **maximum path sum**.

A path:

* Can start and end at any node
* Must follow parent-child connections
* Must contain **at least one node**

---

### Example

```
       -10
       /  \
      9   20
          / \
         15  7
```

### Output

```
42  (15 → 20 → 7)
```

---

### What makes it HARD?

* Path can **turn at any node**
* You must decide **what to return** vs **what to store globally**

---

## 🌲 Q2. Serialize and Deserialize Binary Tree

### Problem

Design an algorithm to serialize and deserialize a binary tree.

---

### Requirements

* Must support negative values
* Tree structure must be preserved
* Should handle null nodes

---

### Follow-ups

1. Preorder vs Level Order?
2. Why include null markers?
3. Time & space complexity?

---

## 🌲 Q3. Lowest Common Ancestor of Binary Tree (No Parent Pointer)

### Problem

Find LCA of two nodes in a binary tree.

---

### Constraints

* Nodes can be anywhere
* Tree is not a BST

---

### Follow-ups

1. What if one node does not exist?
2. How do you optimize?

---

## 🌲 Q4. Recover Binary Search Tree

### Problem

Two nodes of a BST are swapped by mistake. Recover the tree **without changing its structure**.

---

### Follow-ups

1. Inorder traversal property?
2. Can you do it in O(1) space?

---

## 🌲 Q5. Binary Tree Cameras

### Problem

Place cameras such that every node is monitored.

Camera monitors:

* Itself
* Parent
* Children

Return minimum number of cameras.

---

### Why Google Likes It?

* Greedy + Postorder
* Multi-state recursion

---

# 🌐 DAY 7–8: GRAPHS (HARD)

---

## 🌐 Q6. Alien Dictionary (Topological Sort)

### Problem

Given words sorted lexicographically in an alien language, determine the order of characters.

---

### Example

```
["wrt","wrf","er","ett","rftt"]
```

### Output

```
"wertf"
```

---

### Traps

* Prefix issue
* Cycle detection
* Multiple valid orders

---

## 🌐 Q7. Critical Connections in a Network (Tarjan)

### Problem

Find all **bridges** in a network.

---

### Definition

An edge whose removal disconnects the graph.

---

### Why HARD?

* DFS timestamps
* Low-link values

---

## 🌐 Q8. Word Ladder II

### Problem

Find **all shortest transformation sequences** from `beginWord` to `endWord`.

---

### Constraints

* Return all paths
* Use BFS + DFS

---

### Why HARD?

* Path explosion
* Backtracking on BFS tree

---

## 🌐 Q9. Minimum Cost to Connect All Points (MST)

### Problem

Given points in 2D, connect all with minimum cost.

---

### Approaches

1. Prim’s Algorithm
2. Kruskal + Union-Find

---

### Follow-ups

* Time complexity tradeoffs?
* Why Union-Find?

---

## 🌐 Q10. Remove Invalid Parentheses (Graph / BFS)

### Problem

Remove minimum number of invalid parentheses to make string valid.

---

### Why HARD?

* BFS state pruning
* Avoid duplicates
* Stop at correct level

---

---

# ✅ SOLUTIONS & IN-DEPTH EXPLANATIONS

⚠️ **Only read now if you attempted**

---

# ✅ Q1. Binary Tree Maximum Path Sum

### Key Insight

* Return **max downward path**
* Track **global max including split**

```java
int max = Integer.MIN_VALUE;

public int maxPathSum(TreeNode root) {
    dfs(root);
    return max;
}

private int dfs(TreeNode node) {
    if (node == null) return 0;

    int left = Math.max(0, dfs(node.left));
    int right = Math.max(0, dfs(node.right));

    max = Math.max(max, left + right + node.val);

    return node.val + Math.max(left, right);
}
```

---

# ✅ Q2. Serialize & Deserialize Tree

```java
public String serialize(TreeNode root) {
    StringBuilder sb = new StringBuilder();
    serializeHelper(root, sb);
    return sb.toString();
}

private void serializeHelper(TreeNode node, StringBuilder sb) {
    if (node == null) {
        sb.append("null,");
        return;
    }
    sb.append(node.val).append(",");
    serializeHelper(node.left, sb);
    serializeHelper(node.right, sb);
}

public TreeNode deserialize(String data) {
    Queue<String> q = new LinkedList<>(Arrays.asList(data.split(",")));
    return deserializeHelper(q);
}

private TreeNode deserializeHelper(Queue<String> q) {
    String val = q.poll();
    if (val.equals("null")) return null;

    TreeNode node = new TreeNode(Integer.parseInt(val));
    node.left = deserializeHelper(q);
    node.right = deserializeHelper(q);
    return node;
}
```

---

# ✅ Q3. LCA of Binary Tree

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

# ✅ Q4. Recover BST

```java
TreeNode first = null, second = null, prev = null;

public void recoverTree(TreeNode root) {
    inorder(root);
    int temp = first.val;
    first.val = second.val;
    second.val = temp;
}

private void inorder(TreeNode root) {
    if (root == null) return;

    inorder(root.left);

    if (prev != null && root.val < prev.val) {
        if (first == null) first = prev;
        second = root;
    }
    prev = root;

    inorder(root.right);
}
```

---

# ✅ Q5. Binary Tree Cameras

```java
int cameras = 0;
final int NOT_COVERED = 0, HAS_CAMERA = 1, COVERED = 2;

public int minCameraCover(TreeNode root) {
    return dfs(root) == NOT_COVERED ? cameras + 1 : cameras;
}

private int dfs(TreeNode node) {
    if (node == null) return COVERED;

    int left = dfs(node.left);
    int right = dfs(node.right);

    if (left == NOT_COVERED || right == NOT_COVERED) {
        cameras++;
        return HAS_CAMERA;
    }
    if (left == HAS_CAMERA || right == HAS_CAMERA)
        return COVERED;

    return NOT_COVERED;
}
```

---

# ✅ Q6. Alien Dictionary

```java
public String alienOrder(String[] words) {
    Map<Character, Set<Character>> graph = new HashMap<>();
    Map<Character, Integer> indegree = new HashMap<>();

    for (String w : words)
        for (char c : w.toCharArray())
            indegree.put(c, 0);

    for (int i = 0; i < words.length - 1; i++) {
        String w1 = words[i], w2 = words[i + 1];
        if (w1.startsWith(w2) && w1.length() > w2.length()) return "";

        for (int j = 0; j < Math.min(w1.length(), w2.length()); j++) {
            if (w1.charAt(j) != w2.charAt(j)) {
                if (graph.computeIfAbsent(w1.charAt(j), k -> new HashSet<>())
                        .add(w2.charAt(j)))
                    indegree.put(w2.charAt(j), indegree.get(w2.charAt(j)) + 1);
                break;
            }
        }
    }

    Queue<Character> q = new LinkedList<>();
    for (char c : indegree.keySet())
        if (indegree.get(c) == 0) q.offer(c);

    StringBuilder sb = new StringBuilder();
    while (!q.isEmpty()) {
        char c = q.poll();
        sb.append(c);
        if (graph.containsKey(c))
            for (char nei : graph.get(c))
                if (--indegree.put(nei, indegree.get(nei) - 1) == 1)
                    q.offer(nei);
    }

    return sb.length() == indegree.size() ? sb.toString() : "";
}
```

---

# ✅ Q7. Critical Connections (Tarjan)

```java
int time = 0;
List<List<Integer>> res = new ArrayList<>();

public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
    List<Integer>[] graph = new ArrayList[n];
    for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();

    for (List<Integer> c : connections) {
        graph[c.get(0)].add(c.get(1));
        graph[c.get(1)].add(c.get(0));
    }

    int[] disc = new int[n];
    int[] low = new int[n];
    Arrays.fill(disc, -1);

    dfs(0, -1, graph, disc, low);
    return res;
}

private void dfs(int u, int parent, List<Integer>[] graph, int[] disc, int[] low) {
    disc[u] = low[u] = time++;

    for (int v : graph[u]) {
        if (v == parent) continue;

        if (disc[v] == -1) {
            dfs(v, u, graph, disc, low);
            low[u] = Math.min(low[u], low[v]);
            if (low[v] > disc[u])
                res.add(Arrays.asList(u, v));
        } else {
            low[u] = Math.min(low[u], disc[v]);
        }
    }
}
```

---

# ✅ Q8. Word Ladder II (Key Idea)

```java
// BFS builds graph
// DFS backtracks paths
```

(Ask if you want **full code walkthrough** — it’s long but important)

---

# 🎯 Google Interview Readiness Check

If you can:

* Explain recursion return vs global state
* Draw DFS trees for graphs
* Justify BFS vs DFS
* Optimize space & time

👉 **You are at Google Senior level**

---

## 🔥 NEXT OPTIONS

1️⃣ **Day 9–10: Dynamic Programming (Hard)**
2️⃣ **Google mock interview (Trees + Graphs)**
3️⃣ **System Design prep roadmap**

Tell me how you want to proceed 🚀
