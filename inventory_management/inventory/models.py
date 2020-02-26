from django.db import models

# Create your models here.
class Item(models.Model):

	# choices = (
	# 	('AVAILABLE', 'Item ready to be purchased'),
	# 	('SOLD', 'Item sold'),
	# 	('RESTOCKING', 'Item restocking'),
	# )
	# status = models.CharField(max_length=10, choices=choices, default='SOLD')
	
	sku = models.CharField(max_length=50, blank=False, unique=True)
	onhand = models.IntegerField()
	description = models.TextField(blank=False)


	def __str__(self):
		return 'SKU: {0} - Description: {1}'.format(self.sku, self.description)