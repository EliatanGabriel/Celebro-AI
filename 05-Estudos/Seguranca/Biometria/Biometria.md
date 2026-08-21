---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Biometria

#area/estudos #estudos/seguranca #conceito

**Resumo:** Autenticação baseada em características físicas ou comportamentais do usuário, como impressão digital, reconhecimento facial e íris.

## Conceitos-chave
- **Tipos:** fisiológicas (digital, face, íris, palma) e comportamentais (dinâmica de digitação, marcha).
- **Fator "algo que você é":** usado como fator de [[MFA]] junto com senha/token.
- **Enrollment e template:** na primeira captura é criado um template (não a imagem bruta) para comparações futuras.
- **FAR e FRR:** taxa de falso aceite (impostor aprovado) vs. falso rejeitado (usuário legítimo bloqueado); há trade-off entre as duas.
- **Liveness detection:** verifica se a amostra vem de pessoa viva (anti-spoofing).
- **Não revogabilidade:** dados biométricos não podem ser "trocados" como uma senha após vazamento.

## Exemplos
```
# Fluxo típico (conceitual)
captura = sensor.capturar()
template = biometrico.extrair_template(captura)
if biometrico.comparar(template, template_armazenado) > limiar:
    autenticar(usuario)          # FRR/FAR configurados pelo limiar
else:
    registrar_falha(usuario)
```

## Boas práticas
- Usar biometria como fator adicional, não como único fator de autenticação.
- Armazenar apenas templates, nunca imagens brutas, e proteger com criptografia.
- Aplicar liveness detection para mitigar spoofing (fotos, moldes).
- Ajustar limiares conforme o contexto de risco da aplicação.
- Ter plano de fallback quando a biometria falhar ou dados vazarem.

## Armadilhas comuns
- Confiar em biometria como prova infalível — templates podem ser falsificados ou reutilizados.
- Não prever recuperação de conta quando o usuário não consegue se autenticar.
- Ignorar privacidade: coletar dados biométricos sem consentimento e transparência (ver [[Privacidade]]).
- Comparar biometria com senha: ela é conveniente, mas não revogável.

## Relacionadas
- [[Autenticacao]]
- [[MFA]]
- [[Privacidade]]