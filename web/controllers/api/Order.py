from flask import request, jsonify,g

from application import app
from common.models.food.Food import Food
from common.models.member.MemberCart import MemberCart
from web.controllers.api import route_api
from common.libs.member.CartService import CartService
from common.libs.Helper import selectFilterObj,getDicFilterField
from common.libs.UrlManager import UrlManager
import json,decimal

@route_api.route("/order/info",methods=['POST'])
def orderinfo():
    resp = {'code':200,'msg':'操作成功!!','data':{}}
    req = request.values
    params_goods = req['goods'] if 'goods' in req else ''
    member_info = g.member_info
    params_goods_list = []
    if params_goods:
        params_goods_list = json.loads(params_goods)
    food_dic = {}
    for item in params_goods_list:
        food_dic[item['id']] = item['number']
    food_ids = food_dic.keys()
    food_list = Food.query.filter(Food.id.in_(food_ids)).all()
    data_food_list = []
    yun_price = pay_price = decimal.Decimal(0.00)
    if food_list:
        for item in food_list:
            tmp_data = {
                'id':item.id,
                'name':item.name,
                'price':str(item.price),
                'pic_url':UrlManager.buildImageUrl(item.main_image),
                'number':food_dic[item.id],
            }
            pay_price = pay_price + item.price *int(food_dic[item.id])
            data_food_list.append(tmp_data)

    default_address = {
        'name':'陈华齐',
        'mobile':'17638170530',
        'address':'杭州市余杭区恒基旭辉府'
    }
    resp['data']['food_list'] = data_food_list
    resp['data']['pay_price'] = str(pay_price)
    resp['data']['yun_price'] = str(yun_price)
    resp['data']['total_price'] = str(pay_price+yun_price)
    resp['data']['default_address'] = default_address
    return jsonify(resp)


@route_api.route('/order/create',methods=['POST'])
def orderCreate():
    resp = {'code':200,'msg':'操作成功!!','data':{}}
    req = request.values

    type = req['type'] if 'type' in req else ''
    params_goods = req['goods'] if 'goods' in req else None

    item = []
    if params_goods:
        item = json.loads(params_goods)
    if len(item) < 1:
        resp['code'] = -1
        resp['msg'] = '下单失败,没有选择商品!!'
        return jsonify(resp)


    return jsonify(resp)














