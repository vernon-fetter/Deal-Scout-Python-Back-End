from flask_appbuilder.security.sqla.models import User
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Boolean, Table, Text, Sequence
from flask_appbuilder import Model
from .models import Interests, SecurityLevel, Vendors, VendorSites
from flask_appbuilder.security.sqla.models import User, RegisterUser
from flask_appbuilder.models.mixins import AuditMixin

assoc_vendors_user = Table('vendors_user', Model.metadata,
                                      Column('id', Integer, primary_key=True),
                                      Column('vendors_id', Integer, ForeignKey('vendors.id')),
                                      Column('abuser_id', Integer, ForeignKey('ab_user.id'))
)

assoc_vendorsite_user = Table('vendorsite_user', Model.metadata,
                                      Column('id', Integer, primary_key=True),
                                      Column('vendorsites_id', Integer, ForeignKey('vendor_sites.id')),
                                      Column('abuser_id', Integer, ForeignKey('ab_user.id'))
)

class MyUser(User):
    __tablename__ = 'ab_user'

    seclevel_id = Column(Integer, ForeignKey('security_level.id'))
    seclevel = relationship("SecurityLevel")

    user_vendor_id = Column(Integer, ForeignKey('vendors.id'))
    user_vendor = relationship('Vendors', secondary=assoc_vendors_user, backref='abuser')

    user_vendor_site_id = Column(Integer, ForeignKey('vendor_sites.id'))
    user_vendor_site = relationship('VendorSites', secondary=assoc_vendorsite_user, backref='abuser')

assoc_interests_registeruser = Table('interests_registeruser', Model.metadata,
                                      Column('id', Integer, primary_key=True),
                                      Column('interests_id', Integer, ForeignKey('interests.id')),
                                      Column('abregisteruser_id', Integer, ForeignKey('ab_register_user.id'))
)

class MyRegisterUser(AuditMixin, RegisterUser):
    __tablename__ = 'ab_register_user'

    user_interests_id = Column(Integer, ForeignKey('interests.id'))
    user_interests = relationship('Interests', secondary=assoc_interests_registeruser, backref='abregisteruser')

