# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class FarfetchPipeline:
    def __init__(self):
        conn = pymongo.MongoClient(
            'mongodb+srv://subramanyam7:smsrkmsd7@cluster0.zopfa.mongodb.net/'
        )
        db = conn["SubramanyamMantry"]
        #FarfetchMen
        # self.collection = db["FarFetch"]
        #FarFetchWomen
        self.collection = db["FarFetchwomen"]

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        return item
