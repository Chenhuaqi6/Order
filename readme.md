Python Flask订餐系统
=========================

##启动
* export ops_config=local|production && python manage.py runserver


##flsk-sqlacodegen
		flask-sqlacodegen 'mysql://root:@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask

        flask-sqlacodegen 'mysql+pymysql://root:123456@127.0.0.1/food_db' --tables user --outfile "common/models/User.py"  --flask