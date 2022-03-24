import logging
import ckan.lib.base as base


class TajulController(BaseController):

    def daino(self):
        return base.render('home/tajul.html') 
