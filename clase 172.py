class Doctor:
    def __init__(self):
        print("esta es la clase doctor")
    def BMI(weight,height):
        bmi=weight/(height*height)
        print("tu IMC es: "+str(bmi))
    def hart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("muy bien tu frecuensia cardiaca esta bien")
        else:
            print("tu frecuencia cardiaca no esta bien revisala")

class Patient(Doctor):
    def __init__(self,name,weight,height,heart_rates):
        self.patient_name=name
        self.patient_weight=weight
        self.patient_height=height
        self.patient_heart_rates=heart_rates
    def healthCheck(self):
        print("\n Nombre del paciente"+ self. patient_name)
        Doctor.BMI(self.patient_weight, self.patient_height)
        Doctor.heart_rate(self.patient_heart_rates)
       
patient1 = Patient("miguel", "60", "1.60", "80")
patient1.healthCheck()
        
