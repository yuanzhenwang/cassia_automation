# -*- coding: utf-8 -*-
'''
测试点：测试0芯片主动扫描同时，让1芯片被动扫

'''


import unittest, json, sys, os, json
from contextlib import closing
from threading import Timer
import threading
path = os.getcwd().split('cassia_automation')[0] + 'cassia_automation/lib/'
sys.path.append(path)
from tools import get_api, get_model
from logs import set_logger

class testcase(unittest.TestCase):
    logger = set_logger(__name__)
    sdk = get_api()
    model = get_model()

    def setUp(self):
        self.timeout = None
        self.flag1 = None
        self.flag2 = None
        self.logger.info('测试0芯片主动扫描同时，让1芯片被动扫')
        self.timer = Timer(30, self.set_timeout)
        self.timer.start()

    def tearDown(self):
        self.timer.cancel()

    # noinspection PyUnreachableCode
    def test_chips_start_scan_meanwhile(self):
        if self.model.startswith('S') or self.model.startswith('s'):
            self.assertTrue(True)
        else:
            threading.Thread(target=self.chip0_scan).start()
            threading.Thread(target=self.chip1_scan).start()
            while True:
                if self.flag1 and self.flag2:
                    self.assertTrue(True)
                    self.logger.info('pass\n')
                    break
                elif self.timeout:
                    self.fail('Case failed,start scan timeout.')
                    self.logger.info('fail\n')
                    self.logger.error("Case failed,start scan timeout.")
                    breaks

    def chip0_scan(self):
        #step1:chip 1 start active scan,then start chip0 scan.
        with closing(self.sdk.scan(chip=0,active = 1)) as self.sse1:
            count = 0
            for message in self.sse1:
                if count < 300:
                    if message.startswith('data'):
                        # print('chip0',message)
                        count += 1
                        if 'scanData' in message:
                            self.flag1 = True
                            break
                    elif 'keep-alive' in message:
                        pass

                    else:
                        self.logger.error('step 1:start active scan fail,%s' % message)
                else:
                    self.logger.debug("step 1:chip 1 start active scan.")
                    break

    def chip1_scan(self):
        #step2:start chip0 scan.
        with closing(self.sdk.scan(chip=1,active = 0)) as self.sse2:
            count = 0
            for message in self.sse2:
                if count < 300:
                    if message.startswith('data'):
                        # print('chip1',message)
                        count += 1
                    elif 'keep-alive' in message:
                        pass
                    else:
                        self.logger.error('step 2:start scan fail,%s' % message)
                else:
                    self.flag2 = True
                    self.logger.debug("step 2:start chip0 start scan passive success.")   
                    break

    def set_timeout(self):
    	self.timeout = True

if __name__ == '__main__':
	# unittest.main()
    suite=unittest.TestSuite()
    suite.addTest('test_chips_start_scan_meanwhile')
    runner = unittest.TextTestRunner()
    runner.run(suite)
