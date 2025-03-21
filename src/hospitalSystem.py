from collections import deque

class HospitalSystem:
    def __init__(self):
        self.fila = deque()  # Fila de pacientes
        self.historico = []  # Histórico de chamadas
        self.contador = 1    # Contador de senhas

    def gerar_senha(self):
        """Gera uma nova senha para um paciente e adiciona à fila."""
        senha = self.contador
        self.fila.append(senha)  # Adiciona a senha na fila
        self.contador += 1  # Incrementa o contador para a próxima senha
        print(f"Senha {senha} gerada e paciente adicionado à fila.")
    
    def chamar_proximo(self):
        """Chama o próximo paciente da fila (retira o primeiro da fila)."""
        if self.fila:
            senha = self.fila.popleft()  # Remove o primeiro paciente da fila
            self.historico.append(senha)  # Adiciona a senha ao histórico
            print(f"Paciente com a senha {senha} chamado para atendimento.")
        else:
            print("Não há pacientes na fila.")

    def reiniciar_contagem(self):
        """Reinicia a contagem de senhas."""
        self.contador = 1
        self.fila.clear()  # Limpa a fila de pacientes
        self.historico.clear()  # Limpa o histórico de chamadas
        print("Contagem de senhas reiniciada. Fila e histórico limpos.")

    def mostrar_historico(self):
        """Exibe o histórico de todas as senhas chamadas."""
        if self.historico:
            print("Histórico de chamadas:")
            for senha in self.historico:
                print(f"Senha {senha}")
        else:
            print("Nenhuma chamada foi feita ainda.")

    def mostrar_fila(self):
        """Exibe o estado atual da fila de pacientes."""
        if self.fila:
            print("Fila de pacientes:")
            for senha in self.fila:
                print(f"Senha {senha}")
        else:
            print("A fila está vazia.")
