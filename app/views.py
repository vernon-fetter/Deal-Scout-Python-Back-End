from flask import render_template, request, Flask, current_app, g, send_file, session, flash
from flask_appbuilder.security.decorators import protect
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, MultipleView, AppBuilder, BaseView, expose, has_access, action
from app import appbuilder
from flask_appbuilder.fields import AJAXSelectField
from flask_appbuilder.fieldwidgets import Select2AJAXWidget, Select2SlaveAJAXWidget, BS3TextFieldWidget, Select2Widget, Select2ManyWidget
from flask_appbuilder.models.sqla.filters import FilterEqualFunction, FilterStartsWith, FilterEqual
from wtforms import validators

from . import appbuilder, db
from .models import VendorGroup, Vendors, VendorSites, ProductGroup, Products, Promotions, ProductSubGroup, ProductSubSubGroup, Interests
from .models import SecurityLevel
from config import TEMP_FOLDER as mytemps
from PIL import Image

@appbuilder.sm.oauth_user_info_getter
def my_user_info_getter(sm, provider, response=None):
    if provider == 'google':
        me = sm.oauth_remotes[provider].get('userinfo')
        return {'username': me.data.get('id', ''),
                'first_name': me.data.get('given_name', ''),
                'last_name': me.data.get('family_name', ''),
                'email': me.data.get('email', '')}
    # else:
    #     return {}

myapp = appbuilder.get_app
with myapp.app_context():
    user = getattr(g, 'securitylevel_id', None)
    #seclevel =  getattr(g, 'seclevel', None)
    print("______________________________________________________________________")
    print(current_app.name)
    print(current_app)
    #print(seclevel)
    print(user)
    #print (user.name)
    print("______________________________________________________________________")

def myseclevel():
    print(g.user)


def get_user_seclevel():
    return str(g.user.seclev)


def get_user_sec_object():
    seclev = get_user_seclevel()
    if seclev == 'Administrator':
        return str(g.user.administrator())
    elif seclev == 'Sub-Administrator':
        return str(g.user.subadministrator())
    elif seclev == 'Vendor User':
         return str(g.user.vendor())
    elif seclev == 'Vendor Site User':
         return str(g.user.vendorsite())
    else:
        return str(g.user.frontenduser())

def get_user_vendor():
    return (g.user.user_vendor_id)
def get_user_vendor_site():
    return (g.user.user_vendor_site_id)

class SecurityLevelModelView(ModelView):
    datamodel = SQLAInterface(SecurityLevel)

    list_columns = ['name']
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']

class InterestsModelView(ModelView):
    datamodel = SQLAInterface(Interests, db.session)
    list_title = 'Interests List'
    show_title = 'Interests Details'
    add_title = 'Add Interest'
    edit_title = 'Edit Interest'
    label_columns = {
        'interest':'User Interest',
    }
    list_columns = [
        'interest',
    ]
    show_fieldsets = [
        (
            'User Interest',
            {
                'fields': [
                    'interest',
                    ]
                    }
        ),
    ]
    add_fieldsets = [
        (
            'User Interest',
            {
                'fields': [
                    'interest',
                    ]
                    }
        ),
    ]
    edit_fieldsets = [
        (
            'User Interest',
            {
                'fields': [
                    'interest',
                    ]
                    }
        ),
    ]

class VendorModelView(ModelView):
    datamodel = SQLAInterface(Vendors, db.session)
    base_filters = [['id', FilterEqualFunction, get_user_vendor]]
    list_title = 'Vendor List'
    show_title = 'Vendor Details'
    add_title = 'Add Vendor'
    edit_title = 'Edit Vendor'
    label_columns = {
        'id':'Vendor ID',
        'vendor_name':'Vendor Name',
        'photo_img':'Vendor Logo',
        'photo_img_thumbnail':'Vendor Thumbnail',
        'vendor_address':'Vendor Address',
        'vendor_email':'Vendor Email',
        'vendor_telephone_number': 'Vendor Telephone Number',
        'vendor_website':'Vendor Website',
        'vendor_description':'Vendor Description',
        'vendor_group_id':'Vendor Group ID',
        'vendor_group':'Vendor Group'
    }
    list_columns = [
        'id',
        'photo_img_thumbnail',
        'vendor_name',
        'vendor_address',
        'vendor_group',
    ]
    show_fieldsets = [
        ('Vendor Summary', 
        {
            'fields': [
                'vendor_name',
                'vendor_address',
                'vendor_group',
                'photo_img',
                ]
            }
        ),
        ('Vendor Contact Information',
        {
            'fields': [
                'vendor_website',
                'vendor_email',
                'vendor_telephone_number',
                ],
                'expanded': False,
            },
        ),
        ('Additional Data', 
        {
            'fields': [
                'vendor_description'
                ],
                'expanded': False
                }
        ),
    ]
    add_fieldsets = [
        ('Vendor Summary', 
        {
            'fields': [
                'vendor_name',
                'vendor_address',
                'vendor_group',
                'vendor_logo',
                ]
            }
        ),
        ('Vendor Contact Information',
        {
            'fields': [
                'vendor_website',
                'vendor_email',
                'vendor_telephone_number',
                ],
                'expanded': False,
            },
        ),
        ('Additional Data', 
        {
            'fields': [
                'vendor_description'
                ],
                'expanded': False
                }
        ),
    ]
    edit_fieldsets = [
        ('Vendor Summary', 
        {
            'fields': [
                'vendor_name',
                'vendor_address',
                'vendor_group',
                'vendor_logo',
                ]
            }
        ),
        ('Vendor Contact Information',
        {
            'fields': [
                'vendor_website',
                'vendor_email',
                'vendor_telephone_number',
                ],
                'expanded': False,
            },
        ),
        ('Additional Data', 
        {
            'fields': [
                'vendor_description'
                ],
                'expanded': False
                }
        ),
    ]

class VendorSitesModelView(ModelView):
    datamodel = SQLAInterface(VendorSites)
    base_filters = [['id', FilterEqualFunction, get_user_vendor_site]]
    list_title = 'Vendor Sites List'
    show_title = 'Vendor Site Details'
    add_title = 'Add Vendor Site'
    edit_title = 'Edit Vendor Site'
    label_columns = {
        'id':'Vendor ID',
        'vendor_site_name':'Vendor Site Name',
        'vendor_img':'Vendor Site Image or Logo',
        'vendor_img_thumbnail':'Vendor Site Image or Logo Thumbnail',
        'vendor_site_address':'Vendor Site Address',
        'vendor_site_latitude':'Vendor Site Latitude',
        'vendor_site_longitude':'Vendor Site Longitude',
        'vendor_site_email':'Vendor Site Email',
        'vendor_site_telephone_number': 'Vendor Site Telephone Number',
        'vendor_site_unique_website':'Vendor Site Unique Website',
        'vendor_site_unique_description':'Vendor Site Unique Description',
        'vendor_site_vendor_group_id':'Vendor Parent Group ID',
        'vendor_site_vendor_group':'Vendor Parent Group',
        'vendor_site_vendor_id':'Parent Vendor ID',
        'vendor_site_vendor':'Parent Vendor(s)'
    }
    list_columns = [
        'id',
        'vendor_img_thumbnail',        
        'vendor_site_vendor.name',
        'vendor_site_name',
        'vendor_site_vendor_group.name',
        'vendor_site_address',
    ]
    base_order = ('vendor_site_name', 'asc')
    show_fieldsets = [
        ('Vendor Site Summary', 
        {
            'fields': [
                'vendor_site_vendor_group',
                'vendor_site_vendor',
                'vendor_site_name',
                'vendor_img',
                ]
            }
        ),
        ('Vendor Site Location',
        {
            'fields': [
                'vendor_site_address',
                'vendor_site_latitude',
                'vendor_site_longitude',
                ],
                'expanded': False,
            },
        ),
        ('Vendor Site Contact Information',
        {
            'fields': [
                'vendor_site_unique_website',
                'vendor_site_email',
                'vendor_site_telephone_number',
                ],
                'expanded': False,
            },
        ),
        ('Additional Data', 
        {
            'fields': [
                'vendor_site_unique_description'
                ],
                'expanded': False
                }
        ),
    ]
    add_fieldsets = [
        ('Vendor Site Summary', 
        {
            'fields': [
                'vendor_site_vendor_group',
                'vendor_site_vendor',
                'vendor_site_name',
                'vendor_site_image',
                ]
            }
        ),
        ('Vendor Site Location',
        {
            'fields': [
                'vendor_site_address',
                'vendor_site_latitude',
                'vendor_site_longitude',
                ],
                'expanded': False,
            },
        ),
        ('Vendor Site Contact Information',
        {
            'fields': [
                'vendor_site_unique_website',
                'vendor_site_email',
                'vendor_site_telephone_number',
                ],
                'expanded': False,
            },
        ),
        ('Additional Data', 
        {
            'fields': [
                'vendor_site_unique_description'
                ],
                'expanded': False
                }
        ),
    ]
    edit_fieldsets = [
        ('Vendor Site Summary', 
        {
            'fields': [
                'vendor_site_vendor_group',
                'vendor_site_vendor',
                'vendor_site_name',
                'vendor_site_image',
                ]
            }
        ),
        ('Vendor Location',
        {
            'fields': [
                'vendor_site_address',
                'vendor_site_latitude',
                'vendor_site_longitude',
                ],
                'expanded': False,
            },
        ),
        ('Vendor Contact Information',
        {
            'fields': [
                'vendor_site_unique_website',
                'vendor_site_email',
                'vendor_site_telephone_number',
                ],
                'expanded': False,
            },
        ),
        ('Additional Data', 
        {
            'fields': [
                'vendor_site_unique_description'
                ],
                'expanded': False
                }
        ),
    ]
    add_form_extra_fields = {
        'vendor_site_vendor_group': AJAXSelectField(
            'Vendor Group Field',
            description='Vendor Group',
            datamodel=datamodel,
            col_name='vendor_site_vendor_group',
            widget=Select2AJAXWidget(
                endpoint='/vendorsitesmodelview/api/column/add/vendor_site_vendor_group'
            ),
        ),
        'vendor_site_vendor': AJAXSelectField(
            'Vendor Field',
            description='Vendor',
            datamodel=datamodel,
            col_name='vendor_site_vendor',
            widget=Select2SlaveAJAXWidget(
                master_id='vendor_site_vendor_group',
                endpoint='/vendorsitesmodelview/api/column/add/vendor_site_vendor?_flt_0_vendor_group_id={{ID}}'
            ),
        ),
    }
    edit_form_extra_fields = add_form_extra_fields

class VendorGroupModelView(ModelView):
    datamodel = SQLAInterface(VendorGroup, db.session)
    related_views = [VendorModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'
    base_order = ('name','asc')
    list_title = 'Vendor Group List'
    show_title = 'Vendor Group Details'
    add_title = 'Add Vendor Group'
    edit_title = 'Edit Vendor Group'
    label_columns = {
        'name':'Vendor Group',
    }
    list_columns = [
        'name',
    ]
    show_fieldsets = [
        (
            'Vendor Group',
            {
                'fields': [
                    'name',
                    ]
                    }
        ),
    ]
    add_fieldsets = [
        (
            'Vendor Group',
            {
                'fields': [
                    'name',
                    ]
                    }
        ),
    ]
    edit_fieldsets = [
        (
            'Vendor Group',
            {
                'fields': [
                    'name',
                    ]
                    }
        ),
    ]

class ProductModelView(ModelView):
    datamodel = SQLAInterface(Products, db.session)
    list_title = 'Product List'
    show_title = 'Product Details'
    add_title = 'Add Product'
    edit_title = 'Edit Product'
    label_columns = {
        'product_name':'Product Name',
        'product_img':'Product Image',
        'product_img_thumbnail':'Product Thumbnail',
        'product_description':'Product Description',
        'product_price':'Product Price',
        'product_group_id':'Product Group Id',
        'product_group':'Product Group',
        'product_sub_group_id':'Product Sub-Group ID',
        'product_sub_group':'Product Sub-Group',
        'product_sub_sub_group_id': 'Product Sub-Sub-Group ID',
        'product_sub_sub_group': 'Product Sub-Sub-Group',
    }
    list_columns = [
        'product_name',
        'product_img_thumbnail',
        'product_group',
        'product_sub_group',
        'product_sub_sub_group',
    ]
    show_fieldsets = [
        (
            'Product Summary',
            {
                'fields': [
                    'product_name',
                    'product_img',
                    'product_price',
                    'product_group',
                    'product_sub_group',
                    'product_sub_sub_group'
                    ]
                    }
        ),
        (
            'Additional Data',
            {
                'fields': [
                    'product_description'
                    ], 
            'expanded': False}
        ),
    ]
    add_fieldsets = [
        (
            'Product Summary',
            {
                'fields': [
                    'product_name',
                    'product_image',
                    'product_price',
                    'product_group',
                    'product_sub_group',
                    'product_sub_sub_group'
                    ]
                    }
        ),
        (
            'Additional Data',
            {
                'fields': [
                    'product_description'
                    ], 
            'expanded': False}
        ),
    ]
    edit_fieldsets = [
        (
            'Product Summary',
            {
                'fields': [
                    'product_name',
                    'product_image',
                    'product_price',
                    'product_group',
                    'product_sub_group',
                    'product_sub_sub_group'
                    ]
                    }
        ),
        (
            'Additional Data',
            {
                'fields': [
                    'product_description'
                    ], 
            'expanded': False}
        ),
    ]
    add_form_extra_fields = {
        'product_group': AJAXSelectField(
            'Product Group',
            description='Product Group',
            datamodel=datamodel,
            col_name='product_group',
            widget=Select2AJAXWidget(
                endpoint='/productmodelview/api/column/add/product_group'
            ),
        ),
        'product_sub_group': AJAXSelectField(
            'Product Sub-Group',
            description='Product Sub-Group',
            datamodel=datamodel,
            col_name='product_sub_group',
            widget=Select2SlaveAJAXWidget(
                master_id='product_group',
                endpoint='/productmodelview/api/column/add/product_sub_group?_flt_0_product_group_id={{ID}}'
            ),
        ),
        'product_sub_sub_group': AJAXSelectField(
            'Product Sub-Sub-Group',
            description='Product Sub-Sub-Group',
            datamodel=datamodel,
            col_name='product_sub_sub_group',
            widget=Select2SlaveAJAXWidget(
                master_id='product_sub_group',
                endpoint='/productmodelview/api/column/add/product_sub_sub_group?_flt_0_product_sub_group_id={{ID}}'
            ),
        ),
    }
    edit_form_extra_fields = add_form_extra_fields

class ProductSubSubGroupModelView(ModelView):
    datamodel = SQLAInterface(ProductSubSubGroup)
    related_views = [ProductModelView]
    list_title = 'Product Sub-Sub-Group List'
    show_title = 'Product Sub-Sub-Group Details'
    add_title = 'Add Product Sub-Sub-Group'
    edit_title = 'Edit Product Sub-Sub-Group'
    label_columns = {
        'product_group_id': 'Product Group ID',
        'product_group': 'Product Group',
        'product_sub_group_id': 'Sub-Group ID',
        'product_sub_group': 'Sub-Group',
        'name': 'Sub-Sub-Group',
        'product_interests_id':'Product Interests ID',
        'product_interests':'Product Interests',
    }
    list_columns = [
        'product_group',
        'product_sub_group',
        'name',
    ]
    show_fieldsets = [
        (
            'Product Sub-Sub-Group',
            {
                'fields': [
                    'product_group',
                    'product_sub_group',
                    'name',
                    'product_interests',
                ]
            }
        ),
    ]
    add_fieldsets = [
        (
            'Product Sub-Sub-Group',
            {
                'fields': [
                    'product_group',
                    'product_sub_group',
                    'name',
                    'product_interests',
                ]
            }
        ),
    ]
    edit_fieldsets = [
        (
            'Product Sub-Sub-Group',
            {
                'fields': [
                    'product_group',
                    'product_sub_group',
                    'name',
                    'product_interests',
                ]
            }
        ),
    ]

    # edit_form_extra_fields = {'product_group':  QuerySelectField('Student',
    #                                                        query_factory=student_query,
    #                                                        widget=Select2Widget()),
    #                           'product_sub_group':  QuerySelectField('bookstore',
    #                                                          query_factory=bookstore_query,
    #                                                          widget=Select2Widget())

    #                           }
    # add_form_extra_fields = edit_form_extra_fields

    add_form_extra_fields = {
        'product_group': AJAXSelectField(
            'Product Group Field',
            description='Product Group',
            datamodel=datamodel,
            col_name='product_group',
            widget=Select2AJAXWidget(
                endpoint='/productsubsubgroupmodelview/api/column/add/product_group'
            ),
        ),
        'product_sub_group': AJAXSelectField(
            'Product Sub-Group Field',
            description='Product Sub-Group',
            datamodel=datamodel,
            col_name='product_sub_group',
            widget=Select2SlaveAJAXWidget(
                master_id='product_group',
                endpoint='/productsubsubgroupmodelview/api/column/add/product_sub_group?_flt_0_product_group_id={{ID}}'
            ),
        ),
    }

    edit_form_extra_fields = add_form_extra_fields

class ProductSubGroupModelView(ModelView):
    datamodel = SQLAInterface(ProductSubGroup)
    related_views = [ProductSubSubGroupModelView, ProductModelView]
    list_title = 'Product Sub-Group List'
    show_title = 'Product Sub-Group Details'
    add_title = 'Add Product Sub-Group'
    edit_title = 'Edit Product Sub-Group'
    label_columns = {
        'product_group_id':'Product Group ID',
        'product_group':'Product Group',
        'productsubgroup_name':'Product Sub-Group',
        
    }
    list_columns = [
        'product_group',
        'productsubgroup_name',
    ]
    show_fieldsets = [
        (
            'Product Sub-Group',
            {
                'fields': [
                    'product_group',
                    'productsubgroup_name',
                    ]
                    }
        ),
    ]
    add_fieldsets = [
        (
            'Product Sub-Group',
            {
                'fields': [
                    'product_group',
                    'productsubgroup_name',
                    ]
                    }
        ),
    ]
    edit_fieldsets = [
        (
            'Product Sub-Group',
            {
                'fields': [
                    'product_group',
                    'productsubgroup_name',
                    ] 
                    }
        ),
    ]

class ProductGroupModelView(ModelView):
    datamodel = SQLAInterface(ProductGroup)
    related_views = [ProductSubGroupModelView, ProductSubSubGroupModelView, ProductModelView]
    list_title = 'Product Group List'
    show_title = 'Product Group Details'
    add_title = 'Add Product Group'
    edit_title = 'Edit Product Group'
    label_columns = {
        'name':'Product Group',
    }
    list_columns = [
        'name',
    ]
    show_fieldsets = [
        (
            'Product Group',
            {
                'fields': [
                    'name',
                    ]
                    }
        ),
    ]
    add_fieldsets = [
        (
            'Product Group',
            {
                'fields': [
                    'name',
                    ]
                    }
        ),
    ]
    edit_fieldsets = [
        (
            'Product Group',
            {
                'fields': [
                    'name',
                    ]
                    }
        ),
    ]

class PromotionsModelView(ModelView):
    datamodel = SQLAInterface(Promotions, db.session)
    list_title = 'Promotions List'
    show_title = 'Promotion Details'
    add_title = 'Add Promotion'
    edit_title = 'Edit Promotion'
    base_filters = [['id', FilterEqualFunction, get_user_vendor_site]]
    label_columns = {
        'promo_product_sub_sub_group_id':'Product Sub-Sub-Group ID',
        'promo_product_sub_sub_group': 'Product Sub-Sub-Group ID',
        'promo_product_sub_group_id':'Product Sub-Group ID',
        'promo_product_sub_group':'Product Sub-Group', 
        'promo_product_group_id':'Product Group ID',
        'promo_product_group':'Product Group',
        'promo_product_id':'Product ID',
        'promo_product_name':'Product(s)',
        'promo_vendor_group_id':'Vendor Group ID',
        'promo_vendor_group':'Vendor Group',
        'promo_vendor_id':'Vendor ID',
        'promo_vendor_name':'Vendor',
        'promo_vendor_site_id': 'Vendor Site ID',
        'promo_vendor_site': 'Vendor Site',
        'promo_name':'Promotion Name',
        'promo_price':'Promotion Price',
        'promo_date_from':'Promotion Date From',
        'promo_date_to':'Promotion Date To',
        'promo_description':'Promotion Description',
        'promo_active':'Promotion Active?',
        }
    list_columns = [
        'promo_name',
        'promo_description',
        'promo_product_name',
        'promo_vendor_site_name'
        ]
    show_fieldsets = [
        (
            'Promotion Information',
            {'fields': [
                'promo_name',
                'promo_product_group',
                'promo_product_sub_group',
                'promo_product_sub_sub_group',
                'promo_product_name',
                'promo_vendor_group',
                'promo_vendor_name',
                'promo_vendor_site',
                'promo_description',
                'promo_price',
                'promo_date_from',
                'promo_date_to',
                'promo_active',
                ]}
        ),
    ]
    add_fieldsets = [
        (
            'Promotion Information',
            {'fields': [
                'promo_name',
                'promo_product_group',
                'promo_product_sub_group',
                'promo_product_sub_sub_group',
                'promo_product_name',
                'promo_vendor_group',
                'promo_vendor_name',
                'promo_vendor_site',
                'promo_description',
                'promo_price',
                'promo_date_from',
                'promo_date_to',
                'promo_active',
                ]}
        ),
    ]
    edit_fieldsets = [
        (
            'Promotion Information',
            {'fields': [
                'promo_name',
                'promo_product_group',
                'promo_product_sub_group',
                'promo_product_sub_sub_group',
                'promo_product_name',
                'promo_vendor_group',
                'promo_vendor_name',
                'promo_vendor_site',
                'promo_description',
                'promo_price',
                'promo_date_from',
                'promo_date_to',
                'promo_active',
                ]}
        ),
    ]
    add_form_extra_fields = {
        'promo_product_group': AJAXSelectField(
            'Product Group',
            description='Select Product Group',
            datamodel=datamodel,
            col_name='promo_product_group',
            widget=Select2AJAXWidget(
                endpoint='/promotionsmodelview/api/column/add/promo_product_group'
            ),
        ),
        'promo_product_sub_group': AJAXSelectField(
            'Product Sub-Group',
            description='Select Product Sub-Group',
            datamodel=datamodel,
            col_name='promo_product_sub_group',
            widget=Select2SlaveAJAXWidget(
                master_id='promo_product_group',
                endpoint='/promotionsmodelview/api/column/add/promo_product_sub_group?_flt_0_product_group_id={{ID}}'
            ),
        ),
        'promo_product_sub_sub_group': AJAXSelectField(
            'Product Sub-Sub-Group',
            description='Select Product Sub-Sub-Group',
            datamodel=datamodel,
            col_name='promo_product_sub_sub_group',
            widget=Select2SlaveAJAXWidget(
                master_id='promo_product_sub_group',
                endpoint='/promotionsmodelview/api/column/add/promo_product_sub_sub_group?_flt_0_product_sub_group_id={{ID}}'
            ),
        ),
        'promo_product_name': AJAXSelectField(
            'Product',
            description='Select Product',
            datamodel=datamodel,
            col_name='promo_product_name',
            widget=Select2SlaveAJAXWidget(
                master_id='promo_product_sub_sub_group',
                endpoint='/promotionsmodelview/api/column/add/promo_product_name?_flt_0_product_sub_sub_group_id={{ID}}'
            ),
        ),
        'promo_vendor_group': AJAXSelectField(
            'Vendor Group',
            description='Select Promo Vendor Group',
            datamodel=datamodel,
            col_name='promo_vendor_group',
            widget=Select2AJAXWidget(
                endpoint='/promotionsmodelview/api/column/add/promo_vendor_group'
            ),
        ),
        'promo_vendor_name': AJAXSelectField(
            'Vendor',
            description='Select Promo Vendor',
            datamodel=datamodel,
            col_name='promo_vendor_name',
            widget=Select2SlaveAJAXWidget(
                master_id='promo_vendor_group',
                endpoint='/promotionsmodelview/api/column/add/promo_vendor_name?_flt_0_vendor_group_id={{ID}}'
            ),
        ),
        'promo_vendor_site': AJAXSelectField(
            'Vendor Site',
            description='Select Promo Vendor Site',
            datamodel=datamodel,
            col_name='promo_vendor_site',
            widget=Select2SlaveAJAXWidget(
                master_id='promo_vendor_name',
                endpoint='/promotionsmodelview/api/column/add/promo_vendor_site?_flt_0_vendor_site_vendor_id={{ID}}'
            ),
        ),
    }
    edit_form_extra_fields = add_form_extra_fields
    
    @action("Excel Download", "Download Promotional Items to xlsx", "Proceed with download", 'fa-file-excel-o')
    def excel_dl1(self, items):
        xslxfile = gen_xl(self, items)

        return send_file(mytemps + xslxfile,
                         attachment_filename=xslxfile,
                         as_attachment=True)

appbuilder.add_view(
    SecurityLevelModelView, 
    "Security Levels",
    icon="fa-cloud", 
    category="Configuration",
    category_icon="fa-bars")

appbuilder.add_view(
    InterestsModelView,
    "Interests List",
    icon = "fa-folder-open-o",
    category = "User Interests",
    category_icon = "fa-bars"
)

appbuilder.add_view(
    VendorGroupModelView,
    "Vendor Groups",
    icon = "fa-folder-open-o",
    category = "Vendors",
    category_icon = "fa-bars"
)

appbuilder.add_view(
    VendorModelView,
    "Vendor List",
    icon = "fa-folder-open-o",
    category = "Vendors",
    category_icon = "fa-bars"
)

appbuilder.add_view(
    VendorSitesModelView,
    "Vendor Sites List",
    icon = "fa-shopping-cart",
    category = "Vendors",
    category_icon = "fa-bars"
)

appbuilder.add_view(
    ProductGroupModelView,
    "Product Groups",
    icon = "fa-folder-open-o",
    category = "Products",
    category_icon = "fa-bars"
)

appbuilder.add_view(
    ProductSubGroupModelView,
    "Product Sub-Groups",
    icon = "fa-folder-open-o",
    category = "Products",
    category_icon = "fa-bars"
)

appbuilder.add_view(
    ProductSubSubGroupModelView,
    "Product Sub-Sub-Groups",
    icon="fa-folder-open-o",
    category="Products",
    category_icon="fa-bars"
)

appbuilder.add_view(
    ProductModelView,
    "Product List",
    icon = "fa-barcode",
    category = "Products",
    category_icon = "fa-bars"
)

appbuilder.add_view(
    PromotionsModelView,
    "Promotions List",
    icon = "fa-tag",
    category = "Promotions",
    category_icon = "fa-bars"
)

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

appbuilder.security_cleanup()
db.create_all()
