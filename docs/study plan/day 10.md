Excellent choice 🔥
**Day 13–14: Advanced Graphs + DP Mix** is **very Google-specific**.
These problems test whether you can **combine paradigms**, not just apply them individually.

At this stage, interviewers expect:

* Correct modeling
* Hybrid thinking (Graph + DP)
* Optimization and pruning
* Clear explanation of *why* a solution works

As always:

* ❌ **Problems first (no solutions)**
* ✅ **Solutions + deep explanations at the end**

---

# 🧠 DAY 13–14: ADVANCED GRAPHS + DP (GOOGLE LEVEL)

---

## 1️⃣ HOW GOOGLE EXPECTS YOU TO THINK (LOUDLY)

> “This looks like a graph problem, but brute DFS will TLE.
> I’ll cache states → DP on graph nodes.”

Key triggers:

* Graph with **constraints**
* **Repeated states**
* **Longest / shortest / max probability / min cost**
* Cycles → **memoization / topological order**

---

## 2️⃣ CORE PATTERNS YOU MUST MASTER

| Pattern            | Typical Problem          |
| ------------------ | ------------------------ |
| DP on DAG          | Longest path             |
| Graph + Bitmask DP | TSP variants             |
| BFS + DP           | Shortest path with state |
| DFS + Memo         | Word break on graph      |
| Multi-source + DP  | Probability / cost       |
| Topo + DP          | Scheduling problems      |

---

# 📘 PRACTICE PROBLEMS (HARD)

❌ **ATTEMPT FIRST – NO SOLUTIONS**

---

## 🔥 Q1. Longest Increasing Path in a Matrix

### Problem

Given an `m x n` matrix, return the length of the longest increasing path.

Moves allowed:

* Up, Down, Left, Right

---

### Why Hybrid?

* Graph (matrix → nodes)
* DP (memoization)

---

## 🔥 Q2. Cheapest Flights Within K Stops

### Problem

Find the cheapest price from `src` to `dst` with at most `k` stops.

---

### Why Hybrid?

* Graph + DP (Bellman-Ford / BFS layers)

---

## 🔥 Q3. Word Break II (Graph + DP)

### Problem

Return all possible sentences from a string using dictionary words.

---

### Why HARD?

* Exponential paths
* Memoization pruning

---

## 🔥 Q4. Shortest Path in a Grid with Obstacles Elimination

### Problem

You can eliminate up to `k` obstacles.

Return shortest path length.

---

### Why Hybrid?

* BFS + state DP `(row, col, remaining k)`

---

## 🔥 Q5. Number of Ways to Arrive at Destination

### Problem

Count number of shortest paths modulo `1e9+7`.

---

### Why Hybrid?

* Dijkstra + DP counting paths

---

## 🔥 Q6. Frog Jump

### Problem

Frog crosses stones with variable jump sizes.

---

### Why HARD?

* State `(index, last jump)`
* DP + pruning

---

## 🔥 Q7. Minimum Cost to Cut a Stick

### Problem

Minimize cost of cutting stick.

---

### Why Hybrid?

* Interval DP + graph-like dependencies

---

## 🔥 Q8. Maximum Probability Path

### Problem

Find path with maximum success probability.

---

### Why Hybrid?

* Graph + DP + Dijkstra variant

---

---

# ✅ SOLUTIONS & DEEP EXPLANATIONS

⚠️ **Read only after full attempts**

---

# ✅ Q1. Longest Increasing Path in Matrix

### Insight

* Each cell = node
* Directed edges to higher values
* DAG → DFS + memo

```java
int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
int[][] memo;

public int longestIncreasingPath(int[][] matrix) {
    int m = matrix.length, n = matrix[0].length;
    memo = new int[m][n];
    int ans = 0;

    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            ans = Math.max(ans, dfs(matrix, i, j));

    return ans;
}

private int dfs(int[][] mat, int i, int j) {
    if (memo[i][j] != 0) return memo[i][j];

    int max = 1;
    for (int[] d : dirs) {
        int r = i + d[0], c = j + d[1];
        if (r >= 0 && c >= 0 && r < mat.length && c < mat[0].length &&
            mat[r][c] > mat[i][j]) {
            max = Math.max(max, 1 + dfs(mat, r, c));
        }
    }
    memo[i][j] = max;
    return max;
}
```

---

# ✅ Q2. Cheapest Flights Within K Stops

### DP (Bellman-Ford)

```java
public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
    int[] cost = new int[n];
    Arrays.fill(cost, Integer.MAX_VALUE);
    cost[src] = 0;

    for (int i = 0; i <= k; i++) {
        int[] temp = cost.clone();
        for (int[] f : flights) {
            if (cost[f[0]] != Integer.MAX_VALUE) {
                temp[f[1]] = Math.min(temp[f[1]], cost[f[0]] + f[2]);
            }
        }
        cost = temp;
    }
    return cost[dst] == Integer.MAX_VALUE ? -1 : cost[dst];
}
```

---

# ✅ Q3. Word Break II

```java
Map<String, List<String>> memo = new HashMap<>();

public List<String> wordBreak(String s, List<String> dict) {
    if (memo.containsKey(s)) return memo.get(s);
    List<String> res = new ArrayList<>();

    for (String w : dict) {
        if (s.startsWith(w)) {
            if (w.length() == s.length())
                res.add(w);
            else {
                for (String sub : wordBreak(s.substring(w.length()), dict))
                    res.add(w + " " + sub);
            }
        }
    }
    memo.put(s, res);
    return res;
}
```

---

# ✅ Q4. Shortest Path with Obstacles Elimination

```java
public int shortestPath(int[][] grid, int k) {
    int m = grid.length, n = grid[0].length;
    boolean[][][] visited = new boolean[m][n][k + 1];
    Queue<int[]> q = new LinkedList<>();
    q.offer(new int[]{0, 0, k});
    int steps = 0;

    int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};

    while (!q.isEmpty()) {
        int size = q.size();
        while (size-- > 0) {
            int[] cur = q.poll();
            if (cur[0] == m - 1 && cur[1] == n - 1) return steps;

            for (int[] d : dirs) {
                int r = cur[0] + d[0], c = cur[1] + d[1];
                if (r >= 0 && c >= 0 && r < m && c < n) {
                    int nk = cur[2] - grid[r][c];
                    if (nk >= 0 && !visited[r][c][nk]) {
                        visited[r][c][nk] = true;
                        q.offer(new int[]{r, c, nk});
                    }
                }
            }
        }
        steps++;
    }
    return -1;
}
```

---

# ✅ Q5. Number of Ways to Arrive

```java
public int countPaths(int n, int[][] roads) {
    long MOD = 1_000_000_007;
    List<int[]>[] graph = new ArrayList[n];
    for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();

    for (int[] r : roads) {
        graph[r[0]].add(new int[]{r[1], r[2]});
        graph[r[1]].add(new int[]{r[0], r[2]});
    }

    long[] dist = new long[n];
    long[] ways = new long[n];
    Arrays.fill(dist, Long.MAX_VALUE);
    dist[0] = 0;
    ways[0] = 1;

    PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
    pq.offer(new long[]{0, 0});

    while (!pq.isEmpty()) {
        long[] cur = pq.poll();
        long d = cur[0];
        int u = (int) cur[1];

        if (d > dist[u]) continue;

        for (int[] nei : graph[u]) {
            long nd = d + nei[1];
            if (nd < dist[nei[0]]) {
                dist[nei[0]] = nd;
                ways[nei[0]] = ways[u];
                pq.offer(new long[]{nd, nei[0]});
            } else if (nd == dist[nei[0]]) {
                ways[nei[0]] = (ways[nei[0]] + ways[u]) % MOD;
            }
        }
    }
    return (int) ways[n - 1];
}
```

---

# ✅ Q6. Frog Jump

```java
public boolean canCross(int[] stones) {
    Map<Integer, Set<Integer>> dp = new HashMap<>();
    for (int s : stones) dp.put(s, new HashSet<>());
    dp.get(0).add(0);

    for (int s : stones) {
        for (int k : dp.get(s)) {
            for (int step = k - 1; step <= k + 1; step++) {
                if (step > 0 && dp.containsKey(s + step))
                    dp.get(s + step).add(step);
            }
        }
    }
    return !dp.get(stones[stones.length - 1]).isEmpty();
}
```

---

# ✅ Q7. Minimum Cost to Cut Stick

```java
public int minCost(int n, int[] cuts) {
    int m = cuts.length;
    int[] arr = new int[m + 2];
    arr[0] = 0;
    arr[m + 1] = n;
    for (int i = 0; i < m; i++) arr[i + 1] = cuts[i];
    Arrays.sort(arr);

    int[][] dp = new int[m + 2][m + 2];

    for (int len = 2; len < m + 2; len++) {
        for (int i = 0; i + len < m + 2; i++) {
            int j = i + len;
            dp[i][j] = Integer.MAX_VALUE;
            for (int k = i + 1; k < j; k++) {
                dp[i][j] = Math.min(dp[i][j],
                    dp[i][k] + dp[k][j] + arr[j] - arr[i]);
            }
        }
    }
    return dp[0][m + 1];
}
```

---

# ✅ Q8. Maximum Probability Path

```java
public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
    List<double[]>[] graph = new ArrayList[n];
    for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();

    for (int i = 0; i < edges.length; i++) {
        graph[edges[i][0]].add(new double[]{edges[i][1], succProb[i]});
        graph[edges[i][1]].add(new double[]{edges[i][0], succProb[i]});
    }

    double[] prob = new double[n];
    prob[start] = 1.0;

    PriorityQueue<double[]> pq =
        new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));
    pq.offer(new double[]{1.0, start});

    while (!pq.isEmpty()) {
        double[] cur = pq.poll();
        if (cur[1] == end) return cur[0];

        for (double[] nei : graph[(int) cur[1]]) {
            double p = cur[0] * nei[1];
            if (p > prob[(int) nei[0]]) {
                prob[(int) nei[0]] = p;
                pq.offer(new double[]{p, nei[0]});
            }
        }
    }
    return 0.0;
}
```

---

# 🎯 GOOGLE READINESS CHECK

If you can:

* Combine DP + Graph naturally
* Avoid TLE via memo/state pruning
* Explain **why DP is needed**
* Justify algorithm choice

👉 You’re **Google Senior Coding Ready**

---

## 🚀 FINAL PHASE OPTIONS

1️⃣ **Full Google Mock Interview (Coding + Explanation)**
2️⃣ **System Design (Senior / L5–L6)**
3️⃣ **Behavioral + Googleyness**
4️⃣ **Final 30-day revision plan**

Tell me what’s next 💪
