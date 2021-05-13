import requests
from lxml import etree

with open("银行间拆借利率13-17月度日数据.csv","w",encoding="utf-8-sig") as f:
    f.write("日期,利率(%),涨跌(BP)\n")
    for i in range(38,100):
        tree = etree.HTML(requests.get("http://data.eastmoney.com/shibor/shibor.aspx?m=ch&t=98&d=99235&cu=cny&type=009090&p="+str(i)).text)
        for row in tree.xpath("//*[@id='tb']/tr")[1:]:
            rowString=""
            for column in row:
                rowString+=''.join(column.itertext())+","
            f.write(rowString[:-1]+"\n")
    