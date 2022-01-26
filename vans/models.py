from django.db import models


class Van(models.Model):
    van_name = models.CharField(max_length=254)
    van_description = models.TextField()
    size_description = models.CharField(max_length=254, default="Compact")
    fuel_type = models.CharField(max_length=254, default="Diesel")
    sleeps = models.CharField(max_length=254, default="2")
    seats = models.CharField(max_length=254, default="2")
    airconditioning_home_area = models.BooleanField(
        default=True, null=True, blank=True)
    awning = models.BooleanField(default=True, null=True, blank=True)
    refrigerator = models.BooleanField(default=True, null=True, blank=True)
    shower = models.BooleanField(default=False, null=True, blank=True)
    camping_table_chairs = models.BooleanField(
        default=True, null=True, blank=True)
    gas_cylinder = models.BooleanField(default=True, null=True, blank=True)
    solar_panel = models.BooleanField(default=False, null=True, blank=True)
    toilet = models.BooleanField(default=False, null=True, blank=True)
    heating = models.BooleanField(default=True, null=True, blank=True)
    hot_water = models.BooleanField(default=True, null=True, blank=True)
    tv = models.BooleanField(default=True, null=True, blank=True)
    tv_receiver = models.BooleanField(default=False, null=True, blank=True)
    kitchen_equipment = models.BooleanField(
        default=True, null=True, blank=True)
    airconditioning_cabin = models.BooleanField(
        default=True, null=True, blank=True)
    reversing_camera = models.BooleanField(
        default=False, null=True, blank=True)
    roof_rack = models.BooleanField(default=False, null=True, blank=True)
    towbar = models.BooleanField(default=False, null=True, blank=True)
    cruise_control = models.BooleanField(default=True, null=True, blank=True)
    gps = models.BooleanField(default=False, null=True, blank=True)
    power_steering = models.BooleanField(default=True, null=True, blank=True)
    extras_bike_rack = models.BooleanField(
        default=True, null=True, blank=True)
    extras_awning = models.BooleanField(default=True, null=True, blank=True)
    extras_towbar = models.BooleanField(default=True, null=True, blank=True)
    extras_travel_box = models.BooleanField(
        default=True, null=True, blank=True)
    extras_chemical_toilet = models.BooleanField(
        default=True, null=True, blank=True)
    extras_bbq = models.BooleanField(default=True, null=True, blank=True)
    extras_cutlery_crockery = models.BooleanField(
        default=True, null=True, blank=True)
    van_main_image = models.URLField(
        max_length=1024, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)
    daily_rate_december_to_march = models.DecimalField(
        default=90, max_digits=6, decimal_places=2)
    daily_rate_april_to_june = models.DecimalField(
        default=110, max_digits=6, decimal_places=2)
    daily_rate_july_to_september = models.DecimalField(
        default=130, max_digits=6, decimal_places=2)
    daily_rate_october_to_november = models.DecimalField(
        default=110, max_digits=6, decimal_places=2)
    mileage_limit = models.CharField(
        default="1000km", max_length=254)
    price_per_extra_mile = models.DecimalField(
        default=1, max_digits=6, decimal_places=2)
    cleaning_fee = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)
    motorhome_insurance = models.CharField(
        default="Included", max_length=254)
    breakdown_cover = models.CharField(default="National", max_length=254)
    security_deposit = models.DecimalField(
        default=850, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.van_name
