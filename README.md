# 📚 Sistema de Gerenciamento de Biblioteca (SGB)

Projeto desenvolvido em **Python** aplicando **Programação Orientada a Objetos (POO)**, modularização e estruturas de dados em memória com busca otimizada O(1) para catalogação, controle de empréstimos, devoluções e emissão de relatórios via CLI.

## 🚀 Funcionalidades
- **Cadastro de Acervo e Usuários:** Validação de dados e incremento automático de estoque para títulos existentes.
- **Consultas Flexíveis:** Busca por título, autor ou ano de publicação.
- **Controle de Empréstimos e Devoluções:** Verificação de disponibilidade de cópias em tempo real e prevenção de empréstimos duplicados.
- **Tratamento de Exceções:** Exceções customizadas (`BibliotecaErro`) para regras de negócio e validação de tipos de entrada.
- **Relatórios Operacionais:** Listagem de livros disponíveis, exemplares emprestados (com rastreamento de portador) e usuários ativos.

## 📂 Estrutura do Projeto
```text
sistema-biblioteca-python/
├── src/
│   ├── __init__.py
│   ├── modelos.py      # Entidades de dados (Livro e Usuario com @dataclass)
│   └── biblioteca.py   # Regras de negócio, validações e exceções
├── main.py             # Interface interativa de console (CLI)
└── README.md           # Documentação do projeto
```

## 🛠️ Como Executar
Pré-requisito: **Python 3.10+** instalado.

```bash
# Clone o repositório
git clone https://github.com/MacLucass/sistema-biblioteca-python.git
cd sistema-biblioteca-python

# Execute a aplicação
python3 main.py
```

## 👨‍💻 Autor
Desenvolvido por **Lucas Ricardo Machado Corrêa** — Projeto Integrado (Arquitetura de Dados).
