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
import pandas as pd

class Common():

    def __init__(self):
        self.token = ''

    """
    @brief : ライントークンをセット
    @note  : ①set_line_token ②line_notify の順に実行
    """
    def set_line_token(self, file_name, row, col):
        
        if os.path.exists(file_name):
            #print(file_name)
            csv_input = pd.read_csv(file_name)
            #print(csv_input)
            self.token = csv_input.values[row, col]
        else:
            print(file_name + " が存在しません。")

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

    """
    @brief : 指定したCSVの値を取得
    @note  : CSVファイルの1行目はカラム名データとなるため、
             2行目からのデータが取得可能なことに注意
    """        
    def get_csv_val(self, file_name, row, col):

        if os.path.exists(file_name):
            csv_input = pd.read_csv(file_name)
            return csv_input.values[row, col]
        else:
            print(file_name + " が存在しません。")


# In[2]:


# Debug用で作成
#file_name = "../key.csv"
#common = common()
#common.set_line_token(file_name, 0, 1)
#val = common.get_csv_val(file_name,0,0)
#print(val)
#common.line_notify("test")

