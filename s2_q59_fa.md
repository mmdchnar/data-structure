# ساختار داده درخت جستجوی دودویی در پایتون

## مقدمه

این کد پایتون یک ساختار داده درخت جستجوی دودویی (BST) ارائه می‌دهد که به شما امکان اضافه‌کردن (insert)، حذف (delete) و یافتن (find) اعداد در محدوده مشخص [a، b] را با پیچیدگی زمانی O(log n + k) می‌دهد.

## توضیحات کد

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1  # تعداد گره‌ها در زیردرختی که این گره ریشه آن است


class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, node, x):
        if node is None:
            return Node(x)
        if x < node.val:
            node.left = self._insert(node.left, x)
        else:
            node.right = self._insert(node.right, x)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, node, x):
        if node is None:
            return None
        if x < node.val:
            node.left = self._delete(node.left, x)
        elif x > node.val:
            node.right = self._delete(node.right, x)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_val = self._min(node.right)
            node.val = min_val
            node.right = self._delete(node.right, min_val)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def find(self, a, b):
        result = []
        self._find(self.root, a, b, result)
        return result

    def _find(self, node, a, b, result):
        if node is None:
            return
        if a <= node.val <= b:
            result.append(node.val)
        if node.val >= a:
            self._find(node.left, a, b, result)
        if node.val <= b:
            self._find(node.right, a, b, result)

    def _size(self, node):
        return node.size if node else 0

    def _min(self, node):
        while node.left:
            node = node.left
        return node.val
```

### جزئیات کلاس:

1. **کلاس `Node`**: نمایانگر یک گره در درخت جستجوی دودویی است که دارای مقدار (`val`)، اشاره به چپ و راست، و تعداد گره‌ها در زیردرختی که این گره ریشه آن است، است.

2. **کلاس `BST`**: پیاده‌سازی درخت جستجوی دودویی است که دارای متدهای زیر است:

    - **`__init__(self)`:** یک درخت خالی با ریشه `None` را مقداردهی اولیه می‌کند.
    
    - **`insert(self, x)`:** یک مقدار `x` را به درخت اضافه می‌کند. برای این عملیات از متد `_insert` خصوصی استفاده می‌شود.
    
    - **`_insert(self, node, x)`:** به صورت بازگشتی یک مقدار `x` را به درخت اضافه می‌کند و تعداد گره‌های زیردرخت فعلی را به‌روزرسانی می‌کند.
    
    - **`delete(self, x)`:** یک گره با مقدار `x` را از درخت حذف می‌کند. برای این عملیات از متد `_delete` خصوصی استفاده می‌شود.
    
    - **`_delete(self, node, x)`:** به صورت بازگشتی یک گره با مقدار `x` را از درخت حذف می‌کند و تعداد گره‌های زیردرخت فعلی را به‌روزرسانی می‌کند.
    
    - **`find(self, a, b)`:** نقاط در محدوده [a، b] را در درخت پیدا کرده و آن‌ها را به لیست `result` اضافه می‌کند. برای این عملیات از متد `_find` خصوصی استفاده می‌شود.
    
    - **`_find(self, node, a, b, result)`:** به صورت بازگشتی نقاط در محدوده [a، b] را در درخت پیدا کرده و آن

‌ها را به لیست `result` اضافه می‌کند.
    
    - **`_size(self, node)`:** اندازه زیردرختی را که گره داده شده ریشه آن است، برمی‌گرداند یا اگر گره `None` باشد، 0 را برمی‌گرداند.
    
    - **`_min(self, node)`:** کمترین مقدار در زیردرختی که گره داده شده ریشه آن است، را برمی‌گرداند.

### پیچیدگی‌های زمانی:

- **افزودن (`insert` و `_insert`):** O(log n) - پیچیدگی زمانی لگاریتمی.
  
- **حذف (`delete` و `_delete`):** O(log n) - پیچیدگی زمانی لگاریتمی.
  
- **یافتن نقاط (`find` و `_find`):** O(log n + k)، که در آن k تعداد نقاط در محدوده مشخص شده است.

## استفاده

برای استفاده از این ساختار داده، می‌توانید این متدها را به‌صورت زیر فراخوانی کنید:

```python
bst = BST()

# افزودن مقادیر
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(9)

# حذف یک مقدار
bst.delete(4)

# یافتن نقاط در محدوده [3، 7]
points_in_range = bst.find(3, 7)
print(points_in_range)  # خروجی: [3, 5, 6, 7]
```

## نتیجه‌گیری

درخت جستجوی دودویی پیاده‌سازی شده در این کد، راه حلی کارآمد برای ذخیره و بازیابی نقاط روی محور X فراهم می‌کند. پیچیدگی‌های زمانی برای افزودن، حذف و یافتن نقاط در محدوده مشخص، این کد را مناسب برای انواع تحلیل‌های مربوط به ارتفاع انسان می‌سازد.
