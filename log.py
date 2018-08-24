#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/8/25 上午12:19
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : log.py
# @Software: PyCharm

import conf
from common_import import *

def genLogDict(logDir, logFile):
    '''
    配置日志格式的字典
    '''
    logDict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                'format': '%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
            'standard': {
                'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },

            "default": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "simple",
                "filename": os.path.join(logDir, logFile),
                'mode': 'w+',
                "maxBytes": 1024*1024*5,  # 5 MB
                "backupCount": 20,
                "encoding": "utf-8"
            },
        },

        "root": {
            'handlers': ['default'],
            'level': "INFO",
            'propagate': False
        }
    }
    return logDict


def initLogConf():
    '''
    配置日志,初始化设置
    '''
    # 生成日志路径
    baseDir = os.path.dirname(os.path.abspath(__file__))
    logDir = os.path.join(baseDir, conf.LOG_PATH)

    # 创建路径
    if not os.path.exists(logDir):
        os.makedirs(logDir)

    # 生成日志文件
    logFile = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
    logDict = genLogDict(logDir, logFile)
    logging.config.dictConfig(logDict)

initLogConf()