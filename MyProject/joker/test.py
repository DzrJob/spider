#-*-coding:utf-8-*- 
# @File    : test.py
import re

str = """
 -> 
 -> 幽默才子把你笑蒙圈
"""
# r = re.compile('-> (\w+)')
# res = r.findall(str)[0]
# print(res)

lis = ['1、早上送女儿上学，我逗她，让她夸我最帅。女儿白了我一眼，不说话，我威胁她：“你不夸我帅中午我不准你回家吃饭！”', '中午放学了，女儿打电话给媳妇：“妈妈，我不回去吃饭了！我爸今天早上让一个美女夸她帅，我白了他一眼，他就生气了，不准我回家吃饭了！”', '2、老婆：儿子，早睡早起身体才能好，不然就得吃药。', '儿子：好，药呢？！', '老婆。。。', '3、看电视时老婆又开始教训儿子：看看人家四岁学琴，十岁考级，十二岁拿奖。', '再看看你，吉他学几个月了，连哆来咪发都没弄清楚！', '儿子不服气：我出生就会拉屎，半岁自己拿勺子吃饭，六岁就上一年级，我骄傲了吗？', '4、去一个小区找朋友，有点迷路，就上前问一小朋友：“小美女，知道某某号楼是那一栋吗？”', '小女孩开心的对身边的小男孩道：“瞧，有人喊我美女，你还说我丑？”', '小男孩看了我一眼：“她当然叫你美女，因为她比你更丑。”', '我。。。', '5、地上有张100元，儿子想捡，我教育道：“不是你的东西不能要。”', '儿子说：“我捡了不就我的了吗？”', '我竟无言以对。。。']

if lis:
    lis = "\n".join(lis)
print(lis)