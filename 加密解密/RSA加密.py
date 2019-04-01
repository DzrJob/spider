#-*-coding:utf-8-*- 
# @File    : RSA����.py
import rsa

(publickey, privatekey) = rsa,newkeys(1000)  # ������1000���ܵõ���Կ��˽Կ
pub = publickey.save_pkcs1()  # ��ȡ��Կ
# ����Կ���浽�ļ�*************
filepub = open("public.pem", 'w+')
filepub.write(pub.encode('utf-8'))
filepub.close()

pri = privatekey.save_pkcs1()  # ��ȡ˽Կ
# ��˽Կ���浽�ļ�***********
filepri = open('private.pem', 'w+')
filepri.write(pri.encode('utf-8'))
filepri.close()

string = "laomomoblog"  # �����ܵ��ַ���

# ȡ����Կ
with open('publick.pem', 'r') as file_pub:
    f_pub = file_pub.read()
    pubkey = rsa.PublicKey.load_pkcs1(f_pub)

# ȡ��˽Կ
with open('private.pem', 'r') as file_pri:
    f_pri = file_pri.read()
    prikey = rsa.PrivateKey.load_pkcs1(f_pri)

# �����ַ���string

crypt = rsa.encryt(string.encode('utf-8'), pubkey)  # ʹ�ù�Կȥ�����ַ���

# ����
de_crypt = rsa.decrypt(crypt, prikey)  # ��˽Կȥ����

# �������de_crypt��stringӦ������ȵģ��ж�һ��
assert string,de_crypt