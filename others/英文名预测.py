#  编码 UTF-8  #

'''''=================================================
@Project -> File   ：英文取名(ARIMA模型预测) -> MY_ARIMA
@IDE    ：PyCharm
@Author ：吴泽胜
@Date   ：2020/5/23 20:32
=================================================='''

import warnings
import itertools
import os
import gc
# 使用 matplotlib 的 scatter 方法绘制散点图
import matplotlib.pyplot as plt
# Pandas是一个强大的分析结构化数据的工具集；它的使用基础是Numpy（提供高性能的矩阵运算）；用于数据挖掘和数据分析，同时也提供数据清洗功能。
import pandas as pd
# 提供高性能的矩阵运算
import numpy as np
# 自相关函数的库 ACF 和 PACF
import statsmodels.api as sm
# matplotlib绘图
import matplotlib
import matplotlib.dates as mdate
from pylab import rcParams
from statsmodels.graphics.gofplots import qqplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

warnings.filterwarnings("ignore")  # 忽略警告
plt.style.use('fivethirtyeight')  # 定义matplotlib风格 。

# 设置matplotlib对象自定义图形的各种默认属性
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

''''' 
    自回归移动平均模型（ARIMA） 
    该python文件核心函数 
'''


def MY_ARIMA(train_data):
    # 拆分法，检验序数据的稳定性
    # 一阶差分图  t 与 t-1 时刻的差值
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(111)
    # .diff(1) 差分间隔为1个单位 例如 2001年 - 2000年  的数据
    diff1 = train_data.diff(1)
    diff1.plot(ax=ax1)

    # 做acf和pacf图   自相关函数acf的Pk的取值范围[-1,1]    偏自相关函数pacf
    dta1 = train_data.diff(1)
    # 差分的数据记得使用dropna方法去掉空值，否则acf和pacf图很可能出不来
    dta2 = dta1.dropna()
    # 显示 acf 和 pacf 图
    fig = plt.figure(figsize=(12, 8))
    # 此处为20 acf图，lags为滞后阶数
    ax1 = fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(dta2, ax=ax1)
    # pacf 图片
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(dta2, ax=ax2)

    # 暴力测试pdq的最佳搭配值，此方法不是最优解，但是也是一种办法。
    # evaluate parameters
    p_values = d_values = q_values = range(0, 2)
    # 忽略警告
    warnings.filterwarnings("ignore")
    # 调用 evaluate_models 方法，获取最优p,d,q值
    # 均方根
    best_cfg = evaluate_models(train_data.values, p_values, d_values, q_values)
    # 预测模型
    arma_mod20 = sm.tsa.statespace.SARIMAX(train_data,
                                           order=(best_cfg[0], best_cfg[1], best_cfg[2]),
                                           seasonal_order=(1, 1, 0, 12),
                                           enforce_stationarity=False,
                                           enforce_invertibility=False
                                           ).fit()

    arma_mod20.plot_diagnostics(figsize=(16, 8))
    print(arma_mod20.summary().tables[1])

    # 对模型进行检验
    # pred = arma_mod20.get_prediction(start=pd.to_datetime('2013-12-31'), dynamic=False)     #预测值
    # pred_ci = pred.conf_int()   #置信区间
    # # print(pred_ci)
    # ax = train_data['2000':].plot(label='observed')
    # pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(14, 7))
    #
    # ax.fill_between(pred_ci.index,
    #                 pred_ci.iloc[:, 0],
    #                 pred_ci.iloc[:, 1], color='k', alpha=.2)
    #
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Number Of Users')
    # plt.legend()
    # plt.show()

    # arma_mod20 = sm.tsa.ARIMA(train_data, order=(2,0,0)).fit()
    # 输出 AIC：赤池信息准则     BIC：贝叶斯信息准则
    print(arma_mod20.aic, arma_mod20.bic, arma_mod20.hqic)
    # 预测 2019-2024 包区间的使用人数
    predict_sunspots = arma_mod20.predict('2019', '2024', dynamic=True)
    # 预测模型并作图
    fig, ax = plt.subplots(figsize=(12, 8))
    ax = train_data.loc['1979':].plot(ax=ax)
    predict_sunspots.plot(ax=ax)
    plt.show()

    # 返回预测数据
    # 返回的数据进行过滤
    for item_data_index in range(len(predict_sunspots)):
        if predict_sunspots[item_data_index] > 0:
            predict_sunspots[item_data_index] = int(round(predict_sunspots[item_data_index], 0))
            predict_sunspots[item_data_index] = str(predict_sunspots[item_data_index])[0:-2]
        else:
            predict_sunspots[item_data_index] = '0'

    return predict_sunspots


# 寻找最优解pdq组合搭配
# evaluate combinations of p, d and q values for an ARIMA model
def evaluate_models(dataset, p_values, d_values, q_values):
    dataset = dataset.astype('float32')
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p, d, q)
                try:
                    mse = evaluate_arima_model(dataset, order)
                    if mse < best_score:
                        best_score, best_cfg = mse, order
                    print('ARIMA%s MSE=%.3f' % (order, mse))
                except:
                    continue
    print('Best ARIMA%s MSE=%.3f' % (best_cfg, best_score))
    # 返回最优解 p,d,q
    return best_cfg


# evaluate an ARIMA model for a given order (p,d,q)
def evaluate_arima_model(X, arima_order):
    # prepare training dataset
    train_size = int(len(X) * 0.66)
    train, test = X[0:train_size], X[train_size:]
    history = [x for x in train]
    # make predictions
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=arima_order)
        model_fit = model.fit(disp=0)
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test[t])
        # calculate out of sample error
    error = mean_squared_error(test, predictions)
    return error


''''' 
    写入文件函数 
    train_data： 1880-2018数据 
    Forecast_Array_Number： 预测后五年的数据 
    Name： 该组数据的名字 
    Rank_Array： 该组数据每年的排名 
    row_index： 该组数据坐在 CSV 的序号（行数） 
'''


def Write_Data(train_data, Forecast_Array_Number, Name, Rank_Array, row_index, Gender):
    train_data = train_data.astype('int32')
    First_Name = Name[0]
    Impot_File_Txt_Path = 'txt' + First_Name + '/'
    Impot_File_Txt_Name = Name + '.txt'
    file_path = Impot_File_Txt_Path + Impot_File_Txt_Name

    # 创建目录
    if os.path.exists(Impot_File_Txt_Path):
        pass
    else:
        os.mkdir(Impot_File_Txt_Path)

        # 创建文件
    if os.path.exists(file_path):
        print("文件： " + file_path + " 已经存在")
        File_Txt_Data = []
        with open(file_path, mode='r', encoding='utf-8') as File_Txt:
            File_Txt_Data = File_Txt.readlines()

            # F
        if (Gender == 'F'):
            # 先前数据导入txt文件
            for index in range(1, 140):
                item = File_Txt_Data[index].split(',')
                item[1] = str(train_data[index - 1])
                item[3] = str(Rank_Array[index - 1][row_index].astype('int32'))
                str_ = ""
                for item_ in item:
                    str_ = str_ + item_ + ','
                File_Txt_Data[index] = str_[0:-1]
                # 预测数据导入txt文件
            i = 0
            for index in range(140, 146):
                item = File_Txt_Data[index].split(',')
                print(Forecast_Array_Number[i])
                item[1] = str(Forecast_Array_Number[i])[0:-2]
                str_ = ""
                for item_ in item:
                    str_ = str_ + str(item_) + ','
                File_Txt_Data[index] = str_[0:-1]
                i = i + 1
                # M
        else:
            # 先前数据导入txt文件
            for index in range(1, 140):
                item = File_Txt_Data[index].split(',')
                item[2] = str(train_data[index - 1])
                item[4] = str(Rank_Array[index - 1][row_index].astype('int32'))
                str_ = ""
                for item_ in item:
                    str_ = str_ + item_ + ','
                File_Txt_Data[index] = str_[0:-1] + '\n'
                # 预测数据导入txt文件
            i = 0
            for index in range(140, 146):
                item = File_Txt_Data[index].split(',')
                print(Forecast_Array_Number[i])
                item[2] = str(Forecast_Array_Number[i])[0:-2]
                str_ = ""
                for item_ in item:
                    str_ = str_ + str(item_) + ','
                File_Txt_Data[index] = str_[0:-1]
                i = i + 1
        with open(file_path, mode='w', encoding='utf-8') as File_Txt:
            for item_ in File_Txt_Data:
                File_Txt.write(item_)

                # 没有同名文件
    else:
        print("成功创建文件： " + file_path)
        with open(file_path, mode='w', encoding='utf-8') as File_Txt:
            # 创建写入对象
            File_Txt.write('BirthYear, F, M, Frank, Mrank' + '\n')
            # 男性 M
            if (Gender == 'M'):
                # 先前数据导入txt文件
                for item_data_index in range(len(train_data)):
                    item_data = train_data[item_data_index]
                    File_Txt.write(
                        str(Year_Number[item_data_index]) + ',' + '0' + ',' + str(item_data) + ',' + '0' + ',' + str(
                            Rank_Array[item_data_index][row_index].astype('int32')) + '\n')
                    # 预测数据导入txt文件
                for item_data_index in range(len(Forecast_Array_Number)):
                    File_Txt.write(
                        str(Forecast_Year_Number[item_data_index]) + ',' + '0' + ',' + str(
                            Forecast_Array_Number[item_data_index])[0:-2] + ',' + '0' + ',' + '0' + '\n')
                    # 女性 F
            else:
                # 先前数据导入txt文件
                for item_data_index in range(len(train_data)):
                    item_data = train_data[item_data_index]
                    File_Txt.write(str(Year_Number[item_data_index]) + ',' + str(item_data) + ',' + '0' + ',' + str(
                        Rank_Array[item_data_index][row_index].astype('int32')) + ',0\n')
                    # 预测数据导入txt文件
                for item_data_index in range(len(Forecast_Array_Number)):
                    File_Txt.write(
                        str(Forecast_Year_Number[item_data_index]) + ',' + str(Forecast_Array_Number[item_data_index])[
                                                                           0:-2] + ',' + '0' + ',' + '0' + ',' + '0' + '\n')
    File_Txt.close()


def Error_Write_Data(train_data, Forecast_Array_Number, Name, Rank_Array, row_index, Gender):
    train_data = train_data.astype('int32')
    First_Name = Name[0]
    Impot_File_Txt_Path = 'txt' + First_Name + '/'
    Impot_File_Txt_Name = Name + '.txt'
    file_path = Impot_File_Txt_Path + Impot_File_Txt_Name

    # 创建目录
    if os.path.exists(Impot_File_Txt_Path):
        pass
    else:
        os.mkdir(Impot_File_Txt_Path)

        # 创建文件
    if os.path.exists(file_path):
        print("文件： " + file_path + " 已经存在")
        File_Txt_Data = []
        with open(file_path, mode='r', encoding='utf-8') as File_Txt:
            File_Txt_Data = File_Txt.readlines()

            # F
        if (Gender == 'F'):
            # 先前数据导入txt文件
            for index in range(1, 139):
                item = File_Txt_Data[index].split(',')
                item[1] = str(train_data[index])
                item[3] = str(Rank_Array[index][row_index].astype('int32'))
                str_ = ""
                for item_ in item:
                    str_ = str_ + item_ + ','
                File_Txt_Data[index] = str_[0:-1]
                # 预测数据导入txt文件
            i = 0
            for index in range(139, 145):
                item = File_Txt_Data[index].split(',')
                item[1] = '0'
                str_ = ""
                for item_ in item:
                    str_ = str_ + str(item_) + ','
                File_Txt_Data[index] = str_[0:-1]
                i = i + 1
                # M
        else:
            # 先前数据导入txt文件
            for index in range(1, 139):
                item = File_Txt_Data[index].split(',')
                item[2] = str(train_data[index])
                item[4] = str(Rank_Array[index][row_index].astype('int32'))
                str_ = ""
                for item_ in item:
                    str_ = str_ + item_ + ','
                File_Txt_Data[index] = str_[0:-1] + '\n'
                # 预测数据导入txt文件
            i = 0
            for index in range(139, 145):
                item = File_Txt_Data[index].split(',')
                item[2] = '0'
                str_ = ""
                for item_ in item:
                    str_ = str_ + str(item_) + ','
                File_Txt_Data[index] = str_[0:-1]
                i = i + 1
        with open(file_path, mode='w', encoding='utf-8') as File_Txt:
            for item_ in File_Txt_Data:
                File_Txt.write(item_)

                # 没有同名文件
    else:
        print("成功创建文件： " + file_path)
        with open(file_path, mode='w', encoding='utf-8') as File_Txt:
            # 创建写入对象
            File_Txt.write('BirthYear, F, M, Frank, Mrank' + '\n')
            # 男性 M
            if (Gender == 'M'):
                # 先前数据导入txt文件
                for item_data_index in range(len(train_data)):
                    item_data = train_data[item_data_index]
                    File_Txt.write(
                        str(Year_Number[item_data_index]) + ',' + '0' + ',' + str(item_data) + ',' + '0' + ',' + str(
                            Rank_Array[item_data_index][row_index].astype('int32')) + '\n')
                    # 预测数据导入txt文件
                for item_data_index in range(len(Forecast_Array_Number)):
                    File_Txt.write(
                        str(Forecast_Year_Number[
                                item_data_index]) + ',' + '0' + ',' + '0' + ',' + '0' + ',' + '0' + '\n')
                    # 女性 F
            else:
                # 先前数据导入txt文件
                for item_data_index in range(len(train_data)):
                    item_data = train_data[item_data_index]
                    File_Txt.write(str(Year_Number[item_data_index]) + ',' + str(item_data) + ',' + '0' + ',' + str(
                        Rank_Array[item_data_index][row_index].astype('int32')) + ',0\n')
                    # 预测数据导入txt文件
                for item_data_index in range(len(Forecast_Array_Number)):
                    File_Txt.write(str(
                        Forecast_Year_Number[item_data_index]) + ',' + '0' + ',' + '0' + ',' + '0' + ',' + '0' + '\n')
    File_Txt.close()


def Process_Information(row_index):
    print(' ****************************************')
    print()
    print("         运行第 %d 组数据中..." % (row_index + 1))
    print()
    print(' ****************************************')


''''' 
    程序入口，在df流中，遍历获取每组数据 
    数据准备与预处理 

'''
# 创建导入数据对象
df = pd.read_csv("year_of_birth_counts-2018.csv")  # 相对路径Babyname-1880-2018

# 数据年份
Year_Number = []
# 预测年份
Forecast_Year_Number = ['2019', '2020', '2021', '2022', '2023', '2024']
# 年份人数排序
# 男 Male Rank
Rank_Array_M = []
# 女 Female Rank
Rank_Array_F = []
# 过滤每年的男女人数
df_M = df[df["Gender"] != 'F']
df_F = df[df["Gender"] != 'M']
# 写入 1979-2018年 四十年
for item in range(1880, 2019):
    Year_Number.append(str(item))
# 写入排序 M
for item in Year_Number:
    my_df = df_M[item].rank(ascending=0, method='first')
    Rank_Array_M.append(my_df)
# 写入排序 F
for item in Year_Number:
    my_df = df_F[item].rank(ascending=0, method='first')
    Rank_Array_F.append(my_df)
# 遍历每一条数据
for row_index, row in df.iterrows():
    # 异常处理
    try:
        # 打印运行位置
        Process_Information(row_index)
        # 记录性别
        Gender = row[1:2][0]
        # 选择性别排名 三元运算
        Rank_Array = Rank_Array_M if Gender == 'M' else Rank_Array_F
        # 将DataFrame数据转为list
        train_data = np.array(row).tolist()
        # 传值 单条1880-2018年所有数据
        train_data_all = train_data
        train_data_all = pd.Series(train_data_all[2:])
        # 将list数据转为Series 取1979年
        train_data = pd.Series(train_data[101:])
        # ARIMA学习所用的数据是单精度型数据
        train_data = train_data.astype('float32')
        # x轴年份 1880-2018
        train_data.index = pd.Index(sm.tsa.datetools.dates_from_range(start='1979', end='2018', length=0))
        # 设置面板大小
        train_data.plot(figsize=(16, 6))
        # 改变图标题字体,标题设置
        plt.title(str(row[0:1]), fontdict={'weight': 'normal', 'size': 20})
        # 对于测试ARIMA方法调用
        Forecast_Array_Number = MY_ARIMA(train_data)
        # 打印预测 2019年 - 2024年 的预测值
        print(Forecast_Array_Number)
        # 将处理好的数据，写入设计好的文档（txt）
        Write_Data(train_data_all, Forecast_Array_Number, str(row[0:1][0]), Rank_Array, row_index, Gender)
    except:
        # 打印错误的名字
        print("%s 运行错误：" % str(row[0:1][0]))
        # 错误信息写入    将处理好的数据，写入设计好的文档（txt）
        Error_Write_Data(train_data_all, Forecast_Array_Number, str(row[0:1][0]), Rank_Array, row_index, Gender)
        pass
        # 释放内存
    gc.collect()
    continue

''''' 
    Tit = 总迭代次数 
    Tnf = 功能评估总数 
    Tnint = 在Cauchy搜索期间探索的段总数 
    Skip = 跳过的 BFGS 更新数 
    Nact = 最终广义Cauchy点的有效界数 
    Projg = 最终投影坡度的范数 
    F = 最终功能值 
'''
