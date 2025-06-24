from t1 import DataIngestionConfig

class dataobj:
    def __init__(self , obj9 :DataIngestionConfig = DataIngestionConfig(name ="suresh" , place = "vijayawada")):
        self.obj9= obj9
        
obj5 = dataobj()
print(obj5)
print(obj5.obj9.name )
print(obj5.obj9.place)
