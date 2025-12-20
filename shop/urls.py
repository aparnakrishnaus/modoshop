from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop_view, name='shop'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    
    path('profile/', views.profile_page, name='profile_page'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    path('cart/', views.cart_page, name='cart_page'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('wishlist/', views.wishlist_page, name='wishlist_page'),
    path('wishlist/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),

    path('orders/', views.orders, name='orders'),
    path('orders/remove/<int:order_id>/', views.user_delete_order, name='user_delete_order'),

    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),


    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/products/', views.products_page, name='products_page'),
    path('dashboard/categories/', views.categories_page, name='categories_page'),
    path('dashboard/admin/orders/', views.orders_page, name='orders_page'),
    path('dashboard/admin/orders/<int:order_id>/deliver/', views.mark_delivered, name='mark_delivered'),
    path('dashboard/admin/orders/<int:order_id>/delete/', views.delete_order, name='delete_order'),
    path('dashboard/payments/', views.payments_page, name='payments_page'),
    path('dashboard/remove-payment/<int:payment_id>/', views.remove_payment, name='remove_payment'),
    path('dashboard/messages/', views.admin_messages_view, name='admin_messages'),
    path('dashboard/messages/delete/<int:msg_id>/', views.delete_message, name='delete_message'),
    path('dashboard/reports/', views.admin_reports, name='admin_reports'),


    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:product_id>/', views.add_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),

    path('dashboard/add-category/', views.add_category, name='add_category'),
    path('categories/edit/<int:category_id>/', views.add_category, name='edit_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),


    path("gst/add/", views.add_edit_gst, name="add_gst"),
    path("gst/list/", views.list_gst, name="gst_list"),
    path("gst/edit/<int:id>/", views.add_edit_gst, name="edit_gst"),
    path("gst/delete/<int:id>/", views.delete_gst, name="delete_gst"),

    path('cart/checkout/', views.checkout_view, name='checkout'),
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),
    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('order/cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('stripe-success/', views.stripe_success, name='stripe_success'),
    path('buy-now-success/<int:product_id>/', views.buy_now_success, name='buy_now_success'),
    path('update-quantity/<int:item_id>/', views.update_quantity, name='update_quantity'),


    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name='password_reset'),
    
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
         name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
         name='password_reset_confirm'),
    
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
         name='password_reset_complete'),

    path('password-change/', 
         auth_views.PasswordChangeView.as_view(template_name='password_change.html'), 
         name='password_change'),
    path('password-change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
         name='password_change_done'),


    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),

    
]