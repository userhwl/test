from pymongo import *

'''
查询方法：
    find_one()返回满足条件的文档集中第一条数据，类型为字典
                如果没有查询结果返回None
    方法find()返回满足条件的所有文档，类型为Cursor对象，可以使用for...in遍历，每项为字典对象
            如果没有查询结果返一个空的Cursor对象
'''


def select():
    try:
        # 1 创建连接对象
        client = MongoClient(host="localhost", port=27017)
        # 2 获取数据库,
        # 如果这个数据库不存在，就在内存中虚拟创建
        # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        db = client.demo  # 使用demo数据库
        # 从stu查询数据
        # 查询一条,返回一个字典，如果没有结果返回None
        res = db.stu.find_one({"name": 'aa'})
        print(res)
        # 查询全部结果，返回一个Cursor可迭代对象，每一个元素是字典
        # 如果没有查询结果会返回一个空的Cursor对象
        res = db.stu.find({"age": {"$gt": 2}})
        print(res)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    select()
a
