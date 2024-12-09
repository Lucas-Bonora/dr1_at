from collections import deque

class CustomerSupportQueue:
    def __init__(self):
        self.queue = deque()  

    def add_ticket(self, ticket):
      
        self.queue.append(ticket)
        print(f"Chamado '{ticket}' adicionado à fila.")

    def process_ticket(self):
      
        if self.queue:
            ticket = self.queue.popleft()
            print(f"Processando chamado: {ticket}")
        else:
            print("Não há chamados para processar.")

# Exemplo de uso
support_queue = CustomerSupportQueue()
support_queue.add_ticket("Chamado 1")
support_queue.add_ticket("Chamado 2")
support_queue.add_ticket("Chamado 3")

support_queue.process_ticket()  
support_queue.process_ticket() 
support_queue.process_ticket()  
support_queue.process_ticket() 
