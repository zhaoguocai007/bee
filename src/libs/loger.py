# -*- coding: utf-8 -*-
# @Date    : 2019-12-09
# @Author  : zhaoguocai

import logging, os, time, sys
from src.conf.basic_conf import BaseConf
from src.conf.user_config import UserConf


class LogDog:
    """ Log 工厂类 """

    _log_path = os.path.join(BaseConf.base_dir, "output")
    _log_level = UserConf.log_level
    _log_display_format = "%(asctime)s - %(name)s - %(levelname)s : %(message)s"

    def __init__(self):
        if not os.path.exists(LogDog._log_path):
            os.makedirs(LogDog._log_path)
        self.log_file = os.path.join(LogDog._log_path, "{}.log".format(time.strftime('%Y-%m-%d', time.localtime())))

    def get_loger(self):
        logger = logging.getLogger(__name__)
        formatter = logging.Formatter(LogDog._log_display_format)
        console = logging.StreamHandler(sys.stdout)
        file_handler = logging.FileHandler(filename=self.log_file, encoding="utf-8")
        console.setLevel(LogDog._log_level)
        console.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(LogDog._log_level)
        logger.addHandler(console)
        logger.addHandler(file_handler)

        return logging.getLogger()

log = LogDog().get_loger()
