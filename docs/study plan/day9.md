Excellent — **Day 11–12: Dynamic Programming (HARD)** is where **Google differentiates senior engineers** from average ones.

At this level, interviewers care about:

* **State design**
* **Transition correctness**
* **Optimization**
* **Explaining trade-offs clearly**

As always:

* 🔥 **Hard problems first (NO solutions initially)**
* ✅ **All solutions + deep explanations at the end**

---

# 🧠 DAY 11–12: DYNAMIC PROGRAMMING (HARD)

---

## 1️⃣ HARD DP — HOW GOOGLE EXPECTS YOU TO THINK

Before coding, say **out loud**:

> “Let me define the DP state clearly…”

### Google DP Checklist

1. State (what uniquely identifies a subproblem?)
2. Dimensions (1D, 2D, 3D, bitmask?)
3. Transition (choices at each state)
4. Base cases
5. Order (top-down vs bottom-up)
6. Optimization
7. Constraints → feasibility

---

## 2️⃣ HARD DP PATTERNS (MUST MASTER)

| Pattern       | Examples                |
| ------------- | ----------------------- |
| DP on Strings | Edit Distance           |
| Interval DP   | Burst Balloons          |
| DP on Grid    | Dungeon Game            |
| DP on Trees   | House Robber III        |
| Bitmask DP    | TSP                     |
| Partition DP  | Palindrome Partition II |
| LIS variant   | Russian Doll Envelopes  |

---

# 📘 HARD PRACTICE QUESTIONS

❌ **ATTEMPT FIRST – NO SOLUTIONS**

---

## 🔥 Q1. Edit Distance

### Problem

Given two strings `word1` and `word2`, return minimum number of operations to convert `word1` → `word2`.

Allowed:

* Insert
* Delete
* Replace

---

### Follow-ups

* State definition?
* Why greedy fails?
* Space optimization?

---

## 🔥 Q2. Burst Balloons (Interval DP)

### Problem

Given `nums`, burst balloons to maximize coins.

Coins gained:

```
nums[left] * nums[i] * nums[right]
```

---

### Why HARD?

* Reverse thinking
* Interval DP

---

## 🔥 Q3. Palindrome Partitioning II

### Problem

Return minimum cuts needed so every substring is palindrome.

---

### Follow-ups

* Precompute palindrome table?
* Time optimization?

---

## 🔥 Q4. Dungeon Game

### Problem

Find minimum initial health needed to reach bottom-right.

---

### Key Trick

Think **backwards**

---

## 🔥 Q5. House Robber III (Tree DP)

### Problem

Rob houses arranged in a binary tree.

---

### Follow-ups

* State per node?
* Why simple DP fails?

---

## 🔥 Q6. Russian Doll Envelopes

### Problem

Given envelopes `[w, h]`, find max nesting.

---

### Follow-ups

* Why sort width asc & height desc?
* LIS reduction?

---

## 🔥 Q7. Regular Expression Matching

### Problem

Implement regex matching with `.` and `*`.

---

### Why HARD?

* Multiple transitions
* Edge cases

---

## 🔥 Q8. Traveling Salesman Problem (Bitmask DP)

### Problem

Visit all cities with minimum cost and return to start.

---

### Why HARD?

* State explosion
* Bitmasking

---

---

# ✅ SOLUTIONS & DEEP EXPLANATIONS

⚠️ **Only read after serious attempts**

---

# ✅ Q1. Edit Distance

### State

`dp[i][j] = min ops to convert word1[0..i) → word2[0..j)`

```java
public int minDistance(String w1, String w2) {
    int m = w1.length(), n = w2.length();
    int[][] dp = new int[m + 1][n + 1];

    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (w1.charAt(i - 1) == w2.charAt(j - 1))
                dp[i][j] = dp[i - 1][j - 1];
            else
                dp[i][j] = 1 + Math.min(
                    dp[i - 1][j - 1], // replace
                    Math.min(dp[i - 1][j], dp[i][j - 1]) // delete, insert
                );
        }
    }
    return dp[m][n];
}
```

---

# ✅ Q2. Burst Balloons

### Key Insight

👉 Think **last balloon burst** in an interval.

```java
public int maxCoins(int[] nums) {
    int n = nums.length;
    int[] arr = new int[n + 2];
    arr[0] = arr[n + 1] = 1;
    for (int i = 0; i < n; i++) arr[i + 1] = nums[i];

    int[][] dp = new int[n + 2][n + 2];

    for (int len = 2; len <= n + 1; len++) {
        for (int left = 0; left + len <= n + 1; left++) {
            int right = left + len;
            for (int k = left + 1; k < right; k++) {
                dp[left][right] = Math.max(dp[left][right],
                    arr[left] * arr[k] * arr[right] +
                    dp[left][k] + dp[k][right]);
            }
        }
    }
    return dp[0][n + 1];
}
```

---

# ✅ Q3. Palindrome Partition II

```java
public int minCut(String s) {
    int n = s.length();
    boolean[][] pal = new boolean[n][n];

    for (int i = n - 1; i >= 0; i--) {
        for (int j = i; j < n; j++) {
            pal[i][j] = s.charAt(i) == s.charAt(j) &&
                (j - i < 2 || pal[i + 1][j - 1]);
        }
    }

    int[] dp = new int[n];
    Arrays.fill(dp, Integer.MAX_VALUE);

    for (int i = 0; i < n; i++) {
        if (pal[0][i]) dp[i] = 0;
        else {
            for (int j = 0; j < i; j++) {
                if (pal[j + 1][i])
                    dp[i] = Math.min(dp[i], dp[j] + 1);
            }
        }
    }
    return dp[n - 1];
}
```

---

# ✅ Q4. Dungeon Game

### Backward DP

```java
public int calculateMinimumHP(int[][] dungeon) {
    int m = dungeon.length, n = dungeon[0].length;
    int[][] dp = new int[m + 1][n + 1];

    for (int[] row : dp)
        Arrays.fill(row, Integer.MAX_VALUE);

    dp[m][n - 1] = dp[m - 1][n] = 1;

    for (int i = m - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            int need = Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
            dp[i][j] = Math.max(1, need);
        }
    }
    return dp[0][0];
}
```

---

# ✅ Q5. House Robber III

```java
public int rob(TreeNode root) {
    int[] res = dfs(root);
    return Math.max(res[0], res[1]);
}

private int[] dfs(TreeNode node) {
    if (node == null) return new int[]{0, 0};

    int[] left = dfs(node.left);
    int[] right = dfs(node.right);

    int rob = node.val + left[0] + right[0];
    int skip = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);

    return new int[]{skip, rob};
}
```

---

# ✅ Q6. Russian Doll Envelopes

```java
public int maxEnvelopes(int[][] env) {
    Arrays.sort(env, (a, b) ->
        a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);

    int[] dp = new int[env.length];
    int len = 0;

    for (int[] e : env) {
        int i = Arrays.binarySearch(dp, 0, len, e[1]);
        if (i < 0) i = -(i + 1);
        dp[i] = e[1];
        if (i == len) len++;
    }
    return len;
}
```

---

# ✅ Q7. Regular Expression Matching

```java
public boolean isMatch(String s, String p) {
    boolean[][] dp = new boolean[s.length() + 1][p.length() + 1];
    dp[0][0] = true;

    for (int j = 2; j <= p.length(); j++)
        if (p.charAt(j - 1) == '*')
            dp[0][j] = dp[0][j - 2];

    for (int i = 1; i <= s.length(); i++) {
        for (int j = 1; j <= p.length(); j++) {
            if (p.charAt(j - 1) == s.charAt(i - 1) || p.charAt(j - 1) == '.')
                dp[i][j] = dp[i - 1][j - 1];
            else if (p.charAt(j - 1) == '*') {
                dp[i][j] = dp[i][j - 2] ||
                    ((p.charAt(j - 2) == '.' || p.charAt(j - 2) == s.charAt(i - 1))
                     && dp[i - 1][j]);
            }
        }
    }
    return dp[s.length()][p.length()];
}
```

---

# ✅ Q8. Traveling Salesman (Bitmask DP)

```java
public int tsp(int[][] dist) {
    int n = dist.length;
    int[][] dp = new int[1 << n][n];
    for (int[] row : dp) Arrays.fill(row, Integer.MAX_VALUE);

    dp[1][0] = 0;

    for (int mask = 1; mask < (1 << n); mask++) {
        for (int u = 0; u < n; u++) {
            if ((mask & (1 << u)) == 0) continue;
            for (int v = 0; v < n; v++) {
                if ((mask & (1 << v)) == 0)
                    dp[mask | (1 << v)][v] =
                        Math.min(dp[mask | (1 << v)][v],
                            dp[mask][u] + dist[u][v]);
            }
        }
    }

    int res = Integer.MAX_VALUE;
    for (int i = 0; i < n; i++)
        res = Math.min(res, dp[(1 << n) - 1][i] + dist[i][0]);

    return res;
}
```

---

# 🎯 FINAL GOOGLE DP CHECKLIST

If you can:

* Design DP states confidently
* Explain transitions clearly
* Optimize space
* Handle edge cases

👉 **You are DP-ready for Google Senior interviews**

---

## 🚀 WHAT’S NEXT?

1️⃣ **Day 13–14: Advanced Graphs + DP mix**
2️⃣ **Full Google Mock Interview (Coding)**
3️⃣ **System Design (Senior-level)**
4️⃣ **Behavioral + Googleyness**

Tell me your next move 🔥
