import requests
from lxml import etree
import os
from multiprocessing import Pool


def scrapy_main_function(searching_what):
    """
    一个爬取Pexels图片网站图片的爬虫
    :return:
    """
        # 伪造请求头
    ua_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
                  }
    # 不是200的次数
    not_200 = 0
    # 起始页数
    page_number = 1
    # 网站原始 url
    original_url = 'https://www.pexels.com'
    # 没有爬完资源不会终止访问
    while True:
        try:
            # 起始 url
            start_url = '{}/search/{}/?&page={}'.format(original_url, searching_what, page_number)
            # 向网站发起请求
            image_web_responses = requests.get(url=start_url, headers=ua_headers)
            # 将网页的编码自动转换成正确的格式
            image_web_responses.encoding = image_web_responses.apparent_encoding
            print('Status Code is {}'.format(image_web_responses.status_code))
            # 将图片转成可xpath的格式
            html_text = etree.HTML(image_web_responses.text)
            # 获取图片的标题
            searched_images_titles = html_text.xpath('//div[@class="hide-featured-badge hide-favorite-badge"]//a/@title')
            print(searched_images_titles)
            print('Titles Number is {}'.format(len(searched_images_titles)))
            # 获取图片的第一个可访问url
            searched_images_urls = html_text.xpath('//div[@class="hide-featured-badge hide-favorite-badge"]//a[@class="js-photo-link photo-item__link"]/@href')
            print(searched_images_urls)
            print('Images Urls Number is {}'.format(len(searched_images_urls)))
            # 进一步访问该图片
            for sort_number, searched_images_url in enumerate(searched_images_urls):
                # 拼接图片第二个可以访问的url
                second_url = '{}{}'.format(original_url, searched_images_url)
                second_image_web_responses = requests.get(url=second_url, headers=ua_headers)
                image_web_responses.encoding = image_web_responses.apparent_encoding
                print('Second Status Code is {}'.format(second_image_web_responses.status_code))
                assert image_web_responses.status_code == 200
                html_text_2 = etree.HTML(second_image_web_responses.text)
                # 获取图片的可下载的链接
                image_download_url_list = html_text_2.xpath('//div[@class="js-photo-page-action-buttons-download"]//a[@class="js-download-a-tag rd__button rd__button--download"]/@href')
                add_url_str = '?search_query={}&tracking_id=yj9odc1lowd'.format(searching_what)
                print('Download Image Url is {}{}{}'.format(original_url, image_download_url_list[0], add_url_str))
                image_download_url = original_url + image_download_url_list[0] + add_url_str
                download_image_responses = requests.get(url=image_download_url, headers=ua_headers)
                print('Download Image Status Code is {}'.format(download_image_responses.status_code))
                # 如果路径不存在就创建一个新文件夹
                folder_path = os.path.exists('/Volumes/TOSHIBA_SSD/Pic/{}'.format(searching_what))
                if not folder_path:
                    os.makedirs('/Volumes/TOSHIBA_SSD/Pic/{}'.format(searching_what))
                    print('Path is not exist! Create path successful!')
                # 如果文件中含有'/'符号，替换成其他符号
                if '/' in searched_images_titles[sort_number]:
                    searched_images_titles[sort_number] = searched_images_titles[sort_number].replace('/', '-')
                # 开始保存图片
                with open('/Volumes/TOSHIBA_SSD/Pic/{}/{}.jpg'.format(searching_what,
                                                                      searched_images_titles[sort_number]),
                          'wb+') as f_obj:
                    print('Start save image {}!'.format(searched_images_titles[sort_number]))
                    f_obj.write(download_image_responses.content)
                    print('ImageFileName is {}, Save Image Successful!'.format(searched_images_titles[sort_number]))
        except Exception as e:
            print(e)
            not_200 += 1
            if not_200 > 10:
                print('Check Your Internet or Check The URL is exist')
                break
            page_number += 1
            print('This is {} times, responses is not 200!'.format(not_200))


if __name__ == '__main__':
    p = Pool()
    # 输入你想搜索图片的关键词
    searching_text_list = ['sexy woman', 'sexy man', 'cool cars', 'cute dog', 'cute cat', 'plants']
    for searching_text in searching_text_list:
        searching_what = searching_text
        p.apply_async(scrapy_main_function(searching_what))
    p.close()
    p.join()
