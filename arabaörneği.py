class Car:
    def __init__(self,index,make,model,speed):
        self.index=index
        self.make=make
        self.model=model
        self.speed=speed
        
    def show_info (cars,car_no):
        print(f'Araba markasi={cars[car_no-1].make}')
        print(f'Araba modeli={cars[car_no-1].model}')
        print(f'Araba hizi={cars[car_no-1].speed}')

    def speeding (cars,car_no,answer):
        print(f'Araba anlik hiziniz:{cars[car_no-1].speed}')
        cars[car_no-1].speed=cars[car_no-1].speed+answer
        print(f'Araba yeni hiziniz:{cars[car_no-1].speed}')

    def slow_down (cars,car_no,answer2):
        print(f'Araba anlik hiziniz:{cars[car_no-1].speed}')
        cars[car_no-1].speed=cars[car_no-1].speed+answer2
        print(f'Araba yeni hiziniz:{cars[car_no-1].speed}')
        
        
        while True:
            print("""1. Araç ekle
            2. Araç bilgilerini göster
            3. Hizlan
            4. Yavaşla""")
            process = input('Yapmak istediginiz islem nedir?=')
            cars=[]
            index = 0
            match process:
                case 1:
                    index=index+1
                    make=input('Aracin markasi nedir ?=')
                    model=input('Aracin modeli nedir ?=')
                    speed=input('Aracin Anlik hizi nedir?=')
                    new_car=Car(index,make,model,speed)
                    cars.append(new_car)
                    print(f'Araba no:{index}')  
                    break  
                   
                case 2:
                    car_no=input('Araba numaraniz kactir?=')
                    show_info(cars,car_no)
                    break
                case 3:
                    answer=input('Aarabaniz ne kadar hizlansin=')
                    speeding(cars,car_no,answer)
                    break
                case 4:
                    answer2=input('Arabaniz ne kadar yavaslasin=')
                    slow_down(cars,car_no,answer2)
                    break
                




    
    




     

            