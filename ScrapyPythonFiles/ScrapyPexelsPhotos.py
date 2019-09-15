# -*- coding: utf-8 -*-

import requests
from lxml import etree
import os
from multiprocessing import Pool
import pymysql
import logging
from logging import handlers


class Logger(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self, filename, level='info',when='d', backCount=3, fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        # 设置日志格式
        format_str = logging.Formatter(fmt)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))
        # 往屏幕上输出
        sh = logging.StreamHandler()
        # 设置屏幕上显示的格式
        sh.setFormatter(format_str)
        # 往文件里写入#指定间隔时间自动生成文件的处理器
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        # 设置文件里写入的格式
        # 把对象加到logger里
        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)


def enter_password_encryption():
    """
    密码加密函数
    :return:
    """
    pass


def scrapy_main_function():
    """
    一个爬取Pexels图片网站图片的爬虫
    :return:
    """
    # 伪造请求头
    ua_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
                  }
    # 不是200的次数
    not_200 = 0
    # 起始页数
    page_number = 1
    # 网站原始 url
    original_url = 'https://www.pexels.com'
    log = Logger('info.log', level='debug')
    # 打开mysql数据库
    connection = pymysql.connect(host='localhost', user='root', password='Huawei12#$', charset='utf8')
    log.logger.info("Connection Successful!")
    cursor = connection.cursor()
    # 如果数据库不存在则创建
    sql = 'create database if not exists pexels_image_urls character set utf8;'
    cursor.execute(sql)
    log.logger.info('Database create successful!')
    # 选择创建出来的数据库
    cursor.execute("use pexels_image_urls;")
    # 如果表不存在则创建表
    sql = 'create table if not exists image_urls' \
          '(id int primary key auto_increment, ' \
          'searched_images_titles char(100), ' \
          'image_download_url char(100))'
    cursor.execute(sql)
    # 输入你想搜索图片的关键词
    searching_text_list = ['sexy woman', 'sexy man', 'cool cars', 'cute dog', 'cute cat', 'plants']
    for searching_what in searching_text_list:
        # 没有爬完资源不会终止访问
        while True:
            try:
                # 起始 url
                start_url = '{}/search/{}/?&page={}'.format(original_url, searching_what, page_number)
                # 向网站发起请求
                image_web_responses = requests.get(url=start_url, headers=ua_headers)
                # 将网页的编码自动转换成正确的格式
                image_web_responses.encoding = image_web_responses.apparent_encoding
                log.logger.info('Status Code is {}'.format(image_web_responses.status_code))
                # 将图片转成可xpath的格式
                html_text = etree.HTML(image_web_responses.text)
                # 获取图片的标题
                searched_images_titles = html_text.xpath('//div[@class="hide-featured-badge hide-favorite-badge"]//a/@title')
                log.logger.info(searched_images_titles)
                log.logger.info('Titles Number is {}'.format(len(searched_images_titles)))
                # 获取图片的第一个可访问url
                searched_images_urls = html_text.xpath('//div[@class="hide-featured-badge hide-favorite-badge"]//a[@class="js-photo-link photo-item__link"]/@href')
                log.logger.info('Searched urls is {}'.format(searched_images_urls))
                log.logger.info('Images Urls Number is {}'.format(len(searched_images_urls)))
                # 进一步访问该图片
                for sort_number, searched_images_url in enumerate(searched_images_urls):
                    # 拼接图片第二个可以访问的url
                    second_url = '{}{}'.format(original_url, searched_images_url)
                    second_image_web_responses = requests.get(url=second_url, headers=ua_headers)
                    image_web_responses.encoding = image_web_responses.apparent_encoding
                    log.logger.info('Second Status Code is {}'.format(second_image_web_responses.status_code))
                    assert image_web_responses.status_code == 200
                    html_text_2 = etree.HTML(second_image_web_responses.text)
                    # 获取图片的可下载的链接
                    image_download_url_list = html_text_2.xpath('//div[@class="js-photo-page-action-buttons-download"]//a[@class="js-download-a-tag rd__button rd__button--download"]/@href')
                    add_url_str = '?search_query={}&tracking_id=yj9odc1lowd'.format(searching_what)
                    log.logger.info('Download Image Url is {}{}{}'.format(original_url, image_download_url_list[0], add_url_str))
                    image_download_url = original_url + image_download_url_list[0] + add_url_str
                    values = ["{}".format(searched_images_titles[sort_number]), "{}".format(image_download_url)]
                    sql = 'insert into image_urls(searched_images_titles, image_download_url) values(%s, %s)'
                    cursor.execute(sql, values)
                    log.logger.info('Insert data {} successful!'.format(searched_images_titles[sort_number]))
                    connection.commit()
                    # download_image_responses = requests.get(url=image_download_url, headers=ua_headers)
                    # print('Download Image Status Code is {}'.format(download_image_responses.status_code))
                    # # 如果路径不存在就创建一个新文件夹
                    # folder_path = os.path.exists('/Volumes/TOSHIBA_SSD/Pic/{}'.format(searching_what))
                    # if not folder_path:
                    #     os.makedirs('/Volumes/TOSHIBA_SSD/Pic/{}'.format(searching_what))
                    #     print('Path is not exist! Create path successful!')
                    # # 如果文件中含有'/'符号，替换成其他符号
                    # if '/' in searched_images_titles[sort_number]:
                    #     searched_images_titles[sort_number] = searched_images_titles[sort_number].replace('/', '-')
                    # # 开始保存图片
                    # with open('/Volumes/TOSHIBA_SSD/Pic/{}/{}.jpg'.format(searching_what,
                    #                                                       searched_images_titles[sort_number]),
                    #           'wb+') as f_obj:
                    #     print('Start save image {}!'.format(searched_images_titles[sort_number]))
                    #     f_obj.write(download_image_responses.content)
                    #     print('ImageFileName is {}, Save Image Successful!'.format(searched_images_titles[sort_number]))
            except Exception as e:
                log.logger.error(e)
                not_200 += 1
                if not_200 > 10:
                    log.logger.error('Check Your Internet or Check The URL is exist')
                    break
                page_number += 1
                log.logger.error('This is {} times, responses is not 200!'.format(not_200))
        # 关闭数据库连接
        connection.close()
        cursor.close()
        log.logger.info('Closed the database connection!')


if __name__ == '__main__':

    scrapy_main_function()
    #     searching_what = searching_text
    #     p.apply_async(scrapy_main_function(searching_what))
    # p.close()
    # p.join()
    # cursor.execute('select * from image_urls;')
    # while True:
    #     print(cursor.fetchone())
    #     if cursor.fetchone() is None:
    #         break

