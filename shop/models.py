from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def save(self, *args, **kwargs):
        
        if self.gender == 'male':
            self.profile_image = 'avatars/default_male.png'
        elif self.gender == 'female':
            self.profile_image = 'avatars/default_female.png'
        else:
            self.profile_image = 'avatars/default_other.png'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=255)
    image = models.ImageField(upload_to="category_images/", blank=True, null=True)

    def __str__(self):
        return self.name
    
class GST(models.Model):
    name = models.CharField(max_length=50)     
    percent = models.DecimalField(max_digits=5, decimal_places=2) 

    def __str__(self):
        return f"{self.name} ({self.percent}%)"
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default="No description available.")
    offer_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, default=None)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def get_price(self):
        return self.offer_price or self.price
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    PAYMENT_CHOICES = [
        ('COD', 'Cash on Delivery'),
        ('ONLINE', 'Online Payment'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booked_orders',default=1)
    booked_at = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='COD')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    is_deleted_by_user = models.BooleanField(default=False)
    address = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.product.get_price() * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('UPI', 'UPI'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.get_price() * self.quantity
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
        

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
