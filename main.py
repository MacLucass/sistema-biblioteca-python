from src.biblioteca import Biblioteca, BibliotecaErro


def exibir_menu() -> None:
    print("\n" + "=" * 55)
    print("   SISTEMA DE GERENCIAMENTO DE BIBLIOTECA (SGB)")
    print("=" * 55)
    print("1. Cadastrar Livro")
    print("2. Cadastrar Usuário")
    print("3. Consultar Livros (Título, Autor ou Ano)")
    print("4. Realizar Empréstimo")
    print("5. Realizar Devolução")
    print("6. Relatório: Livros Disponíveis")
    print("7. Relatório: Livros Emprestados")
    print("8. Relatório: Usuários Cadastrados")
    print("0. Sair")
    print("=" * 55)


def popular_dados_iniciais(bib: Biblioteca) -> None:
    """Carrega dados iniciais para facilitar testes rápidos."""
    bib.cadastrar_livro("Python Fluente", "Luciano Ramalho", 2015, 2)
    bib.cadastrar_livro("Arquitetura Limpa", "Robert C. Martin", 2019, 1)
    bib.cadastrar_livro("Engenharia de Dados", "Joe Reis", 2022, 3)
    bib.cadastrar_usuario("U01", "Lucas Corrêa", "lucas@email.com")
    bib.cadastrar_usuario("U02", "Rafaeli Sales", "rafa@email.com")


def main() -> None:
    biblioteca = Biblioteca()
    popular_dados_iniciais(biblioteca)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                print("\n--- CADASTRO DE LIVRO ---")
                titulo = input("Título: ")
                autor = input("Autor: ")
                ano = int(input("Ano de publicação: "))
                copias = int(input("Número de cópias: "))
                livro = biblioteca.cadastrar_livro(titulo, autor, ano, copias)
                print(f"[SUCESSO] Livro registrado: {livro}")

            elif opcao == "2":
                print("\n--- CADASTRO DE USUÁRIO ---")
                id_usr = input("ID de Identificação (ex: U03): ")
                nome = input("Nome completo: ")
                contato = input("Contato (Telefone/E-mail): ")
                usuario = biblioteca.cadastrar_usuario(id_usr, nome, contato)
                print(f"[SUCESSO] Usuário cadastrado: {usuario}")

            elif opcao == "3":
                print("\n--- CONSULTA DE LIVROS ---")
                termo = input("Digite título, autor ou ano (Enter para listar todos): ")
                resultados = biblioteca.consultar_livros(termo)
                if not resultados:
                    print("[AVISO] Nenhum livro encontrado para o termo informado.")
                else:
                    for item in resultados:
                        print(f" - {item}")

            elif opcao == "4":
                print("\n--- EMPRÉSTIMO DE LIVRO ---")
                id_usr = input("ID do Usuário: ")
                titulo = input("Título exato do Livro: ")
                biblioteca.emprestar_livro(id_usr, titulo)
                print(f"[SUCESSO] Empréstimo de '{titulo}' registrado para o ID {id_usr}!")

            elif opcao == "5":
                print("\n--- DEVOLUÇÃO DE LIVRO ---")
                id_usr = input("ID do Usuário: ")
                titulo = input("Título exato do Livro: ")
                biblioteca.devolver_livro(id_usr, titulo)
                print(f"[SUCESSO] Devolução de '{titulo}' concluída com sucesso!")

            elif opcao == "6":
                print("\n--- RELATÓRIO: LIVROS DISPONÍVEIS ---")
                disponiveis = biblioteca.listar_livros_disponiveis()
                if not disponiveis:
                    print("Nenhum livro disponível no momento.")
                for l in disponiveis:
                    print(f" - {l}")

            elif opcao == "7":
                print("\n--- RELATÓRIO: LIVROS EMPRESTADOS ---")
                emprestados = biblioteca.listar_livros_emprestados()
                if not emprestados:
                    print("Nenhum livro emprestado no momento.")
                for reg in emprestados:
                    print(f" - {reg}")

            elif opcao == "8":
                print("\n--- RELATÓRIO: USUÁRIOS CADASTRADOS ---")
                usuarios = biblioteca.listar_usuarios()
                for u in usuarios:
                    print(f" - {u}")

            elif opcao == "0":
                print("\nEncerrando o sistema. Até logo!")
                break

            else:
                print("[ERRO] Opção inválida. Digite um número de 0 a 8.")

        except ValueError:
            print("[ERRO DE ENTRADA] Ano e número de cópias devem ser números inteiros válidos.")
        except BibliotecaErro as e:
            print(f"[ERRO DE VALIDAÇÃO] {e}")
        except Exception as e:
            print(f"[ERRO INESPERADO] {e}")


if __name__ == "__main__":
    main()
