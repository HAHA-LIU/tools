# -*- coding:utf-8 -*-
# author: LIUWENYU
# datetime: 2020/10/14 11:10
# describe:
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '1091761664@qq.com'  # 发件人邮箱账号
my_pass = 'vpacwzbdosuzbabd'     # 发件人邮箱密码(即授权码)
my_user = '840575620@qq.com'    # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        mail_msg = """
        <p>你好  李狗 </p>
        """
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From'] = formataddr(('我系你老豆', my_sender))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(('收件人昵称', my_user))  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # msg['From'] = formataddr(('', my_sender))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # msg['To'] = formataddr(('', my_user))  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e :  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        ret = False
    return ret

for i in range(15):
    ret = mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")