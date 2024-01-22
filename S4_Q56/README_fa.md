# مقایسه قد در پایتون

## مقدمه

کد پایتون یک تابع ارائه می‌دهد که بررسی می‌کند آیا بلندترین فرد در یک لیست داده شده برابر یا بلندتر از دو برابر قد کوتاه‌ترین فرد است. این قابلیت با پیچیدگی زمانی O(n) انجام شده و برای برنامه‌های مختلف مرتبط با داده‌های ارتفاع انسان مناسب است.

## توضیحات کد

```python
def is_tallest_double_of_shortest(heights: list):
    if not heights or len(heights) < 2:
        return False

    shortest_height = float('inf')
    tallest_height = float('-inf')

    for height in heights:
        if height < shortest_height:
            shortest_height = height
        if height > tallest_height:
            tallest_height = height

    return tallest_height >= 2 * shortest_height
```

### گام‌های الگوریتم:

1. `shortest_height` و `tallest_height` را به ترتیب به مثبت و منفی بی‌نهایت مقداردهی اولیه کنید.
2. از لیست داده شده به عنوان `heights` عبور کنید.
3. اگر ارتفاع فعلی کوچکتر باشد، `shortest_height` را به‌روز کنید.
4. اگر ارتفاع فعلی بزرگتر باشد، `tallest_height` را به‌روز کنید.
5. بررسی کنید آیا بلندترین ارتفاع برابر یا بلندتر از دو برابر کوتاه‌ترین ارتفاع است.
6. اگر شرط برآورده شود، `True` را برگردانید؛ در غیر این صورت، `False` را برگردانید.

### پیچیدگی‌های زمانی:

الگوریتم به پیچیدگی زمانی O(n) می‌رسد، که در آن n طول لیست ورودی است.

## مثال‌ها

### مثال 1: False
```python
heights_list_false = [160, 175, 150, 180, 155]
result_false = is_tallest_double_of_shortest(heights_list_false)
print(result_false)  # خروجی: False
```

### مثال 2: True
```python
heights_list_true = [60, 175, 150, 180, 155, 190]
result_true = is_tallest_double_of_shortest(heights_list_true)
print(result_true)  # خروجی: True
```

## نتیجه‌گیری

این تابع مقایسه ارتفاع یک راه‌حل کارآمد برای تعیین اینکه آیا بلندترین فرد در یک لیست داده شده برابر یا بلندتر از دو برابر قد کوتاه‌ترین فرد است یا خیر فراهم می‌کند. این تابع با پیچیدگی زمانی O(n) عمل می‌کند که آن را برای موارد مختلف مرتبط با تجزیه و تحلیل ارتفاع مناسب می‌سازد.
