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
        dbp_table = DBP.objects.all()
        self.temp_total_distance = self.Total_distance
        self.dbp_price = 0
        for x in dbp_table:
            if self.temp_total_distance <= x.distance:
                self.dbp_price = x.price
                self.temp_total_distance = self.temp_total_distance - x.distance
                if self.temp_total_distance < 0:
                    self.temp_total_distance = 0
                break
        if self.dbp_price == 0:
            tt = DBP.objects.aggregate(models.Max('distance'))
            tt_price  = DBP.objects.get(distance = tt['distance__max'])
            self.dbp_price = tt_price.price
            self.temp_total_distance = self.temp_total_distance - tt['distance__max']

        print(self.dbp_price)
        print(self.temp_total_distance)
        tmf_table = TMF.objects.all()
        self.tmf_price = 0
        for x in tmf_table:
            if self.Total_time <= x.Time:
                self.tmf_price = x.price
                break
        
        if self.tmf_price == 0:
            tt = TMF.objects.aggregate(models.Max('Time'))
            tt_price  = TMF.objects.get(Time = tt['Time__max'])
            self.tmf_price = tt_price.price

        print(self.tmf_price)

        self.dap_price = self.dap * self.temp_total_distance

        print(self.dap_price)

        self.price = (float(self.dbp_price) + float(self.dap_price)) * float(self.tmf_price)

        super(Price, self).save(*args, **kwargs)