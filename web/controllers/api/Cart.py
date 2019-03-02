from flask import request, jsonify,g

from application import app
from common.models.food.Food import Food
from common.models.member.MemberCart import MemberCart
from web.controllers.api import route_api
from common.libs.member.CartService import CartService
from common.libs.Helper import selectFilterObj,getDicFilterField
from common.libs.UrlManager import UrlManager
import json
@route_api.route('/cart/index')
def cartIndex():
    resp = {'code': 200, 'msg': '操作成功!', 'data': {}}
    #查找全局变量也就是登录用户
    member_info = g.member_info
    #如果没用户,说明未登录!
    if not member_info:
        resp['code'] = -1
        resp['msg'] = '获取失败,未登录!!'
        return jsonify(resp)
    #通过用户的id查找该用户在购物车的所有操作
    cart_list =MemberCart.query.filter_by(member_id = member_info.id).all()
    # print('cart_list',cart_list)

    data_cart_list = []
    if cart_list:
        #该用户在购物车所有商品的id
        food_ids = selectFilterObj(cart_list,"food_id")
        # print('food_ids',food_ids)
        #得到{商品id:商品}
        food_map = getDicFilterField(Food,Food.id,'id',food_ids)
        # print('food_map',food_map)
        #对购物车里的商品进行遍历
        for item in cart_list:
            #遍历到哪个商品使用哪个商品
            tmp_food_info = food_map[item.food_id]
            # print('tmp_food_info',tmp_food_info)
            tmp_data = {
                'id':item.id,
                'food_id':item.food_id,
                'number':item.quantity,
                'name':tmp_food_info.name,
                'price': str(tmp_food_info.price),
                'pic_url':UrlManager.buildImageUrl(tmp_food_info.main_image),
                'active':True,

            }
            data_cart_list.append(tmp_data)
    # print('data_cart_list',data_cart_list)
    resp['data']['list'] = data_cart_list
    return jsonify(resp)


@route_api.route('/cart/set',methods=['POST'])
def setCart():
    resp = {'code': 200, 'msg': '操作成功!', 'data': {}}
    req = request.values
    food_id = int(req['id']) if 'id' in req else 0
    number = int(req['number']) if 'number' in req else 0
    if food_id < 1 or number < 1:
        resp['code'] = -1
        resp['msg'] = '添加购物车失败-1'
        return jsonify(resp)
    member_info = g.member_info
    if not member_info:
        resp['code'] = -1
        resp['msg'] = '添加购物车失败-2'
        return jsonify(resp)

    food_info = Food.query.filter_by(id = food_id).first()
    if not food_info:
        resp['code'] = -1
        resp['msg'] = '添加购物车失败-3'
        return jsonify(resp)
    if food_info.stock < number:
        resp['code'] = -1
        resp['msg'] = '添加购物车失败,库存不足!!!'
        return jsonify(resp)
    ret = CartService.setItems(member_id=member_info.id,food_id=food_id,number=number)
    if not ret:
        resp['code'] = -1
        resp['msg'] = '添加购物车失败-4'
        return jsonify(resp)
    return jsonify(resp)


@route_api.route('/cart/del',methods=['POST'])
def delCart():
    resp = {'code': 200, 'msg': '操作成功!', 'data': {}}
    req = request.values
    params_goods = req['goods'] if 'goods' in req else None

    items = []
    if params_goods:
        items = json.loads(params_goods)
    if not items or len(items) < 1:
        return jsonify(resp)
    member_info = g.member_info
    if not member_info:
        resp['code'] = -1
        resp['msg'] = '删除购物车失败-1'
        return jsonify(resp)

    ret = CartService.deleteItem(member_id=member_info.id,items = items)
    if not ret:
        resp['code'] = -1
        resp['msg'] = '删除购物车失败-2'
        return jsonify(resp)

    return jsonify(resp)




