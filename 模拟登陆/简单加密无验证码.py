#-*-coding:utf-8-*- 
# @File    : �򵥼�������֤��.py
import requests
import json
login_url='https://passport.cnblogs.com/user/signin'
return_url='https://home.cnblogs.com/u/-E6-/'#�ҵ���ҳ
session=requests.session()

#��ȡVerificationToken
login_page=session.get(login_url)
p=login_page.text.find('VerificationToken')+len('VerificationToken')+4
token=login_page.text[p:login_page.text.find("'",p)]

headers={'Content-Type': 'application/json; charset=UTF-8',
          'X-Requested-With': 'XMLHttpRequest',
          'VerificationToken':token}
session.headers.update(headers)
#����ͨ��ץ����ȡ���ܺ���û��������룬�ҽ��ڸ�¼���ֽ��������Python�м���
data={"input1":"������ʡ�ԡ�����",
      "input2":"������ʡ�ԡ�����",
      "remember":True}

#ģ���¼
response=session.post(login_url,data=json.dumps(data))
print(response.text)
#{"success":true}
#��¼�ɹ�

#��ת����ҳ
home_page=session.get(return_url)
#��ȡ��ҳ����
p=home_page.text.find('<title>')+len('<title>')
title=home_page.text[p:home_page.text.find('</title>',p)]
print(title)
#E6����ҳ - ����԰
#�����¼ʧ�ܣ���ת����ҳʱ���صĽ��û��title��ǩ��home_page.text��Ϊ'��Ҫ��½'