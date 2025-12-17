Excellent approach 👍 — this is **exactly how Google wants you to practice**.

Below is **Day 1–2: Core Data Structures – PRACTICE SET** presented in **two sections**:

1. **📘 QUESTIONS ONLY (very detailed, interview-style)**
2. **✅ SOLUTIONS & IN-DEPTH EXPLANATIONS (at the end)**

Do **NOT** scroll to the solutions until you attempt them.

---

# 📘 DAY 1–2 PRACTICE QUESTIONS (NO SOLUTIONS)

## Q1️⃣ Two Sum (HashMap Pattern)

### Problem Statement

You are given an integer array `nums` and an integer `target`.

Return the **indices** of the two numbers such that:

* `nums[i] + nums[j] == target`
* Each input has **exactly one solution**
* You may **not** use the same element twice

---

### Constraints

* `2 <= nums.length <= 10⁵`
* `-10⁹ <= nums[i] <= 10⁹`
* `-10⁹ <= target <= 10⁹`

---

### Follow-up (Google likes this)

1. Can you solve this in **O(n)** time?
2. Why is sorting not ideal if indices are required?
3. How would the solution change if duplicates exist?

---

## Q2️⃣ Group Anagrams (Hashing + String Pattern)

### Problem Statement

Given an array of strings `strs`, group the anagrams together.

An **anagram** is a word formed by rearranging the letters of another word.

---

### Input Example

```
["eat","tea","tan","ate","nat","bat"]
```

### Output

```
[
  ["eat","tea","ate"],
  ["tan","nat"],
  ["bat"]
]
```

---

### Constraints

* `1 <= strs.length <= 10⁴`
* `0 <= strs[i].length <= 100`
* Strings consist of lowercase English letters

---

### Follow-up

1. What is the time complexity using sorting?
2. How can you optimize it?
3. Why is a frequency array better than sorting?

---

## Q3️⃣ Subarray Sum Equals K (Prefix Sum + HashMap)

### Problem Statement

Given an integer array `nums` and an integer `k`, return the **total number of continuous subarrays** whose sum equals `k`.

---

### Input Example

```
nums = [1,2,3]
k = 3
```

### Output

```
2
```

(Explanation: `[1,2]` and `[3]`)

---

### Constraints

* `1 <= nums.length <= 2 * 10⁴`
* `-1000 <= nums[i] <= 1000`
* `-10⁷ <= k <= 10⁷`

---

### Follow-up

1. Why does sliding window **not** work here?
2. How do negative numbers affect the approach?
3. Why do we store prefix sums in a HashMap?

---

## Q4️⃣ Container With Most Water (Two Pointers)

### Problem Statement

You are given an integer array `height` where `height[i]` represents the height of a vertical line at index `i`.

Find two lines that together with the x-axis form a container that holds the **maximum amount of water**.

---

### Input Example

```
height = [1,8,6,2,5,4,8,3,7]
```

### Output

```
49
```

---

### Follow-up

1. Why does brute force fail?
2. Why do we move the pointer with smaller height?
3. Can this be solved using sorting?

---

## Q5️⃣ Longest Substring Without Repeating Characters (Sliding Window)

### Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

---

### Input Example

```
"abcabcbb"
```

### Output

```
3
```

---

### Constraints

* `0 <= s.length <= 5 * 10⁴`
* `s` consists of English letters, digits, symbols, and spaces

---

### Follow-up

1. What invariant does the sliding window maintain?
2. Why do we shrink the window from the left?
3. Can we optimize space further?

---

## Q6️⃣ Product of Array Except Self (Prefix + Suffix)

### Problem Statement

Given an integer array `nums`, return an array `answer` such that:

```
answer[i] = product of all elements except nums[i]
```

---

### Constraints

* No division allowed
* Time: **O(n)**
* Space: **O(1)** (excluding output array)

---

### Input Example

```
nums = [1,2,3,4]
```

### Output

```
[24,12,8,6]
```

---

### Follow-up

1. How do you handle zero?
2. Why is division not allowed?
3. How does prefix/suffix help?

---

## Q7️⃣ 3Sum (Sorting + Two Pointers)

### Problem Statement

Given an integer array `nums`, return all **unique triplets** `[nums[i], nums[j], nums[k]]` such that:

```
nums[i] + nums[j] + nums[k] == 0
```

---

### Constraints

* Triplets must be **unique**
* Order does not matter

---

### Input Example

```
nums = [-1,0,1,2,-1,-4]
```

### Output

```
[[-1,-1,2],[-1,0,1]]
```

---

### Follow-up

1. Why do we sort first?
2. How do we avoid duplicates?
3. Time complexity?

---

# ✅ SOLUTIONS & IN-DEPTH EXPLANATIONS (SCROLL ONLY AFTER ATTEMPT)

---

## ✅ Q1 Solution: Two Sum

```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
        int need = target - nums[i];
        if (map.containsKey(need)) {
            return new int[]{map.get(need), i};
        }
        map.put(nums[i], i);
    }
    return new int[]{};
}
```

### Explanation

* Store numbers as you traverse
* Check if complement exists
* Single pass → **O(n)**

---

## ✅ Q2 Solution: Group Anagrams

```java
public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> map = new HashMap<>();

    for (String s : strs) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;

        String key = Arrays.toString(freq);
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
    }
    return new ArrayList<>(map.values());
}
```

### Explanation

* Frequency array uniquely identifies anagram
* Faster than sorting

---

## ✅ Q3 Solution: Subarray Sum Equals K

```java
public int subarraySum(int[] nums, int k) {
    Map<Integer, Integer> map = new HashMap<>();
    map.put(0, 1);

    int sum = 0, count = 0;
    for (int num : nums) {
        sum += num;
        count += map.getOrDefault(sum - k, 0);
        map.put(sum, map.getOrDefault(sum, 0) + 1);
    }
    return count;
}
```

### Explanation

* Prefix sum technique
* Handles negative numbers

---

## ✅ Q4 Solution: Container With Most Water

```java
public int maxArea(int[] height) {
    int left = 0, right = height.length - 1, max = 0;

    while (left < right) {
        int area = Math.min(height[left], height[right]) * (right - left);
        max = Math.max(max, area);

        if (height[left] < height[right]) left++;
        else right--;
    }
    return max;
}
```

---

## ✅ Q5 Solution: Longest Substring Without Repeating Characters

```java
public int lengthOfLongestSubstring(String s) {
    Set<Character> set = new HashSet<>();
    int left = 0, max = 0;

    for (int right = 0; right < s.length(); right++) {
        while (set.contains(s.charAt(right))) {
            set.remove(s.charAt(left++));
        }
        set.add(s.charAt(right));
        max = Math.max(max, right - left + 1);
    }
    return max;
}
```

---

## ✅ Q6 Solution: Product of Array Except Self

```java
public int[] productExceptSelf(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];

    result[0] = 1;
    for (int i = 1; i < n; i++) {
        result[i] = result[i - 1] * nums[i - 1];
    }

    int suffix = 1;
    for (int i = n - 1; i >= 0; i--) {
        result[i] *= suffix;
        suffix *= nums[i];
    }
    return result;
}
```

---

## ✅ Q7 Solution: 3Sum

```java
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> res = new ArrayList<>();

    for (int i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;

        int l = i + 1, r = nums.length - 1;
        while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];

            if (sum == 0) {
                res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                while (l < r && nums[l] == nums[l + 1]) l++;
                while (l < r && nums[r] == nums[r - 1]) r--;
                l++; r--;
            } else if (sum < 0) l++;
            else r--;
        }
    }
    return res;
}
```

---

## 🎯 What You Should Master After This

* Identify the **pattern in 30 seconds**
* Explain trade-offs
* Write clean, bug-free code
* Speak while coding

---

## NEXT?

I can now:

* Move to **Day 3–4 (Linked List, Stack, Queue)**
* Give **sliding window HARD problems**
* Conduct **Google-style mock interview**

Just tell me 👍
