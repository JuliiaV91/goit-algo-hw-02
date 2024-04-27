
from queue import Queue

#Створити чергу заявок
queue = Queue(maxsize=4)
# відстеження кількості елементів у черзі
request_num = 0

def main ():
    global request_num
    while True:
        new_request = input("Натисніть enter, щоб створити нову заявку; введіть exit, щоб вийти --> ")
        if new_request.strip().lower() == 'exit':
            break  
        else: 
            generate_request()  
            print(f"Наразі {request_num + 1} заявки. Очікуйте.")
            process_request()  

def generate_request():
    global request_num
    if not queue.full():
        request = request_num + 1 
        print (f"Ваш запит номер:{request}")
        queue.put(request)
        print (f"Ваш запит прийнято. Очікуйте.")
    else:
        print ("Заявки не приймаються. Спробуйте пізніше.")

def process_request():
    global request_num
    if not queue.empty():
        current_request = queue.get()
        request_num = current_request 
        print(f"Наразі виконується заявка {current_request}. Очікуйте.")   
    else:
        print (f"Заявки відсутні.")

if __name__ == "__main__":
    main() 

    
