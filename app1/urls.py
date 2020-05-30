from django.urls import path
from . import views
from .views import  process_payment,ItemDetailView, OrderSummaryView, PaymentView, CheckoutView, RequestRefundView, AddCouponView


urlpatterns = [
    path('', views.home, name='home'),
    path('Item/<slug>/', ItemDetailView.as_view()),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',
         views.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', views.remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('payment/', views.process_payment, name='payment'),
    path('paymentbycash/', PaymentView.as_view(), name='paymentbycash'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),

]


#PaymentView.as_view()
  # path('payment/<payment_option>/', PaymentView.as_view(, name='payment'),