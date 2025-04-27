
---

# 📚 LeetCode Problem Solving Patterns — Explanations + Pseudocode

---

## 1. **Hashing**

### What it is:
- Store values (keys) for fast O(1) lookup using a **Hash Table** (Dictionary/Map).
- Common for counting, checking duplicates, quick search.

### When to use:
- "Find two numbers", "check if exists", "frequency count".

### Pseudocode:

```plaintext
Initialize empty hash map
For each item in input:
    If item is in hash map:
        Do something (e.g., return, count)
    Else:
        Add item to hash map
```

---

## 2. **Two Pointers**

### What it is:
- Maintain **two indices** to traverse a list, either moving **together** or **towards each other**.
- Optimize space/time compared to nested loops.

### When to use:
- Sorted arrays, finding pairs/triplets, removing duplicates.

### Pseudocode:

```plaintext
Initialize two pointers: left = 0, right = end of list
While left < right:
    If condition is met:
        Do something (e.g., save pair, move pointers)
    Else if need a bigger value:
        Move left pointer
    Else:
        Move right pointer
```

---

## 3. **Sliding Window**

### What it is:
- Maintain a **subarray** and **slide** the window without re-computing everything.
- Optimizes problems that need "substrings", "subarrays", "k-length windows".

### When to use:
- Longest substring, max sum of subarray, minimum window.

### Pseudocode:

```plaintext
Initialize window start
For window end from 0 to n:
    Expand window
    If window is valid:
        Update answer
        (Optionally) Shrink window from start
```

---

## 4. **Dynamic Programming (DP)**

### What it is:
- Break big problem into **subproblems**.
- Store solutions to subproblems (memoization/tabulation).
- Avoid recalculating.

### When to use:
- "Max/Min ways", "number of combinations", "optimization problems".

### Pseudocode:

```plaintext
Create DP table initialized for base cases
For i from 1 to n:
    For each option/choice:
        DP[i] = best solution based on previous DP states
Return DP[n]
```

---

## 5. **Expand Around Center**

### What it is:
- Start from the center of the string and **expand outward**.
- Used for symmetric patterns (like palindromes).

### When to use:
- Palindromic substrings, center-based problems.

### Pseudocode:

```plaintext
For each character (or between characters) in string:
    Expand outward while left == right
    Update longest result
```

---

## 6. **Interval Merging**

### What it is:
- Sort intervals, then merge overlapping ones.

### When to use:
- Calendar meetings, merging ranges, overlapping areas.

### Pseudocode:

```plaintext
Sort intervals by start time
Initialize merged list
For each interval:
    If merged is empty or no overlap:
        Add interval
    Else:
        Merge with last interval
Return merged
```

---

## 7. **Sweep Line**

### What it is:
- Think of events on a **number line** ordered by time.
- Process "start" and "end" events separately.

### When to use:
- Counting overlaps, event scheduling.

### Pseudocode:

```plaintext
Create events list: (+1 for start, -1 for end)
Sort events by time
Initialize counter = 0
For each event:
    Update counter
    Track maximum overlap
```

---

## 8. **Binary Search**

### What it is:
- Divide the search space into halves every step.
- O(log n) search time.

### When to use:
- Search sorted arrays, rotated arrays, "min/max" problems.

### Pseudocode:

```plaintext
Initialize low and high pointers
While low <= high:
    Compute mid
    If mid value == target:
        Return mid
    Else if mid value > target:
        Search left half
    Else:
        Search right half
Return not found
```

---

## 9. **Backtracking**

### What it is:
- Explore **all possibilities** by making a choice, exploring further, and undoing the choice ("backtrack").

### When to use:
- Combinations, permutations, puzzles like Sudoku, N-Queens.

### Pseudocode:

```plaintext
Define backtrack(current state):
    If goal reached:
        Save current solution
    For each choice:
        Make a choice
        Call backtrack(next state)
        Undo the choice
Call backtrack(initial state)
```

---

## 10. **Topological Sort / Cycle Detection**

### What it is:
- **Ordering of tasks** given dependency constraints.
- Detect cycles in a directed graph.

### When to use:
- Course schedule, build systems, dependency resolution.

### Pseudocode:

```plaintext
Build graph and in-degree table
Initialize queue with nodes of 0 in-degree
While queue is not empty:
    Pop a node
    Decrease in-degree of its neighbors
    If neighbor has 0 in-degree, add to queue
If all nodes processed:
    Return valid order
Else:
    Cycle detected (no valid ordering)
```

---

## 11. **Heap / Priority Queue**

### What it is:
- Maintain dynamically the **minimum** or **maximum** element.
- Useful for top-K problems.

### When to use:
- Top K frequent, merging sorted lists, median stream.

### Pseudocode:

```plaintext
Initialize min heap or max heap
For each element:
    Add to heap
    If heap size > K:
        Remove top element
Return heap elements
```

---

## 12. **Design (Hashmap + Linked List etc.)**

### What it is:
- Carefully design efficient data structures combining multiple structures (e.g., hashmaps for O(1) lookup + linked list for O(1) updates).

### When to use:
- LRU cache, design Twitter feed, random set.

### Pseudocode:

```plaintext
Use hashmap for fast lookup
Use linked list to track order
On get:
    Move item to front
On put:
    If exists, update and move to front
    Else:
        Add new item to front
        If over capacity:
            Remove least recently used item
```

---

## 13. **Bit Manipulation**

### What it is:
- Directly manipulate bits to achieve **O(1)** or very fast solutions.
- Tricks like XOR, bit shifts.

### When to use:
- Math problems, missing number, odd-even, add/subtract without + operator.

### Pseudocode:

```plaintext
While second number is not 0:
    Carry = (a AND b) shifted left by 1
    Sum = (a XOR b)
    Update a and b
Return a
```

---
---

# LeetCode Problem-Solving Patterns — Explained with Python Examples

---

## 1. **Hashing / Two Pointers**

### Hashing

- **Idea:** Use a dictionary (hashmap) to store and lookup values in constant time.
- **When:** Fast lookup, duplicate detection, frequency counts.

### Example: Two Sum (LeetCode 1)

```python
def twoSum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
```

---

### Two Pointers

- **Idea:** Use two pointers moving towards each other or in the same direction.
- **When:** Sorted arrays, finding pairs, removing duplicates.

### Example: 3Sum

```python
def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicates
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return res
```

---

## 2. **Sliding Window**

- **Idea:** Maintain a window (subarray) and slide it to optimize.
- **When:** Maximum/minimum subarray, unique substrings.

### Example: Longest Substring Without Repeating Characters

```python
def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

---

## 3. **Dynamic Programming (DP)**

- **Idea:** Break the problem into smaller subproblems and build the answer from them.
- **When:** Overlapping subproblems and optimal substructure.

### Example: Coin Change

```python
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
    return dp[amount] if dp[amount] != float('inf') else -1
```

---

## 4. **Expand Around Center**

- **Idea:** For problems like palindromic substrings, expand outwards from the center.
- **When:** Finding symmetric properties.

### Example: Longest Palindromic Substring

```python
def longestPalindrome(s):
    res = ""
    
    for i in range(len(s)):
        res = max(res, expand(s, i, i), expand(s, i, i+1), key=len)
    
    return res

def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]
```

---

## 5. **Interval Merging**

- **Idea:** Sort intervals and merge overlapping ones.
- **When:** Calendar, meetings, ranges.

### Example: Merge Intervals

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged
```

---

## 6. **Sweep Line**

- **Idea:** Think of the events happening on a number line in sorted order.
- **When:** Scheduling, overlapping intervals.

### Example: Meeting Rooms II

```python
import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = []
    
    heapq.heappush(heap, intervals[0][1])
    
    for interval in intervals[1:]:
        if heap[0] <= interval[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
    
    return len(heap)
```

---

## 7. **Binary Search**

- **Idea:** Divide and conquer to locate an element in O(log n) time.
- **When:** Sorted array, rotated array, search space problems.

### Example: Search in Rotated Sorted Array

```python
def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
```

---

## 8. **Backtracking**

- **Idea:** Try all possibilities and backtrack if a choice leads to an invalid solution.
- **When:** Combinations, subsets, puzzles.

### Example: Subsets

```python
def subsets(nums):
    res = []
    
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    
    backtrack(0, [])
    return res
```

---

## 9. **Topological Sort / Graph Cycle Detection**

- **Idea:** Order nodes so that for every directed edge `u → v`, `u` comes before `v`.
- **When:** Scheduling, prerequisites.

### Example: Course Schedule

```python
def canFinish(numCourses, prerequisites):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    for u, v in prerequisites:
        graph[v].append(u)
        indegree[u] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    
    while queue:
        course = queue.popleft()
        numCourses -= 1
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return numCourses == 0
```

---

## 10. **Heap / Priority Queue**

- **Idea:** Always retrieve the minimum or maximum element efficiently.
- **When:** Merging sorted lists, frequent elements.

### Example: Top K Frequent Elements

```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

---

## 11. **Design**

- **Idea:** Combine data structures properly to meet complex requirements.
- **When:** LRU cache, Twitter design, random set.

### Example: LRU Cache

```python
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

---

## 12. **Bit Manipulation**

- **Idea:** Manipulate individual bits using bitwise operators.
- **When:** Math tricks, optimization, XOR problems.

### Example: Sum of Two Integers

```python
def getSum(a, b):
    MASK = 0xFFFFFFFF
    MAX = 0x7FFFFFFF

    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    return a if a <= MAX else ~(a ^ MASK)
```

---

