# 初始化
tushare_token = "a97545f3a2e44b56fd62e8dd5aaf4e988f255d34ad5b92a1890ee605"
import pandas as pd
import tushare as ts
pro = ts.pro_api(tushare_token)

# from MyQuantification.settings import DATABASES
# import tushare as ts

# from sqlalchemy import create_engine
# user = DATABASES['default']['USER']
# password = DATABASES['default']['PASSWORD']
# database_name = DATABASES['default']['NAME']
# host = DATABASES['default']['HOST']
# port = DATABASES['default']['PORT']

# database_url = 'mysql://{user}:{password}@{host}:{port}/{database_name}?charset=utf8mb4'.format(
#     user=user,
#     password=password,
#     host=host,
#     port=port,
#     database_name=database_name,
# )
#
# engine = create_engine(database_url, echo=False, encoding='utf-8')

ts_code = '002797.SZ'

data = pro.daily(ts_code=ts_code, start_date='20100101', end_date='20191120')
df = data.to_csv('E:\python学习资料\MyQuantification\data\{0}.csv'.format(ts_code))
##