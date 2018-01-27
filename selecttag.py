import pandas as pd
import re
import numpy as np
#数据文件夹路径
path = r"D:\stackoverflow\mysql"
#读取到的dataframe
dataTag = pd.read_csv(path + r'\tags.csv')
#存储tagname和相应的count的字典
newDataTagDict = {}
#遍历
for index in dataTag.index:
     row = dataTag.loc[index]
     name = row['TagName']
     if(name is not np.nan):
          #下面是一些不清楚是否需要合并的：
          # 1. utf-8 iso-8859-1 是字体，需要和并吗
          # 2. preview - 5 是什么？ 按照网上的结果好像是某软件某一次版本更新的概述，并不是一个具体的语言或者工具？
          #.3. net-4.0-beta-2 这个怎么处理。。
          # 4. http-status-code 被合并了

          # ia-32 是指 Intel Architecture-32
          #ora 是 oracle数据库所写

          #有版本信息的tag的正则表达式
          matchresult = re.match('(.*)-((.{1}(\..{1}){1,})|([0-9]{1,}))$', name)
          if(matchresult):
               print(name)
               if(name is not "utf" or not 'iso-8859'):
                    name = matchresult.group(1)
               print("被统一为:"+ name)
          #如果字典里有，直接加count
          if(not name in newDataTagDict.keys()):
               newDataTagDict[name] = row['Count']
          #没有就创建
          else:
               newDataTagDict[name] = newDataTagDict[name] + row['Count']
#输出一些统计特征
print("最大count:" + str(max(newDataTagDict.values())))
print("平均count:" + str(sum(newDataTagDict.values()) / len(newDataTagDict.values())))
#初步设定低于50的count被删除
mincount = 50

#根据统计特征把数量较少的除去，newdata是最后结果
newdata = {}
for key in newDataTagDict.keys():
     print(key)
     if(newDataTagDict[key] < mincount):
          print("删除" + key + " " + str(newDataTagDict[key]))
     else:
          newdata[key] = newDataTagDict[key]
#最后仅仅输出相应的name和count到文件里
newDataTag = pd.DataFrame({'TagName' : list(newdata.keys()), 'Count' : list(newdata.values())}, columns = ['TagName', 'Count'])
newDataTag.to_csv("result.csv")

