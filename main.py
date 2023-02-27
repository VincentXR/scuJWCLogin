import json

str = "{'err_no': 0, 'err_str': 'OK', 'pic_id': '1169213517976400008', 'pic_str': 'xoet', 'md5': 'ca9bc4fda521498d2b3aba5dbb4ee4ac'}"
json_str = str.replace("'", '"')
# json.loads() ,要求json串格式中必须的双引号！！转换为字典
json_dict = json.loads(json_str)
print(json_dict['pic_str'])
