#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
@brief : 
@note  : 
"""

#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import requests
import csv
import pandas as pd

class Common():

    def __init__(self):
        self.token = ''
        self.key_dict = {}

    """
    @brief : ファイル名と行列を指定してCSVの値を取得
    @note  : CSVファイルの1行目はカラム名データとなるため、
             2行目からのデータが取得可能なことに注意
    """        
    def get_csv_val(self, file_name, row, col):
        if os.path.exists(file_name):
            csv_input = pd.read_csv(file_name)
            return csv_input.values[row, col]
        else:
            print(file_name + " が存在しません。")
 
    """
    @brief : ファイル名とkeyを指定してCSVの値を取得
    @note  : 
    """
    def get_csv_val_by_key(self, file_name, key):
        self.key_dict = {}
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                self.key_dict[row[0]] = row[1]
                #print(key_dict)
        return self.key_dict[key]

        
    """
    @brief : ライントークンをセット
    @note  : ①set_line_token ②line_notify の順に実行
    """
    def set_line_token(self, token):        
        self.token = token

    """
    @brief : ラインにメッセージを送信
    @note  : ①set_line_token ②line_notify の順に実行
    """        
    def line_notify(self, message):
        line_notify_token = self.token
        line_notify_api = "https://notify-api.line.me/api/notify"
        payload = {"message": message}
        headers = {"Authorization": "Bearer " + line_notify_token} 
        requests.post(line_notify_api, data=payload, headers=headers)


# In[2]:


# Debug用で作成
#file_name = "../keys.csv"
#common = Common()
#key = common.get_csv_val_by_key(file_name, "key1")
#print(key)
#common = Common()
#token = common.get_csv_val(file_name, 0, 1)
#common.set_line_token(token)
#common.line_notify("test")

