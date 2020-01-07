import datetime
import sys
from flask import Markup, url_for, Flask
from flask_appbuilder import Model
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Boolean, Table, Text
from sqlalchemy.orm import relationship

# Author: VC Fetter

class SecurityLevel(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class VendorGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)

    def __repr__(self):
        return self.name

# assoc_vendorgroup_vendors = Table('vendorgroup_vendors', Model.metadata,
#                                       Column('id', Integer, primary_key=True),
#                                       Column('vendorgroup_id', Integer, ForeignKey('vendor_group.id')),
#                                       Column('vendors_id', Integer, ForeignKey('vendors.id'))
# )

class Vendors(Model):
    id = Column(Integer, primary_key=True)
    vendor_name = Column(String(150))
    vendor_logo = Column(ImageColumn(size=(300,300,True), thumbnail_size=(30,30,True)))
    vendor_address = Column(String(500), default='Street', nullable=False)
    vendor_email = Column(String(150))
    vendor_telephone_number = Column(String(15))
    vendor_website = Column(String(150))
    vendor_description = Column(String(500))
    vendor_group_id = Column(Integer, ForeignKey('vendor_group.id'), nullable=False)
    vendor_group = relationship(
        'VendorGroup')
    # vendor_group = relationship('VendorGroup', secondary=assoc_vendorgroup_vendors, backref='vendorgroup')

    def __repr__(self):
        return self.vendor_name
    
    def photo_img(self):
        im = ImageManager()
        if self.vendor_logo:
            return Markup('<a href="' + url_for('VendorModelView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="' + im.get_url(self.vendor_logo) +\
              '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('VendorModelView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        if self.vendor_logo:
            return Markup('<a href="' + url_for('VendorModelView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.vendor_logo) +\
              '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('VendorModelView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

class VendorSites(Model):
    id = Column(Integer, primary_key=True)
    vendor_site_name = Column(String(150), nullable=False)
    vendor_site_image = Column(ImageColumn(
        size=(300, 300, True), thumbnail_size=(30, 30, True)))
    vendor_site_address = Column(String(500), default='Street', nullable=False)
    vendor_site_latitude = Column(Float, nullable=False)
    vendor_site_longitude = Column(Float, nullable=False)
    vendor_site_email = Column(String(150))
    vendor_site_telephone_number = Column(String(15))
    vendor_site_unique_website = Column(String(150))
    vendor_site_unique_description = Column(String(500))
    vendor_site_vendor_group_id = Column(
        Integer, ForeignKey('vendor_group.id'), nullable=False)
    vendor_site_vendor_group = relationship("VendorGroup")
    vendor_site_vendor_id = Column(
        Integer, ForeignKey('vendors.id'), nullable=False)
    vendor_site_vendor = relationship("Vendors")

    def __repr__(self):
        return self.vendor_site_name

    def vendor_img(self):
        im = ImageManager()
        if self.vendor_site_image:
            return Markup('<a href="' + url_for('VendorSitesModelView.show', pk=str(self.id)) +
                          '" class="thumbnail"><img src="' + im.get_url(self.vendor_site_image) +
                          '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('VendorSitesModelView.show', pk=str(self.id)) +
                          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def vendor_img_thumbnail(self):
        im = ImageManager()
        if self.vendor_site_image:
            return Markup('<a href="' + url_for('VendorSitesModelView.show', pk=str(self.id)) +
                          '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.vendor_site_image) +
                          '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('VendorSitesModelView.show', pk=str(self.id)) +
                          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

class ProductGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class ProductSubGroup(Model):
    id = Column(Integer, primary_key=True)
    productsubgroup_name = Column(String(150), unique=True, nullable=False)
    product_group_id = Column(Integer, ForeignKey('product_group.id'))
    product_group = relationship("ProductGroup")

    def __repr__(self):
        return self.productsubgroup_name

assoc_interests_productsubsubgroup = Table('interests_productsubsubgroup', Model.metadata,
                                      Column('id', Integer, primary_key=True),
                                      Column('interests_id', Integer, ForeignKey('interests.id')),
                                      Column('productsubsubgroup_id', Integer, ForeignKey('product_sub_sub_group.id'))
)

class InterestsProductsubsubgroup(Model):
    __tablename__ = 'interests_productsubsubgroup'

class ProductSubSubGroup(Model):
    id = Column(Integer, primary_key=True)
    product_group_id = Column(Integer, ForeignKey('product_group.id'))
    product_group = relationship("ProductGroup")
    product_sub_group_id = Column(Integer, ForeignKey('product_sub_group.id'))
    product_sub_group = relationship("ProductSubGroup")
    name = Column(String(150), unique=True, nullable=False)
    product_interests_id = Column(Integer, ForeignKey('interests.id'))
    product_interests = relationship('Interests', secondary=assoc_interests_productsubsubgroup, backref='productsubsubgroup')

    def __repr__(self):
        return self.name

class Products(Model):
    id = Column(Integer, primary_key=True)
    product_name = Column(String(150), unique=True, nullable=False)
    product_image = Column(ImageColumn(size=(300,300,True), thumbnail_size=(30,30,True)), nullable=False)
    product_description = Column(String(500), nullable=False)
    product_price = Column(Float, nullable=False)
    product_group_id = Column(Integer, ForeignKey('product_group.id'), nullable=False)
    product_group = relationship("ProductGroup")
    product_sub_group_id = Column(Integer, ForeignKey('product_sub_group.id'), nullable=False)
    product_sub_group = relationship("ProductSubGroup")
    product_sub_sub_group_id = Column(Integer, ForeignKey('product_sub_sub_group.id'), nullable=False)
    product_sub_sub_group = relationship("ProductSubSubGroup")

    def __repr__(self):
        return self.product_name

    def product_img(self):
        im = ImageManager()
        if self.product_image:
            return Markup('<a href="' + url_for('ProductModelView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="' + im.get_url(self.product_image) +\
              '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('ProductModelView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def product_img_thumbnail(self):
        im = ImageManager()
        if self.product_image:
            return Markup('<a href="' + url_for('ProductModelView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.product_image) +\
              '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('ProductModelView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')


# assoc_vendors_promotions = Table('vendors_promotions', Model.metadata,
#                                       Column('id', Integer, primary_key=True),
#                                       Column('vendors_id', Integer, ForeignKey('vendors.id')),
#                                       Column('promotions_id', Integer, ForeignKey('promotions.id'))
# )

# assoc_products_promotions = Table('products_promotions', Model.metadata,
#                                       Column('id', Integer, primary_key=True),
#                                       Column('products_id', Integer, ForeignKey('products.id')),
#                                       Column('promotions_id', Integer, ForeignKey('promotions.id'))
# )

class Promotions(Model):
    id = Column(Integer, primary_key=True)
    promo_product_sub_sub_group_id = Column(Integer, ForeignKey('product_sub_sub_group.id'), nullable=False)
    promo_product_sub_sub_group = relationship("ProductSubSubGroup")
    promo_product_sub_group_id = Column(Integer, ForeignKey('product_sub_group.id'), nullable=False)
    promo_product_sub_group = relationship("ProductSubGroup")
    promo_product_group_id = Column(Integer, ForeignKey('product_group.id'), nullable=False)
    promo_product_group = relationship("ProductGroup")
    promo_product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    promo_product_name = relationship(
        'Products')
    # promo_product_name = relationship('Products', secondary=assoc_products_promotions, backref='products')
    promo_vendor_group_id = Column(Integer, ForeignKey('vendor_group.id'), nullable=False)
    promo_vendor_group = relationship("VendorGroup")
    promo_vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=False)
    promo_vendor_name = relationship(
        'Vendors')
    # promo_vendor_name = relationship('Vendors', secondary=assoc_vendors_promotions, backref='vendors')
    promo_vendor_site_id = Column(Integer, ForeignKey('vendor_sites.id'), nullable=False)
    promo_vendor_site = relationship(
        'VendorSites')
    promo_name = Column(String(250), nullable=False)
    promo_price = Column(Float, nullable=False)
    promo_date_from = Column(Date, nullable=False)
    promo_date_to = Column(Date, nullable=False)
    promo_description = Column(String(500))
    promo_active = Column(Boolean)

    def __repr__(self):
        return self.promo_name

class Interests(Model):
    id = Column(Integer, primary_key=True)
    interest = Column(String(150), unique=True, nullable=False)

    def __repr__(self):
        return self.interest
