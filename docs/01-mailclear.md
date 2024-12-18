# 垃圾邮件清理

## 简介

垃圾邮件清理器，用于清理垃圾邮件。

## 使用

### 邮件授权码获取教程
    - 谷歌邮箱：https://support.google.com/accounts/answer/185833
    - 腾讯邮箱：https://service.mail.qq.com/detail/0/75

### 代码使用
```python
from app.mailclear.mailclear import MailClear

mailclear = MailClear('your_email@gmail.com', 'your_password')
mailclear.clear()
```
