from cnocr import CnOcr
import datetime
import time
# 导入xlrd ,读取excel库
import xlrd
# 导入xlwt ，写入excel库
import xlwt
import pymysql
import xlrd
db = pymysql.connect(host='59.110.216.16',
                     user='vm_2023',
                     password='vm_2023.',
                     database='db_shitplay')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
# 查询 mysql 版本
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
# 导出航信啊
excelHead=['起始-到达','起飞日期','航班','价格']

# 根据表头和表格数据生成excel表格
    # excelTitle 表头
    # excelData 表格数据
    # sheetName sheet名称
    # docName
def doExportExcel (excelHead,excelData,sheetName,docName):
    # 新建工作簿，编码格式为utf-8
    workbook = xlwt.Workbook(encoding='utf-8')
    # sheet name
    worksheet = workbook.add_sheet(sheetName)
    # 设置表头
    for i in range(len(excelHead)):
        worksheet.write(0, i, excelHead[i])

    currentDateTime=datetime.datetime.now()
    

    # 遍历赋值
    # i 表示行数 j 表示列数
    for i in range(len(excelData)):
        # print("表格行数："+str(len(excelData)))
        # # print("内容是："+excelData)
        # print(excelData[i][0])
        for j in range(len(excelData[i])):
            # print("内容是："+excelData[i][j])
            # print("i="+str(i))
            # print("j="+str(j))
            worksheet.write(i+1, j, excelData[i][j])

    # 表格名称由固定字符加当前时间共同组成
    workbook.save(docName+currentDateTime.strftime('%Y-%m-%d-%H-%M-%S')+'.xls')
    print("导出excel表格")
    # 导出表格数据
excelData =[]
ocr = CnOcr()
i=1

for i in range(1,20):
    res = ocr.ocr('D:/wangh_work/root/git_python/python_practice_code/practice/ocr/qunar/img/image%s.png'% i)
    start =0
    step=12
    end=len(res)
    print(res)
    for i in range(start,end,step):
        x=i
        tempArray=res[x:x+step]
        for j in tempArray:
            print(j['text'])
        excelElement = []
        # 起始-到达
        excelElement.append(str(tempArray[0]['text']))
        # 起飞日期
        excelElement.append(str(tempArray[6]['text']))
        # 航班
        excelElement.append(str(tempArray[8]['text']))
         # 价格
        excelElement.append(str(tempArray[9]['text']))
        excelData.append(excelElement)  
        print('dddddddddddddddddddddddddddddd=%s' %i)
        excelElement = []
          # 起始-到达
        excelElement.append(str(tempArray[1]['text']))
        # 起飞日期
        excelElement.append(str(tempArray[7]['text']))
        # 航班
        excelElement.append(str(tempArray[10]['text']))
         # 价格
        excelElement.append(str(tempArray[11]['text']))
        excelData.append(excelElement) 
        
            
        # excelData.append(excelElement)
        
doExportExcel(excelHead,excelData,'t','t')      
    # print("Predicted Chars:", res)