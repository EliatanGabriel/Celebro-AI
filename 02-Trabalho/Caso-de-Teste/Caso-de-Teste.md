---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Caso de Teste

#area/trabalho #trabalho/caso-de-teste #conceito

**Resumo:** Descrição estruturada de um cenário a ser validado.

## Conceitos-chave
- Caso de teste descreve pré-condições, passos, dados e resultado esperado de um cenário.
- É a unidade básica da documentação de testes e base para execução manual e automação.
- Bem escrito, serve como requisito verificável e reduz ambiguidade.

## Exemplos
```
ID: CT-014
Título: Login com e-mail válido e senha correta
Pré-condições: usuário cadastrado e ativo
Dados: email "qa@exemplo.com", senha "S3cret!"
Passos:
1. Abrir /login
2. Preencher e-mail
3. Preencher senha
4. Clicar em "Entrar"
Resultado esperado: redireciona para o dashboard e exibe nome do usuário
Prioridade: alta
```

## Boas práticas
- Escrever um único cenário por caso; separar variações em casos distintos.
- Usar pré-condições e dados concretos e repetíveis.
- Definir resultado esperado verificável (mensagem, URL, estado).
- Revisar os casos com o time e manter a rastreabilidade com o requisito.

## Armadilhas comuns
- Caso com vários cenários misturados, difícil de manter e diagnosticar.
- Resultado esperado vago ("funciona") sem critério objetivo.
- Depender de dados que mudam ou não existem no ambiente.
- Casos desatualizados após mudança de requisito.

## Relacionadas
- [[Testes-Automatizados]]
- [[Bug-Report]]
- [[Documentacao-de-Testes]]