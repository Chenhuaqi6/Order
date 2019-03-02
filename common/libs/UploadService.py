from werkzeug.utils import secure_filename
from application import app,db
from common.libs.Helper import getCurrentDate
import os,stat,uuid
from common.models.Image import Image
class UploadService():
    @staticmethod
    def uploadByfile(file):
        config_upload = app.config['UPLOAD']
        resp = {'code':200,'msg':'操作成功','data':{}}
        filename = secure_filename(file.filename)
        ext = filename.rsplit(".",1)[1]
        #判断后缀名是否在配置允许当中
        if ext not in config_upload['ext']:
            resp['code'] = -1
            resp['msg'] = '不允许的扩展类型文件!!'
            return resp
        #当前项目的目录+配置中的'prefix_path':'/web/static/upload/'
        root_path = app.root_path + config_upload['prefix_path']
        #生成时间格式的文件夹名
        file_dir = getCurrentDate("%Y%m%d")
        #图片的位置
        save_dir = root_path + file_dir
        #如果每天该地址则创建
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
            #给图片权限
            os.chmod(save_dir,stat.S_IRWXU | stat.S_IRGRP | stat.S_IRWXO)
        #拼接文件名
        file_name = str(uuid.uuid4()).replace("-","")+"."+ext
        file.save("{0}/{1}".format(save_dir,file_name))
        #存入数据库用于在线管理
        model_image = Image()
        model_image.file_key = file_dir + "/" + file_name
        model_image.created_time = getCurrentDate()
        db.session.add(model_image)
        db.session.commit()


        resp['data'] = {
            'file_key':model_image.file_key
        }
        return resp