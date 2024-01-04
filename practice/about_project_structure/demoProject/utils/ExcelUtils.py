# -*- coding: UTF-8 -*-

# 导入xlrd ,读取excel库
import xlrd
# 导入xlwt ，写入excel库
import xlwt
# 导入 datetime
import datetime

# from QunarCommonConstant import QunarCommonConstant


# from QunarConstant import QunarCommonConstant

# excel表格工具类



# 生成excel表格

class ExcelUtils:
    '表格工具类，提供各种excel生成与读取方法'

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

# eu=ExcelUtils.doExportExcel(QunarConstant.getSpecialPriceExcelHead(),"b")

