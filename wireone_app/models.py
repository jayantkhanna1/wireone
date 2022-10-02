from django.db import models

# Create your models here.

class DBP(models.Model):
    distance = models.IntegerField()
    price = models.IntegerField()

class TMF(models.Model):
    Time = models.IntegerField()
    price = models.DecimalField(max_digits = 5, decimal_places = 2)

class Price(models.Model):
    Total_distance = models.IntegerField()
    Total_time = models.IntegerField()
    dap = models.IntegerField()
    price = models.IntegerField(default = 0)

    
    def save(self, *args, **kwargs):
        # Get all data from DBP table
        dbp_table = DBP.objects.all()
        # making copy of total distance
        self.temp_total_distance = self.Total_distance

        # initial DBP price
        self.dbp_price = 0

        # If price is less than equal to largest distance in table then its value is stored and loop is broken
        for x in dbp_table:
            if self.temp_total_distance <= x.distance:
                self.dbp_price = x.price
                self.temp_total_distance = self.temp_total_distance - x.distance
                if self.temp_total_distance < 0:
                    self.temp_total_distance = 0
                break
        
        # In case distance travelled is greater than max distance in DBP table then we get max distance prce subtract it and then use DPA for left distance
        if self.dbp_price == 0:
            tt = DBP.objects.aggregate(models.Max('distance'))
            tt_price  = DBP.objects.get(distance = tt['distance__max'])
            self.dbp_price = tt_price.price
            self.temp_total_distance = self.temp_total_distance - tt['distance__max']

        # Get all data from TMF table
        tmf_table = TMF.objects.all()
        self.tmf_price = 0
        # If time is less than equal to largest time in table then its value is stored and loop is broken
        for x in tmf_table:
            if self.Total_time <= x.Time:
                self.tmf_price = x.price
                break
        # In case time is greater than max time in TMF table then we get max time price and use it 
        if self.tmf_price == 0:
            tt = TMF.objects.aggregate(models.Max('Time'))
            tt_price  = TMF.objects.get(Time = tt['Time__max'])
            self.tmf_price = tt_price.price

        # Calculating price
        self.dap_price = self.dap * self.temp_total_distance
        self.price = (float(self.dbp_price) + float(self.dap_price)) * float(self.tmf_price)

        # Saving price in DB
        super(Price, self).save(*args, **kwargs)