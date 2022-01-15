
import logging
import os

logging.basicConfig(
    # 文件
    filename="a.txt",
    # 日志格式
    # format='%(asctime)s-%(name)s-%(levelname)s-%(module)s: %(message)s',
    level=10,
)
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
test_format = '%(asctime)s] %(message)s'

BASE_PATH = os.path.dirname(os.path.dirname(__file__))  # log文件的目录
logfile_dir = os.path.join(BASE_PATH,'log').replace('\\','/')
logfile_name = 'atm.log'
logfile_path = os.path.join(logfile_dir,logfile_name)
# 日志配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        # 'other': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',  # 保存到文件
        #     'formatter': 'test',
        #     'filename': 'a2.log',
        #     'encoding': 'utf-8',
        # },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        'kkk': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG', # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        # '专门的采集': {
        #     'handlers': ['other',],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
}
logging.debug("hello")
logging.info("hello")
logging.warning("hello")
logging.error("hello")
logging.critical("hello世界")
