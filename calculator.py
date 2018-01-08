#!/usr/bin/env python3
import sys
class config(object):
    def __init__(self,sys.argv):
        self._config = {}
	args = sys.argv[1:]
	index = args.index('-c')
	self.configfile = args[index+1]
    def get_config:
        with open(self.configfile) as configf:
	    configf.read()    
	    self._config = configf.strip().split('=')
    def JishuL:
        self.JishuL = self._config['JishuL']
    def JishuH:
        self.JishuH = self._config['JishuH']
    def YangLao:
        self.YangLao = self._config['YangLao']
    def ShiYe:
        self.Shiye = self._config['ShiYe']
    def GongShang:
        self.GongShang = self._config['GongShang']
    def ShengYu:
        self.ShengYu = self._config['ShengYu']
    def GongJiJin:
        self.GongYu = self._config['GongJiJin']
    
class salary(object):
    def __init__(self,sys.argv):
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

    	    
