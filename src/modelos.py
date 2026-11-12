from dataclasses import dataclass, field
from typing import List


@dataclass
class Livro:
    """Representa a entidade Livro no acervo da biblioteca."""
    titulo: str
    autor: str
    ano: int
    copias_totais: int
    copias_disponiveis: int = field(init=False)

    def __post_init__(self):
        # Ao cadastrar um livro novo, o estoque disponível começa igual ao total
        self.copias_disponiveis = self.copias_totais

    def __str__(self) -> str:
        return (
            f"Título: '{self.titulo}' | Autor: {self.autor} | Ano: {self.ano} | "
            f"Disponíveis: {self.copias_disponiveis}/{self.copias_totais}"
        )


@dataclass
class Usuario:
    """Representa um usuário cadastrado na biblioteca."""
    id_usuario: str
    nome: str
    contato: str
    livros_emprestados: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        livros = ", ".join(self.livros_emprestados) if self.livros_emprestados else "Nenhum"
        return (
            f"ID: {self.id_usuario} | Nome: {self.nome} | "
            f"Contato: {self.contato} | Em posse de: [{livros}]"
        )
