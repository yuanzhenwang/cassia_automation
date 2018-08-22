import jsonimport osimport sysimport timeimport unittestfrom contextlib import closingimport threadingpath = os.getcwd().split('cassia_automation')[0] + 'cassia_automation/lib/'sys.path.append(path)import ddtfrom ExcelUtil import ExcelUtilfrom tools import read_job_config, get_api@ddt.ddtclass test_api(unittest.TestCase):    conf = read_job_config()    sdk = get_api()    path = os.getcwd().split('cassia_automation')[0] + 'cassia_automation/'    testdata = ExcelUtil(path + 'test_data/' + conf['data_file'])    dd = testdata.get_all()    def setUp(self):        self.case_run_flag = None        self.timeout_timer = threading.Timer(self.conf['case_timeout'], self.time_out)        self.timeout_timer.start()    @ddt.data(*dd['scandata'])    def test_scan(self, values):        if self.sdk.model.upper().startswith('S'):            expect_result = values['expect_result_s1000']        else:            expect_result = values['expect_result_other']        filter_duplicates = values['filter_duplicates']        filter_name = values['filter_name']        filter_mac = values['filter_mac']        filter_rssi = values['filter_rssi']        filter_uuid = values['filter_uuid']        para = {}        tmp = ['__name__', 'expect_result_s1000', 'expect_result_other']        for key in values:            if values[key] != '' and key not in tmp:                para[key] = values[key]        with closing(self.sdk.scan(**para)) as r:            '''            该部分主要测试过滤相关参数，也就是说            进入到这个部分的测试用例全部是开启扫描成功的            '''            if r.status_code == 200:                if filter_duplicates and filter_name:                    # 过滤条件为filter_duplicates和filter_name，下面分支语句情况类似                    t = threading.Thread(target=self.__filter_duplicates_name, args=(r,))                    t.setDaemon(True)                    t.start()                    while True:                        if self.case_run_flag == 'success':                            return                        elif self.case_run_flag == 'fail':                            self.fail('filter failed!')                            return                        elif self.case_run_flag == 'timeout':                            self.fail('case run tome out.')                            return                        else:                            time.sleep(0.5)                elif filter_duplicates and filter_rssi:                    t = threading.Thread(target=self.__filter_duplicates_rssi, args=(r, filter_rssi,))                    t.setDaemon(True)                    t.start()                    while True:                        if self.case_run_flag == 'success':                            return                        elif self.case_run_flag == 'fail':                            self.fail('filter failed!')                            return                        elif self.case_run_flag == 'timeout':                            self.fail('case run tome out.')                            return                        else:                            time.sleep(0.5)                elif filter_duplicates:                    t = threading.Thread(target=self.__filter_duplicates, args=(r,))                    t.setDaemon(True)                    t.start()                    while True:                        if self.case_run_flag == 'success':                            return                        elif self.case_run_flag == 'fail':                            self.fail('filter failed!')                            return                        elif self.case_run_flag == 'timeout':                            self.fail('case run tome out.')                            return                        else:                            time.sleep(0.5)                elif filter_name and filter_rssi:                    t = threading.Thread(target=self.__filter_name_rssi, args=(r, filter_name, filter_rssi))                    t.setDaemon(True)                    t.start()                    while True:                        if self.case_run_flag == 'success':                            return                        elif self.case_run_flag == 'fail':                            self.fail('filter failed!')                            return                        elif self.case_run_flag == 'timeout':                            self.fail('case run tome out.')                            return                        else:                            time.sleep(0.5)                elif filter_name and filter_uuid:                    t = threading.Thread(target=self.__filter_name_uuid, args=(r, filter_name, filter_uuid))                    t.setDaemon(True)                    t.start()                    while True:                        if self.case_run_flag == 'success':                            return                        elif self.case_run_flag == 'fail':                            self.fail('filter failed!')                            return                        elif self.case_run_flag == 'timeout':                            self.fail('case run tome out.')                            return                        else:                            time.sleep(0.5)                elif filter_uuid and filter_rssi:                    t = threading.Thread(target=self.__filter_uuid_rssi, args=(r, filter_uuid, filter_rssi))                    t.setDaemon(True)                    t.start()                    while True:                        if self.case_run_flag == 'success':                            return                        elif self.case_run_flag == 'fail':                            self.fail('filter failed!')                            return                        elif self.case_run_flag == 'timeout':                            self.fail('case run tome out.')                            return                        else:                            time.sleep(0.5)                elif filter_uuid:                    t = threading.Thread(target=self.__filter_uuid, args=(r, filter_uuid,))                    t.setDaemon(True)                    t.start()                    while True:                        if self.case_run_flag == 'success':                            return                        elif self.case_run_flag == 'fail':                            self.fail('filter failed!')                            return                        elif self.case_run_flag == 'timeout':                            self.fail('case run tome out.')                            return                        else:                            time.sleep(0.5)                elif filter_mac:                    t = threading.Thread(target=self.__filter_mac, args=(r, filter_mac,))                    t.setDaemon(True)                    t.start()                    while True:                        if self.case_run_flag == 'success':                            return                        elif self.case_run_flag == 'fail':                            self.fail('filter failed!')                            return                        elif self.case_run_flag == 'timeout':                            self.fail('case run tome out.')                            return                        else:                            time.sleep(0.5)                elif filter_rssi:                    t = threading.Thread(target=self.__filter_rssi, args=(r, filter_rssi,))                    t.setDaemon(True)                    t.start()                    while True:                        if self.case_run_flag == 'success':                            return                        elif self.case_run_flag == 'fail':                            self.fail('filter failed!')                            return                        elif self.case_run_flag == 'timeout':                            self.fail('case run tome out.')                            return                        else:                            time.sleep(0.5)                elif filter_name:                    t = threading.Thread(target=self.__filter_name, args=(r, filter_name,))                    t.setDaemon(True)                    t.start()                    while True:                        if self.case_run_flag == 'success':                            return                        elif self.case_run_flag == 'fail':                            self.fail('filter failed!')                            return                        elif self.case_run_flag == 'timeout':                            self.fail('case run tome out.')                            return                        else:                            time.sleep(0.5)                elif duration:					t=threading.Thread(target=self.__filter_duration,args=(r,duration))                else:                    for test_result in r.iter_lines():                        test_result = str(test_result, encoding='utf8')                        if test_result.startswith('data'):                            print('start scan success.')                            return            else:                self.assertEqual(r.text, expect_result)    def __filter_duplicates_name(self, res):        tmp = []        for test_result in res.iter_lines():            test_result = str(test_result, encoding='utf8')            if test_result.startswith('data'):                test_result = json.loads(test_result[5:])                filters = test_result['bdaddrs'][0]['bdaddr'] + test_result['adData'] + test_result['name']                if len(tmp) < self.conf['filter_count']:                    if filters in tmp:                        self.case_run_flag = 'fail'                        print('\n', test_result, '\n', tmp)                        return                    else:                        print(test_result)                        tmp.append(filters)                else:                    self.case_run_flag = 'success'                    return    def __filter_duplicates_rssi(self, res, filter_rssi):        tmp = []        for test_result in res.iter_lines():            test_result = str(test_result, encoding='utf8')            if test_result.startswith('data'):                test_result = json.loads(test_result[5:])                filters = test_result['bdaddrs'][0]['bdaddr'] + test_result['adData']                if len(tmp) < self.conf['filter_count']:                    if filters in tmp or int(test_result['rssi']) < int(filter_rssi):                        print(int(test_result['rssi']), '\n', tmp)                        self.case_run_flag = 'fail'                        return                    else:                        tmp.append(filters)                        print(test_result)                else:                    self.case_run_flag = 'success'                    return    def __filter_duplicates(self, res):        tmp = []        print('__filter_duplicates')        print(type(res))        print(res)        for test_result in res.iter_lines():            test_result = str(test_result, encoding='utf8')            if test_result.startswith('data'):                test_result = json.loads(test_result[5:])                filters = test_result['bdaddrs'][0]['bdaddr'] + test_result['adData']                if len(tmp) < self.conf['filter_count']:                    if filters in tmp:                        self.case_run_flag = 'fail'                        print('\n', test_result, '\n', tmp)                        return                    else:                        print(test_result)                        tmp.append(filters)                else:                    self.case_run_flag = 'success'                    return    def __filter_name_rssi(self, res, filter_name, filter_rssi):        tmp = []        for test_result in res.iter_lines():            test_result = str(test_result, encoding='utf8')            if test_result.startswith('data'):                test_result = json.loads(test_result[5:])                filters = test_result['name']                if len(tmp) < self.conf['filter_count']:                    if filters != filter_name or int(test_result['rssi']) < int(filter_rssi):                        self.case_run_flag = 'fail'                        print('\n', test_result, '\n', tmp)                        return                    else:                        print(test_result)                        tmp.append(filters)                else:                    self.case_run_flag = 'success'                    return    def __filter_name_uuid(self, res, filter_name, filter_uuid):        tmp = []        for test_result in res.iter_lines():            test_result = str(test_result, encoding='utf8')            if test_result.startswith('data'):                test_result = json.loads(test_result[5:])                expect = filter_name + str(filter_uuid)[2:] + str(filter_uuid)[:2]                uuid = self.get_uuid(test_result['adData'])                if uuid:                    filters = test_result['name'] + uuid                    if len(tmp) < self.conf['filter_count']:                        if filters != expect:                            self.case_run_flag = 'fail'                            print(filters, expect)                            return                        else:                            tmp.append(filters)                            print(test_result)                    else:                        self.case_run_flag = 'success'                        return    def __filter_uuid_rssi(self, res, filter_uuid, filter_rssi):        tmp = []        for test_result in res.iter_lines():            test_result = str(test_result, encoding='utf8')            if test_result.startswith('data'):                test_result = json.loads(test_result[5:])                uuid = self.get_uuid(test_result['adData'])                sort_uuid = str(filter_uuid)[2:] + str(filter_uuid)[:2]                if uuid:                    filters = uuid                    if len(tmp) < self.conf['filter_count']:                        if filters != sort_uuid or int(test_result['rssi']) < int(filter_rssi):                            print(filters, sort_uuid, '\n', test_result['rssi'] < filter_rssi)                            self.case_run_flag = 'fail'                            return                        else:                            tmp.append(filters)                            print(test_result)                    else:                        self.case_run_flag = 'success'                        return                else:                    self.case_run_flag = 'fail'                    print(test_result)                    return    def __filter_uuid(self, res, filter_uuid):        tmp = []        for test_result in res.iter_lines():            test_result = str(test_result, encoding='utf8')            if test_result.startswith('data'):                test_result = json.loads(test_result[5:])                uuid = self.get_uuid(test_result['adData'])                sort_uuid = str(filter_uuid)[2:] + str(filter_uuid)[:2]                if uuid:                    filters = uuid                    if len(tmp) < self.conf['filter_count']:                        if filters != sort_uuid:                            print('\n', filters, '≠', filter_uuid, '\n')                            self.case_run_flag = 'fail'                            return                        else:                            tmp.append(filters)                            print(test_result)                    else:                        self.case_run_flag = 'success'                        return                else:                    self.case_run_flag = 'fail'                    print(test_result)                    return    def __filter_name(self, res, filter_name):        tmp = []        for test_result in res.iter_lines():            test_result = str(test_result, encoding='utf8')            if test_result.startswith('data'):                test_result = json.loads(test_result[5:])                filters = test_result['name']                if len(tmp) < self.conf['filter_count']:                    if filters != filter_name:                        print('\n', filters, '≠', filter_name, '\n')                        self.case_run_flag = 'fail'                        return                    else:                        tmp.append(filters)                        print(test_result)                else:                    self.case_run_flag = 'success'                    return    def __filter_rssi(self, res, filter_rssi):        tmp = []        for test_result in res.iter_lines():            test_result = str(test_result, encoding='utf8')            if test_result.startswith('data'):                test_result = json.loads(test_result[5:])                filters = int(test_result['rssi'])                if len(tmp) < self.conf['filter_count']:                    if filters < int(filter_rssi):                        print('\n', filters, '≠', filter_rssi, '\n')                        self.case_run_flag = 'fail'                        return                    else:                        tmp.append(filters)                        print(test_result)                else:                    self.case_run_flag = 'success'                    return    def __filter_mac(self, res, filter_mac):        tmp = []        for test_result in res.iter_lines():            test_result = str(test_result, encoding='utf8')            if test_result.startswith('data'):                test_result = json.loads(test_result[5:])                filters = test_result['bdaddrs'][0]['bdaddr']                if len(tmp) < self.conf['filter_count']:                    if filters != filter_mac:                        print('\n', filters, '≠', filter_mac, '\n')                        self.case_run_flag = 'fail'                        return                    else:                        tmp.append(filters)                        print(test_result)                else:                    self.case_run_flag = 'success'                    return    @ddt.data(*dd['connectdata'])    def test_connect(self, values):        if self.sdk.model.upper().startswith('S'):            expect_result = values['expect_result_s1000']        else:            expect_result = values['expect_result_other']        device = values['device']        chip = values['chip']        try:            chip = int(chip)        except Exception as e:            print(e)            pass        types = values['types']        timeout = values['timeout']        self.sdk.disconnect_device(device)        if chip:            code, body, duration = self.sdk.connect_device(device, types, chip, timeout)            if body == 'chip is busy':                time.sleep(3)                code, body, duration = self.sdk.connect_device(device, types, chip, timeout)        else:            code, body, duration = self.sdk.connect_device(device, types, timeout=timeout)            if body == 'chip is busy':                time.sleep(3)                code, body, duration = self.sdk.connect_device(device, types, timeout=timeout)        test_result = str(code) + ',' + body        self.assertEqual(test_result, expect_result)        if int(code) == 200:            self.sdk.disconnect_device(device)    @ddt.data(*dd['disconnectdata'])    def test_disconnect(self, values):        expect_result = values['expect_result']        device = values['device']        timeout = values['timeout']        code, body = self.sdk.disconnect_device(device, timeout)        test_result = str(code) + ',' + body        self.assertEqual(test_result, expect_result)    @ddt.data(*dd['getdevlist'])    def test_get_dev_list(self, values):        expect_result = values['expect_result']        connect_state = values['connection_state']        code, _ = self.sdk.get_devices_list(connect_state)        test_result = int(code)        self.assertEqual(test_result, int(expect_result))    @ddt.data(*dd['discover_service'])    def test_discover_service(self, values):        device = values['device']        dev_type = values['type']        service_uuid = values['service_uuid']        expect_result = values['expect_result']        i = 0        while i <= 3:            self.sdk.connect_device(device, dev_type)            time.sleep(2)            if device in self.sdk.get_devices_list('connected')[1]:                break            i += 1        code, body = self.sdk.discovery_services(device, service_uuid)        test_result = str(code) + ',' + body        self.assertEqual(test_result, expect_result)    @ddt.data(*dd['discover_characs'])    def test_discover_characs(self, values):        device = values['device']        dev_type = values['type']        server_uuid = str(values['service_uuid'])        expect_result = values['expect_result']        i = 0        while i <= 3:            self.sdk.connect_device(device, dev_type)            time.sleep(2)            if device in self.sdk.get_devices_list('connected')[1]:                break            i += 1        code, body = self.sdk.discovery_characteristics(device, server_uuid)        test_result = str(code) + ',' + body        self.assertEqual(test_result, expect_result)    @ddt.data(*dd["discover_charac"])    def test_discover_charac(self, values):        device = values['device']        dev_type = values['type']        charac_uuid = values['charac_uuid']        expect_result = values['expect_result']        i = 0        while i <= 3:            self.sdk.connect_device(device, dev_type)            time.sleep(2)            if device in self.sdk.get_devices_list('connected')[1]:                break            i += 1        code, body = self.sdk.discovery_charateristic(device, charac_uuid)        test_result = str(code) + ',' + body        self.assertEqual(test_result, expect_result)    @ddt.data(*dd['discover_des'])    def test_discover_des(self, values):        device = values['device']        dev_type = values['type']        charac_uuid = values['charac_uuid']        expect_result = values['expect_result']        i = 0        while i <= 3:            self.sdk.connect_device(device, dev_type)            time.sleep(2)            if device in self.sdk.get_devices_list('connected')[1]:                break            i += 1        code, body = self.sdk.discover_descriptors(device, charac_uuid)        test_result = str(code) + ',' + body        self.assertEqual(test_result, expect_result)    @ddt.data(*dd['discover_all'])    def test_discover_all(self, values):        device = values['device']        dev_type = values['type']        expect_result = values['expect_result']        i = 0        while i <= 3:            self.sdk.connect_device(device, dev_type)            time.sleep(2)            if device in self.sdk.get_devices_list('connected')[1]:                break            i += 1        code, body = self.sdk.discover_all(device)        if code == 200:            self.assertEqual(len(body), len(expect_result))        else:            test_result = str(code) + ',' + body            self.assertEqual(test_result, expect_result)    @ddt.data(*dd['read_by_handle'])    def test_read_by_handle(self, values):        device = values['device']        dev_type = values['type']        handle = values['handle']        expect_result = values['expect_result']        i = 0        while i <= 3:            self.sdk.connect_device(device, dev_type)            time.sleep(2)            if device in self.sdk.get_devices_list('connected')[1]:                break            i += 1        code, body = self.sdk.read_by_handle(device, handle)        test_result = str(code) + ',' + body        self.assertEqual(test_result, expect_result)    @ddt.data(*dd['write_by_handle'])    def test_write_by_handle(self, values):        device = values['device']        dev_type = values['type']        handle = values['handle']        handle_data = values['handle_data']        expect_result = values['expect_result']        i = 0        while i <= 3:            self.sdk.connect_device(device, dev_type)            time.sleep(2)            if device in self.sdk.get_devices_list('connected')[1]:                break            i += 1        else:            print('device connected failed!!!')        code, body = self.sdk.write_by_handle(device, handle, handle_data)        test_result = str(code) + ',' + body        self.assertEqual(test_result, expect_result)    @ddt.data(*dd['get_connect_state'])    def test_get_device_connect_state(self, values):        self.message = None        device = values['device']        types = values['type']        expect_result = values['expect_result']        res = self.sdk.get_device_connect_state()        t = threading.Thread(target=self.recv_message, args=(res,))        t.setDaemon(True)        t.start()        if expect_result == 'connected':            self.sdk.disconnect_device(device)            time.sleep(5)            self.message = None            code, body, duration = self.sdk.connect_device(device, types, 0, 10000)            print(code, body)            while 1:                if self.time_out_flag:                    self.fail('case time out')                    break                else:                    if self.message:                        if self.message['handle'] == device:                            self.assertTrue(True)                            self.sdk.disconnect_device(device)                            self.message = None                            break                        else:                            self.assertTrue(False)                            self.sdk.disconnect_device(device)                            self.message = None                            break        else:            self.sdk.connect_device(device, types, 0, 10000)            time.sleep(5)            self.message = None            code, body = self.sdk.disconnect_device(device)            print(code, body)            while 1:                if self.time_out_flag:                    self.fail('case time out')                    break                else:                    if self.message:                        if self.message['handle'] == device:                            self.assertTrue(True)                            self.sdk.disconnect_device(device)                            self.message = None                            break                        else:                            self.assertTrue(False)                            self.sdk.disconnect_device(device)                            self.message = None                            break    @ddt.data(*dd['recv_notification'])    def test_recive_notification(self, values):        device = values['device']        expect_result = values['expect_result']        dev_type = values['device_type']        i = 0        while i <= 3:            self.sdk.connect_device(device, dev_type)            time.sleep(2)            if device in self.sdk.get_devices_list('connected')[1]:                break            i += 1        else:            self.fail('device connected failed!!!')            return        #start Thread to receive notification        res = self.sdk.recive_notification()        t = threading.Thread(target=self.recv_message, args=(res,))        t.setDaemon(True)        t.start()        #wtite handle to open device notification        code,_ = self.sdk.write_by_handle(device,'17','0100')        print(1,code)        if code == '200':            start_handle = values['start_handle']            srart_handle_value1 = values['start_handle_value1']            srart_handle_value2 = values['start_handle_value2']            stop_handle_value = values['stop_handle_value']            code,body = self.sdk.write_by_handle(device, start_handle, srart_handle_value1)            print(2,code,body)            if code == '200':                code, _ = self.sdk.write_by_handle(device, start_handle, srart_handle_value2)                print(3,code)                if code == '200':                    while 1:                        if self.message:                            print(self.message)                            self.assertEqual(self.message, expect_result)                            self.sdk.write_by_handle(device, start_handle, stop_handle_value)                            break                    return        self.fail('write handle failed!')    @staticmethod    def get_uuid(data):        start = 0        head_length = int(data[start:start + 2], 16)        start = 2 + head_length * 2        data_length = int(data[start:start + 2], 16)        start = start + 2        adv_data = data[start:start + data_length * 2]        adv_tpye = int(adv_data[0:2], 16)        if 2 <= adv_tpye <= 7:            uuid = adv_data[2:]            # print(uuid)            return str(uuid)        else:            return None    def recv_message(self, res):        for msg in res:            print(msg)            if msg != ':keep-alive':                try:                    self.message = json.loads(msg)                except:                    pass    def time_out(self):        self.case_run_flag = 'timeout'    def tearDown(self):        self.timeout_timer.cancel()if __name__ == '__main__':    unittest.main(verbosity=2)