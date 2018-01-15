#!/usr/bin/env python3
import sys
class config(object):
    def __init__(self):
        self.config = {}
        args = sys.argv[1:]
        index = args.index('-c')
        self.configfile = args[index+1]
    def _get_config(self):
        with open(self.configfile) as configf:
            for line in configf.readlines():
                key,value = configf.strip().split('=')
            try:
                    config[key.strip()] = float(value.strip())
            except ValueError:
                    print("Parameter Error")
                    exit()                    
            return config
    @property
    def config_give(self):
        return self._get_config
class salary(object):
    def __init__(self):
        self.salary_dict = {}
        args = sys.argv[1:]
        index = args.index['-d']
        self.salafile = argv[index+1]
    def getsala(self):
        with open(self.salafile) as sfile:
            for line in sfile.readlines():
                key,value = sfile.split(',')
            try:
                self.salary_dict[key.strip()] = float(value.strip())
            except ValueError:
                print("ParameterError")
                exit()
            return salary_dict
    @property
    def salary_give(self):
        return salary.getsala
def insert(s):
    args = sys.argv[1:]
    index = args['-o']
    sfile = args[index+1]
    file = open('sflie','w')
    for line in file.readlines('sflie'):
        file.write(list(flie.readlines('sflie')).append(s))
    file.close()
class cal(object):
    def bao(self):
        config = config.config_give
        sala = salary.salary_give
        for x in sala:
            if sala[x] < config['JiShuL']:
                xian = config['JiShuL'] * (config['YangLao']+config['YiLiao']+config['Shiye']+config['GongShang']+config['ShengYu']+config['GongJiJin'])
            elif sala[x] > config['JiShuH']:
                xian = config['JiShuH'] * (config['YangLao']+config['YiLiao']+config['Shiye']+config['GongShang']+config['ShengYu']+config['GongJiJin'])  
            else:
                xian = sala[x] * (config['YangLao']+config['YiLiao']+config['Shiye']+config['GongShang']+config['ShengYu']+config['GongJiJin'])  
            return insert(xian)
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
        return insert(r)
    def ge(self,qian,bao,result):
        g = qian - bao - result
        return insert(g)
if __name__ == "__main__":
    try:
        args = sys.argv[1:]
        index = args['-o']
        sfile = args[index+1]
        with open(salary.salary_give) as copy:
            for line in copy.readlines():
                file('sfile','w')
    except:
        print('Error')
    cal.bao
    cal.ge
    cal.result
