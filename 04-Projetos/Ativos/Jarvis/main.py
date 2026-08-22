import argparse
import sys

from jarvis import ui
from jarvis.assistant import executar

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jarvis - Assistente pessoal estilo FRIDAY")
    parser.add_argument("--teclado", action="store_true", help="Força o modo de teclado (sem microfone)")
    parser.add_argument("--teste", action="store_true", help="Mostra o diagnóstico do sistema")
    parser.add_argument("--voz", action="store_true", help="Testa a voz falando uma frase")
    args = parser.parse_args()
    try:
        ui.habilitar_cores()
        if args.voz:
            from jarvis.voice import testar_voz
            testar_voz()
            sys.exit(0)
        executar(usar_mic=False if args.teclado else None, teste=args.teste)
    except KeyboardInterrupt:
        sys.exit(0)