# -*- coding: utf-8 -*-
# @Date    : 2019-12-09
# @Author  : zhaoguocai

from jinja2 import Environment


class ReportLib:

    def __html_report_rendering(self, html_template, report_render_object):
        """ render a html format report by jinja2 """
        return Environment().from_string(html_template).render(report_render_object)

    def report_gen(self, report_path):
        """ save report to local """
        report_content = self.__html_report_rendering()
        with open(report_path, "wb") as f:
            f.write(report_content)


