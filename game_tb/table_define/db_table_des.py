# -*- coding: utf-8 -*-

__author__ = 'mknight'

import time
import os
# cpp文件的路径
cpp_file_path = './cpp_code'

# 常用数据类型
class DbDataType(object):
    VAL_TYPE_BIG_INT = 'bigint'
    VAL_TYPE_INT = 'int'
    VAL_TYPE_STR = 'string'
    cpp_type_dic = {"bigint": "int64_t", "int": "int32_t",
                    "string": "std::string"}

# 字段描述
class DBTableFieldDes(object):
    def __init__(self, field_name, value_type, primary_key):
        self.field_name = field_name
        self.value_type = value_type
        self.primary_key = primary_key
        # field_name分割格式化
        field_word_str = field_name.split("_")
        self.AaBbField = ""
        for word in field_word_str:
            self.AaBbField = self.AaBbField + word.capitalize()
        '''
        self.AABBField = ""
        for word in field_word_str:
            self.AABBField = self.AABBField + word.upper()
        '''

    def upper_field(self):
        return self.field_name.upper()


# 数据表描述
class DBTableDes(object):
    def __init__(self, tb_name):
        self.table_name = tb_name
        self.field_list = []
        name_word_str = tb_name.split("_")
        self.AaBbName = ""
        for word in name_word_str:
            self.AaBbName = self.AaBbName + word.capitalize()
        self.AABBName = ""
        for word in name_word_str:
            self.AABBName = self.AABBName + word.upper()
        self.custom_code_dic = {}
        for i in range(1, 5):
            self.custom_code_dic[i] = []



    def append_field(self, field_name, value_type, primary_key):
        one_field = DBTableFieldDes(field_name, value_type, primary_key)
        self.field_list.append(one_field)

    def upper_table_name(self):
        return self.table_name.upper()

    def load_custom_code(self):

        hfile = "%s/tb_%s.h" % (cpp_file_path, self.table_name)
        if os.path.isfile(hfile):
            # 文件存在
            print('load custom code hfile')
            start_custom = False
            custom_code_index = 0
            with open(hfile, 'r') as f:
                one_line = f.readline()
                while len(one_line) > 0:
                    if start_custom == False:
                        if one_line.find('custom code_1 begin') != -1:
                            start_custom = True
                            custom_code_index = 1
                        elif one_line.find('custom code_2 begin') != -1:
                            start_custom = True
                            custom_code_index = 2
                    else:
                        if one_line.find('custom code') == -1:
                            self.custom_code_dic[custom_code_index].append(one_line)
                            print("custom_code:%s,%s" % (custom_code_index, one_line))
                        else:
                            start_custom = False
                            custom_code_index = 0
                    one_line = f.readline()

        start_custom = False
        custom_code_index = 0
        cppfile = "%s/tb_%s.cpp" % (cpp_file_path, self.table_name)
        if os.path.isfile(cppfile):
            # 文件存在
            print('load custom code cppfile')
            start_custom = False
            custom_code_index = 0
            with open(cppfile, 'r') as f:
                one_line = f.readline()
                while len(one_line) > 0:
                    if start_custom == False:
                        if one_line.find('custom code_3 begin') != -1:
                            start_custom = True
                            custom_code_index = 3
                        elif one_line.find('custom code_4 begin') != -1:
                            start_custom = True
                            custom_code_index = 4
                    else:
                        if one_line.find('custom code') == -1:
                            self.custom_code_dic[custom_code_index].append(one_line)
                            print("custom_code_%d,%s" % (custom_code_index, one_line))
                        else:
                            start_custom = False
                            custom_code_index = 0
                    one_line = f.readline()

    def gen_cpp_code(self):
        self.load_custom_code()
        print("gen cpp table code, tbname:%s" % (self.table_name))
        with open("%s/tb_%s.h" % (cpp_file_path, self.table_name), "w") as f :
            date_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write('// this file created by gen_dbtable.py script at %s\n\n' % date_time_str)
            hdefine = "#ifndef __TB_%s_H__\n#define __TB_%s_H__\n\n" % (self.table_name.upper(), self.table_name.upper())
            f.write(hdefine)
            f.write('// --------- custom code_1 begin --------\n')
            if 1 in self.custom_code_dic:
                for custom_line in self.custom_code_dic[1]:
                    f.write('%s' % custom_line)
            f.write('// --------- custom code_1 end ----------\n\n')
            f.write("enum ETb%sField\n" % self.AaBbName)
            f.write('{\n')
            # field enum
            for one_field in self.field_list:
                print(one_field.field_name)
                f.write("\tE_TB_%s_FLD_%s,\n" % (self.AABBName, one_field.upper_field()))
            f.write('\tE_TB_%s_FLD_END\n')
            f.write('};\n\n')
            # class
            f.write('class Tb%s : public DataTableBase\n' % self.AaBbName)
            f.write("{\n")
            f.write('public:\n')
            f.write('\tTb%s(int32_t table_id);\n' % self.AaBbName)
            f.write('\t~Tb%s();\n' % self.AaBbName)
            f.write('public:\n')
            for one_field in self.field_list:
                cpp_type = DbDataType.cpp_type_dic[one_field.value_type]
                f.write('\t// %s\n' % one_field.field_name)

                for i in range(1, 3):
                    if i == 1:
                        f.write('\t%s Get%s()\n' % (cpp_type, one_field.AaBbField))
                    else:
                        f.write('\t%s Get%s() const\n' % (cpp_type, one_field.AaBbField))
                    f.write('\t{\n')
                    fun_code = ""
                    if cpp_type == "int64_t":
                        fun_code = 'GetFieldBigIntValue(E_TB_%s_FLD_%s)\n' % (self.AABBName, one_field.upper_field())
                    elif cpp_type == "int32_t":
                        fun_code = 'GetFieldIntValue(E_TB_%s_FLD_%s)\n' % (self.AABBName, one_field.upper_field())
                    elif cpp_type == "std::string":
                        fun_code = 'GetFieldStringValue(E_TB_%s_FLD_%s)\n' % (self.AABBName, one_field.upper_field())

                    f.write('\t\treturn %s' % fun_code)
                    f.write('\t}\n')

                f.write('\tvoid Set%s(%s %s)\n' % (one_field.AaBbField, cpp_type, one_field.field_name))
                f.write('\t{\n')
                fun_write_code = ""
                if cpp_type == "int64_t":
                    fun_write_code = 'SetFieldBigIntValue(E_TB_%s_FLD_%s, %s)\n' % (self.AABBName, one_field.upper_field(), one_field.field_name)
                elif cpp_type == "int32_t":
                    fun_write_code = 'SetFieldIntValue(E_TB_%s_FLD_%s, %s)\n' % (self.AABBName, one_field.upper_field(), one_field.field_name)
                elif cpp_type == "std::string":
                    fun_write_code = 'SetFieldStringValue(E_TB_%s_FLD_%s, %s.c_str(), %s.size())\n' % (\
                    self.AABBName, one_field.upper_field(), one_field.field_name, one_field.field_name)

                f.write('\t\t%s' % fun_write_code)
                f.write('\t}\n')

            f.write('// --------- custom code_2 begin --------\n')
            if 2 in self.custom_code_dic:
                for custom_line in self.custom_code_dic[2]:
                    f.write('%s' % custom_line)
            f.write('// --------- custom code_2 end ----------\n')
            f.write('};\n\n')
            hdefine_end = "#endif // __TB_%s_H__" % (self.table_name.upper())
            f.write(hdefine_end)

        # cpp file
        with open("%s/tb_%s.cpp" % (cpp_file_path, self.table_name), "w") as f:
            f.write('// this file created by gen_dbtable.py script at %s\n\n' % date_time_str)
            f.write("#include \"tb_%s.h\"\n\n" % self.table_name)
            f.write('// --------- custom code_3 begin --------\n')
            if 3 in self.custom_code_dic:
                for custom_line in self.custom_code_dic[3]:
                    f.write('%s' % custom_line)
            f.write('// --------- custom code_3 end ----------\n\n')
            f.write('Tb%s::Tb%s(int32_t table_id) : DataTableBase(table_id)\n' % (self.AaBbName, self.AaBbName))
            f.write('{\n')
            for one_field in self.field_list:
                cpp_type = DbDataType.cpp_type_dic[one_field.value_type]
                f.write('\t// %s\n' % one_field.field_name)
                enum_code = ""
                if cpp_type == "int64_t":
                    enum_code = 'E_FIELD_VALUE_TYPE_BIG_INT'
                elif cpp_type == "int32_t":
                    enum_code = 'E_FIELD_VALUE_TYPE_INT'
                elif cpp_type == "std::string":
                    enum_code = 'E_FIELD_VALUE_TYPE_STRING'
                if one_field.primary_key:
                    fun_code = 'AddField(%s, true);' % enum_code
                else:
                    fun_code = 'AddField(%s, false);' % enum_code

                f.write('\t%s\n' % fun_code)

            f.write('}\n')
            # destruct
            f.write('Tb%s::~Tb%s()\n' % (self.AaBbName, self.AaBbName))
            f.write('{\n')
            f.write('}\n')
            f.write('// --------- custom code_4 begin --------\n')
            if 4 in self.custom_code_dic:
                for custom_line in self.custom_code_dic[4]:
                    f.write('%s' % custom_line)
            f.write('// --------- custom code_4 end ----------\n\n')