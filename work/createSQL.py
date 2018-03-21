#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

fileName = "/Users/xzy/Desktop/xzy/changeIdSQL.txt"  # 文件路径可以修改


def fn_changeidsql():
    with open(fileName, 'w') as f:
        for i in range(len(x)):
            f.write("update cabinet_user set user_id = " + str(y[i]) + " where user_id = " + str(x[i]))

        for i in range(len(x)):
            f.write("update company_certification set user_id = " + str(y[i]) + " where user_id = " + str(x[i]))

        for i in range(len(x)):
            f.write("update contract set signature_user_id = " + str(y[i]) + " where signature_user_id = " + str(x[i]))

        for i in range(len(x)):
            f.write("update pay_bill set pay_user_id = " + str(y[i]) + " where pay_user_id = " + str(x[i]))

        for i in range(len(x)):
            f.write("update receipt_application set apply_user_id = " + str(y[i]) + " where apply_user_id = " + str(x[i]))

        for i in range(len(x)):
            f.write("update station_order set book_user_id = " + str(y[i]) + " and operation_book_user_id = " + str(
                  y[i]) + " and manual_change_user_id = " + str(y[i]) + " where book_user_id = " + str(x[i]))

        for i in range(len(x)):
            f.write("update station_status_info set book_user_id = " + str(y[i]) + " where book_user_id = " + str(x[i]))

        for i in range(len(x)):
             f.write("update station_user set user_id = " + str(y[i]) + " where user_id = " + str(x[i]))

        for i in range(len(x)):
             f.write("update station_user_history set user_id = " + str(y[i]) + " where user_id = " + str(x[i]))

        for i in range(len(x)):
             f.write("update visit_application set applier_user_id = " + str(y[i]) + " and process_user_id = " + str(
                  y[i]) + " where applier_user_id = " + str(x[i]))

# id订正


x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 17, 18, 19, 20, 21, 22, 25, 26, 28, 31, 34, 35, 36, 38, 41, 42, 43, 51, 56,
     61, 70, 71, 73, 74, 75, 76, 77, 78, 85, 104, 138, 147, 153, 156, 159, 162, 177, 191, 193, 194, 196, 206, 226, 232,
     237, 239, 243, 248, 280, 285, 302, 304, 305, 327, 328, 335, 336, 345, 366, 370, 372, 375, 387, 388, 395, 410, 440,
     455, 456, 458, 459, 494, 514, 529, 543, 576, 608, 619, 620, 633, 638, 660, 688, 700, 705, 710, 712, 714, 718, 719,
     727, 743, 752, 753, 757, 777, 781, 793, 804, 805, 815, 828, 835, 838, 849, 858, 862, 863, 881, 884, 888, 897, 898,
     901, 966, 970, 1012, 1020, 1035, 1036, 1037, 1038, 1065, 1073, 1080, 1098, 1105, 1111, 1139, 1140, 1160, 1177,
     1182, 1281, 1346, 1365, 1414, 1415, 1418, 1427, 1428, 1432, 1439, 1440, 1449, 1455, 1493, 1504, 1510, 1632, 1641,
     1645, 1646, 1671, 1692, 1694, 1699, 1701, 1803, 1843, 1891, 1951, 2044, 2113, 2161, 2162, 2213, 2222, 2293, 2295,
     2309, 2325, 2326, 2350, 2422, 2425, 2514, 2551, 2556, 2569, 2584, 2606, 2630, 2634, 2648, 2660, 2686, 2764, 2765,
     2833, 2834, 2838, 2882, 2912, 2924, 2998, 3000, 3063, 3074, 3122, 3135, 3147, 3149, 3151, 3158, 3161, 3176, 3214,
     3270, 3313, 3328, 3364, 3399, 3401, 3406, 3430, 3431, 3432, 3439, 3476, 3534, 3593, 3631, 3635, 3640, 3651, 3670,
     3709, 3716, 3725, 3732, 3763, 3803, 3810, 3850, 3852, 3879, 3880, 3938, 4039, 4042, 4049, 4052, 4101, 4110, 4121,
     4124, 4137, 4141, 4160, 4190, 4197, 4198, 4199, 4205, 4208, 4230, 4238, 4261, 4262, 4271, 4283, 4285, 4286, 4304,
     4306, 4315, 4325, 4337, 4383, 4400, 4431, 4512, 4524, 4568, 4570, 4592, 4594, 4611, 4612, 4617, 4618, 4621, 4626,
     4638, 4659, 4675, 4692, 4700, 4701, 4702, 4715, 4722, 4734, 4738, 4746, 4752, 4813, 4865, 4866, 4878, 4887, 4907,
     4946, 4947, 4979, 5003, 1200006, 1200040, 1200053, 1200081, 1200082, 1200083, 1200087, 1200095, 963359, 965132,
     962808, 865955, 955929, 895493, 964404, 963071, 972087, 909765, 1067779, 1200100, 1200101, 1200102, 1200103,
     1200105]

y = [859007,
     902953,
     859019,
     902949,
     859000,
     859001,
     846752,
     941395,
     876654,
     904735,
     934892,
     902952,
     951629,
     843439,
     934651,
     880807,
     853364,
     859004,
     869976,
     848605,
     904008,
     857626,
     933817,
     902972,
     859008,
     904294,
     846984,
     859017,
     903051,
     869311,
     885034,
     867267,
     853339,
     960079,
     854837,
     850972,
     859709,
     854996,
     846352,
     846350,
     911499,
     902948,
     930566,
     847442,
     856195,
     858042,
     851860,
     851784,
     890926,
     881322,
     842776,
     974504,
     871700,
     859009,
     905417,
     889571,
     859023,
     1066131,
     861232,
     889572,
     845727,
     890679,
     858710,
     854147,
     869981,
     854494,
     856179,
     867010,
     866730,
     856185,
     853361,
     930568,
     861236,
     902950,
     856184,
     843200,
     930889,
     856712,
     880803,
     858380,
     847441,
     933923,
     903996,
     853359,
     902935,
     934893,
     854882,
     858992,
     843437,
     853343,
     856865,
     854855,
     845683,
     854880,
     869809,
     854998,
     854861,
     845679,
     851095,
     850980,
     851033,
     851076,
     854866,
     850971,
     879899,
     853366,
     854838,
     851194,
     851116,
     845975,
     868209,
     854864,
     930405,
     853341,
     854839,
     854859,
     854847,
     854873,
     851015,
     854836,
     902206,
     851086,
     854881,
     854835,
     851073,
     846450,
     854871,
     846521,
     904669,
     851044,
     930567,
     926876,
     845766,
     854841,
     854867,
     930406,
     869984,
     850942,
     902211,
     902212,
     854884,
     850943,
     851014,
     845694,
     902218,
     854878,
     854862,
     851080,
     853379,
     853377,
     853385,
     866014,
     866243,
     952501,
     866012,
     853350,
     854856,
     971116,
     853358,
     853368,
     902217,
     865940,
     875406,
     853387,
     853376,
     845676,
     850609,
     865938,
     865937,
     865941,
     976186,
     1066215,
     926874,
     870096,
     865942,
     977245,
     853352,
     853355,
     902226,
     853383,
     858411,
     847190,
     847189,
     933918,
     917358,
     853381,
     850707,
     854875,
     854854,
     854874,
     865932,
     853382,
     904672,
     854877,
     904671,
     866780,
     854850,
     870050,
     932311,
     858322,
     846349,
     867885,
     952066,
     903258,
     854879,
     865954,
     845677,
     851013,
     927111,
     854872,
     875203,
     931614,
     846776,
     854705,
     852961,
     865966,
     846819,
     869043,
     865963,
     853349,
     853362,
     853367,
     903259,
     853344,
     880936,
     888610,
     853374,
     853372,
     853375,
     853370,
     854870,
     871698,
     870095,
     853389,
     865953,
     853380,
     853388,
     927913,
     853371,
     855020,
     999491,
     858410,
     896751,
     853378,
     849980,
     876795,
     897346,
     853373,
     930858,
     856788,
     843808,
     865965,
     859416,
     854858,
     856789,
     865955,
     855029,
     848828,
     864695,
     967127,
     912094,
     935953,
     937073,
     851046,
     850973,
     851103,
     912548,
     864011,
     901177,
     864782,
     912566,
     962828,
     849077,
     848962,
     853347,
     853354,
     929158,
     864783,
     879592,
     963147,
     859189,
     870102,
     863774,
     845219,
     942182,
     854974,
     941295,
     859193,
     902241,
     914511,
     845692,
     849286,
     859708,
     902242,
     902243,
     846407,
     925158,
     854999,
     859338,
     854978,
     845693,
     870094,
     854972,
     962756,
     854973,
     967128,
     847021,
     270931,
     845370,
     957895,
     904159,
     845224,
     896096,
     859432,
     890026,
     854887,
     893661,
     939200,
     955745,
     962826,
     866013,
     850668,
     931850,
     863076,
     904556,
     865933,
     962469,
     1082344,
     1082346,
     1082342,
     1082338,
     1082341,
     1082339,
     1082345,
     1082343,
     1082348,
     1082340,
     1082350,
     962490,
     962491,
     962516,
     962518,
     962523]

# | cabinet_user                   |user_id
# | company_certification          |user_id
# | contract                       |signature_user_id
# | pay_bill                       |pay_user_id
# | receipt_application            |apply_user_id
# | station_order                  |book_user_id operation_book_user_id  manual_change_user_id
# | station_status_info            |book_user_id
# | station_user                   |user_id
# | station_user_history           |user_id
# | visit_application              |applier_user_id  process_user_id
for i in range(len(x)):
    print("update cabinet_user set user_id = " + str(y[i]) + " where user_id = " + str(x[i]))

for i in range(len(x)):
    print("update company_certification set user_id = " + str(y[i]) + " where user_id = " + str(x[i]))

for i in range(len(x)):
    print("update contract set signature_user_id = " + str(y[i]) + " where signature_user_id = " + str(x[i]))

for i in range(len(x)):
    print("update pay_bill set pay_user_id = " + str(y[i]) + " where pay_user_id = " + str(x[i]))

for i in range(len(x)):
    print("update receipt_application set apply_user_id = " + str(y[i]) + " where apply_user_id = " + str(x[i]))

for i in range(len(x)):
    print("update station_order set book_user_id = " + str(y[i]) + " and operation_book_user_id = " + str(y[i]) + " and manual_change_user_id = " + str(y[i]) + " where book_user_id = " + str(x[i]))

for i in range(len(x)):
    print("update station_status_info set book_user_id = " + str(y[i]) + " where book_user_id = " + str(x[i]))

for i in range(len(x)):
    print("update station_user set user_id = " + str(y[i]) + " where user_id = " + str(x[i]))

for i in range(len(x)):
    print("update station_user_history set user_id = " + str(y[i]) + " where user_id = " + str(x[i]))

for i in range(len(x)):
    print("update visit_application set applier_user_id = " + str(y[i]) + " and process_user_id = " + str(y[i]) + " where applier_user_id = " + str(x[i]))

# 生成并把SQL保存到文件

fn_changeidsql()

print("end")