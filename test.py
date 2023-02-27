import io
import json
from PIL import Image
from selenium.webdriver.common.by import By
import time
import sys
import os
from twocaptcha import TwoCaptcha
import undetected_chromedriver as uc

usr = input("请输入账号:")  # 输入变量a的值
pw = input("请输入密码:")  # 输入变量b的值
browser = uc.Chrome()
url = 'http://zhjw.scu.edu.cn/login'
browser.get(url)
time.sleep(4)
browser.find_element(By.ID, 'input_username').send_keys(usr)
time.sleep(4)
browser.find_element(By.ID, 'input_password').send_keys(pw)
# captcha
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
api_key = os.getenv('APIKEY_2CAPTCHA', 'b5f56c9c9272c2d59ed2749583d59f2a')
time.sleep(5)
imgId = browser.find_element(By.ID, 'captchaImg')
time.sleep(2)
# img存储
img = imgId.screenshot_as_png
bytes_stream = io.BytesIO(img)
roiImg = Image.open(bytes_stream)
roiImg.save('red.png')
time.sleep(2)
# 调用2cap接口
solver = TwoCaptcha(api_key)
time.sleep(2)
try:
    result = solver.normal('D:\\A学习\\python学习\\PycharmProjects\\scuJWCLogin\\red.png', maxLen=4)
    print("success get result")
except Exception as e:
    print(e)

else:
    print('solved: ' + str(result))
# json.loads() ,要求json串格式中必须的双引号！！转换为字典
json_str = str(result).replace("'", '"')
json_dict = json.loads(json_str)
code = json_dict['code']
print(code)
# 提交验证码登录
browser.find_element(By.ID, 'input_checkcode').send_keys(code)
time.sleep(5)
browser.find_element(By.ID, 'loginButton').click()
time.sleep(15)
# 登录已完成
