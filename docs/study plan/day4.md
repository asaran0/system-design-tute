Excellent 🔥
Now we’re moving into **Google Senior–level HARD questions** across **Day 1–4 topics**.

As requested:

* ✅ **QUESTIONS FIRST (very detailed, interview-style)**
* ❌ **NO solutions mixed in**
* ✅ **SOLUTIONS & DEEP EXPLANATIONS AT THE END**
* ✅ Covers **Arrays, Strings, HashMap, Sliding Window, Linked List, Stack, Queue**
* ✅ These are **commonly asked / Google-style hard mediums & hards**

---

# 📘 HARD PRACTICE QUESTIONS (DAY 1–4)

⚠️ **Do NOT scroll down until you attempt each question**

---

## 🔴 Q1️⃣ Minimum Window Substring (Sliding Window – HARD)

### Problem Statement

Given two strings `s` and `t`, return the **minimum window substring** of `s` such that **every character in `t` (including duplicates)** is included in the window.

If no such substring exists, return an empty string.

---

### Input Example

```
s = "ADOBECODEBANC"
t = "ABC"
```

### Output

```
"BANC"
```

---

### Constraints

* `1 <= s.length, t.length <= 10⁵`
* Characters may repeat

---

### Interview Follow-ups

1. Why is this not a simple sliding window?
2. How do duplicates in `t` affect logic?
3. What invariant does the window maintain?

---

## 🔴 Q2️⃣ Longest Substring with At Most K Distinct Characters (Sliding Window)

### Problem Statement

Given a string `s` and integer `k`, return the length of the **longest substring** that contains **at most k distinct characters**.

---

### Input

```
s = "eceba", k = 2
```

### Output

```
3
```

---

### Follow-ups

1. How is this different from “no repeating characters”?
2. How do you maintain character counts?
3. Time & space complexity?

---

## 🔴 Q3️⃣ Product of Array Except Self (HARD Constraints Thinking)

### Problem Statement

Given an integer array `nums`, return an array such that:

```
answer[i] = product of all elements except nums[i]
```

---

### Constraints

* No division allowed
* O(n) time
* O(1) extra space (excluding output)

---

### Input

```
nums = [1,2,3,4]
```

---

### Follow-ups

1. How do you handle multiple zeros?
2. Why does prefix–suffix work?
3. Overflow concerns?

---

## 🔴 Q4️⃣ Subarrays with Exactly K Distinct Integers (HashMap + Sliding Window)

### Problem Statement

Given an integer array `nums` and integer `k`, return the number of subarrays with **exactly k distinct integers**.

---

### Input

```
nums = [1,2,1,2,3]
k = 2
```

### Output

```
7
```

---

### Follow-ups

1. Why not brute force?
2. Why do we calculate “at most k”?
3. What is the key mathematical trick?

---

## 🔴 Q5️⃣ Copy List with Random Pointer (Linked List – HARD)

### Problem Statement

A linked list node has:

* `next` pointer
* `random` pointer (points to any node or null)

Create a **deep copy** of the list.

---

### Input

```
Node(val, next, random)
```

---

### Follow-ups

1. Why not just copy nodes?
2. How do you avoid extra space?
3. How do you restore original list?

---

## 🔴 Q6️⃣ LRU Cache (HashMap + Doubly Linked List – HARD)

### Problem Statement

Design and implement a **Least Recently Used (LRU) Cache** with:

* `get(key)`
* `put(key, value)`

---

### Constraints

* O(1) time per operation
* Capacity limited

---

### Follow-ups

1. Why HashMap + Doubly Linked List?
2. Why not singly linked list?
3. How eviction works?

---

## 🔴 Q7️⃣ Largest Rectangle in Histogram (Monotonic Stack – HARD)

### Problem Statement

Given an array representing histogram bar heights, return the **largest rectangle area**.

---

### Input

```
heights = [2,1,5,6,2,3]
```

### Output

```
10
```

---

### Follow-ups

1. Why monotonic stack?
2. Why width calculation is tricky?
3. Time complexity?

---

## 🔴 Q8️⃣ Sliding Window Maximum (Deque – HARD)

### Problem Statement

Given array `nums` and window size `k`, return maximum of each window.

---

### Input

```
nums = [1,3,-1,-3,5,3,6,7], k = 3
```

---

### Follow-ups

1. Why not heap?
2. Why deque?
3. How do we maintain order?

---

---

# ✅ SOLUTIONS & DEEP EXPLANATIONS

(Scroll only after attempting)

---

## ✅ Q1 Solution: Minimum Window Substring

```java
public String minWindow(String s, String t) {
    Map<Character, Integer> need = new HashMap<>();
    for (char c : t.toCharArray())
        need.put(c, need.getOrDefault(c, 0) + 1);

    int left = 0, right = 0, required = need.size();
    int formed = 0;
    Map<Character, Integer> window = new HashMap<>();

    int[] ans = {-1, 0, 0};

    while (right < s.length()) {
        char c = s.charAt(right);
        window.put(c, window.getOrDefault(c, 0) + 1);

        if (need.containsKey(c) && window.get(c).intValue() == need.get(c))
            formed++;

        while (left <= right && formed == required) {
            if (ans[0] == -1 || right - left + 1 < ans[0]) {
                ans[0] = right - left + 1;
                ans[1] = left;
                ans[2] = right;
            }

            char ch = s.charAt(left);
            window.put(ch, window.get(ch) - 1);
            if (need.containsKey(ch) && window.get(ch) < need.get(ch))
                formed--;
            left++;
        }
        right++;
    }
    return ans[0] == -1 ? "" : s.substring(ans[1], ans[2] + 1);
}
```

### Key Insight

* Track **how many required characters are satisfied**
* Shrink window only when valid

---

## ✅ Q2 Solution: At Most K Distinct

```java
public int lengthOfLongestSubstringKDistinct(String s, int k) {
    Map<Character, Integer> map = new HashMap<>();
    int left = 0, max = 0;

    for (int right = 0; right < s.length(); right++) {
        map.put(s.charAt(right), map.getOrDefault(s.charAt(right), 0) + 1);

        while (map.size() > k) {
            char c = s.charAt(left++);
            map.put(c, map.get(c) - 1);
            if (map.get(c) == 0) map.remove(c);
        }
        max = Math.max(max, right - left + 1);
    }
    return max;
}
```

---

## ✅ Q3 Solution: Product Except Self

```java
public int[] productExceptSelf(int[] nums) {
    int n = nums.length;
    int[] res = new int[n];

    res[0] = 1;
    for (int i = 1; i < n; i++)
        res[i] = res[i - 1] * nums[i - 1];

    int suffix = 1;
    for (int i = n - 1; i >= 0; i--) {
        res[i] *= suffix;
        suffix *= nums[i];
    }
    return res;
}
```

---

## ✅ Q4 Solution: Exactly K Distinct

```java
public int subarraysWithKDistinct(int[] nums, int k) {
    return atMost(nums, k) - atMost(nums, k - 1);
}

private int atMost(int[] nums, int k) {
    Map<Integer, Integer> map = new HashMap<>();
    int left = 0, res = 0;

    for (int right = 0; right < nums.length; right++) {
        map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);

        while (map.size() > k) {
            int n = nums[left++];
            map.put(n, map.get(n) - 1);
            if (map.get(n) == 0) map.remove(n);
        }
        res += right - left + 1;
    }
    return res;
}
```

---

## ✅ Q5 Solution: Copy List with Random Pointer

```java
public Node copyRandomList(Node head) {
    if (head == null) return null;

    Node curr = head;
    while (curr != null) {
        Node copy = new Node(curr.val);
        copy.next = curr.next;
        curr.next = copy;
        curr = copy.next;
    }

    curr = head;
    while (curr != null) {
        if (curr.random != null)
            curr.next.random = curr.random.next;
        curr = curr.next.next;
    }

    curr = head;
    Node dummy = new Node(0);
    Node copyCurr = dummy;

    while (curr != null) {
        copyCurr.next = curr.next;
        curr.next = curr.next.next;
        curr = curr.next;
        copyCurr = copyCurr.next;
    }
    return dummy.next;
}
```

---

## ✅ Q6 Solution: LRU Cache

```java
class LRUCache {
    class Node {
        int key, value;
        Node prev, next;
    }

    private Map<Integer, Node> map = new HashMap<>();
    private int capacity;
    private Node head = new Node(), tail = new Node();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        if (!map.containsKey(key)) return -1;
        Node node = map.get(key);
        remove(node);
        insert(node);
        return node.value;
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) remove(map.get(key));
        if (map.size() == capacity) {
            map.remove(tail.prev.key);
            remove(tail.prev);
        }
        Node node = new Node();
        node.key = key;
        node.value = value;
        insert(node);
        map.put(key, node);
    }

    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void insert(Node node) {
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
        node.prev = head;
    }
}
```

---

## ✅ Q7 Solution: Largest Rectangle Histogram

```java
public int largestRectangleArea(int[] heights) {
    Stack<Integer> stack = new Stack<>();
    int max = 0;

    for (int i = 0; i <= heights.length; i++) {
        int h = (i == heights.length) ? 0 : heights[i];
        while (!stack.isEmpty() && h < heights[stack.peek()]) {
            int height = heights[stack.pop()];
            int width = stack.isEmpty() ? i : i - stack.peek() - 1;
            max = Math.max(max, height * width);
        }
        stack.push(i);
    }
    return max;
}
```

---

## ✅ Q8 Solution: Sliding Window Maximum

```java
public int[] maxSlidingWindow(int[] nums, int k) {
    Deque<Integer> dq = new LinkedList<>();
    int[] res = new int[nums.length - k + 1];
    int idx = 0;

    for (int i = 0; i < nums.length; i++) {
        while (!dq.isEmpty() && dq.peekFirst() <= i - k)
            dq.pollFirst();

        while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i])
            dq.pollLast();

        dq.offerLast(i);
        if (i >= k - 1)
            res[idx++] = nums[dq.peekFirst()];
    }
    return res;
}
```

---

# 🎯 What Google Tests With These

* Pattern recognition under pressure
* Handling edge cases
* Space–time trade-offs
* Clear explanation

---

## NEXT?

👉 **Day 5–6: Trees & Recursion (HARD set)**
👉 **Google mock interview simulation**
👉 **System Design warm-up**

Just say the word 👍
