import re
import imaplib
import email
from email.header import decode_header

# 电子邮件自动清理器
class MailClear:
    def __init__(self, email, password, host='imap.gmail.com'):
        self.host = host
        self.email = email
        self.password = password
        self.mail = imaplib.IMAP4_SSL(self.host)
        self.mail.login(self.email, self.password)
        self.mail.select('inbox')

    # 清理邮件
    def clear(self):
        # 获取所有邮件
        status, messages = self.mail.search(None, 'ALL')
        email_ids  = messages[0].split()

        # 循环查看所有电子邮件，过滤掉不需要的邮件
        for email_id in email_ids:
            status, msg_data = self.mail.fetch(email_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    # 检查主题是否包含促销关键词
                    if isinstance(subject, bytes):  # 添加此行以处理字节类型的主题
                        subject = subject.decode(encoding if encoding else 'utf-8')  # 解码主题
                    if re.search(r"(sale|promotion|offer|newsletter|dev|welcome)", subject, re.IGNORECASE):
                        self.mail.store(email_id, '+FLAGS', '\\Deleted')  # 标记为已删除 deleted
                        print(f"Deleted: {subject}")

        # 删除已删除的邮件
        self.mail.expunge()
        self.logout()

    # 登出
    def logout(self):
        self.mail.logout()