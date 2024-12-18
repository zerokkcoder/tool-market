import re
import imaplib
import email
from email.header import decode_header

# 连接到 Gmail 服务器
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('your_email@gmail.com', 'your_password')
mail.select('inbox')

# 获取所有邮件
status, messages = mail.search(None, 'ALL')
email_ids  = messages[0].split()

# 循环查看所有电子邮件，过滤掉不需要的邮件
for email_id in email_ids:
    status, msg_data = mail.fetch(email_id, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            # 检查主题是否包含促销关键词
            if re.search(r"(sale|promotion|offer|newsletter)", subject, re.IGNORECASE):
                mail.store(email_id, '+FLAGS', '\\Deleted')  # 标记为已删除 deleted
                print(f"Deleted: {subject}")
# 删除已删除的邮件
mail.expunge()
mail.logout()
