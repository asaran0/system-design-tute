Great 👍
We’ll continue in the **same practice-first format** (questions first → solutions at the end), exactly aligned with **Google Senior (L5/L6)** expectations.

---

# 📅 DAY 3–4: LINKED LIST, STACK & QUEUE

**(Practice First – Solutions at the End)**

---

## 🧠 Core Patterns You Must Recognize

* **Linked List** → Pointer manipulation, fast/slow pointers
* **Stack** → LIFO, monotonic stack
* **Queue / Deque** → BFS, sliding window optimization

Google checks:

* Pointer safety
* Space optimization
* Invariants
* Clear reasoning

---

# 📘 PRACTICE QUESTIONS (DO NOT SCROLL)

---

## Q1️⃣ Reverse Linked List (Fundamental Pointer Test)

### Problem Statement

Given the head of a singly linked list, reverse the list and return the new head.

---

### Input

```
1 → 2 → 3 → 4 → 5 → null
```

### Output

```
5 → 4 → 3 → 2 → 1 → null
```

---

### Follow-up (Important)

1. Can you do it **iteratively**?
2. Can you do it **recursively**?
3. What is the space complexity in both approaches?

---

## Q2️⃣ Linked List Cycle (Fast & Slow Pointer)

### Problem Statement

Given the head of a linked list, determine if the list has a cycle.

---

### Input Example

```
3 → 2 → 0 → -4
     ↑________|
```

### Output

```
true
```

---

### Follow-up

1. Why does fast & slow pointer work?
2. Can you detect the **starting point** of the cycle?
3. What if you use a HashSet?

---

## Q3️⃣ Merge Two Sorted Lists (Linked List + Merge Logic)

### Problem Statement

Given two sorted linked lists, merge them into one sorted list.

---

### Input

```
l1 = 1 → 2 → 4
l2 = 1 → 3 → 4
```

### Output

```
1 → 1 → 2 → 3 → 4 → 4
```

---

### Follow-up

1. Iterative vs recursive?
2. Space complexity?
3. Why is dummy node useful?

---

## Q4️⃣ Remove Nth Node From End of List (Two Pointers)

### Problem Statement

Remove the nth node from the end of a linked list.

---

### Input

```
1 → 2 → 3 → 4 → 5, n = 2
```

### Output

```
1 → 2 → 3 → 5
```

---

### Follow-up

1. Why two pointers?
2. How do you handle edge cases?
3. What if n equals list length?

---

## Q5️⃣ Valid Parentheses (Stack – Classic Google)

### Problem Statement

Given a string containing parentheses `()[]{}`, determine if the input string is valid.

---

### Input

```
"({[]})"
```

### Output

```
true
```

---

### Follow-up

1. Why stack?
2. What invariant does stack maintain?
3. How to fail early?

---

## Q6️⃣ Next Greater Element (Monotonic Stack)

### Problem Statement

Given an array, return the next greater element for each element.

---

### Input

```
nums = [2,1,2,4,3]
```

### Output

```
[4,2,4,-1,-1]
```

---

### Follow-up

1. Why is this O(n)?
2. Why monotonic decreasing stack?
3. Where is this used in real systems?

---

## Q7️⃣ Implement Queue Using Stacks

### Problem Statement

Implement a queue using two stacks.

---

### Operations

* `push(x)`
* `pop()`
* `peek()`
* `empty()`

---

### Follow-up

1. Amortized complexity?
2. Why two stacks?
3. Where is lazy transfer used?

---

## Q8️⃣ Sliding Window Maximum (Deque – HARD Medium)

### Problem Statement

Given an array `nums` and integer `k`, return the maximum in each sliding window.

---

### Input

```
nums = [1,3,-1,-3,5,3,6,7], k = 3
```

### Output

```
[3,3,5,5,6,7]
```

---

### Follow-up

1. Why not heap?
2. Why deque?
3. How is deque maintained?

---

# ✅ SOLUTIONS & IN-DEPTH EXPLANATIONS

(ONLY AFTER ATTEMPTING)

---

## ✅ Q1 Solution: Reverse Linked List

```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null, curr = head;

    while (curr != null) {
        ListNode next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
```

### Explanation

* Reverse pointers one by one
* Iterative → **O(1) space**
* Recursive → O(n) stack space

---

## ✅ Q2 Solution: Linked List Cycle

```java
public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;

    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}
```

### Why It Works

Fast pointer catches slow pointer if cycle exists.

---

## ✅ Q3 Solution: Merge Two Sorted Lists

```java
public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0);
    ListNode curr = dummy;

    while (l1 != null && l2 != null) {
        if (l1.val <= l2.val) {
            curr.next = l1;
            l1 = l1.next;
        } else {
            curr.next = l2;
            l2 = l2.next;
        }
        curr = curr.next;
    }
    curr.next = (l1 != null) ? l1 : l2;
    return dummy.next;
}
```

---

## ✅ Q4 Solution: Remove Nth Node From End

```java
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;

    ListNode fast = dummy, slow = dummy;
    for (int i = 0; i <= n; i++) fast = fast.next;

    while (fast != null) {
        fast = fast.next;
        slow = slow.next;
    }
    slow.next = slow.next.next;
    return dummy.next;
}
```

---

## ✅ Q5 Solution: Valid Parentheses

```java
public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();

    for (char c : s.toCharArray()) {
        if (c == '(') stack.push(')');
        else if (c == '{') stack.push('}');
        else if (c == '[') stack.push(']');
        else if (stack.isEmpty() || stack.pop() != c) return false;
    }
    return stack.isEmpty();
}
```

---

## ✅ Q6 Solution: Next Greater Element

```java
public int[] nextGreaterElements(int[] nums) {
    int n = nums.length;
    int[] res = new int[n];
    Stack<Integer> stack = new Stack<>();

    for (int i = n - 1; i >= 0; i--) {
        while (!stack.isEmpty() && stack.peek() <= nums[i]) {
            stack.pop();
        }
        res[i] = stack.isEmpty() ? -1 : stack.peek();
        stack.push(nums[i]);
    }
    return res;
}
```

---

## ✅ Q7 Solution: Queue Using Stacks

```java
class MyQueue {
    Stack<Integer> in = new Stack<>();
    Stack<Integer> out = new Stack<>();

    public void push(int x) {
        in.push(x);
    }

    public int pop() {
        peek();
        return out.pop();
    }

    public int peek() {
        if (out.isEmpty()) {
            while (!in.isEmpty()) {
                out.push(in.pop());
            }
        }
        return out.peek();
    }

    public boolean empty() {
        return in.isEmpty() && out.isEmpty();
    }
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
        while (!dq.isEmpty() && dq.peekFirst() <= i - k) {
            dq.pollFirst();
        }
        while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i]) {
            dq.pollLast();
        }
        dq.offerLast(i);
        if (i >= k - 1) {
            res[idx++] = nums[dq.peekFirst()];
        }
    }
    return res;
}
```

---

# 🎯 After Day 3–4 You Should Be Able To

* Manipulate pointers safely
* Use stack for **structure & monotonic problems**
* Optimize sliding window with deque
* Explain **why** not just **how**

---

## NEXT STEP?

👉 **Day 5–6: Trees & Recursion (LCA, DFS, BFS, Serialization)**
or
👉 **Google-style mock interview (Live walkthrough)**

Tell me 👍
