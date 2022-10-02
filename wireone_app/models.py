from django.db import models
import json
# Create your models here.

class DBP(models.Model):
    data = models.CharField(max_length=10000)
    enabled = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.enabled:
            try:
                temp = DBP.objects.get(enabled=True)
                if self != temp:
                    temp.enabled = False
                    temp.save()
            except DBP.DoesNotExist:
                pass
        super(DBP, self).save(*args, **kwargs)

class TMF(models.Model):
    data = models.CharField(max_length=10000)
    enabled = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.enabled:
            try:
                temp = TMF.objects.get(enabled=True)
                if self != temp:
                    temp.enabled = False
                    temp.save()
            except TMF.DoesNotExist:
                pass
        super(TMF, self).save(*args, **kwargs)

class DAP(models.Model):
    value = models.IntegerField()
    enabled = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.enabled:
            try:
                temp = DAP.objects.get(enabled=True)
                if self != temp:
                    temp.enabled = False
                    temp.save()
            except DAP.DoesNotExist:
                pass
        super(DAP, self).save(*args, **kwargs)

class Price(models.Model):
    Total_distance = models.IntegerField()
    Total_time = models.IntegerField()
    price = models.IntegerField(default = 0)

    
    def save(self, *args, **kwargs):
        # making copy of total distance
        self.temp_total_distance = self.Total_distance

        # Get all data from DBP table
        dbp_table = DBP.objects.filter(enabled = True)
        
        self.json_dbp_data = json.loads(str(dbp_table[0].data))
        self.dbp_price = 0
        for x in self.json_dbp_data:
            if self.temp_total_distance < x['distance']:
                self.price += x['price']
                self.temp_total_distance -= x['distance']
                break
        
        if self.dbp_price == 0:
            self.dbp_price = self.json_dbp_data[-1]['price']
            self.price += self.dbp_price
            self.temp_total_distance = self.temp_total_distance - self.json_dbp_data[-1]['distance']
        
        # Get all data from TMF table
        tmf_table = TMF.objects.filter(enabled = True)
        self.tmf_price = 0
        self.json_tmf_data = json.loads(str(tmf_table[0].data))
        for x in self.json_tmf_data:
            if self.Total_time <= x['time']:
                self.tmf_price += x['price']
                break

        if self.tmf_price == 0:
            self.tmf_price = self.json_tmf_data[-1]['price']

        # Get all data from DAP table
        dap_table = DAP.objects.filter(enabled = True)
        self.dap_price = dap_table[0].value

        # Calculating price
        self.dap_price = self.dap_price * self.temp_total_distance
        self.price = (float(self.dbp_price) + float(self.dap_price)) * float(self.tmf_price)

        # Saving price in DB
        super(Price, self).save(*args, **kwargs)