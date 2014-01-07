from ratelimitbackend import admin
from coupons.models import Coupon, UserBillingProfile

admin.site.register(Coupon)
admin.site.register(UserBillingProfile)
