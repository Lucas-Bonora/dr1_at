class BrowserNavigation:
    def __init__(self):
        self.back_stack = []  
        self.forward_stack = []  
        self.current_page = None

    def visit(self, url):
        if self.current_page:
            self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()  
        print(f"Visitando: {self.current_page}")

    def go_back(self):
        if self.back_stack:
            self.forward_stack.append(self.current_page)
            self.current_page = self.back_stack.pop()
            print(f"Voltando para: {self.current_page}")
        else:
            print("Não há páginas para voltar.")

    def go_forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current_page)
            self.current_page = self.forward_stack.pop()
            print(f"Avançando para: {self.current_page}")
        else:
            print("Não há páginas para avançar.")

browser = BrowserNavigation()
browser.visit("primeiraPagina.com")
browser.visit("segundaPagina.com")
browser.visit("terceiraPagina.com")
browser.go_back()  
browser.go_back()  
browser.go_forward()  
browser.visit("quartaPagina.com")  
browser.go_back()  
