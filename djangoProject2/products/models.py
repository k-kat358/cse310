# Create your models here.
from typing import Tuple
from django.contrib.auth.models import User
from django.db import models

#cpu,cpu cooler, motherboard, memory, storage, gpu,psu, case

class CPU(models.Model):
    photo= models.ImageField(upload_to='CPU/',null=True, blank=True)
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100) #e.g. am5, lga1156
    generation = models.CharField(max_length=100)
    cores= models.IntegerField()
    threads= models.IntegerField()
    core_clock= models.FloatField()
    boost_clock = models.FloatField()
    cache = models.IntegerField()
    power= models.FloatField()
    warranty = models.IntegerField()
    price = models.FloatField(default=0)
    shop = models.CharField(max_length=100, default="Default Shop")

    class Meta:
        ordering = ['name', 'shop']

    def __str__(self) -> str:
        return f"{self.name} (Shop: {self.shop})"

class MOBO(models.Model):
    photo= models.ImageField(upload_to='MOBO/',null=True, blank=True)
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100) #e.g. am5, lga1156
    chipset = models.CharField(max_length=100)
    mobo_form_factor = models.CharField(max_length=100)
    audio_chipset = models.CharField(max_length=100)
    ram_type = models.CharField(max_length=100) #e.g. ddr5,ddr4
    ram_capacity = models.IntegerField()
    ram_slot = models.IntegerField()
    connector_and_ports = models.TextField()
    warranty = models.IntegerField() #in years
    power= models.FloatField() #scarping a pawa difficult
    price = models.FloatField(default=0)
    shop = models.CharField(max_length=100, default="Default Shop")

    class Meta:
        ordering = ['name', 'shop']

    def __str__(self) -> str:
        return f"{self.name} (Shop: {self.shop})"

class CPUCooler(models.Model):
    photo= models.ImageField(upload_to='CPUCOOLER/',null=True, blank=True)
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100) #e.g. am5, lga1156, but ekhane supported shb platform er naam e nite hobe. Probably string matching kora lagbe with cpu
    number_of_fans = models.IntegerField()
    fan_speed = models.IntegerField()
    fan_airflow = models.FloatField()
    noise_level = models.FloatField() #unit add korte hobe pore, noise in dB,speed in rpm and airflow in CFM
    material = models.CharField(max_length=100)
    dimension = models.TextField()
    warranty = models.IntegerField() #in years
    price = models.FloatField(default=0)
    shop = models.CharField(max_length=100, default="Default Shop")

    class Meta:
        ordering = ['name', 'shop']

    def __str__(self) -> str:
        return f"{self.name} (Shop: {self.shop})"

class RAM(models.Model):
    photo= models.ImageField(upload_to='RAM/',null=True, blank=True)
    name = models.CharField(max_length=100)
    ram_type = models.CharField(max_length=100) #e.g. ddr5,ddr4
    ram_capacity = models.IntegerField()
    ram_frequency = models.IntegerField() #unit Mhz
    operating_voltage = models.FloatField() #in volt
    cas_latency = models.CharField(max_length=100)
    warranty = models.IntegerField() #in years
    power= models.FloatField() #scarping a pawa difficult
    price = models.FloatField(default=0)
    shop = models.CharField(max_length=100, default="Default Shop")

    class Meta:
        ordering = ['name', 'shop']

    def __str__(self) -> str:
        return f"{self.name} (Shop: {self.shop})"

class Storage(models.Model):
    photo= models.ImageField(upload_to='Storage/',null=True, blank=True)
    name = models.CharField(max_length=100)
    storage_type = models.CharField(max_length=100) #either ssd or hdd
    storage_capacity = models.IntegerField()
    form_factor = models.CharField(max_length=100) #e.g 3.5inch for hdd, m.2 2280 for ssd
    speed = models.CharField(max_length=100) #mbps, r/w
    interface = models.CharField(max_length=100) #m.2 , sata3
    warranty = models.IntegerField() #in years
    power= models.FloatField() #scarping a pawa difficult
    #ekta text field dewa jay for other details, not for now
    price = models.FloatField(default=0)
    shop = models.CharField(max_length=100, default="Default Shop")

    class Meta:
        ordering = ['name', 'shop']

    def __str__(self) -> str:
        return f"{self.name} (Shop: {self.shop})"

class GPU(models.Model):
    photo= models.ImageField(upload_to='GPU/',null=True, blank=True)
    name = models.CharField(max_length=100)
    chip_maker = models.CharField(max_length=100) #nvidia,intel or amd
    memory_capacity = models.IntegerField()
    memory_type= models.CharField(max_length=10)
    core_clock= models.CharField(max_length=100) # er moddhei boost clock etc thakbe, just copied from website
    memory_clock = models.CharField(max_length=100)
    cuda_core_or_stream_processor= models.IntegerField() #nvidia hole cuda,amd hole stream processor,ref - chip maker
    output_ports = models.CharField(max_length=100)
    dimension_weight = models.CharField(max_length=100)
    other_features = models.TextField()
    warranty = models.IntegerField() #in years
    power= models.IntegerField()
    price = models.FloatField(default=0)
    shop = models.CharField(max_length=100, default="Default Shop")

    class Meta:
        ordering = ['name', 'shop']

    def __str__(self) -> str:
        return f"{self.name} (Shop: {self.shop})"

class PSU(models.Model):
    photo= models.ImageField(upload_to='PSU/',null=True, blank=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField() #in watts
    certification = models.CharField(max_length=100)
    modular_type = models.CharField(max_length=100)
    connector_types = models.TextField()
    warranty = models.IntegerField() #in years
    #pore dimension add kore case compatibility check kora jabe
    price = models.FloatField(default=0)
    shop = models.CharField(max_length=100, default="Default Shop")

    class Meta:
        ordering = ['name', 'shop']

    def __str__(self) -> str:
        return f"{self.name} (Shop: {self.shop})"

class CASE(models.Model):
    photo= models.ImageField(upload_to='CASE/',null=True, blank=True)
    name = models.CharField(max_length=100)
    case_type = models.CharField(max_length=100) #minitower,full-tower
    mobo_form_factor = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    expansion_slots = models.CharField(max_length=100)
    radiator_support = models.CharField(max_length=100)
    fan_support = models.CharField(max_length=100)
    storage_support = models.CharField(max_length=100)
    front_panel_ports = models.CharField(max_length=100)
    gpu_and_cooler_clearance = models.CharField(max_length=100)
    warranty = models.IntegerField() #in years
    price = models.FloatField(default=0)
    shop = models.CharField(max_length=100, default="Default Shop")

    class Meta:
        ordering = ['name', 'shop']

    def __str__(self) -> str:
        return f"{self.name} (Shop: {self.shop})"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    product_type = models.CharField(max_length=50)  # e.g., 'CPU', 'GPU', etc.
    product_id = models.PositiveIntegerField()  # ID of the product from the respective table
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField()  # Store the price of the product at the time of addition

    def __str__(self):
        return f"{self.product_type} - {self.product_id} (Qty: {self.quantity}) for {self.user.username}"

    @property
    def total_price(self):
        return self.quantity * self.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()
    status = models.CharField(max_length=50, default="Pending")  # e.g., Pending, Completed, Cancelled

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product_type = models.CharField(max_length=50)
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.product_type} - {self.product_id} (Qty: {self.quantity}) for Order #{self.order.id}"

    @property
    def total_price(self):
        return self.quantity * self.price
