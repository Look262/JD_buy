from selenium import webdriver

import datetime

import time


def login(good):
    now = datetime.datetime.now()
    browser.get('https://www.jd.com/')
    time.sleep(2)
    if browser.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]'):
        browser.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
        print("请用户扫码登录")
        time.sleep(10)
        print('登录时间结束')

    time.sleep(1)

    print('登录成功，正在打开商品链接...', now.strftime('%Y-%m-%d %H:%M:%S.%f'))
    browser.get(good)


def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        if now >= times:
            # 加入购物车
            print('抢购开始..')
            while True:
                try:
                    if browser.find_element_by_xpath('//*[@id="InitCartUrl"]'):
                        browser.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
                        print('正在加入购物车...')
                        time.sleep(0.01)
                        break
                except:
                    if browser.find_element_by_link_text('商品已成功加入购物车！'):
                        break

            time.sleep(0.1)
            browser.get('https://cart.jd.com/cart_index')
            print('转到购物车界面...')

            # 检测全选 并结算
            while True:
                try:
                    if browser.find_element_by_xpath('//input[@clstag="pageclick|keycount|Shopcart_CheckAll|0"]'):
                        browser.find_element_by_xpath('//*[@id="cart-body"]/div[1]/div[3]/div[1]/div/input').click()
                        time.sleep(0.1)
                        break
                except:
                    break
            print('全选商品')

            # 结算
            while True:
                try:
                    if browser.find_element_by_xpath(
                            '//*[@id="cart-body"]/div[1]/div[5]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a'):
                        browser.find_element_by_xpath(
                            '//*[@id="cart-body"]/div[1]/div[5]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a').click()
                        time.sleep(0.1)
                        break
                except:
                    print('结算失败，继续尝试', now)

            # 提交订单
            while True:
                try:
                    if browser.find_element_by_xpath('//*[@id="order-submit"]/b'):
                        browser.find_element_by_xpath('//*[@id="order-submit"]/b').click()
                        time.sleep(0.1)
                        break
                except:
                    print('提交订单失败，将继续尝试', now)
            time.sleep(0.5)


def check():
    try:
        # 成功
        if browser.find_element_by_xpath(
                '//*[@id="indexBlurId"]/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]'):
            return 0
    except:
        # 失败
        return 1


if __name__ == '__main__':

    times = '2021-08-24 23:59:58.000000'
    # 商品链接

    good_link = 'https://item.jd.com/100011553443.html'

    browser = webdriver.Edge(executable_path='./msedgedriver.exe')
    login(good_link)
    buy(times)
    if check():
        print('抢购未成功，将重新抢购')
    else:
        print('抢购已成功，请尽快支付！感谢您的使用！')
