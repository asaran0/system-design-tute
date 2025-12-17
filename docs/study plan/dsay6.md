Perfect 👍
Now we move to **Day 7–8: GRAPHS** — this is **high-impact for Google**, especially for **distributed systems, dependency resolution, and scheduling problems**.

As requested, the structure is:

* 🧠 **Core concepts & mental models**
* 📘 **Medium practice questions FIRST (NO solutions)**
* ✅ **Solutions & deep explanations at the end**

---

# 🌐 DAY 7–8: GRAPHS — CONCEPTS & MENTAL MODELS

## 1️⃣ Graph Basics (Must Be Clear)

### Graph Types

* **Directed / Undirected**
* **Weighted / Unweighted**
* **Cyclic / Acyclic**
* **Connected / Disconnected**

### Representations

| Type             | When to Use               |
| ---------------- | ------------------------- |
| Adjacency List   | Sparse graphs (preferred) |
| Adjacency Matrix | Dense graphs              |
| Edge List        | Union-Find                |

---

## 2️⃣ BFS vs DFS (Google Decision Point)

### BFS

* Level-wise traversal
* Shortest path (unweighted)
* Uses **Queue**

### DFS

* Deep exploration
* Cycle detection
* Uses **Recursion / Stack**

---

## 3️⃣ Topological Sort (DAG Only)

### Used For

* Course scheduling
* Build systems
* Dependency resolution

### Two Approaches

1. **Kahn’s Algorithm (BFS + Indegree)**
2. **DFS + Stack**

---

## 4️⃣ Union-Find (Disjoint Set Union)

### Used For

* Dynamic connectivity
* Cycle detection
* Kruskal’s MST

### Optimizations

* Path compression
* Union by rank

---

## 5️⃣ Common Graph Patterns

| Pattern          | Example         |
| ---------------- | --------------- |
| Multi-source BFS | Rotten Oranges  |
| Graph as grid    | Islands         |
| Cycle detection  | Course Schedule |
| Connectivity     | Union-Find      |

---

# 📘 MEDIUM PRACTICE QUESTIONS

❌ **ATTEMPT FIRST – NO SOLUTIONS YET**

---

## Q1️⃣ Number of Islands (DFS / BFS)

### Problem Statement

Given a 2D grid of `'1'` (land) and `'0'` (water), count the number of islands.

---

### Input

```
[
  ["1","1","0","0"],
  ["1","1","0","0"],
  ["0","0","1","0"],
  ["0","0","0","1"]
]
```

### Output

```
3
```

---

### Follow-ups

1. DFS vs BFS?
2. Time complexity?
3. Can this be solved using Union-Find?

---

## Q2️⃣ Course Schedule (Topological Sort)

### Problem Statement

Given `numCourses` and a list of prerequisites, determine if all courses can be finished.

---

### Input

```
numCourses = 2
prerequisites = [[1,0]]
```

### Output

```
true
```

---

### Follow-ups

1. How do you detect cycles?
2. BFS vs DFS approach?
3. Why indegree matters?

---

## Q3️⃣ Clone Graph (DFS / BFS)

### Problem Statement

Given a reference to a node in a connected undirected graph, return a **deep copy** of the graph.

---

### Follow-ups

1. Why HashMap?
2. DFS vs BFS?
3. Handling cycles?

---

## Q4️⃣ Rotting Oranges (Multi-source BFS)

### Problem Statement

Given a grid:

* `0` = empty
* `1` = fresh orange
* `2` = rotten orange

Each minute, rotten oranges rot adjacent fresh ones.

Return minimum minutes to rot all oranges.

---

### Input

```
[[2,1,1],[1,1,0],[0,1,1]]
```

### Output

```
4
```

---

### Follow-ups

1. Why multi-source BFS?
2. Why BFS instead of DFS?
3. How do you track time?

---

## Q5️⃣ Graph Valid Tree (Union-Find)

### Problem Statement

Given `n` nodes and edges, determine if the graph is a valid tree.

---

### Conditions

* Connected
* No cycles

---

### Follow-ups

1. Why Union-Find?
2. Edge count condition?
3. Time complexity?

---

## Q6️⃣ Detect Cycle in Directed Graph (DFS)

### Problem Statement

Detect if a directed graph has a cycle.

---

### Follow-ups

1. Why recursion stack?
2. Difference from undirected cycle detection?
3. Relation to topological sort?

---

## Q7️⃣ Evaluate Division (Graph + DFS)

### Problem Statement

Given equations like:

```
a / b = 2.0
b / c = 3.0
```

Answer queries like:

```
a / c = ?
```

---

### Follow-ups

1. Graph modeling?
2. Handling disconnected components?
3. Precision concerns?

---

# ✅ SOLUTIONS & IN-DEPTH EXPLANATIONS

(Only after attempting)

---

## ✅ Q1 Solution: Number of Islands

```java
public int numIslands(char[][] grid) {
    int count = 0;
    for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[0].length; j++) {
            if (grid[i][j] == '1') {
                dfs(grid, i, j);
                count++;
            }
        }
    }
    return count;
}

private void dfs(char[][] grid, int i, int j) {
    if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == '0')
        return;

    grid[i][j] = '0';
    dfs(grid, i + 1, j);
    dfs(grid, i - 1, j);
    dfs(grid, i, j + 1);
    dfs(grid, i, j - 1);
}
```

---

## ✅ Q2 Solution: Course Schedule (BFS – Kahn)

```java
public boolean canFinish(int numCourses, int[][] prerequisites) {
    int[] indegree = new int[numCourses];
    List<List<Integer>> graph = new ArrayList<>();

    for (int i = 0; i < numCourses; i++)
        graph.add(new ArrayList<>());

    for (int[] p : prerequisites) {
        graph.get(p[1]).add(p[0]);
        indegree[p[0]]++;
    }

    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < numCourses; i++)
        if (indegree[i] == 0) q.offer(i);

    int taken = 0;
    while (!q.isEmpty()) {
        int course = q.poll();
        taken++;
        for (int next : graph.get(course)) {
            if (--indegree[next] == 0)
                q.offer(next);
        }
    }
    return taken == numCourses;
}
```

---

## ✅ Q3 Solution: Clone Graph

```java
Map<Node, Node> map = new HashMap<>();

public Node cloneGraph(Node node) {
    if (node == null) return null;
    if (map.containsKey(node)) return map.get(node);

    Node clone = new Node(node.val);
    map.put(node, clone);

    for (Node neighbor : node.neighbors) {
        clone.neighbors.add(cloneGraph(neighbor));
    }
    return clone;
}
```

---

## ✅ Q4 Solution: Rotting Oranges

```java
public int orangesRotting(int[][] grid) {
    Queue<int[]> q = new LinkedList<>();
    int fresh = 0, time = 0;

    for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[0].length; j++) {
            if (grid[i][j] == 2) q.offer(new int[]{i, j});
            if (grid[i][j] == 1) fresh++;
        }
    }

    int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};

    while (!q.isEmpty() && fresh > 0) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            int[] cell = q.poll();
            for (int[] d : dirs) {
                int r = cell[0] + d[0], c = cell[1] + d[1];
                if (r >= 0 && c >= 0 && r < grid.length && c < grid[0].length && grid[r][c] == 1) {
                    grid[r][c] = 2;
                    fresh--;
                    q.offer(new int[]{r, c});
                }
            }
        }
        time++;
    }
    return fresh == 0 ? time : -1;
}
```

---

## ✅ Q5 Solution: Graph Valid Tree (Union-Find)

```java
public boolean validTree(int n, int[][] edges) {
    if (edges.length != n - 1) return false;

    UnionFind uf = new UnionFind(n);
    for (int[] e : edges) {
        if (!uf.union(e[0], e[1])) return false;
    }
    return true;
}

class UnionFind {
    int[] parent, rank;

    UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    boolean union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;

        if (rank[px] < rank[py]) parent[px] = py;
        else if (rank[px] > rank[py]) parent[py] = px;
        else {
            parent[py] = px;
            rank[px]++;
        }
        return true;
    }
}
```

---

## ✅ Q6 Solution: Detect Cycle in Directed Graph

```java
public boolean hasCycle(int n, List<List<Integer>> graph) {
    boolean[] visited = new boolean[n];
    boolean[] stack = new boolean[n];

    for (int i = 0; i < n; i++) {
        if (dfs(i, graph, visited, stack)) return true;
    }
    return false;
}

private boolean dfs(int node, List<List<Integer>> graph, boolean[] visited, boolean[] stack) {
    if (stack[node]) return true;
    if (visited[node]) return false;

    visited[node] = true;
    stack[node] = true;

    for (int nei : graph.get(node)) {
        if (dfs(nei, graph, visited, stack)) return true;
    }
    stack[node] = false;
    return false;
}
```

---

## ✅ Q7 Solution: Evaluate Division

```java
public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
    Map<String, Map<String, Double>> graph = new HashMap<>();

    for (int i = 0; i < equations.size(); i++) {
        String a = equations.get(i).get(0);
        String b = equations.get(i).get(1);
        double val = values[i];

        graph.putIfAbsent(a, new HashMap<>());
        graph.putIfAbsent(b, new HashMap<>());
        graph.get(a).put(b, val);
        graph.get(b).put(a, 1.0 / val);
    }

    double[] res = new double[queries.size()];
    for (int i = 0; i < queries.size(); i++) {
        res[i] = dfs(queries.get(i).get(0), queries.get(i).get(1), new HashSet<>(), graph);
    }
    return res;
}

private double dfs(String src, String dst, Set<String> visited, Map<String, Map<String, Double>> graph) {
    if (!graph.containsKey(src)) return -1.0;
    if (src.equals(dst)) return 1.0;

    visited.add(src);
    for (String nei : graph.get(src).keySet()) {
        if (!visited.contains(nei)) {
            double val = dfs(nei, dst, visited, graph);
            if (val != -1.0) return val * graph.get(src).get(nei);
        }
    }
    return -1.0;
}
```

---

# 🎯 After Day 7–8 You Should Be Able To

* Choose BFS vs DFS confidently
* Implement Topo Sort
* Use Union-Find correctly
* Explain graph problems clearly

---

## NEXT STEP?

👉 **Day 9–10: Dynamic Programming (Medium → Hard)**
👉 **Google-style graph mock interview**
👉 **Hard graph problems**

Just tell me 👍
