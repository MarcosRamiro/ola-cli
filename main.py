import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import pyfiglet


@click.command()
@click.argument("nome")
@click.option("--formal", is_flag=True, help="Usa saudação formal")
@click.option(
    "--lang",
    default="pt",
    type=click.Choice(["pt", "en", "es"]),
    help="Idioma da saudação",
)
def cumprimentar(nome, formal, lang):
    """Script que cumprimenta um usuário pelo nome, com saída formatada usando Rich."""
    console = Console()

    # Dicionário com saudações em diferentes idiomas
    saudacoes = {
        "pt": {
            "informal": f"Olá, {nome}! Seja bem-vindo! 👋👋",
            "formal": f"Olá, Sr./Sra. {nome}. É um prazer recebê-lo(a).",
        },
        "en": {
            "informal": f"Hello, {nome}! Welcome! 👋",
            "formal": f"Good day, Mr./Ms. {nome}. It is a pleasure to meet you.",
        },
        "es": {
            "informal": f"¡Hola, {nome}! ¡Bienvenido! 👋",
            "formal": f"Buenos días, Sr./Sra. {nome}. Es un placer recibirle.",
        },
    }

    # Seleciona a saudação apropriada
    tipo = "formal" if formal else "informal"
    mensagem = saudacoes[lang][tipo]
    raw_title = "saudacao"

    figlet_input = raw_title

    banner_text = pyfiglet.figlet_format(figlet_input)

    console.print(Align.center(Text(banner_text, style="bold green")))
    # Mostra o título com acento logo abaixo (como subtítulo legível)
    console.print(Align.center(Text(raw_title, style="bold magenta")))
    console.print()

    # Usa um painel para a mensagem principal
    panel = Panel.fit(mensagem, title="Mensagem", border_style="blue")
    console.print(Align.left(panel))

    console.print()
    console.print(
        Align.left(Text(f"✨ Saudação gerada em: {lang.upper()}", style="dim"))
    )
    console.print()


if __name__ == "__main__":
    cumprimentar()
