# Precibake Monitoring Service

class PBMonitoringService:
    def __init__(self, monitoring_factory = None) -> None:
        self._monitoring_factory = monitoring_factory

    def show_monitoring_summary(self) -> None:
        monitoring_service = self._monitoring_factory()
        print(f'Monitoring service: {str(monitoring_service)}')
        print(f'Annual cost: {monitoring_service.annual_cost()}')

class Grill:
    def annual_cost(self) -> float:
        return 50000
 
    def __str__(self):
        return "Grill"
 
class Fryer:
    def annual_cost(self) -> float:
        return 100000
 
    def __str__(self):
        return "Fryer"
 
class Oven:
    def annual_cost(self) -> float:
        return 70000
 
    def __str__(self):
        return 'Oven'

if __name__=="__main__":
    available_services = [Grill, Fryer, Oven]

    print("\nPrecibake Monitoring Service")
    print("=" * 50)
    for item in available_services:
        service = PBMonitoringService(monitoring_factory=item)
        service.show_monitoring_summary()
        print("\n")
    
    print("=" * 50)