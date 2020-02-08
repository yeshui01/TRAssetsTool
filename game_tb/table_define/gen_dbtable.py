# -*- coding: utf-8 -*-

__author__ = 'mknight'

import json
import xlrd
import sys
import os.path
#import imp
#imp.reload(sys)

from db_table_des import *


def read_excel_table_describe(file_name, sheet_name, specified_table):
    worksheet = xlrd.open_workbook(file_name)
    sheet = worksheet.sheet_by_name(sheet_name)
    start_one_table = False
    des_table = None
    for row in range(sheet.nrows):
        # for col in range(sheet.ncols):
        if sheet.ncols < 2:
            continue

        if start_one_table == False:
            cell = sheet.cell(row, 0)
            des_str = str(cell.value)
            if des_str == 'table_begin':
                table_name = str(sheet.cell(row, 1).value)
                if specified_table != 'all_tables' and specified_table != table_name:
                    continue
                start_one_table = True
                #print('table_name = %s' % table_name)
                des_table = DBTableDes(table_name)
        else:
            cell = sheet.cell(row, 0)
            field_name = str(cell.value)
            if field_name != 'table_end':
                # field
                value_type = str(sheet.cell(row, 1).value)
                key_primary = False
                if sheet.ncols > 2:
                    key_str = str(sheet.cell(row, 2).value)
                    if key_str == 'key':
                        key_primary = True
                #print('filed_name:%s, value_type:%s' % (file_name, value_type))
                des_table.append_field(field_name, value_type, key_primary)

            else:
                # table des end
                des_table.gen_cpp_code()
                start_one_table = False
                des_table = None


if __name__ == "__main__":
    print("export dbtable code file")
    db_des = DBTableDes('test_tb')

    role_id_field = DBTableFieldDes("role_id", DbDataType.VAL_TYPE_BIG_INT,True)
    acc_id_field = DBTableFieldDes("acc_id", DbDataType.VAL_TYPE_BIG_INT, False)

    # print("test role_id_field:%s,%s" % (role_id_field.upper_field(), role_id_field.AaBbField))
    # db_des.append_field("role_id", DbDataType.VAL_TYPE_BIG_INT, True)
    # db_des.append_field("acc_id", DbDataType.VAL_TYPE_BIG_INT, False)
    # db_des.append_field("nickname", DbDataType.VAL_TYPE_STR, False)
    # db_des.gen_cpp_code()
    if len(sys.argv) > 1:
        run_param = sys.argv[1]
        print("run_param:%s" % run_param)
        # gen single specified table
        read_excel_table_describe('tr_game_table.xlsx', 'table_describe', run_param)
    else:
        # gen all tables
        read_excel_table_describe('tr_game_table.xlsx', 'table_describe', "all_tables")

    if os.path.isfile('./cpp_code/tb_role_base.h'):
        print('tb_role_base.h existed')
    else:
        print('not found file')
