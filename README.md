<div align="center">

# 🌍 All OS Commands

### Cross-platform terminal helpers for Python  
### دستیار چندسکویی برای کار با ترمینال در پایتون

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.7%2B-blue.svg" />
  <img alt="Platform" src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-success" />
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-orange" />
</p>

</div>

---

## ✨ Overview | معرفی

| English | فارسی |
|---|---|
| `all_os_commands` is a tiny utility package that gives you simple, practical terminal helpers that work across different operating systems. | `all_os_commands` یک پکیج کوچک و کاربردی است که چند ابزار ساده‌ی ترمینال را به‌صورت چندسکویی در اختیار شما قرار می‌دهد. |
| Current helpers: clear terminal screen and detect Enter key press in terminal apps. | ابزارهای فعلی: پاک کردن صفحه‌ی ترمینال و تشخیص فشردن کلید Enter در برنامه‌های ترمینالی. |

---

## 📦 Installation | نصب

### Using pip from GitHub

```bash
pip install git+https://github.com/Rmin-code2005/AllOsCommands.git
```

---

## 🚀 Quick Start | شروع سریع

```python
from all_os_commands import clearOnAllUI, is_enter_pressed

clearOnAllUI()

if is_enter_pressed():
    print("Enter pressed!")
```

---

## 🧩 Available Functions | توابع موجود

### `clearOnAllUI()`
- **EN:** Clears terminal output on Windows (`cls`) and Unix-like systems (`clear`).
- **FA:** خروجی ترمینال را در ویندوز با `cls` و در لینوکس/مک با `clear` پاک می‌کند.

### `is_enter_pressed() -> bool`
- **EN:** Non-blocking check for Enter key press in terminal input.
- **FA:** بررسی غیرمسدودکننده برای تشخیص فشرده شدن کلید Enter در ترمینال.

---

## 💡 Example Loop | مثال حلقه

```python
import time
from all_os_commands import is_enter_pressed

print("Press Enter to stop...")

while True:
    if is_enter_pressed():
        print("Stopped by Enter")
        break
    # Do your work here
    time.sleep(0.05)
```

---

## 🤝 Contributing | مشارکت

- **EN:** Issues and pull requests are welcome.
- **FA:** ارسال Issue و Pull Request خوشحالمان می‌کند.

## 📄 License | لایسنس

- **EN:** Add your preferred license file (MIT recommended).
- **FA:** فایل لایسنس دلخواه خود را اضافه کنید (پیشنهاد: MIT).
