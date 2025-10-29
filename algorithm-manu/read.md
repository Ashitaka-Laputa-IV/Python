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

### 队列 (Queue)

#### 💡 核心概念

队列是一种先进先出(FIFO)的数据结构。在 Python 中，可以使用 collections.deque 实现高效的队列。

#### ⏱️ 时间复杂度分析

| 操作 | 时间复杂度 | 说明 |
|------|------------|------|
| 入队(enqueue) | O(1) | 在队尾添加元素 |
| 出队(dequeue) | O(1) | 从队首移除元素 |
| 查看队首元素 | O(1) | 获取队首元素但不移除 |
| 判断队列是否为空 | O(1) | 检查队列是否为空 |

#### 🛠️ 常用方法调用示例

```python
from collections import deque
import queue
import threading
import time

# 基于collections.deque的队列实现（推荐）
class DequeQueue:
    """基于collections.deque的队列实现（推荐）"""
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        """检查队列是否为空"""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """入队"""
        self.items.append(item)
    
    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()
    
    def peek(self):
        """查看队首元素"""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]
    
    def size(self):
        """获取队列大小"""
        return len(self.items)
    
    def __str__(self):
        return str(list(self.items))

# 基于queue.Queue的线程安全队列
class ThreadSafeQueue:
    """基于queue.Queue的线程安全队列"""
    def __init__(self, maxsize=0):
        self.queue = queue.Queue(maxsize)
    
    def is_empty(self):
        """检查队列是否为空"""
        return self.queue.empty()
    
    def enqueue(self, item, block=True, timeout=None):
        """入队"""
        self.queue.put(item, block=block, timeout=timeout)
    
    def dequeue(self, block=True, timeout=None):
        """出队"""
        return self.queue.get(block=block, timeout=timeout)
    
    def peek(self):
        """查看队首元素（非阻塞）"""
        try:
            return self.queue.queue[0]
        except IndexError:
            raise IndexError("peek from empty queue")
    
    def size(self):
        """获取队列大小"""
        return self.queue.qsize()
    
    def task_done(self):
        """标记任务完成"""
        self.queue.task_done()
    
    def join(self):
        """等待所有任务完成"""
        self.queue.join()
    
    def __str__(self):
        return str(list(self.queue.queue))

# 基于列表的队列实现（不推荐，出队操作效率低）
class ListQueue:
    """基于列表的队列实现（不推荐，出队操作效率低）"""
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """检查队列是否为空"""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """入队"""
        self.items.append(item)
    
    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)  # O(n)操作，效率低
    
    def peek(self):
        """查看队首元素"""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]
    
    def size(self):
        """获取队列大小"""
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

# 循环队列实现
class CircularQueue:
    """循环队列实现"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0
    
    def is_empty(self):
        """检查队列是否为空"""
        return self.count == 0
    
    def is_full(self):
        """检查队列是否已满"""
        return self.count == self.capacity
    
    def enqueue(self, item):
        """入队"""
        if self.is_full():
            raise Exception("Queue is full")
        
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
    
    def dequeue(self):
        """出队"""
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return item
    
    def peek(self):
        """查看队首元素"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[self.front]
    
    def size(self):
        """获取队列大小"""
        return self.count
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        
        result = []
        index = self.front
        for _ in range(self.count):
            result.append(str(self.items[index]))
            index = (index + 1) % self.capacity
        
        return "[" + ", ".join(result) + "]"

# 队列的应用示例

# 1. 约瑟夫问题
def josephus_problem(n, k):
    """约瑟夫问题：n个人围成一圈，从第一个人开始报数，数到k的人出列"""
    q = DequeQueue()
    
    # 初始化队列
    for i in range(1, n + 1):
        q.enqueue(i)
    
    result = []
    while not q.is_empty():
        # 将前k-1个人移到队尾
        for _ in range(k - 1):
            q.enqueue(q.dequeue())
        
        # 第k个人出列
        result.append(q.dequeue())
    
    return result

# 2. 任务调度器
def task_scheduler(tasks, cooldown):
    """任务调度器：相同任务之间至少需要cooldown个时间单位"""
    from collections import defaultdict, deque
    
    task_count = defaultdict(int)
    for task in tasks:
        task_count[task] += 1
    
    # 按任务数量排序
    sorted_tasks = sorted(task_count.items(), key=lambda x: x[1], reverse=True)
    
    # 使用队列模拟时间线
    time = 0
    task_queue = deque()
    
    # 初始化任务队列
    for task, count in sorted_tasks:
        task_queue.append((task, count, 0))  # (任务, 剩余次数, 可执行时间)
    
    while task_queue:
        time += 1
        
        # 检查队首任务是否可以执行
        if task_queue[0][2] <= time:
            task, count, _ = task_queue.popleft()
            count -= 1
            
            if count > 0:
                # 任务还有剩余，加入队列尾部，设置冷却时间
                task_queue.append((task, count, time + cooldown))
    
    return time

# 3. 二叉树的层序遍历（使用队列）
class TreeNode:
    """二叉树节点定义"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    """二叉树的层序遍历"""
    if not root:
        return []
    
    result = []
    q = DequeQueue()
    q.enqueue(root)
    
    while not q.is_empty():
        level_size = q.size()
        current_level = []
        
        for _ in range(level_size):
            node = q.dequeue()
            current_level.append(node.val)
            
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        
        result.append(current_level)
    
    return result

# 4. 生产者-消费者模型
def producer_consumer_example():
    """生产者-消费者模型示例"""
    buffer = ThreadSafeQueue(maxsize=5)  # 缓冲区大小为5
    
    def producer():
        """生产者线程"""
        for i in range(10):
            item = f"Item-{i}"
            buffer.enqueue(item)
            print(f"生产: {item}")
            time.sleep(0.1)  # 模拟生产时间
    
    def consumer():
        """消费者线程"""
        for _ in range(10):
            item = buffer.dequeue()
            print(f"消费: {item}")
            time.sleep(0.2)  # 模拟消费时间
    
    # 创建并启动线程
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    producer_thread.start()
    consumer_thread.start()
    
    # 等待线程完成
    producer_thread.join()
    consumer_thread.join()

# 5. 队列排序
def sort_queue(q):
    """使用递归对队列进行排序（升序）"""
    if q.is_empty():
        return q
    
    # 获取队首元素
    temp = q.dequeue()
    
    # 递归排序剩余队列
    sort_queue(q)
    
    # 将元素插入到正确位置
    insert_sorted(q, temp)
    return q

def insert_sorted(q, item):
    """将元素插入到已排序队列的正确位置"""
    # 如果队列为空或队首元素大于等于待插入元素，直接入队
    if q.is_empty() or q.peek() >= item:
        q.enqueue(item)
        return
    
    # 否则，递归处理
    temp = q.dequeue()
    insert_sorted(q, item)
    q.enqueue(temp)

# 6. 队列反转
def reverse_queue(q):
    """反转队列"""
    if q.is_empty():
        return q
    
    # 获取队首元素
    temp = q.dequeue()
    
    # 递归反转剩余队列
    reverse_queue(q)
    
    # 将元素入队
    q.enqueue(temp)
    return q

# 示例使用
if __name__ == "__main__":
    # 创建队列
    q = DequeQueue()
    print("队列是否为空:", q.is_empty())  # True
    
    # 入队操作
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("队列内容:", q)  # [1, 2, 3]
    print("队列大小:", q.size())  # 3
    print("队首元素:", q.peek())  # 1
    
    # 出队操作
    item = q.dequeue()
    print("出队元素:", item)  # 1
    print("队列内容:", q)  # [2, 3]
    
    # 约瑟夫问题
    result = josephus_problem(7, 3)
    print("约瑟夫问题结果:", result)  # [3, 6, 2, 7, 5, 1, 4]
    
    # 任务调度器
    tasks = ["A", "A", "A", "B", "B", "B"]
    min_time = task_scheduler(tasks, 2)
    print("任务调度最短时间:", min_time)  # 8
    
    # 二叉树层序遍历
    # 构建二叉树
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    traversal = level_order_traversal(root)
    print("二叉树层序遍历:", traversal)  # [[1], [2, 3], [4, 5, 6]]
    
    # 循环队列
    circular_q = CircularQueue(5)
    for i in range(1, 6):
        circular_q.enqueue(i)
    print("循环队列:", circular_q)  # [1, 2, 3, 4, 5]
    
    circular_q.dequeue()
    circular_q.dequeue()
    circular_q.enqueue(6)
    circular_q.enqueue(7)
    print("循环队列操作后:", circular_q)  # [3, 4, 5, 6, 7]
    
    # 队列排序
    unsorted_q = DequeQueue()
    for num in [3, 1, 4, 2, 5]:
        unsorted_q.enqueue(num)
    print("排序前:", unsorted_q)  # [3, 1, 4, 2, 5]
    sorted_q = sort_queue(unsorted_q)
    print("排序后:", sorted_q)  # [1, 2, 3, 4, 5]
    
    # 队列反转
    reverse_test_q = DequeQueue()
    for num in [1, 2, 3, 4, 5]:
        reverse_test_q.enqueue(num)
    print("反转前:", reverse_test_q)  # [1, 2, 3, 4, 5]
    reversed_q = reverse_queue(reverse_test_q)
    print("反转后:", reversed_q)  # [5, 4, 3, 2, 1]
```

---

### 哈希表 (Hash Table)

#### 💡 核心概念

哈希表是通过键(key)的哈希值来映射到存储位置的数据结构。在 Python 中，字典(dict)和集合(set)都是基于哈希表实现的。

#### ⏱️ 时间复杂度分析

| 操作 | 时间复杂度 | 说明 |
|------|------------|------|
| 插入元素 | 平均 O(1)，最坏 O(n) | 哈希冲突时可能退化为链表 |
| 删除元素 | 平均 O(1)，最坏 O(n) | 哈希冲突时可能退化为链表 |
| 查找元素 | 平均 O(1)，最坏 O(n) | 哈希冲突时可能退化为链表 |
| 获取所有键/值 | O(n) | 需要遍历整个哈希表 |

#### 🛠️ 常用方法调用示例

```python
# Python字典(dict)常用操作示例

# 1. 创建字典
def create_dictionaries():
    """创建字典的不同方式"""
    # 空字典
    empty_dict = {}
    
    # 使用字面量创建
    person = {"name": "Alice", "age": 30, "city": "New York"}
    
    # 使用dict()构造函数
    student = dict(name="Bob", age=20, major="Computer Science")
    
    # 从键值对列表创建
    employee = dict([("id", 1001), ("position", "Developer"), ("salary", 80000)])
    
    # 从字典创建副本
    person_copy = person.copy()
    
    return empty_dict, person, student, employee, person_copy

# 2. 访问和修改字典
def access_and_modify():
    """访问和修改字典元素"""
    book = {"title": "Python Programming", "author": "John Doe", "price": 49.99}
    
    # 访问元素
    print("书名:", book["title"])  # 直接访问，如果键不存在会抛出KeyError
    print("作者:", book.get("author", "Unknown"))  # 使用get()，可以设置默认值
    
    # 修改元素
    book["price"] = 39.99  # 直接修改
    print("修改后的价格:", book["price"])
    
    # 添加元素
    book["publisher"] = "Tech Books"
    print("添加出版社后:", book)
    
    # 更新多个键值对
    book.update({"pages": 300, "year": 2023})
    print("更新多个键值对后:", book)
    
    return book

# 3. 删除字典元素
def delete_elements():
    """删除字典元素"""
    inventory = {"apple": 10, "banana": 15, "orange": 8, "grape": 12}
    print("原始库存:", inventory)
    
    # 删除指定键
    removed_count = inventory.pop("banana", 0)  # 删除并返回值，可以设置默认值
    print("删除香蕉数量:", removed_count)
    print("删除后库存:", inventory)
    
    # 删除并返回最后一个键值对（Python 3.7+）
    last_item = inventory.popitem()
    print("删除的最后一项:", last_item)
    print("删除后库存:", inventory)
    
    # 使用del删除
    del inventory["apple"]
    print("使用del删除苹果后:", inventory)
    
    # 清空字典
    inventory.clear()
    print("清空后:", inventory)
    
    return inventory

# 4. 字典遍历
def iterate_dictionary():
    """遍历字典的不同方式"""
    grades = {"Alice": 90, "Bob": 85, "Charlie": 92, "David": 88}
    
    # 遍历键
    print("遍历键:")
    for name in grades.keys():
        print(f"  {name}")
    
    # 遍历值
    print("\n遍历值:")
    for score in grades.values():
        print(f"  {score}")
    
    # 遍历键值对
    print("\n遍历键值对:")
    for name, score in grades.items():
        print(f"  {name}: {score}")
    
    return grades

# 5. 字典推导式
def dictionary_comprehensions():
    """字典推导式示例"""
    numbers = [1, 2, 3, 4, 5]
    
    # 创建平方字典
    squares = {num: num**2 for num in numbers}
    print("平方字典:", squares)
    
    # 条件筛选
    even_squares = {num: num**2 for num in numbers if num % 2 == 0}
    print("偶数平方字典:", even_squares)
    
    # 字符串操作
    words = ["hello", "world", "python", "programming"]
    word_lengths = {word: len(word) for word in words}
    print("单词长度字典:", word_lengths)
    
    return squares, even_squares, word_lengths

# 6. 字典的高级应用
def advanced_dictionary_operations():
    """字典的高级应用"""
    # 嵌套字典
    employees = {
        1001: {"name": "Alice", "department": "HR", "skills": ["communication", "recruitment"]},
        1002: {"name": "Bob", "department": "IT", "skills": ["programming", "networking"]},
        1003: {"name": "Charlie", "department": "Finance", "skills": ["accounting", "analysis"]}
    }
    
    # 访问嵌套字典
    print("员工1002的技能:", employees[1002]["skills"])
    
    # 添加新员工
    employees[1004] = {"name": "David", "department": "Marketing", "skills": ["advertising", "sales"]}
    
    # 字典排序
    sorted_by_name = {emp_id: emp_data for emp_id, emp_data in sorted(employees.items(), key=lambda x: x[1]["name"])}
    print("按姓名排序的员工字典:")
    for emp_id, emp_data in sorted_by_name.items():
        print(f"  {emp_id}: {emp_data['name']} - {emp_data['department']}")
    
    # 字典合并（Python 3.9+）
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged_dict = dict1 | dict2  # 合并运算符
    print("合并后的字典:", merged_dict)
    
    return employees, merged_dict

# 7. 集合(set)常用操作
def set_operations():
    """集合常用操作"""
    # 创建集合
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    # 添加元素
    set1.add(6)
    print("添加6后的set1:", set1)
    
    # 删除元素
    set1.discard(1)  # 如果元素不存在，不会抛出异常
    print("删除1后的set1:", set1)
    
    # 集合运算
    print("set1:", set1)
    print("set2:", set2)
    print("并集:", set1.union(set2))  # 或 set1 | set2
    print("交集:", set1.intersection(set2))  # 或 set1 & set2
    print("差集:", set1.difference(set2))  # 或 set1 - set2
    print("对称差集:", set1.symmetric_difference(set2))  # 或 set1 ^ set2
    
    # 子集和超集
    subset = {2, 3}
    print(f"{subset}是{set1}的子集:", subset.issubset(set1))
    print(f"{set1}是{subset}的超集:", set1.issuperset(subset))
    
    # 列表去重
    numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1]
    unique_numbers = list(set(numbers))
    print("去重后的列表:", unique_numbers)
    
    return set1, set2, unique_numbers

# 8. 自定义哈希表实现
class HashTable:
    """简单的哈希表实现"""
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # 使用链地址法处理冲突
    
    def _hash_function(self, key):
        """简单的哈希函数"""
        return hash(key) % self.size
    
    def set(self, key, value):
        """设置键值对"""
        index = self._hash_function(key)
        
        # 查找键是否已存在
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # 更新值
                return
        
        # 键不存在，添加新键值对
        self.table[index].append((key, value))
    
    def get(self, key):
        """获取键对应的值"""
        index = self._hash_function(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        return None  # 键不存在
    
    def delete(self, key):
        """删除键值对"""
        index = self._hash_function(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        
        return False  # 键不存在
    
    def keys(self):
        """获取所有键"""
        keys = []
        for bucket in self.table:
            for k, _ in bucket:
                keys.append(k)
        return keys
    
    def values(self):
        """获取所有值"""
        values = []
        for bucket in self.table:
            for _, v in bucket:
                values.append(v)
        return values
    
    def items(self):
        """获取所有键值对"""
        items = []
        for bucket in self.table:
            items.extend(bucket)
        return items
    
    def __str__(self):
        return str(self.items())

# 示例使用
if __name__ == "__main__":
    # 创建字典
    empty_dict, person, student, employee, person_copy = create_dictionaries()
    print("空字典:", empty_dict)
    print("人员字典:", person)
    print("学生字典:", student)
    print("员工字典:", employee)
    print("人员字典副本:", person_copy)
    
    # 访问和修改
    book = access_and_modify()
    
    # 删除元素
    delete_elements()
    
    # 遍历字典
    iterate_dictionary()
    
    # 字典推导式
    dictionary_comprehensions()
    
    # 高级操作
    advanced_dictionary_operations()
    
    # 集合操作
    set_operations()
    
    # 自定义哈希表
    custom_hash = HashTable()
    custom_hash.set("name", "Alice")
    custom_hash.set("age", 30)
    custom_hash.set("city", "New York")
    custom_hash.set("name", "Bob")  # 更新值
    
    print("自定义哈希表:", custom_hash)
    print("获取name:", custom_hash.get("name"))
    print("获取age:", custom_hash.get("age"))
    print("所有键:", custom_hash.keys())
    print("所有值:", custom_hash.values())
    
    custom_hash.delete("city")
    print("删除city后:", custom_hash)
```

---

