from flask_appbuilder.security.views import UserDBModelView, RegisterUserModelView
from flask_babelpkg import lazy_gettext
from flask_appbuilder.fields import AJAXSelectField
from flask_appbuilder.fieldwidgets import Select2AJAXWidget, Select2SlaveAJAXWidget
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget, Select2ManyWidget
from flask_appbuilder.security.registerviews import RegisterUserDBView
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from flask import g, current_app
from .models import Vendors, VendorSites
# from . import appbuilder, db, models

# myapp = appbuilder.get_app
# with myapp.app_context():
#     user = getattr(g, 'securitylevel_id', None)
#     #seclevel =  getattr(g, 'seclevel', None)
#     print("______________________________________________________________________")
#     print(current_app.name)
#     print(current_app)
#     #print(seclevel)
#     print(user)
#     #print (user.name)
#     print("______________________________________________________________________")

# def myseclevel():
#     print(g.user)

# def get_user_seclevel():
#     return str(g.user.seclev)

# def get_user_sec_object():
#     seclev = get_user_seclevel()
#     if seclev == 'Administrator':
#         return str(g.user.administrator())
#     elif seclev == 'Sub-Administrator':
#         return str(g.user.subadministrator())
#     elif seclev == 'Vendor User':
#          return str(g.user.vendor())
#     elif seclev == 'Vendor Site User':
#          return str(g.user.vendorsite())
#     else:
#         return str(g.user.frontenduser())

# def get_user_vendor():
#     return (g.user.user_vendor_id)

# def get_user_vendor_site():
#     return (g.user.user_vendor_site_id)

# def vendor_query():
#     ven = get_user_vendor()
#     qry = db.session.query(Vendors).filter(Vendors.id == ven)
#     return (qry)

# def vendorsite_query():
#     ven = get_user_vendor_site()
#     qry = db.session.query(VendorSites).filter(VendorSites.id == ven)
#     return (qry)

class MyUserDBModelView(UserDBModelView):
    show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'seclevel', 'user_vendor', 'user_vendor_site', 'login_count']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email', 'user_interests'], 'expanded': True}),
        (lazy_gettext('Audit Info'),
         {'fields': ['last_login', 'fail_login_count', 'created_on',
                     'created_by', 'changed_on', 'changed_by'], 'expanded': False}),
    ]
    user_show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'login_count', 'user_vendor', 'user_vendor_site']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email', 'user_interests'], 'expanded': True}),
    ]
    add_columns = [
        'first_name',
        'last_name',
        'username',
        'active',
        'email',
        'roles',
        'seclevel',
        'user_vendor', 
        'user_vendor_site',
        'user_interests',
        'password',
        'conf_password'
    ]
    list_columns = [
        'first_name',
        'last_name',
        'username',
        'email',
        'active',
        'roles',
        'seclevel',
        'user_vendor', 
        'user_vendor_site'
    ]
    edit_columns = [
        'first_name',
        'last_name',
        'username',
        'active',
        'email',
        'roles',
        'seclevel',
        'user_vendor', 
        'user_vendor_site',
        'user_interests'
    ]
    # add_form_extra_fields = {'student':  QuerySelectField('Vendor',
    #                             query_factory=vendor_query,
    #                             widget=Select2Widget()),
    #                         'vendor_site':  QuerySelectMultipleField('vendor_site',
    #                             query_factory=vendorsite_query,
    #                             widget=Select2ManyWidget())
    # }
    # edit_form_extra_fields = add_form_extra_fields

# class MyRegisterUserDBView(RegisterUserDBView):
#     email_template = 'register_mail.html'
#     email_subject = lazy_gettext('Your Account activation')
#     activation_template = 'activation.html'
#     form_title = lazy_gettext('Fill out the registration form')
#     error_message = lazy_gettext('Not possible to register you at the moment, try again later')
#     message = lazy_gettext('Registration sent to your email')

# class MyRegisterUserModelView(RegisterUserModelView):
#     show_fieldsets = [
#         (lazy_gettext('User info'),
#          {'fields': ['username']}),
#         (lazy_gettext('Personal Info'),
#          {'fields': ['first_name', 'last_name', 'email', 'user_interests'], 'expanded': True}),
#         (lazy_gettext('Audit Info'),
#          {'fields': ['last_login', 'fail_login_count', 'created_on',
#                      'created_by', 'changed_on', 'changed_by'], 'expanded': False}),
#     ]
#     user_show_fieldsets = [
#         (lazy_gettext('User info'),
#          {'fields': ['username']}),
#         (lazy_gettext('Personal Info'),
#          {'fields': ['first_name', 'last_name', 'email', 'user_interests'], 'expanded': True}),
#     ]
#     add_columns = [
#         'first_name',
#         'last_name',
#         'username',
#         'email',
#         'user_interests',
#         'password',
#     ]
#     list_columns = [
#         'first_name',
#         'last_name',
#         'username',
#         'email',
#     ]
#     edit_columns = [
#         'first_name',
#         'last_name',
#         'username',
#         'email',
#         'user_interests'
#     ]
