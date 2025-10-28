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

---

### 链表 (Linked List)

#### 💡 核心概念

链表是由节点组成的线性数据结构，每个节点包含数据和指向下一个节点的指针。与数组不同，链表的元素在内存中不连续。

#### ⏱️ 时间复杂度分析

| 操作 | 时间复杂度 | 说明 |
|------|------------|------|
| 访问元素 | O(n) | 需要从头节点遍历 |
| 修改元素 | O(n) | 需要先找到元素 |
| 插入元素 | O(1) | 如果已有指针 |
| 删除元素 | O(1) | 如果已有指针 |
| 搜索元素 | O(n) | 需要遍历链表 |

#### 🛠️ 常用方法调用示例

```python
# 链表节点定义
class ListNode:
    """链表节点定义"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 创建链表
def create_linked_list(values):
    """根据值列表创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

# 遍历链表
def traverse_linked_list(head):
    """遍历链表并返回值列表"""
    values = []
    current = head
    
    while current:
        values.append(current.val)
        current = current.next
    
    return values

# 在链表头部插入节点
def insert_at_head(head, val):
    """在链表头部插入节点"""
    new_node = ListNode(val, head)
    return new_node

# 在链表尾部插入节点
def insert_at_tail(head, val):
    """在链表尾部插入节点"""
    new_node = ListNode(val)
    
    if not head:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    return head

# 在指定位置插入节点
def insert_at_position(head, val, position):
    """在指定位置插入节点"""
    if position == 0:
        return insert_at_head(head, val)
    
    new_node = ListNode(val)
    current = head
    
    # 找到插入位置的前一个节点
    for _ in range(position - 1):
        if not current:
            return head  # 位置超出链表长度
        current = current.next
    
    if current:
        new_node.next = current.next
        current.next = new_node
    
    return head

# 删除指定值的节点
def delete_by_value(head, val):
    """删除第一个值为val的节点"""
    if not head:
        return None
    
    # 如果要删除的是头节点
    if head.val == val:
        return head.next
    
    current = head
    while current.next and current.next.val != val:
        current = current.next
    
    if current.next:
        current.next = current.next.next
    
    return head

# 删除指定位置的节点
def delete_at_position(head, position):
    """删除指定位置的节点"""
    if not head:
        return None
    
    if position == 0:
        return head.next
    
    current = head
    
    # 找到要删除节点的前一个节点
    for _ in range(position - 1):
        if not current.next:
            return head  # 位置超出链表长度
        current = current.next
    
    if current.next:
        current.next = current.next.next
    
    return head

# 查找节点
def find_node(head, val):
    """查找值为val的节点，返回节点引用"""
    current = head
    
    while current:
        if current.val == val:
            return current
        current = current.next
    
    return None

# 获取链表长度
def get_length(head):
    """获取链表长度"""
    length = 0
    current = head
    
    while current:
        length += 1
        current = current.next
    
    return length

# 获取链表中间节点
def get_middle_node(head):
    """获取链表中间节点（使用快慢指针）"""
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# 反转链表
def reverse_linked_list(head):
    """反转链表"""
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# 合并两个有序链表
def merge_sorted_lists(l1, l2):
    """合并两个有序链表"""
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 else l2
    return dummy.next

# 检测链表是否有环
def has_cycle(head):
    """检测链表是否有环"""
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True

# 创建带环的链表（用于测试）
def create_cyclic_list(values, cycle_pos):
    """创建带环的链表，cycle_pos表示环的起始位置"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    cycle_node = None
    
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        
        if i == cycle_pos:
            cycle_node = current
    
    # 如果cycle_pos为0，则头节点是环的起始节点
    if cycle_pos == 0:
        cycle_node = head
    
    # 创建环
    if cycle_node:
        current.next = cycle_node
    
    return head

# 示例使用
if __name__ == "__main__":
    # 创建链表
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    print("原始链表:", traverse_linked_list(head))  # [1, 2, 3, 4, 5]
    
    # 在头部插入
    head = insert_at_head(head, 0)
    print("头部插入后:", traverse_linked_list(head))  # [0, 1, 2, 3, 4, 5]
    
    # 在尾部插入
    head = insert_at_tail(head, 6)
    print("尾部插入后:", traverse_linked_list(head))  # [0, 1, 2, 3, 4, 5, 6]
    
    # 在指定位置插入
    head = insert_at_position(head, 99, 3)
    print("位置3插入后:", traverse_linked_list(head))  # [0, 1, 2, 99, 3, 4, 5, 6]
    
    # 删除指定值的节点
    head = delete_by_value(head, 99)
    print("删除99后:", traverse_linked_list(head))  # [0, 1, 2, 3, 4, 5, 6]
    
    # 删除指定位置的节点
    head = delete_at_position(head, 0)
    print("删除位置0后:", traverse_linked_list(head))  # [1, 2, 3, 4, 5, 6]
    
    # 查找节点
    node = find_node(head, 3)
    print("查找3:", node.val if node else "未找到")  # 3
    
    # 获取链表长度
    length = get_length(head)
    print("链表长度:", length)  # 6
    
    # 获取中间节点
    middle = get_middle_node(head)
    print("中间节点:", middle.val if middle else "未找到")  # 3
    
    # 反转链表
    head = reverse_linked_list(head)
    print("反转后:", traverse_linked_list(head))  # [6, 5, 4, 3, 2, 1]
    
    # 创建另一个有序链表
    values2 = [2, 4, 6, 8]
    head2 = create_linked_list(values2)
    
    # 合并两个有序链表
    merged = merge_sorted_lists(head, head2)
    print("合并后:", traverse_linked_list(merged))  # [1, 2, 2, 3, 4, 4, 5, 6, 6, 8]
    
    # 检测环
    cyclic_head = create_cyclic_list([1, 2, 3, 4], 1)  # 在位置1创建环
    print("是否有环:", has_cycle(cyclic_head))  # True
```

---

### 栈 (Stack)

#### 💡 核心概念

栈是一种后进先出(LIFO)的数据结构。在 Python 中，可以使用列表(list)或 collections.deque 实现栈。

#### ⏱️ 时间复杂度分析

| 操作 | 时间复杂度 | 说明 |
|------|------------|------|
| 入栈(push) | O(1) | 在栈顶添加元素 |
| 出栈(pop) | O(1) | 从栈顶移除元素 |
| 查看栈顶元素 | O(1) | 获取栈顶元素但不移除 |
| 判断栈是否为空 | O(1) | 检查栈是否为空 |

#### 🛠️ 常用方法调用示例

```python
# 基于列表的栈实现
class ListStack:
    """基于列表的栈实现"""
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """检查栈是否为空"""
        return len(self.items) == 0
    
    def push(self, item):
        """入栈"""
        self.items.append(item)
    
    def pop(self):
        """出栈"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def size(self):
        """获取栈大小"""
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

# 基于collections.deque的栈实现（推荐）
from collections import deque

class DequeStack:
    """基于collections.deque的栈实现（推荐）"""
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        """检查栈是否为空"""
        return len(self.items) == 0
    
    def push(self, item):
        """入栈"""
        self.items.append(item)
    
    def pop(self):
        """出栈"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def size(self):
        """获取栈大小"""
        return len(self.items)
    
    def __str__(self):
        return str(list(self.items))

# 栈的应用示例

# 1. 括号匹配
def check_brackets(expression):
    """检查表达式中的括号是否匹配"""
    stack = DequeStack()
    brackets = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in brackets.keys():  # 左括号
            stack.push(char)
        elif char in brackets.values():  # 右括号
            if stack.is_empty():
                return False
            
            left_bracket = stack.pop()
            if brackets[left_bracket] != char:
                return False
    
    return stack.is_empty()

# 2. 中缀表达式转后缀表达式
def infix_to_postfix(expression):
    """中缀表达式转后缀表达式"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = DequeStack()
    output = []
    
    for char in expression:
        if char.isalnum():  # 操作数
            output.append(char)
        elif char == '(':  # 左括号
            stack.push(char)
        elif char == ')':  # 右括号
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # 弹出左括号
        else:  # 操作符
            while (not stack.is_empty() and stack.peek() != '(' and
                   precedence.get(stack.peek(), 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.push(char)
    
    # 弹出栈中剩余的操作符
    while not stack.is_empty():
        output.append(stack.pop())
    
    return ''.join(output)

# 3. 计算后缀表达式
def evaluate_postfix(expression):
    """计算后缀表达式"""
    stack = DequeStack()
    
    for char in expression:
        if char.isdigit():  # 操作数
            stack.push(int(char))
        else:  # 操作符
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            elif char == '^':
                result = operand1 ** operand2
            
            stack.push(result)
    
    return stack.pop()

# 4. 栈排序
def sort_stack(stack):
    """使用一个辅助栈对原栈进行排序（从栈底到栈顶递增）"""
    temp_stack = DequeStack()
    
    while not stack.is_empty():
        # 将原栈的元素弹出
        temp = stack.pop()
        
        # 将辅助栈中比当前元素大的元素移回原栈
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        
        # 将当前元素压入辅助栈
        temp_stack.push(temp)
    
    # 将辅助栈中的元素移回原栈
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    
    return stack

# 5. 删除栈中所有特定元素
def remove_elements(stack, value):
    """删除栈中所有值为value的元素"""
    temp_stack = DequeStack()
    
    # 将所有不是value的元素移到临时栈
    while not stack.is_empty():
        item = stack.pop()
        if item != value:
            temp_stack.push(item)
    
    # 将元素移回原栈
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    
    return stack

# 6. 反转栈
def reverse_stack(stack):
    """反转栈"""
    queue = deque()  # 使用队列作为辅助
    
    # 将栈中元素移到队列
    while not stack.is_empty():
        queue.append(stack.pop())
    
    # 将队列中元素移回栈
    while queue:
        stack.push(queue.popleft())
    
    return stack

# 示例使用
if __name__ == "__main__":
    # 创建栈
    stack = DequeStack()
    print("栈是否为空:", stack.is_empty())  # True
    
    # 入栈操作
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("栈内容:", stack)  # [1, 2, 3]
    print("栈大小:", stack.size())  # 3
    print("栈顶元素:", stack.peek())  # 3
    
    # 出栈操作
    item = stack.pop()
    print("出栈元素:", item)  # 3
    print("栈内容:", stack)  # [1, 2]
    
    # 括号匹配
    expression = "{[()()]}"
    print("括号是否匹配:", check_brackets(expression))  # True
    
    # 中缀转后缀
    infix = "a+b*(c^d-e)^(f+g*h)-i"
    postfix = infix_to_postfix(infix)
    print("中缀表达式:", infix)
    print("后缀表达式:", postfix)  # abcd^e-fgh*+^*+i-
    
    # 计算后缀表达式
    postfix_expr = "231*+9-"
    result = evaluate_postfix(postfix_expr)
    print("后缀表达式 {} 的计算结果:".format(postfix_expr), result)  # -4
    
    # 栈排序
    unsorted_stack = DequeStack()
    for num in [3, 1, 4, 2, 5]:
        unsorted_stack.push(num)
    print("排序前:", unsorted_stack)  # [3, 1, 4, 2, 5]
    sorted_stack = sort_stack(unsorted_stack)
    print("排序后:", sorted_stack)  # [5, 4, 3, 2, 1]
    
    # 删除特定元素
    stack_with_duplicates = DequeStack()
    for num in [1, 2, 3, 2, 4, 2, 5]:
        stack_with_duplicates.push(num)
    print("删除前:", stack_with_duplicates)  # [1, 2, 3, 2, 4, 2, 5]
    cleaned_stack = remove_elements(stack_with_duplicates, 2)
    print("删除2后:", cleaned_stack)  # [1, 3, 4, 5]
    
    # 反转栈
    stack_to_reverse = DequeStack()
    for num in [1, 2, 3, 4, 5]:
        stack_to_reverse.push(num)
    print("反转前:", stack_to_reverse)  # [1, 2, 3, 4, 5]
    reversed_stack = reverse_stack(stack_to_reverse)
    print("反转后:", reversed_stack)  # [5, 4, 3, 2, 1]
```

---