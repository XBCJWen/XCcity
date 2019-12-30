# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ScrapyhotelPipeline(object):
    cityTable = 'XC_cityT'
    shangQTable = 'XC_shangT'

    def __init__(self):
        self.db = pymysql.connect(host='101.132.128.168', user='root', passwd='123456',db='spider')

    def open_spider(self, spider):
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()

    def process_item(self, item, spider):
        sql = 'replace into {table} (id,py,name) values ("{id}","{py}","{name}")'
        sql2 = 'replace into {table} (id,shangId,shangName) values ("{id}","{shangId}","{shangName}")'
        for i in range(len(item['cityId'])):
            s1 = sql.format(table=self.cityTable,id=item['cityId'][i],py=item['cityPy'][i],name=item['cityName'][i])
            print(s1,',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
            try:
                self.cursor.execute(s1)
                self.db.commit()
            except Exception as e :
                print('erro',e)
                self.db.rollback()

            for ii in range(len(item['shangId'])):
                print('len',len(item['shangId']),'........',item['cityId'][i],ii)
                s = sql2.format(table=self.shangQTable, id=item['cityId'][i], shangId=item['shangId'][ii],shangName=item['shangName'][ii])
                print('存入商圈名...',s)
                try:
                    self.cursor.execute(s)
                    self.db.commit()
                except Exception as e:
                    print('erro', e)
                    self.db.rollback()
        return item
