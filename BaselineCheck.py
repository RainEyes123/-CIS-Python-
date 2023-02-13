#!/usr/bin/python3
import sqlite3
import os
import re
import json
import sys

class MdDocProcessing(object):#md文档格式化处理类如已有编号，自动更新；更新1-6 级标题；

    def __init__(self):
        pass

    def start_processing(self):#导入文档
        #self._command_check()

        doc_list = sys.argv[1:]

        if len(doc_list) == 0:
            doc_list=('test.md')
        self.title_style_convert(doc_list)
        # print("文档<%s>转换完成。"%(doc_list, ))

    def title_style_convert(self, file_name):
        """
        标题自动编号
        编号格式为： 1.1.1. 标题
        :param file_name:
        :return:
        """

        title_num_cur = [0]*6

        # 匹配正则表达式
        reg = r'^((#{2,6})[\s\d\.]{0,})(.*)$'
        pattern = re.compile(reg)

        # 输出文件对象
        res_file = open('_' + file_name, 'w', encoding='utf-8')

        with open(file_name, 'r', encoding='utf-8') as fi:
            line = fi.readline()
            while line:
                res = re.match(pattern, line)
                if res:
                    length = len(res.group(2))
                    title_num_cur, title_str = self._title_nuber_process(title_num_cur, length)
                    line = res.group(2) + ' ' + title_str + res.group(3) + '\n'

                res_file.write(line)
                line = fi.readline()
        # 关闭输出文件
        res_file.close()

        #os.rename(file_name, file_name + '.tmp')
        # 删除原文件
        os.remove(file_name)
        # 将输出文件改为原文件名
        os.rename('_' + file_name, file_name)
        return 

    def _command_check(self):
        #print(sys.argv)
        cmd_params = sys.argv[1:]
        if len(cmd_params) <= 0:
            self.help()
            exit()


    def _title_nuber_process(self, title_num, length=0):
        """
        根据目录级别及前一标题编号返回新编号
        :param title_num: 前一标题编号 list
        :param length: 标题级别 int
        :return: res: 标号 str
        """
        if length == 0:
            return ''

        title_num_z = [0]*6
        title_num[length-2] += 1
        title_num = title_num[:length-1] + title_num_z[length-1:]
        res = '.'.join(str(x) if x else '1' for x in title_num[:length-1]) + '. '
        return (title_num, res)

    # @staticmethod
    # def help():
    #     print('%s没有md' % sys.argv[0])

def ljpd(lj):#逻辑判断有大小等于
    for key,value in Dict.items():
        if lj==key:
            return value
def fu_hao(fhz):#将之送入对应结果进行判断
    if fhz==1:
        den_yu(data,jz,xm)
    elif fhz==2:
        xiaoyu_denyu(data,jz,xm)
    elif fhz==3:
        dayu_denyu(data,jz,xm)


def search_id(shuoshu_id):#判断所属id与模块id
    c=conn.cursor()
    cursor=c.execute("SELECT 模块id,模块名,父模块id from modular2")
    for list in cursor:
        module_id=list[0]
        module_name=list[1]
        if shuoshu_id==module_id:
            return module_name

def insert_str(name,xm,md,jg):#添加md表
    file=open('test.md','r')
    content=file.read()
    post=content.find(name)
    i = '''
|  编号  |  项目  |  核查结果  |  整改意见  |
| ----- | ----- | ----- | ----- |
| +++++++++++++++ | +++++++++++++++ | +++++++++++++++ | +++++++++++++++ |
'''
    post2=content.find(i)
    if post2 == -1:
        if post !=-1:
            cont=content[:post+len(name)]+'\n'+i+'| '+str(id)+' | '+xm+' | '+md+' | '+jg+' |'+content[post+len(name):]+'\n'
            file=open('test.md','w')
            file.write(cont)
            file.close()
    else:
        if post !=-1:
            cont=content[:post+len(name)+len(i)]+'\n'+'| '+str(id)+' | '+xm+' | '+md+' | '+jg+' |'+content[post+len(name)+len(i):]
            file=open('test.md','w')
            file.write(cont)
            file.close()

def den_yu(data,jz,xm):
    if data==jz:
        md = "核查成功"
        name=search_id(shuoshu_id)
        insert_str(name,xm,md,'保持')
        jsontext['points'].append({'核查项目':xm,'核查结果':'核查成功','核查建议':'保持'})
        print(xm,"\033[1;32;40mOK\033[0m")
    else:
        md = "核查失败"
        name=search_id(shuoshu_id)
        jg=zg
        insert_str(name,xm,md,jg)
        jsontext['points'].append({'核查项目':xm,'核查结果':'核查失败','核查建议':jg})
        print(xm,"\033[1;31;40mERROR\033[0m")

def xiaoyu_denyu(data,jz,xm):
    if data<=jz:
        md = "核查成功"
        name=search_id(shuoshu_id)
        insert_str(name,xm,md,'保持')
        jsontext['points'].append({'核查项目':xm,'核查结果':'核查成功','核查建议':'保持'})
        print(xm,"\033[1;32;40mOK\033[0m")
    else:
        md = "核查失败"
        name=search_id(shuoshu_id)
        jg=zg
        insert_str(name,xm,md,jg)
        jsontext['points'].append({'核查项目':xm,'核查结果':'核查失败','核查建议':jg})
        print(xm,"\033[1;31;40mERROR\033[0m")

def dayu_denyu(data,jz,xm):
    if data>=jz:
        md = "核查成功"
        name=search_id(shuoshu_id)
        insert_str(name,xm,md,'保持')
        jsontext['points'].append({'核查项目':xm,'核查结果':'核查成功','核查建议':'保持'})
        print(xm,"\033[1;32;40mOK\033[0m")
    else:
        md = "核查失败"
        name=search_id(shuoshu_id)
        jg=zg
        insert_str(name,xm,md,jg)
        jsontext['points'].append({'核查项目':xm,'核查结果':'核查失败','核查建议':jg})
        print(xm,"\033[1;31;40mERROR\033[0m")

def search_father(module_father,i):#父模块id是否模块id
    c=conn.cursor()
    cursor=c.execute("SELECT 模块id,模块名,父模块id from modular2")
    for list in cursor:
        module_id=list[0]
        if module_father!=0:
            i+=1
            module_father=module_id
            return i
        return i

def start():
    so = MdDocProcessing()
    so.start_processing()

# if __name__ == '__main__':
#     start()
#     pass

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("SELECT max(rowid) from modular2")
n = c.fetchone()[0]
cursor2 = c.execute("SELECT 模块id,模块名,父模块id from modular2")
for list in cursor2:#调用模块表
    module_id=list[0]
    module_name=list[1]
    module_father=list[2]
    i=1
    j=search_father(module_father,i)
    f=open('test.md','a')
    jinhao='#'
    f.write(jinhao*j+'#'+ ' ' + module_name+'\n')

Dict={'=':1,'<=':2,'>=':3}
jsontext = {'points':[]}
conn = sqlite3.connect('test.db')
c = conn.cursor()#调用规则表
cursor = c.execute("SELECT 编号, 所属id, 核查项目, 核查命令, 核查结果, 基准值, 正则表达式, 正则结果, 逻辑运算关系, 整改意见  from rule2 order by 编号 desc")
for row in cursor:
    id=row[0]
    shuoshu_id=row[1]
    xm=row[2]
    jz=row[5]
    zz=row[6]
    lj=row[8]
    zg=row[9]
    print ("编号 = ", row[0])
    print ("所属id = ", row[1])
    print ("核查项目 = ", row[2])
    tmp=os.popen(row[3],'r').read()
    # if tmp!=tmp:
    #     tmp='null'
    # print ("核查结果 = ", tmp)
    print ("基准值 = ", row[5])
    print ("正则表达式 = ", row[6])
    print ("核查结果 ： ")
    ret=re.search(zz,str(tmp))
    if ret == None:
        ret=re.search(zz,str("null"))
    data=ret.group()
    fhz=ljpd(lj)
    fu_hao(fhz)
    print ("\n")
jsondata = json.dumps(jsontext,indent=4,separators=(',', ': '),ensure_ascii=False)
f = open('test.json', 'w')
f.write(jsondata)
f.close()
conn.close()
start()