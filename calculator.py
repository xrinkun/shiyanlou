#!/usr/bin/env python3
import sys
class config(object):
    def __init__(self):
        self._config = {}
        args = sys.argv[1:]
        index = args.index('-c')
        self.configfile = args[index+1]
    def get_config():
        with open(self.configfile) as configf:
            configf.read()
            self._config = configf.strip().split('=')
    def Shu(self):
        self.config = self._config
class salary(object):
    def __init__(self):
        self._sa = {}
        args = sys.argv[1:]
        index = args.index['-d']
        self.salaflie = argv[index+1]
    def getsala(self):
        with open(self.salafile) as sfile:
            sfile.read()
            self._sa = sfile.split(',')
    def sala(self):
        self.sala = self._sa
def insert(s):
    args = sys.argv[1:]
    index = args['-o']
    sflie = args[index+1]
    li = salary.getsala()
    flie = open('~/Gongzi.csv','w')
    flie.write(li.append(s))
    flie.close()
class cal(object):
    def bao(self):
        config = config.Shu
        sala = salary.sala
        for x in sala:
            if sala[x] < config['JiShuL']:
                xian = config['JiShuL'] * (config['YangLao']+config['YiLiao']+config['Shiye']+config['GongShang']+config['ShengYu']+config['GongJiJin'])
            elif sala[x] > config['JiShuH']:
                xian = config['JiShuH'] * (config['YangLao']+config['YiLiao']+config['Shiye']+config['GongShang']+config['ShengYu']+config['GongJiJin'])  
            else:
                xian = sala[x] * (config['YangLao']+config['YiLiao']+config['Shiye']+config['GongShang']+config['ShengYu']+config['GongJiJin'])  
            insert(xian)
    def result(self,n,xian):
        if n <= 3500:
            r = format(n-n*xian, ".2f")    
        elif n <= 5000:
            r = format(n-(n-xian-3500) * 0.03 + n*xian, ".2f")
        elif n <= 8000:
            r = format(n-(n-xian-3500) * 0.1 + 105 + n*xian, ".2f")
        elif n <= 12500:
            r = format(n-(n-xian-3500) * 0.2 + 555 + n*xian, ".2f")
        elif n <= 38500:
            r = format(n-(n-xian-3500) * 0.25 + 1005 + n*xian, ".2f")
        elif n <= 58500:
            r = format(n-(n-xian-3500) * 0.3 + 2775 + n*xian, ".2f")
        elif n <= 83500:
            r = format(n-(n-xian-3500) * 0.35 + 5505 + n*xian, ".2f")
        else:
            r = format(n-(n-xian-3500) * 0.45 + 13505 + n*xian, ".2f")
        insert(r)
    def ge(self,qian,bao,result):
        g = qian - bao - result
        insert(g)
cal.bao
cal.result
cal.ge
