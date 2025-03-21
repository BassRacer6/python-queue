from hospitalSystem import HospitalSystem

class Menu:
    def __init__(self):
        self.sistema = HospitalSystem()

    def exibir_menu(self):
        """Exibe o menu de navegação"""
        while True:
            print("\nMenu:")
            print("1. Gerar nova senha")
            print("2. Chamar próximo paciente")
            print("3. Reiniciar contagem de senhas")
            print("4. Mostrar histórico de chamadas")
            print("5. Mostrar fila de pacientes")
            print("6. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.sistema.gerar_senha()
            elif opcao == "2":
                self.sistema.chamar_proximo()
            elif opcao == "3":
                self.sistema.reiniciar_contagem()
            elif opcao == "4":
                self.sistema.mostrar_historico()
            elif opcao == "5":
                self.sistema.mostrar_fila()
            elif opcao == "6":
                print("Saindo...")
                break  # Sai do loop e termina o programa
            else:
                print("Opção inválida, tente novamente.")
