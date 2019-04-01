#-*-coding:utf-8-*- 
# @File    : RSA加密.py
import rsa

(publickey, privatekey) = rsa,newkeys(1000)  # 对数字1000加密得到公钥和私钥
pub = publickey.save_pkcs1()  # 获取公钥
# 将公钥保存到文件*************
filepub = open("public.pem", 'w+')
filepub.write(pub.encode('utf-8'))
filepub.close()

pri = privatekey.save_pkcs1()  # 获取私钥
# 将私钥保存到文件***********
filepri = open('private.pem', 'w+')
filepri.write(pri.encode('utf-8'))
filepri.close()

string = "laomomoblog"  # 待加密的字符串

# 取出公钥
with open('publick.pem', 'r') as file_pub:
    f_pub = file_pub.read()
    pubkey = rsa.PublicKey.load_pkcs1(f_pub)

# 取出私钥
with open('private.pem', 'r') as file_pri:
    f_pri = file_pri.read()
    prikey = rsa.PrivateKey.load_pkcs1(f_pri)

# 加密字符串string

crypt = rsa.encryt(string.encode('utf-8'), pubkey)  # 使用公钥去加密字符串

# 解密
de_crypt = rsa.decrypt(crypt, prikey)  # 用私钥去解密

# 解出来的de_crypt与string应该是相等的，判断一下
assert string,de_crypt