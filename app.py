from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def index1():
    return index()


@app.route('/movie')
def movie():
    temp = []
    client = MongoClient(host='127.0.0.1', port=27017)
    col = client.hot.clo
    for one in col.find({"$or": [{"type": {'$regex': "电影榜"}}, {"type": {'$regex': "电视剧榜"}}, {"type": {'$regex': '小说榜'}}]}):
        # print(one)
        temp.append(one)
    # num = len(temp)
    client.close()
    return render_template('movie.html', list=temp)


@app.route('/hot')
def hot():
    temp = list()
    client = MongoClient(host='127.0.0.1', port=27017)
    col = client.hot.clo
    for one in col.find(
            {"$or": [{"type": {'$regex': "热搜榜"}}, {"type": {'$regex': '汽车榜'}}]}):
        # print(one)
        temp.append(one)
    # num = len(temp)
    client.close()
    return render_template('hot.html', list=temp)


@app.route('/game')
def game():
    temp = list()
    client = MongoClient(host='127.0.0.1', port=27017)
    col = client.hot.clo
    for one in col.find({"type": {'$regex': '游戏榜'}}):
        # print(one)
        temp.append(one)
    # num = len(temp)
    client.close()
    return render_template('game.html', list=temp)


@app.route('/rank')
def rank():
    client = MongoClient(host='127.0.0.1', port=27017)
    col = client.hot.clo
    hot_num_list = []
    result = col.count_documents({'hot': {'$lte': 10000}})
    hot_num_list.append(result)
    result = col.count_documents({'$and': [{'hot': {'$gt': 10000}}, {'hot': {'$lte': 100000}}]})
    hot_num_list.append(result)
    result = col.count_documents({'$and': [{'hot': {'$gt': 100000}}, {'hot': {'$lte': 200000}}]})
    hot_num_list.append(result)
    result = col.count_documents({'$and': [{'hot': {'$gt': 200000}}, {'hot': {'$lte': 500000}}]})
    hot_num_list.append(result)
    result = col.count_documents({'$and': [{'hot': {'$gt': 500000}}, {'hot': {'$lte': 1000000}}]})
    hot_num_list.append(result)
    result = col.count_documents({'hot': {'$gt': 1000000}})
    hot_num_list.append(result)
    # hot_list = ["热度小于一万", "热度一万到十万", "热度十万到二十万", "热度二万到五十万", "热度五万到一百万", "热度一百万以上"]

    result = col.find({'hot': {'$gte': 1000000}})
    hot_list = list()
    for one in result:
        hot_list.append(one)

    client.close()

    return render_template('rank.html', list=hot_num_list, hot=hot_list)


@app.route('/word')
def word():
    return render_template('word.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)      # 这里由于pycharm的问题不能指定ip端口; 需要edit configution(右上角):--host=0.0.0.0 --port=5000
