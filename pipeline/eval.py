import pandas as pd
import os
from sklearn.metrics import classification_report

# xlsx_path = '/Users/michaelsmith/Desktop/project/data/牛皮癣/badcase/manguo_result_0114.xlsx'
# xlsx_path = '/Users/michaelsmith/Desktop/project/data/牛皮癣/badcase/manguo_result_new_0119.xlsx'
xlsx_path = '/Users/michaelsmith/Desktop/project/data/牛皮癣/badcase/result.xlsx'
# xlsx_path = '/Users/michaelsmith/Desktop/project/data/牛皮癣/badcase/manguo_result_new_detect_new_ps_0119.xlsx'
xlsx_path_gt = '/Users/michaelsmith/Desktop/project/data/牛皮癣/badcase/manguo_1000_gt.xlsx'


data_gt = pd.read_excel(xlsx_path_gt)
data_pre = pd.read_excel(xlsx_path)


gt_labels = []
pred_labels = []

for i in range(1001):
    # print(data_gt.values[i])
    goods_id_gt, goods_name_gt, url_gt, result_gt = data_gt.values[i][1:5]
    goods_id, goods_name, url, result, score = data_pre.values[i][1:6]
    if result_gt not in ('0', '1'):
        continue

    assert url_gt == url, "ERROR, url not match"
    gt_labels.append(str(result_gt))
    pred_labels.append(str(result))


result = classification_report(gt_labels, pred_labels)
print(result)
print(len(gt_labels))