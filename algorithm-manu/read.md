## 基础数据结构

### 数组 (Array)

#### 💡 核心概念

数组是一种线性数据结构，使用连续的内存空间存储相同类型的元素。在 Python 中，列表(list)就是动态数组的实现。

#### ⏱️ 时间复杂度分析

| 操作 | 时间复杂度 | 说明 |
|------|------------|------|
| 访问元素 | O(1) | 通过索引直接访问 |
| 修改元素 | O(1) | 通过索引直接修改 |
| 插入元素 | O(n) | 可能需要移动后续元素 |
| 删除元素 | O(n) | 可能需要移动后续元素 |
| 搜索元素 | O(n) | 需要遍历数组 |

#### 🛠️ 常用方法调用示例

```python
# 创建数组
arr = [1, 2, 3, 4, 5]
empty_arr = []
nested_arr = [[1, 2], [3, 4], [5, 6]]

# 访问元素
first_element = arr[0]          # 获取第一个元素: 1
last_element = arr[-1]          # 获取最后一个元素: 5
sub_array = arr[1:4]            # 获取子数组: [2, 3, 4]
step_array = arr[::2]           # 步长为2的切片: [1, 3, 5]

# 修改元素
arr[2] = 10                     # 修改索引为2的元素: [1, 2, 10, 4, 5]
arr[1:3] = [20, 30]             # 替换切片: [1, 20, 30, 4, 5]

# 添加元素
arr.append(6)                    # 在末尾添加元素: [1, 20, 30, 4, 5, 6]
arr.insert(2, 15)               # 在索引2处插入元素: [1, 20, 15, 30, 4, 5, 6]
arr.extend([7, 8])               # 扩展列表: [1, 20, 15, 30, 4, 5, 6, 7, 8]

# 删除元素
removed = arr.pop()              # 删除并返回最后一个元素: 8, 数组变为 [1, 20, 15, 30, 4, 5, 6, 7]
removed = arr.pop(2)             # 删除并返回索引2的元素: 15, 数组变为 [1, 20, 30, 4, 5, 6, 7]
arr.remove(30)                   # 删除第一个值为30的元素: [1, 20, 4, 5, 6, 7]
del arr[1:3]                     # 删除切片: [1, 5, 6, 7]

# 查找元素
index = arr.index(5)            # 查找元素5的索引: 1
count = arr.count(5)             # 统计元素5出现的次数: 1
is_present = 5 in arr            # 检查元素是否存在: True

# 排序
arr.sort()                       # 原地排序: [1, 5, 6, 7]
arr.sort(reverse=True)           # 降序排序: [7, 6, 5, 1]
sorted_arr = sorted(arr)         # 返回排序后的新数组: [1, 5, 6, 7]

# 反转
arr.reverse()                    # 原地反转: [1, 5, 6, 7]
reversed_arr = arr[::-1]         # 切片反转: [7, 6, 5, 1]

# 数组操作
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
combined = arr1 + arr2           # 数组连接: [1, 2, 3, 4, 5, 6]
repeated = arr1 * 3              # 数组重复: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 数组函数
length = len(arr)                # 数组长度: 4
max_val = max(arr)               # 最大值: 7
min_val = min(arr)               # 最小值: 1
total = sum(arr)                 # 求和: 19

# 数组转换
str_arr = list("hello")          # 字符串转数组: ['h', 'e', 'l', 'l', 'o']
num_str = "".join(map(str, arr)) # 数组转字符串: '1567'

# 列表推导式
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in arr if x % 2 == 0]  # [6]
nested_flat = [x for sublist in nested_arr for x in sublist]  # [1, 2, 3, 4, 5, 6]

# 二维数组操作
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(matrix)               # 行数: 3
cols = len(matrix[0])            # 列数: 3
diagonal = [matrix[i][i] for i in range(min(rows, cols))]  # 对角线元素: [1, 5, 9]
transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]  # 转置矩阵

# 数组复制
shallow_copy = arr.copy()        # 浅拷贝
deep_copy = arr[:]               # 浅拷贝
import copy
deep_copy2 = copy.deepcopy(arr)  # 深拷贝

# 数组清空
arr.clear()                      # 清空数组: []
```

#### 🔍 常见问题与技巧

- **原地操作**：利用双指针技巧实现原地修改数组，节省空间
- **边界处理**：注意数组为空、只有一个元素等边界情况
- **索引越界**：确保数组访问不会越界，特别是在循环中

#### 🎯 LeetCode 常见应用

```python
# 1. 双指针技巧 - 两数之和
def two_sum(nums, target):
    """
    两数之和 - 使用哈希表优化
    时间复杂度: O(n), 空间复杂度: O(n)
    LeetCode: 1. Two Sum
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# 2. 双指针技巧 - 删除排序数组中的重复项
def remove_duplicates(nums):
    """
    删除排序数组中的重复项
    时间复杂度: O(n), 空间复杂度: O(1)
    LeetCode: 26. Remove Duplicates from Sorted Array
    """
    if not nums:
        return 0
    
    slow = 0  # 慢指针指向不重复元素的最后一个位置
    for fast in range(1, len(nums)):  # 快指针遍历整个数组
        if nums[fast] != nums[slow]:  # 发现不重复元素
            slow += 1
            nums[slow] = nums[fast]  # 将不重复元素移到前面
    
    return slow + 1  # 返回不重复数组的长度

# 3. 滑动窗口 - 长度最小的子数组
def min_subarray_len(s, nums):
    """
    长度最小的子数组
    时间复杂度: O(n), 空间复杂度: O(1)
    LeetCode: 209. Minimum Size Subarray Sum
    """
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        # 当窗口内和大于等于目标值时，尝试缩小窗口
        while current_sum >= s:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

# 4. 螺旋矩阵
def spiral_order(matrix):
    """
    螺旋矩阵
    时间复杂度: O(m*n), 空间复杂度: O(1) (不计结果存储)
    LeetCode: 54. Spiral Matrix
    """
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # 从左到右
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # 从上到下
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # 从右到左
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # 从下到上
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result
```

---