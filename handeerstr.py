# -*- coding: utf-8 -*-
# @createTime    : 2019/5/17 13:54
# @author  : Huanglg
# @fileName: handeerstr.py
# @email: luguang.huang@mabotech.com
str = """零 件 名 : CRH3 系 列 电 机 吊 架 返 修 - 焊 后 检 测 日 期 | 2014.10.30
lll } 兰
测 试 报 告
修 订 号 : 部 件 号 201507 操 作 者
FCF同轴度1‖ 毫 米 [ © goos _| A ]
特 征 NOMINAL ___ +TOL -TOL MEAS Dev OUtTToL BONUS
柱 体 2 0.000 0.030 0.410 0.410 0.380 Pe
FCF同轴度2‖ 毫 木 [ © [Foos _| a ]
特 征 NOMINAL ___ +TOL TOL MEAS Dev OUtTToL BONUS
柱 体 4 0.000 0.030 0.520 0.520 0.490 Pe
ag Is Le Fon To]
特 征 NOMINAL ___ +TOL -TOL MEAS Dev OUtTToL BONUS
柱 体 2 0.000 0.030 0.017 0.017 0.000 | , , , 不 画 画 盯
FCFR 轴 庞 弓 " 毫 米 [L@ oos_Lc ]
特 征 NOMINAL ___ +TOL -TOL MEAS Dev OUtTToL BONUS
柱 体 1 0.000 0.030 0.019 0.019 0.000 Coorg --I
ma] ¢ [& Foos To]
特 征 NOMINAL ___ +TOL TOL MEAS Dev OUtTToL BONUS
柱 体 3 0.000 0.030 0.011 0.011 0.000 用 园 国 一
R 矿 Le For To)
特 征 NOMINAL ___ +TOL ToL MEAS Dev OUtTToL BONUS
柱 体 4 0.000 0.030 0.031 0.031 0.001 Pe
# | 毫米 位 置 2 - 柱 体 2
AX NOMINAL +TOL -TOL MEAS DEV OuTToL
x 0.127 0.050 -0.050 0.002 -0.129 -0.079 i
Z -95.500 0.050 -0.050 -95.179 0.321 0.271 mom ___ :
D 60.000 0.050 0.050 62.485 2.485 2.435 -- -- RM
# | 毫米 位 置 1 - 柱 体 !
AX NOMINAL +TOL -TOL MEAS DEV OuTToL
x 0.127 0.050 -0.050 -0.101 -0.228 -0.178 i
Z -95.500 0.050 -0.050 -95.160 0.340 0.290 --- RM
D 60.000 0.050 0.050 62.499 2.499 2.449 [ -- RM
# | 毫米 倍 置 3 - 柱 体 3
AX NOMINAL +TOL -TOL MEAS DEV OuTToL
Y 0.000 0.050 -0.050 -0.028 -0.028 0.000 J .
2 -95.500 0.050 -0.050 -95.118 0.382 0.332 --- mM
D 60.000 0.050 -0.050 62.492 2.492 2.442 [ 一 和 命 国 酥
"""

import re

str = re.sub(u"\\[.*?]", "", str)
result = str.replace("©", '').replace("lll", '').replace("兰", '').replace("|", '').replace("_", '').replace("[",'').replace("}", '').replace("‖", '').replace("OUtTToL", 'OUTTOL').replace("Pe",'')

print(result)
