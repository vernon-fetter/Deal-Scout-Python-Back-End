from flask import flash, redirect, session, url_for, request
from flask_appbuilder.views import expose, PublicFormView
from flask_babel import lazy_gettext
# from .forms import CustomRegistration
from flask_appbuilder.validators import Unique
from flask_appbuilder._compat import as_unicode
from flask_mail import Mail, Message
from flask_appbuilder import const
import logging

log = logging.getLogger(__name__)

def get_first_last_name(fullname):
    names = fullname.split()
    if len(names) > 1:
        return names[0], ' '.join(names[1:])
    elif names:
        return names[0], ''

class MyRegisterUserDBView(PublicFormView):
    email_template = 'register_mail.html'
    activation_template = 'activation.html'
    email_subject = lazy_gettext('Your Account activation for Deal-n-All')
    form_title = lazy_gettext('Fill out the registration form for Deal-n-All')
    error_message = lazy_gettext('Not possible to register you at the moment, try again later')
    message = lazy_gettext('Registration sent to your email')

    def send_email(self, register_user):
        mail = Mail(self.appbuilder.get_app)
        msg = Message()
        msg.subject = self.email_subject
        url = url_for('.activation', _external=True, activation_hash=register_user.registration_hash)
        msg.html = self.render_template(self.email_template,
                                        url=url,
                                        username=register_user.username,)
        msg.recipients = [register_user.email]
        try:
            mail.send(msg)
        except Exception as e:
            return False
        return True

    def add_registration(self, username, first_name, last_name, email, user_interests, password=''):
        register_user = self.appbuilder.sm.add_register_user(username, first_name, last_name, email, password)
        if register_user:
            if self.send_email(register_user):
                flash(as_unicode(self.message), 'info')
                return register_user
            else:
                flash(as_unicode(self.error_message), 'danger')
                self.appbuilder.sm.del_register_user(register_user)
                return None

    @expose('/activation/<string:activation_hash>')
    def activation(self, activation_hash):
        reg = self.appbuilder.sm.find_register_user(activation_hash)
        if not reg:
            flash(as_unicode(self.false_error_message), 'danger')
            return redirect(self.appbuilder.get_url_for_index)
        if not self.appbuilder.sm.add_user(username=reg.username,
                                           email=reg.email,
                                           first_name=reg.first_name,
                                           last_name=reg.last_name,
                                           role=self.appbuilder.sm.find_role(
                                                            self.appbuilder.sm.auth_user_registration_role),
                                           hashed_password=reg.password):
            flash(as_unicode(self.error_message), 'danger')
            return redirect(self.appbuilder.get_url_for_index)
        else:
            self.appbuilder.sm.del_register_user(reg)
            return self.render_template(self.activation_template,
                               username=reg.username,
                               appbuilder=self.appbuilder)

    def add_form_unique_validations(self, form):
        datamodel_user = self.appbuilder.sm.get_user_datamodel
        datamodel_register_user = self.appbuilder.sm.get_register_user_datamodel
        if len(form.username.validators) == 1:
            form.username.validators.append(Unique(datamodel_user, 'username'))
            form.username.validators.append(Unique(datamodel_register_user, 'username'))
        if len(form.email.validators) == 2:
            form.email.validators.append(Unique(datamodel_user, 'email'))
            form.email.validators.append(Unique(datamodel_register_user, 'email'))

class Register(MyRegisterUserDBView):

    # form = CustomRegistration 

    redirect_url = '/home/new/'

    def form_get(self, form):
        self.add_form_unique_validations(form)

    def form_post(self, form):
        self.add_form_unique_validations(form)
        self.add_registration(username=form.username.data,
                              first_name=form.username.data,
                              last_name='',
                              email=form.email.data,
                              password=form.password.data
                              )