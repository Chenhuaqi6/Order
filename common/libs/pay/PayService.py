import decimal


class PayService():
    def __init__(self):
        pass

    def createOrder(self, member_id, items=None, params=None):
        resp = {'code': 200, 'msg': '操作成功!!', 'data': {}}
        pay_price = decimal.Decimal(0.00)
        continue_cnt = 0
        foods_id = []
        for item in items:
            if decimal.Decimal(item['price']) < 0:
                continue_cnt += 1
                continue

            pay_price = pay_price + decimal.Decimal(item['price']) * int(item['number'])
            foods_id.append(item['id'])

        if continue_cnt >= len(items):
            resp['code'] = -1
            resp['msg'] = '商品items为空'
            return resp
        yun_price = params['yun_price'] if params and 'yun_price' in params else 0
        note = params['note'] if params and 'note' in params else ''

        yun_price = decimal.Decimal(yun_price)
        total_price = pay_price + yun_price
        try:
            pass
        except Exception as e:
            pass

        return resp
