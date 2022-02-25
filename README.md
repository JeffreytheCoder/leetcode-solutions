# leetcode-solutions
My leetcode solutions in Python, updating ~10 problems per week :rocket:

## Solution Format
Each solution contains
<ul>
  <li> category [difficulty out of 5] </li>
  <li> key: one to two important key concepts to understand the approach of this solution </li> 
  <li> solutions with different approaches, e.g. iterative & recursive </li>
  <li> time & space complexity </li>
</ul>
*difficulty is set by personal consideration, since I think the leetcode default easy/medium/hard difficulty for some problems is not accurate

### Example
```
# hashmap [1/5]

# key: to find another value that adds up to target with current value in a single loop, use hashmap to store {num in nums: its idx}

# for each (num, idx) in nums:
#   if (target - num) is in hashmap, return idx and hashmap[target - num]
#   else store {num: idx} to hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for idx, val in enumerate(nums):
            if (target - val) in dict:
                return [idx, dict[target - val]]
            else:
                dict[val] = idx
                
# time: O(n)
# space: O(n)
```

## Categories of Solutions
<table>
  <thead>
    <th> Category </th>
    <th> # of problems </th>
  </thead>
  <tr>
    <td> Array </td>
    <td> 1 </td>
  </tr>
  <tr>
    <td> String </td>
    <td> 2 </td>
  </tr>
  <tr>
    <td> Linked List </td>
    <td> 1 </td>
  </tr>
  <tr>
    <td> Stack & Queue </td>
    <td> 1 </td>
  </tr>
  <tr>
    <td> Hashmap </td>
    <td> 3 </td>
  </tr>
  <tr>
    <td> Binary Tree </td>
    <td> 18 </td>
  </tr>
  <tr>
    <td> Binary Search Tree </td>
    <td> 0 </td>
  </tr>
  <tr>
    <td> Backtracking </td>
    <td> 0 </td>
  </tr>
  <tr>
    <td> Greedy </td>
    <td> 0 </td>
  </tr>
  <tr>
    <td> Dynammic Programming </td>
    <td> 1 </td>
  </tr>
</table>
Each solution can be in more than one category


Happy leetcode!
