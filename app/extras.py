from app.models import Centers

def initialize_centers():
    Centers.objects.update_or_create(center_name='Jankupuram')
    Centers.objects.update_or_create(center_name='Faizullaganj 1')
    Centers.objects.update_or_create(center_name='Faizullaganj 2')
    Centers.objects.update_or_create(center_name='Aliganj')
    Centers.objects.update_or_create(center_name='Triveni Nagar')
    Centers.objects.update_or_create(center_name='Daliganj')
    Centers.objects.update_or_create(center_name='Khadra')
    Centers.objects.update_or_create(center_name='Hussainabad')
    Centers.objects.update_or_create(center_name='Daulatganj')
    Centers.objects.update_or_create(center_name='Thakurganj')