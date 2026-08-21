---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Assembly

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem de baixo nível que representa diretamente as instruções do processador, usada em sistemas embarcados, drivers, boot e engenharia reversa.

## Conceitos-chave
- Paradigma imperativo de baixo nível, com mnemônicos (mov, add, jmp) mapeados 1:1 para opcodes do CPU.
- Sem tipagem de alto nível: os dados são tratados como bytes, words e words duplas conforme a arquitetura.
- A montagem (assembling) converte o código-fonte em código de máquina via assembler (ex.: NASM, GAS).
- Opera sobre registradores (eax, rbx, etc.), memória RAM e pilha (stack); cada arquitetura (x86, x86-64, ARM, RISC-V) tem conjunto de instruções próprio.
- Acesso direto ao hardware, o que exige controle total do programador sobre memória e periféricos.
- Utilizada em kernels, drivers, firmwares, bootloaders e em trechos de performance crítica de outras linguagens.

## Exemplos
```asm
; x86-64 (NASM) — programa "Olá, mundo" via chamada de sistema
section .data
    msg db "Olá, mundo", 0xa
    len equ $-msg

section .text
    global _start
_start:
    mov rax, 1        ; syscall write
    mov rdi, 1        ; fd = stdout
    mov rsi, msg      ; ponteiro para a mensagem
    mov rdx, len      ; tamanho
    syscall
    mov rax, 60       ; syscall exit
    xor rdi, rdi
    syscall
```

## Boas práticas
- Comente cada instrução explicando a intenção, pois o código é ilegível por natureza.
- Prefira instruções simples e evite "truques" obscuros que comprometem a manutenibilidade.
- Conheça a convenção de chamada da plataforma (System V AMD64, cdecl, etc.) ao interoperar com C.
- Teste em emulador ou VM antes de executar em hardware real para evitar danos.
- Use assembler com macros e símbolos (labels) em vez de endereços numéricos fixos.

## Armadilhas comuns
- Confundir ordem dos operandos: em AT&T (Intel) a ordem é destino/origem, mas em GAS o padrão é origem/destino.
- Esquecer que cada arquitetura tem sintaxe e conjunto de instruções diferentes — código não é portável.
- Usar registradores de 32 bits em contexto de 64 bits, truncando endereços e causando segmentation fault.
- Esquecer de preservar registradores callee-saved ao chamar funções externas.
- Desalinhar a pilha, violando o ABI e corrompendo a execução.

## Relacionadas
- [[C]]