# Precibake Monitoring Service

from abc import ABC, abstractclassmethod

class PBMonitoring(ABC):

    @abstractclassmethod
    def annual_cost() -> float:
        raise NotImplementedError
    

class Grill(PBMonitoring):
    def annual_cost(self) -> float:
        return 50000
 
    def __str__(self):
        return "Grill"
 
class Fryer(PBMonitoring):
    def annual_cost(self) -> float:
        return 100000
 
    def __str__(self):
        return "Fryer"
 
class Oven(PBMonitoring):
    def annual_cost(self) -> float:
        return 70000
 
    def __str__(self):
        return 'Oven'

class PBMonitoringService:
    def __init__(self, monitoring_factory = None) -> None:
        self._monitoring_factory = monitoring_factory

    def show_monitoring_summary(self) -> None:
        monitoring_service = self._monitoring_factory()
        print(f'Monitoring service: {str(monitoring_service)}')
        print(f'Annual cost: {monitoring_service.annual_cost()}')

if __name__=="__main__":
    available_services = [Grill, Fryer, Oven]

    print("\nPrecibake Monitoring Service")
    print("=" * 50)
    for item in available_services:
        service = PBMonitoringService(monitoring_factory=item)
        service.show_monitoring_summary()
        print("\n")
    
    print("=" * 50)