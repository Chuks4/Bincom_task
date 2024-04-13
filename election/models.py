# from django.db import models

# # Create your models here.
# class LocalGovResult(models.Model):
#     result_id = models.IntegerField(default=0)
#     lga_name = models.CharField(max_length=20, null=True, blank=True)
#     party_abbreviation = models.CharField(max_length=10, null=True, blank=True)
#     party_score = models.IntegerField(default=0)
#     entered_by_user = models.CharField(max_length=30)
#     date_entered = models.DateTimeField(auto_now_add=True)
#     user_ip_address = models.CharField(max_length=20)
    
    
# class PollingResult(models.Model):    
#     result_id = models.IntegerField(default=0)
#     polling_unit_uniqueid = models.IntegerField(default=0)
#     party_abbreviation = models.CharField(max_length=10, null=True, blank=True)
#     entered_by_user = models.CharField(max_length=30)
#     date_entered = models.DateTimeField(auto_now_add=True)
#     user_ip_address = models.CharField(max_length=20)

# class StateResult(models.Model):
#     result_id = models.IntegerField(default=0)
#     state_name = models.CharField(max_length=20, null=True, blank=True)
#     party_abbreviation = models.CharField(max_length=10, null=True, blank=True)
#     party_score = models.IntegerField(default=0)
#     entered_by_user = models.CharField(max_length=30)
#     date_entered = models.DateTimeField(auto_now_add=True)
#     user_ip_address = models.CharField(max_length=20)
    
    


# class LocalGov(models.Model):
#     uniqueid = models.IntegerField()
#     lga_id = models.IntegerField()
#     lga_name = models.CharField(max_length=30)
#     state_id = models.ForeignKey('StateGov', on_delete=models.CASCADE)
#     lga_description = models.CharField(max_length=50)
#     entered_by_user = models.CharField(max_length=30)
#     date_entered = models.DateTimeField(auto_now_add=True)
#     user_ip_address = models.CharField(max_length=20)
    

# class Party(models.Model):
#     id = models.IntegerField()
#     party_id = models.IntegerField()
#     party_name = models.CharField(max_length=20)
    
    
# class PollingUnit(models.Model):
#     unique_id = models.IntegerField()
#     polling_unit_id = models.IntegerField()
#     ward_id = models.IntegerField()
#     lga_id = models.ForeignKey(LocalGov, on_delete=models.CASCADE)
#     unique_ward_id = models.IntegerField()
#     polling_unit_number = models.IntegerField()
#     polling_unit_name = models.CharField(max_length=50)
#     polling_unit_description = models.CharField(max_length=100)
#     lat = models.CharField(max_length=20)
#     long = models.CharField(max_length=20)
#     entered_by_user = models.CharField(max_length=30)
#     date_entered = models.DateTimeField(auto_now_add=True)
#     user_ip_address = models.CharField(max_length=20)
    
    

# class StateGov(models.Model):
#     state_id = models.IntegerField()
#     state_name = models.CharField(max_length=30)
    

# class Ward(models.Model):
#     uniqueid = models.IntegerField()
#     ward_id = models.IntegerField()
#     ward_name = models.CharField(max_length=30)
#     lga_id = models.ForeignKey(LocalGov, on_delete=models.CASCADE)
#     ward_description = models.CharField(max_length=50)
#     entered_by_user = models.CharField(max_length=30)
#     date_entered = models.DateTimeField(auto_now_add=True)
#     user_ip_address = models.CharField(max_length=20)
    