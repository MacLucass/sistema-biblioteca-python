from typing import Dict, List
from src.modelos import Livro, Usuario


class BibliotecaErro(Exception):
    """Exceção personalizada para erros de regra de negócio da biblioteca."""
    pass


class Biblioteca:
    """Gerencia o acervo de livros, usuários, empréstimos e relatórios."""

    def __init__(self):
        self.livros: Dict[str, Livro] = {}
        self.usuarios: Dict[str, Usuario] = {}

    def _chave_livro(self, titulo: str) -> str:
        return titulo.strip().lower()

    def cadastrar_livro(self, titulo: str, autor: str, ano: int, copias: int) -> Livro:
        """Cadastra um novo livro ou adiciona cópias caso já exista."""
        if not titulo.strip() or not autor.strip():
            raise BibliotecaErro("Título e autor são obrigatórios.")
        if copias <= 0:
            raise BibliotecaErro("A quantidade de cópias deve ser maior que zero.")

        chave = self._chave_livro(titulo)
        if chave in self.livros:
            livro_existente = self.livros[chave]
            livro_existente.copias_totais += copias
            livro_existente.copias_disponiveis += copias
            return livro_existente

        novo_livro = Livro(
            titulo=titulo.strip(),
            autor=autor.strip(),
            ano=ano,
            copias_totais=copias
        )
        self.livros[chave] = novo_livro
        return novo_livro

    def cadastrar_usuario(self, id_usuario: str, nome: str, contato: str) -> Usuario:
        """Cadastra um novo usuário validando duplicidade de ID."""
        id_limpo = id_usuario.strip()
        if not id_limpo or not nome.strip():
            raise BibliotecaErro("ID e Nome do usuário são obrigatórios.")
        if id_limpo in self.usuarios:
            raise BibliotecaErro(f"Já existe um usuário cadastrado com o ID '{id_limpo}'.")

        novo_usuario = Usuario(
            id_usuario=id_limpo,
            nome=nome.strip(),
            contato=contato.strip()
        )
        self.usuarios[id_limpo] = novo_usuario
        return novo_usuario

    def consultar_livros(self, termo: str) -> List[Livro]:
        """Consulta livros por título, autor ou ano de publicação."""
        termo_busca = termo.strip().lower()
        if not termo_busca:
            return list(self.livros.values())

        resultados = []
        for livro in self.livros.values():
            if (
                termo_busca in livro.titulo.lower()
                or termo_busca in livro.autor.lower()
                or termo_busca == str(livro.ano)
            ):
                resultados.append(livro)
        return resultados

    def emprestar_livro(self, id_usuario: str, titulo: str) -> None:
        """Realiza o empréstimo validando usuário, existência do livro e estoque."""
        id_limpo = id_usuario.strip()
        chave = self._chave_livro(titulo)

        if id_limpo not in self.usuarios:
            raise BibliotecaErro(f"Usuário com ID '{id_limpo}' não encontrado.")
        if chave not in self.livros:
            raise BibliotecaErro(f"Livro '{titulo}' não encontrado no acervo.")

        usuario = self.usuarios[id_limpo]
        livro = self.livros[chave]

        if livro.titulo in usuario.livros_emprestados:
            raise BibliotecaErro(f"O usuário {usuario.nome} já está com uma cópia de '{livro.titulo}'.")
        if livro.copias_disponiveis <= 0:
            raise BibliotecaErro(f"Todas as cópias de '{livro.titulo}' estão emprestadas no momento.")

        livro.copias_disponiveis -= 1
        usuario.livros_emprestados.append(livro.titulo)

    def devolver_livro(self, id_usuario: str, titulo: str) -> None:
        """Registra a devolução de um livro e recompõe o estoque disponível."""
        id_limpo = id_usuario.strip()
        chave = self._chave_livro(titulo)

        if id_limpo not in self.usuarios:
            raise BibliotecaErro(f"Usuário com ID '{id_limpo}' não encontrado.")
        if chave not in self.livros:
            raise BibliotecaErro(f"Livro '{titulo}' não pertence ao acervo da biblioteca.")

        usuario = self.usuarios[id_limpo]
        livro = self.livros[chave]

        if livro.titulo not in usuario.livros_emprestados:
            raise BibliotecaErro(f"O usuário {usuario.nome} não possui empréstimo ativo de '{livro.titulo}'.")

        livro.copias_disponiveis += 1
        usuario.livros_emprestados.remove(livro.titulo)

    def listar_livros_disponiveis(self) -> List[Livro]:
        """Retorna todos os livros com pelo menos 1 cópia disponível."""
        return [l for l in self.livros.values() if l.copias_disponiveis > 0]

    def listar_livros_emprestados(self) -> List[str]:
        """Retorna relação detalhada de livros atualmente emprestados e seus portadores."""
        relatorio = []
        for usuario in self.usuarios.values():
            for titulo_livro in usuario.livros_emprestados:
                relatorio.append(
                    f"Livro: '{titulo_livro}' -> Emprestado para: {usuario.nome} (ID: {usuario.id_usuario})"
                )
        return relatorio

    def listar_usuarios(self) -> List[Usuario]:
        """Retorna todos os usuários cadastrados."""
        return list(self.usuarios.values())
