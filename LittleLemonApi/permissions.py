

class Permissions:
    @staticmethod
    def is_manager(request):
        return request.user.groups.filter(name='Manager').exists()
    
    @staticmethod
    def is_customer(request):
        return request.user.groups.filter(name='Customer').exists()
    
    @staticmethod
    def is_delivery_crew(request):
        return request.user.groups.filter(name='Delivery Crew').exists()
