
class MySingletonClass:
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(MySingletonClass, cls).__new__(cls)
    
    return cls.instance
   
class MySingletonChildClass(MySingletonClass):
    pass

def test_singleton_class() -> None:
    singleton_1 = MySingletonClass()
    singleton_2 = MySingletonChildClass()

    if singleton_1 is singleton_2:
       print("Singleton class..!")
    else:
       print("Not a singleton class...!")

if __name__== '__main__':
    print("\nSingleton Pattern")
    print("=" * 50)
    
    test_singleton_class()