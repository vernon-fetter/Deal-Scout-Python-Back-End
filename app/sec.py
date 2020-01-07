from flask import redirect
from flask_appbuilder.actions import action
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_appbuilder.security.views import UserDBModelView
from .sec_models import MyUser, MyRegisterUser
from .sec_view import MyUserDBModelView
from .custom_registration import Register

class MyUserDBView(MyUserDBModelView):
    @action("muldelete", "Delete", "Delete all Really?", "fa-rocket", single=False)
    def muldelete(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())

class MySecurityManager(SecurityManager):
    user_model = MyUser
    userdbmodelview = MyUserDBModelView
    registeruser_model = MyRegisterUser
    # registerusermodelview = MyRegisterUserModelView
    registeruserdbview = Register
    