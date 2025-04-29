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
 
if __name__=="__main__":
    g = Grill()
    f = Fryer()
    o = Oven()
 
    print("\nPrecibake Monitoring Service")
    print("=" * 50)

    print(f'{str(g)} monitoring annual cost {g.annual_cost()} euros')
    print(f'{str(f)} monitoring annual cost {f.annual_cost()} euros')
    print(f'{str(o)} monitoring annual cost {o.annual_cost()} euros\n')