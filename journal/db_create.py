"""
Read OneJsonObj.json and create sql  create
"""
import json
f = open('/home/limawhiskeydelta/PycharmProjects/dgl-tda-api/journal/OneJsonObj.json','r')
data = json.load(f)
# print(f'data keys: {data.keys()}')
# print(f"fees: {data['fees']}")
trades_list = []
lists = {}
for k, v in data.items():
    print(f"k: {k} v: {v} dict: {isinstance(v, dict)}")
    if isinstance(v,dict):
        lists[k] = v
        for kk, vv in v.items():
            print(f"kk: {kk} v: {vv} dict: {isinstance(vv, dict)}")
            if  isinstance(vv, dict):
                lists[kk] = vv
    else: trades_list.append(k)
    print(f"trades_list: {trades_list}")
    print(f"lists: {lists}")

    for l in trades_list:
        print(f"l:  {l}")
    print('++++++ \n')
    for k, v in lists.items():
        print(f"K: {k} v: {v}")



