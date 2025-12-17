Perfect.
**Day 9–10: Dynamic Programming (Medium)** is *extremely important for Google*, especially for **problem decomposition, optimization, and correctness reasoning**.

As before, this is **Google-style**:

* Concepts first (how to think)
* **Medium problems (NO solutions initially)**
* **All solutions + deep explanations at the end**

---

# 🧠 DAY 9–10: DYNAMIC PROGRAMMING (MEDIUM)

---

## 1️⃣ Dynamic Programming — Core Mental Model (Google Expectation)

### When to Use DP?

If the problem has:

1. **Optimal substructure**
2. **Overlapping subproblems**

---

### DP Thinking Framework (Google Favorite)

Always answer these **out loud**:

1. **State** – What does `dp[i]` represent?
2. **Transition** – How do I compute it?
3. **Base case**
4. **Order of computation**
5. **Answer extraction**
6. **Optimization (space/time)**

---

## 2️⃣ Common DP Patterns (Medium)

| Pattern       | Examples               |
| ------------- | ---------------------- |
| 1D DP         | House Robber           |
| 2D DP         | Grid paths             |
| Knapsack      | Subset sum             |
| LIS style     | Increasing subsequence |
| DP on Strings | LCS                    |
| DP on Trees   | Robber III             |
| Partition DP  | Palindrome partition   |

---

# 📘 PRACTICE QUESTIONS (ATTEMPT FIRST)

❌ **NO SOLUTIONS YET**

---

## 🔹 Q1. Climbing Stairs

### Problem

You are climbing a staircase with `n` steps.
You can climb 1 or 2 steps at a time.

Return the number of distinct ways.

---

### Follow-ups

* Can you optimize space?
* Relation to Fibonacci?

---

## 🔹 Q2. House Robber

### Problem

You are a robber planning to rob houses.
Adjacent houses cannot be robbed.

Return the maximum amount you can rob.

---

### Follow-ups

* Why greedy fails?
* Space optimization?

---

## 🔹 Q3. Coin Change (Minimum Coins)

### Problem

Given coins of different denominations and an amount,
return the minimum number of coins needed.

---

### Example

```
coins = [1,2,5], amount = 11
Output: 3
```

---

### Follow-ups

* Why greedy fails?
* Time complexity?

---

## 🔹 Q4. Longest Increasing Subsequence (LIS)

### Problem

Return the length of the longest strictly increasing subsequence.

---

### Follow-ups

* O(n²) vs O(n log n)?
* Binary search logic?

---

## 🔹 Q5. Unique Paths

### Problem

Robot moves from top-left to bottom-right of grid.
Can only move right or down.

Return number of unique paths.

---

### Follow-ups

* Grid with obstacles?
* Space optimization?

---

## 🔹 Q6. Longest Common Subsequence (LCS)

### Problem

Given two strings, return length of LCS.

---

### Follow-ups

* How to reconstruct the sequence?
* Space optimization?

---

## 🔹 Q7. Partition Equal Subset Sum

### Problem

Given array, determine if it can be partitioned into two subsets with equal sum.

---

### Follow-ups

* Why knapsack?
* Optimization tricks?

---

## 🔹 Q8. Decode Ways

### Problem

Given a digit string, count number of ways to decode it.

---

### Follow-ups

* Why recursion is tricky?
* Handling zeros?

---

---

# ✅ SOLUTIONS & IN-DEPTH EXPLANATIONS

⚠️ **Read only after attempting**

---

## ✅ Q1. Climbing Stairs

### State

`dp[i] = ways to reach step i`

### Transition

```
dp[i] = dp[i-1] + dp[i-2]
```

```java
public int climbStairs(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
        int c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

---

## ✅ Q2. House Robber

### State

`dp[i] = max money till house i`

```java
public int rob(int[] nums) {
    int prev2 = 0, prev1 = 0;
    for (int num : nums) {
        int temp = Math.max(prev1, prev2 + num);
        prev2 = prev1;
        prev1 = temp;
    }
    return prev1;
}
```

---

## ✅ Q3. Coin Change

```java
public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;

    for (int i = 1; i <= amount; i++) {
        for (int coin : coins) {
            if (coin <= i)
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}
```

---

## ✅ Q4. Longest Increasing Subsequence

### O(n log n) Method

```java
public int lengthOfLIS(int[] nums) {
    int[] tails = new int[nums.length];
    int size = 0;

    for (int num : nums) {
        int i = Arrays.binarySearch(tails, 0, size, num);
        if (i < 0) i = -(i + 1);
        tails[i] = num;
        if (i == size) size++;
    }
    return size;
}
```

---

## ✅ Q5. Unique Paths

```java
public int uniquePaths(int m, int n) {
    int[] dp = new int[n];
    Arrays.fill(dp, 1);

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[j] += dp[j - 1];
        }
    }
    return dp[n - 1];
}
```

---

## ✅ Q6. Longest Common Subsequence

```java
public int longestCommonSubsequence(String text1, String text2) {
    int[][] dp = new int[text1.length() + 1][text2.length() + 1];

    for (int i = 1; i <= text1.length(); i++) {
        for (int j = 1; j <= text2.length(); j++) {
            if (text1.charAt(i - 1) == text2.charAt(j - 1))
                dp[i][j] = 1 + dp[i - 1][j - 1];
            else
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    return dp[text1.length()][text2.length()];
}
```

---

## ✅ Q7. Partition Equal Subset Sum

```java
public boolean canPartition(int[] nums) {
    int sum = Arrays.stream(nums).sum();
    if (sum % 2 != 0) return false;

    boolean[] dp = new boolean[sum / 2 + 1];
    dp[0] = true;

    for (int num : nums) {
        for (int j = sum / 2; j >= num; j--) {
            dp[j] = dp[j] || dp[j - num];
        }
    }
    return dp[sum / 2];
}
```

---

## ✅ Q8. Decode Ways

```java
public int numDecodings(String s) {
    if (s.charAt(0) == '0') return 0;

    int prev2 = 1, prev1 = 1;
    for (int i = 1; i < s.length(); i++) {
        int curr = 0;
        if (s.charAt(i) != '0')
            curr = prev1;

        int two = Integer.parseInt(s.substring(i - 1, i + 1));
        if (two >= 10 && two <= 26)
            curr += prev2;

        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}
```

---

# 🎯 By End of Day 10 You Should:

* Derive DP states yourself
* Optimize space confidently
* Explain transitions clearly
* Avoid recursion traps

---

## NEXT STEPS (FINAL STAGE)

👉 **Day 11–12: Dynamic Programming (Hard)**
👉 **Full Google Mock Interview (DSA + System Design)**
👉 **Behavioral + Googleyness**

Tell me what’s next 🚀
