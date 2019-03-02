Python Flask订餐系统
=========================
author:chenhuaqi
ebv:python3.5
Email:chenhuaqiY@163.com
Github:https://github.com/Chenhuaqi6
##启动
        export ops_config=local|production && python manage.py runserver


##使用flsk-sqlacodegen,快速生成orm models
		flask-sqlacodegen 'mysql://root:@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask

        flask-sqlacodegen 'mysql+pymysql://root:123456@127.0.0.1/food_db' --tables user --outfile "common/models/User.py"  --flask
  