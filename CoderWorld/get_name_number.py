import re
import time
start_time = time.clock()
name_all = '李锐31, 刘腾21, 陈翔782, 陈思聪862, 符义红683, 刘琳098'
name_list = name_all.split(',')
name_info = {}
for name in name_list:
    for i, j in enumerate(name):
        if j.isnumeric() and not name[i-1].isnumeric():
            name_info[name[:i]] = name[i:]
end_time = time.clock()
print(name_info)
print(end_time - start_time)


# start_time = time.clock()
# a = '李锐31, 刘腾21, 陈翔782, 陈思聪862, 符义红683, 刘琳098'
#
#
# def get_name_dict(text):
#     num_name_dict = dict()
#     for txt in list(map(lambda x:x.strip(), text.split(','))):
#         res = re.findall(r'\d', txt)
#         num = [num for num in res if num]
#         num_name_dict[txt[0:-len(num[0])]] = num[0]
#     end_time = time.clock()
#     print(num_name_dict)
#     print(end_time - start_time)
#
#
# if __name__ == '__main__':
#     get_name_dict(a)
