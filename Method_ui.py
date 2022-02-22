import yaml
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
class BasePage(object):
    Mom_assert='Mom_assert'
    Mom_element='Mom_element'
    Mom_variable='Mom_variable'
    def __init__(self,driver):
        self.driver=driver

    def g_url(self,url):
        '''
        # 获取网址方法
        '''
        try:
            self.driver.get(self.get_data(url))
        except Exception as e:
            print('# 获取网址方法',e)
            raise e


    def find_element(self,*loc):
        '''
        # 类函数通用方法——定位元素方法
        '''
        try:
             return self.driver.find_element(*loc)
        except Exception as e:
            if 'Unable to locate element' in str(e):
                print('找不到该元素:',e)
                raise e
            else:
                print(e)
                raise e


    def delifram(self):
        '''
        # 退出所有弹窗
        '''
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    def get_data(self,txt):
        '''
        获取Mom_variable参数
        '''
        try:
            with open(self.Mom_variable, 'r',
                      encoding='utf-8') as p:
                dataE = yaml.load(p, Loader=yaml.FullLoader)
            return dataE[txt]
        except Exception as e:
            if 'while scanning a simple key' in str(e):
                print('Mom_variable.yml文件内出现错误格式数据，请参考下面异常信息删除异常数据',e)
                raise e
            elif KeyError:
                print('Mom_variable.yml文件没有该参数：',self.Mom_variable,e)
                raise e
            else:
                print('请参考下面异常信息：',e)
                raise e


    def find_data_element(self,loc):
        '''
        #获取Mom_element.yml文件【'value'】参数且根据
        #  id   classname   link_text  name   css_selector   partial_link_text    tagname   xpath赋予对应元素写法
        '''
        try:
            with open(self.Mom_element, 'r',encoding='utf-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
            if data[loc][0]['by'] == 'id':
                data_id = By.ID, data[loc][0]['value']
                return data_id
            elif data[loc][0]['by'] == 'classname':
                data_classname = By.CLASS_NAME, data[loc][0]['value']
                return data_classname
            elif data[loc][0]['by'] == 'link_text':
                data_linktext = By.LINK_TEXT, data[loc][0]['value']
                return data_linktext
            elif data[loc][0]['by'] == 'name':
                data_name = By.NAME, data[loc][0]['value']
                return data_name
            elif data[loc][0]['by'] == 'css_selector':
                data_SELECTOR = By.CSS_SELECTOR, data[loc][0]['value']
                return data_SELECTOR
            elif data[loc][0]['by'] == 'partial_link_text':
                data_partial_link_text = By.PARTIAL_LINK_TEXT, data[loc][0]['value']
                return data_partial_link_text
            elif data[loc][0]['by'] == 'tagname':
                data_tagname = By.TAG_NAME, data[loc][0]['value']
                return data_tagname
            else:
                data_xpath = By.XPATH, data[loc][0]['value']
                return data_xpath
        except Exception as e:
            if 'while scanning a simple key' in str(e):
                print('Mom_element.yml文件内出现错误格式数据，请参考下面异常信息删除异常数据', e)
                raise e
            elif KeyError:
                print('Mom_element.yml文件没有该参数：', e)
                raise e
            else:
                print('请参考下面异常信息：', e)
                raise e



    def find_data_assert(self,loc):
        '''
        # 获取Mom_assert.yml文件【'value'】参数且根据
        #  id   classname   link_text  name   css_selector   partial_link_text    tagname   xpath赋予对应元素写法
        '''
        try:
            with open(self.Mom_assert, 'r',
                      encoding='utf-8') as d:
                data = yaml.load(d, Loader=yaml.FullLoader)
            if data[loc]['by'] == 'id':
                data_id = By.ID, data[loc]['value']
                return data_id
            elif data[loc]['by'] == 'classname':
                data_classname = By.CLASS_NAME, data[loc]['value']
                return data_classname
            elif data[loc]['by'] == 'link_text':
                data_linktext = By.LINK_TEXT, data[loc]['value']
                return data_linktext
            elif data[loc]['by'] == 'name':
                data_name = By.NAME, data[loc]['value']
                return data_name
            elif data[loc]['by'] == 'css_selector':
                data_SELECTOR = By.CSS_SELECTOR, data[loc]['value']
                return data_SELECTOR
            elif data[loc]['by'] == 'partial_link_text':
                data_partial_link_text = By.PARTIAL_LINK_TEXT, data[loc]['value']
                return data_partial_link_text
            elif data[loc]['by'] == 'tagname':
                data_tagname = By.TAG_NAME, data[loc]['value']
                return data_tagname
            else:
                data_xpath = By.XPATH, data[loc]['value']
                return data_xpath
        except Exception as e:
            if 'while scanning a simple key' in str(e):
                print('Mom_assert.yml文件内出现错误格式数据，请参考下面异常信息删除异常数据',e)
                raise e
            elif KeyError:
                print('Mom_assert.yml文件没有该参数：',e)
                raise e
            else:
                print('请参考下面异常信息：',e)
                raise e


    def find_data_variable(self,txt):
        '''
        #调用variable文件【'txt'】参数
        '''
        try:
            with open(self.Mom_variable, 'r',
                      encoding='utf-8') as p:
                dataE = yaml.load(p, Loader=yaml.FullLoader)
            return dataE[txt]
        except Exception as e:
            if 'while scanning a simple key' in str(e):
                print('Mom_variable.yml文件内出现错误格式数据，请参考下面异常信息删除异常数据',e)
                raise e
            elif KeyError:
                print('Mom_variable.yml文件没有该参数：',e)
                raise e
            else:
                print('请参考下面异常信息：',e)
                raise e


    def click(self,loc):
        '''
        #点击方法
        '''
        count=1
        while count <20:
            count=count+1
            try:
                element=WebDriverWait(self.driver,10,0.3).until(EC.element_to_be_clickable((self.find_data_element(loc))))
                time.sleep(0.5)
                element.click()
            except Exception as g:
                if 'element click intercepted: Element' in str(g):
                    time.sleep(0.3)
                elif 'element is not attached to the page document' in str(g):
                    time.sleep(0.3)
                    # element = WebDriverWait(self.driver, 10, 0.3).until(
                    #     EC.element_to_be_clickable((self.find_data_element(loc))))
                    # time.sleep(0.5)
                    # element.click()
                else:
                    print('#点击方法，找不到元素：',loc)
                    raise g
            else:
                break


    def input(self, loc,txt):
        '''
        # 输入文本方法
        '''
        count = 1
        while count<20:
            count = count + 1
            try:
                element = WebDriverWait(self.driver, 10, 0.3).until(
                    EC.element_to_be_clickable((self.find_data_element(loc))))
                time.sleep(0.3)
                element.click()
                element.send_keys(self.find_data_variable(txt))
            except Exception as g:
                if 'element click intercepted: Element' in str(g):
                    time.sleep(0.3)
                elif 'element is not attached to the page document' in str(g):
                    time.sleep(0.3)
                    # element = WebDriverWait(self.driver, 10, 0.3).until(
                    #     EC.element_to_be_clickable((self.find_data_element(loc))))
                    # time.sleep(0.5)
                    # element.click()
                else:
                    print('# 输入文本方法,找不到元素',loc)
                    raise g
            else:
                break

    def clear_input(self, loc,txt):
        '''
        # 输入文本方法
        '''
        count = 1
        while count<20:
            count = count + 1
            try:
                element = WebDriverWait(self.driver, 10, 0.3).until(
                    EC.element_to_be_clickable((self.find_data_element(loc))))
                time.sleep(0.3)
                element.click()
                for i in range(10):
                    actions=ActionChains(self.driver)
                    actions.send_keys(Keys.BACK_SPACE)
                    actions.perform()
                element.send_keys(self.find_data_variable(txt))
            except Exception as g:
                if 'element click intercepted: Element' in str(g):
                    time.sleep(0.3)
                elif 'element is not attached to the page document' in str(g):
                    time.sleep(0.3)
                    # element = WebDriverWait(self.driver, 10, 0.3).until(
                    #     EC.element_to_be_clickable((self.find_data_element(loc))))
                    # time.sleep(0.5)
                    # element.click()
                else:
                    print('# 输入文本方法,找不到元素',loc)
                    raise g
            else:
                break

    def clcik_right(self, loc):
        '''
        #右键方法
        '''
        while True:
            try:
                element=WebDriverWait(self.driver,10,0.3).until(EC.element_to_be_clickable((self.find_data_element(loc))))
                time.sleep(0.3)
                ActionChains.context_click(element).perform()
            except Exception as g:
                if 'element click intercepted: Element' in str(g):
                    time.sleep(0.3)
                elif 'element is not attached to the page document' in str(g):
                    time.sleep(0.3)
                else:
                    print('#点击方法',g)
                    raise g
            else:
                break


    def click_double(self, loc):
        '''
        # 双击方法
        '''
        while True:
            try:
                element=WebDriverWait(self.driver,10,0.3).until(EC.element_to_be_clickable((self.find_data_element(loc))))
                time.sleep(0.3)
                ActionChains.double_click(element).perform()
            except Exception as g:
                if 'element click intercepted: Element' in str(g):
                    time.sleep(0.3)
                elif 'element is not attached to the page document' in str(g):
                    time.sleep(0.3)
                else:
                    print('#双击方法',g)
                    raise g
            else:
                break


    def dy_txt(self, loc):
        '''
         #断言文本相等方法
         '''
        with open(self.Mom_assert, 'r',
                  encoding='utf-8') as d:
            data = yaml.load(d, Loader=yaml.FullLoader)
        while True:
            try:
                element=WebDriverWait(self.driver,10,0.3).until(EC.visibility_of_element_located(self.find_data_assert(loc)))
                time.sleep(0.5)
                assert element.text == data[loc]['asstxt']
            except Exception as g:
                if 'element click intercepted: Element' in str(g):
                    time.sleep(0.3)
                elif 'element is not attached to the page document' in str(g):
                    time.sleep(0.3)
                else:
                    print('断言失败,定位返回文本：', self.find_element(*self.find_data_assert(loc)).text, '断言文本：',
                          data[loc]['asstxt'])
                    raise g
            else:
                break






    def dy_my(self, loc):
        '''
        #多数据断言
        '''
        with open(self.Mom_element, 'r', encoding='utf-8') as p:
            data = yaml.load(p, Loader=yaml.FullLoader)
            a = data[loc]['asstxt']
            list1 = a.split(",")
        with open(self.Mom_assert, 'r',encoding='utf-8') as t:
            datat = yaml.load(t, Loader=yaml.FullLoader)
        while True:
            try:
                els = self.driver.find_elements_by_tag_name(data[loc]['tagname'])
                qw = []
                for i in els:
                    qw.append(i.text)
                for lo in list1:
                    if lo in qw:
                        pass
                    else:
                        print("断言失败")
                        break
            except BaseException as g:
                if 'element is not attached' in str(g):
                    time.sleep(1)
                else:
                    print(g)
                    quit()
            else:
                break

    def swith_iframe(self, loc):
        '''
        #切换iframe功能
        '''
        get_iframe = self.driver.find_elements_by_tag_name('iframe')
        try:
            while True:
                #相同功能
                # iframe=WebDriverWait(self.driver,10,0.3).until(EC.visibility_of_element_located(self.find_data_element(loc)))
                # self.driver.switch_to.frame(iframe)
                WebDriverWait(self.driver,10,0.3).until(EC.frame_to_be_available_and_switch_to_it(self.find_data_element(loc)))
                get_iframe2=self.driver.find_elements_by_tag_name('iframe')
                if get_iframe == get_iframe2 :
                    time.sleep(0.3)
                else:
                    break
        except Exception as e:
            print(' # 切换到指定动态窗口方法',e)
            raise e


    def down(self):
        '''
        键盘事件：点击键盘向下方向键
        :return:
        '''
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN)
        actions.perform()


    def enter(self):
        '''
        键盘事件：点击键盘enter键
        :return:
        '''
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()


    def keywork(self):
        '''
        键盘事件说明
        Keys.BACK_SPACE	回退键（BackSpace）
        Keys.TAB	制表键（Tab）
        Keys.ENTER	回车键（Enter）
        Keys.SHIFT	大小写转换键（Shift）
        Keys.CONTROL	Control键（Ctrl）
        Keys.ALT	ALT键（Alt）
        Keys.ESCAPE	返回键（Esc）
        Keys.SPACE	空格键（Space）
        Keys.PAGE_UP	翻页键上（Page Up）
        Keys.PAGE_DOWN	翻页键下（Page Down）
        Keys.END	行尾键（End）
        Keys.HOME	行首键（Home）
        Keys.LEFT	方向键左（Left）
        Keys.UP	方向键上（Up）
        Keys.RIGHT	方向键右（Right）
        Keys.DOWN	方向键下（Down）
        Keys.INSERT	插入键（Insert）
        Keys.DELETE	删除键（Delete）
        Keys.NUMPAD0 ~ NUMPAD9	数字键1-9
        Keys.F1 ~ F12	F1 - F12键
        (Keys.CONTROL, 'a')	组合键Ctrf+a，全选
        (Keys.CONTROL, 'c')	组合键Ctrf+c，复制
        (Keys.CONTROL, 'x')	组合键Ctrf+x，剪切
        (Keys.CONTROL, 'v')	组合键Ctrf+v，粘贴
        :return:
        '''
    def unskip(test=''):
        "获取上个用例执行成败装饰器"
        def wraps_skip(fun):
            @wraps(wraps_skip)
            def inner_skip():
                if test == wraps_skip.__name__:
                    pass
                return pass
            return inner_skip
        return wraps_skip
                
