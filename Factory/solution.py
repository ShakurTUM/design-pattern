# Precibake Monitoring Service

class Grill:
    def annual_cost(self):
        return 50000
 
    def __str__(self):
        return "Grill"
 
class Fryer:
    def annual_cost(self):
        return 100000
 
    def __str__(self):
        return "Fryer"
 
class Oven:
    def annual_cost(self):
        return 70000
 
    def __str__(self):
        return 'Oven'


def PBFactory(service_name: str):
    factory = {
        "Grill": Grill,
        "Fryer": Fryer,
        "Oven": Oven,
    }
    return factory[service_name]()

if __name__=="__main__":
    g = PBFactory("Grill")
    f = PBFactory("Fryer")
    o = PBFactory("Oven")
 
    print("\nPrecibake Monitoring Service")
    print("=" * 50)

    print(f'{str(g)} monitoring annual cost {g.annual_cost()} euros')
    print(f'{str(f)} monitoring annual cost {f.annual_cost()} euros')
    print(f'{str(o)} monitoring annual cost {o.annual_cost()} euros\n')