from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


def APIcheck():
     APIList = ['你的名字','brysjhhrhl']
     check = 0
     API = input('请输入你的授权码值：')
     if(API == "mjTree"):
          a = input('输入授权码:')
          APIList.append(a)
          API = input('请输入你的授权码值：')
	  #ycdmcizhiqmsbchd
          if API in APIList:
               check = 1
               return check
          else:
               return check
     else:
          if API in APIList:
               check = 1
               return check
          else:
               return check


def inputInfo():
     #sender_qq为发件人的qq号码
     MyQQNum = input('输入你的QQ号：')
     sender_qq = MyQQNum

     #pwd为qq邮箱的授权码
     code = input('输入你qq邮箱授权码：')
     pwd = code

     #收件人邮箱receiver
     OtherQQNum = input('输入收件人的邮箱：')
     receiver = OtherQQNum

     #邮件的正文内容
     content  = input('输入邮件内容：')
     mail_content = content 

     #邮件标题
     str4 = input('输入邮件标题：')
     mail_title = str4
     return (sender_qq,pwd,receiver,mail_content,mail_title)


def send_mail(sender_qq='',pwd='',receiver='',mail_title='',mail_content=''):
     # qq邮箱smtp服务器
     host_server = 'smtp.qq.com'
     sender_qq_mail = sender_qq+'@qq.com'

     #ssl登录
     smtp = SMTP_SSL(host_server)
     
     #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
     smtp.set_debuglevel(1)
     smtp.ehlo(host_server)
     smtp.login(sender_qq, pwd)

     msg = MIMEText(mail_content, "plain", 'utf-8')
     msg["Subject"] = Header(mail_title, 'utf-8')
     msg["From"] = sender_qq_mail
     msg["To"] = receiver
     smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
     smtp.quit()


def main():
     check = APIcheck()
     if(check != 1):
          print('请拥有授权码再来使用吧^_^')
          exit(0)
     else:
          print('授权码正确，请继续使用！！\n\n')
     while(1):
          sender_qq1,pwd1,receiver1,mail_content1,mail_title1 = inputInfo()
          
          num = input('请输入你要一次性发送几条邮箱<1—1亿>:')
          j=1
          for i in range(int(num)):
               send_mail(sender_qq=sender_qq1,pwd=pwd1,receiver=receiver1,mail_title=mail_title1,mail_content=mail_content1)
          ch = input('是否继续发送<Y/N>:')
          if(ch=='Y'or ch=='y'):
               continue
          elif(ch=='N'or ch=='n'):
               print('发送邮件结束')
               return
          else:
               return

main()

