#singletan function
import threading#this is for blocking multi treading (yadi do ya do se jade log ka saath object banane ka try kare)

class Singletan:
    _instance=None
    _lock=threading.Lock()
    def __new__(cls):

        if cls._instance is None:#first check without lock
            with cls._lock:
                if cls._instance is None:#double check with lock
              
                    print("Creating first time Object:")
                    cls._instance=super().__new__(cls)
                else:
                    print("purana object fir mil raha hai")   

        return cls._instance
s1=Singletan()
s2=Singletan()
s3=Singletan()
print(s1 is s3)
print(id(s1), id(s2), id(s3))