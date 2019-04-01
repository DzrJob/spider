#-*-coding:utf-8-*- 
# @File    : Crypto.py

# ��python�м�����ҪCrypto��base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
from base64 import b64encode
"""
����ҳԴ�����п���ֱ���ҵ���Կ��λ��setPublicKey()�������MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCp0wHYbg/NOPO3nzMD3dndwS0MccuMeXCHgVlGOoYyFwLdS24Im2e7YyhB0wrUsyYf0/nhzCzBK8ZC9eCWqd0aHbdgOQT6CuFQBMjbyGYvlVYU2ZP7kG9Ft6YV6oc9ambuO7nPZh+bvXH0zDKfi02prknrScAKC0XhadTHT3Al0QIDAQAB
��׼�Ĺ�Կ��ʽΪ
���ƴ���
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDNPaXE9SARgvD7l5FgU5B/ibE/
Uuu4okbt6LGzXVYtx1tzgdnV9/BiDgauRsWGjofo0o3+cVLs16hUdRJ9BoAr0jL8
00AKy9rkcOi0lJI8XBZrtX2Ad+uwf4kLNjL2MkLkSbhtwRzpiAFcjMrhyOi6y/0c
KafXI3SXOgVBA5w2dQIDAQAB
-----END PUBLIC KEY-----
���ƴ���
ÿ��64���ַ���
"""
#��׼�Ĺ�Կ��ʽ��bytes���ͣ�ÿ64�ַ���һ����
key_bytes=b"-----BEGIN PUBLIC KEY-----\n\
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCp0wHYbg/NOPO3nzMD3dndwS0M\n\
cc\uMeXCHgVlGOoYyFwLdS24Im2e7YyhB0wrUsyYf0/nhzCzBK8ZC9eCWqd0aHbd\n\
gOQT6CuFQBMjbyGYv\lVYU2ZP7kG9Ft6YV6oc9ambuO7nPZh+bvXH0zDKfi02prk\n\
nrScAKC0XhadTHT3Al0QIDAQAB\n\
-----END PUBLIC KEY-----"
#����Crypto.PublicKey.RSA._RSAobj���͵Ķ���
publickey=RSA.importKey(key_bytes)
#���조��������
encryptor=PKCS1_v1_5.new(publickey)
#���ܵ����ݱ���Ϊbytes����
username=b'123'
password=b'abc'
#���ܣ��������ת�����ַ���
input1=str(b64encode(encryptor.encrypt(username)),'utf-8')
input2=str(b64encode(encryptor.encrypt(password)),'utf-8')

data={'input1':input1,'input2':input2,'remember':True}