from flask_appbuilder import ModelRestApi
from flask_appbuilder.api import BaseApi, expose, rison, safe, ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder, db
from .models import VendorGroup, Vendors, VendorSites, ProductGroup, Products, Promotions, ProductSubGroup, ProductSubSubGroup
from .models import Interests
from .sec_models import MyUser

class MyUserModelApi(ModelRestApi):
    base_permissions = ['can_get', 'can_post']
    resource_name = 'user'
    datamodel = SQLAInterface(MyUser)

appbuilder.add_api(MyUserModelApi)

class InterestsModelApi(ModelRestApi):
    base_permissions = ['can_get', 'can_post']
    resource_name = 'interests'
    datamodel = SQLAInterface(Interests)

appbuilder.add_api(InterestsModelApi)

class VendorSiteModelApi(ModelRestApi):
    base_permissions = ['can_get', 'can_post']
    resource_name = 'vendorsite'
    datamodel = SQLAInterface(VendorSites)

appbuilder.add_api(VendorSiteModelApi)

class VendorModelApi(ModelRestApi):
    base_permissions = ['can_get', 'can_post']
    resource_name = 'vendor'
    datamodel = SQLAInterface(Vendors)

appbuilder.add_api(VendorModelApi)

class VendorGroupModelApi(ModelRestApi):
    base_permissions = ['can_get', 'can_post']
    resource_name = 'vendorgroup'
    datamodel = SQLAInterface(VendorGroup)

appbuilder.add_api(VendorGroupModelApi)

class ProductModelApi(ModelRestApi):
    base_permissions = ['can_get', 'can_post']
    resource_name = 'product'
    datamodel = SQLAInterface(Products)

appbuilder.add_api(ProductModelApi)

class ProductGroupModelApi(ModelRestApi):
    base_permissions = ['can_get', 'can_post']
    resource_name = 'productgroup'
    datamodel = SQLAInterface(ProductGroup)

appbuilder.add_api(ProductGroupModelApi)

class ProductSubGroupModelApi(ModelRestApi):
    base_permissions = ['can_get', 'can_post']
    resource_name = 'productsubgroup'
    datamodel = SQLAInterface(ProductSubGroup)

appbuilder.add_api(ProductSubGroupModelApi)


class ProductSubSubGroupModelApi(ModelRestApi):
    base_permissions = ['can_get', 'can_post']
    resource_name = 'productsubsubgroup'
    datamodel = SQLAInterface(ProductSubSubGroup)


appbuilder.add_api(ProductSubSubGroupModelApi)

class PromotionsModelApi(ModelRestApi):
    base_permissions = ['can_get', 'can_post']
    resource_name = 'promo'
    datamodel = SQLAInterface(Promotions)

appbuilder.add_api(PromotionsModelApi)

# class DistanceCalc(BaseApi):
#     @expose('/distance/<string:latitude>,<string:longitude>')
#     def distancecalculation(self, vendors, lat, lng):
#         if isinstance(vendors, list):
#             for vendorsites in vendors:
#                 vendorsites.vendor_site_distance = haversine(latitude, longitude)
#                 self.datamodel.edit(vendorsites)
#                 self.update_redirect()
#                 self.response(200, message=lat)
#             else:
#                 vendorsites.vendor_site_distance = haversine(latitude, longitude)
#                 self.datamodel.edit(vendorsites)
#             return redirect(self.get_redirect())

# appbuilder.add_api(DistanceCalc)

# def haversine(lat,lng):
#     lng, lat, VendorSites.vendor_site_longitude, VendorSites.vendor_site_latitude = map(radians, [lng, lat, VendorSites.vendor_site_longitude, VendorSites.vendor_site_latitude])

#     dlon = VendorSites.vendor_site_longitude - lng 
#     dlat = VendorSites.vendor_site_latitude - lat
#     a = sin(dlat/2)**2 + cos(lat) * cos(VendorSites.vendor_site_latitude) * sin(dlon/2)**2
#     c = 2 * asin(sqrt(a)) 
#     r = 6371
#     return c * r
