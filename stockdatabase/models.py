from django.db import models

# Create your models here.


class StockBasic(models.Model):
    """
        获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
    """
    id = models.AutoField(primary_key=True)
    ts_code = models.CharField(max_length=150, unique=True)  # TS代码
    symbol = models.CharField(max_length=150,)  # 股票代码
    name = models.CharField(max_length=150)  # 股票名称
    area = models.CharField(max_length=150)  # 所在地域
    industry = models.CharField(max_length=150, )  # 所属行业
    fullname = models.CharField(max_length=150, )  # 股票全称
    enname = models.CharField(max_length=150, )  # 英文全称
    market = models.CharField(max_length=150, )  # 市场类型 （主板/中小板/创业板/科创板）
    exchange = models.CharField(max_length=150, )  # 交易所代码
    curr_type = models.CharField(max_length=100)  # 交易货币
    list_status = models.CharField(max_length=50, )  # 上市状态： L上市 D退市 P暂停上市
    list_date = models.CharField(max_length=150)  # 上市日期
    delist_date = models.CharField(max_length=150)  # 退市日期
    is_hs = models.CharField(max_length=50)  # 是否沪深港通标的，N否 H沪股通 S深股通


class HSConst(models.Model):
    """
        沪深股通成份股
    """
    id = models.AutoField(primary_key=True)
    ts_code = models.CharField(max_length=150, unique=True)  # TS代码
    hs_type = models.CharField(max_length=150)  # 沪深港通类型SH沪SZ深
    in_date = models.DateField()  # 纳入日期
    out_date = models.DateField()  # 剔除日期
    is_new = models.BooleanField()  # 是否最新 1是 0否


class Daily(models.Model):
    """
    日线行情
    """
    id = models.AutoField(primary_key=True)
    ts_code = models.CharField(max_length=150, unique=True)  # 股票代码
    trade_date = models.CharField(max_length=100)  # 交易日期
    open = models.FloatField()  # 开盘价
    high = models.FloatField()  # 最高价
    low = models.FloatField()  # 最低价
    close = models.FloatField()  # 收盘价
    pre_close = models.FloatField()  # 昨收价
    change = models.FloatField()  # 涨跌幅
    pct_chg = models.FloatField()  # 涨跌幅 （未复权）
    vol = models.FloatField()  # 交量（手）
    amount = models.FloatField()  # 成交额(千元)


class IndexBasic(models.Model):
    """
    指数基本信息
    """
    id = models.AutoField(primary_key=True)
    ts_code = models.CharField(max_length=150, )
    name = models.CharField(max_length=100)  # 简称
    fullname = models.CharField(max_length=100)  # 指数全称
    market = models.CharField(max_length=100)  # 市场
    publisher = models.CharField(max_length=100)  # 发布方
    index_type = models.CharField(max_length=100)  # 指数风格
    category = models.CharField(max_length=100)  # 指数类别
    base_date = models.CharField(max_length=100)  # 基期
    base_point = models.CharField(max_length=100)  # 基点
    list_date = models.CharField(max_length=100)  # 发布日期
    weight_rule = models.CharField(max_length=100)  # 加权方式
    desc = models.CharField(max_length=200)  # 描述
    exp_date = models.CharField(max_length=100)  # 终止日期

# 市场说明(market)
#
# 市场代码	说明
# MSCI	MSCI指数
# CSI	中证指数
# SSE	上交所指数
# SZSE	深交所指数
# CICC	中金所指数
# SW	申万指数
# OTH	其他指数


