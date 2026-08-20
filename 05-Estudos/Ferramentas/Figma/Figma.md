---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Figma

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Ferramenta colaborativa baseada em navegador para design de interfaces e prototipagem, com componentes reutilizáveis, design systems, comentários em tempo real e modo de desenvolvimento para engenharia.

## Conceitos-chave
- **Frames e Autolayout**: frames funcionam como containers; Auto Layout define espaçamento, alinhamento e responsividade dos elementos internos.
- **Components e Variants**: componentes reutilizáveis com propriedades de variante (estado, tamanho, cor) que centralizam mudanças.
- **Design system / Libraries**: bibliotecas de estilos e componentes publicadas e compartilhadas entre arquivos e times.
- **Prototipagem**: conexões entre frames com transições, interações e overlays para validar fluxos navegáveis.
- **Dev Mode**: modo de inspeção para desenvolvedores — CSS, tokens, dimensionamento e especificações de spacing.
- **Colaboração**: comentários, edição simultânea, histórico de versões e multiplayers.

## Exemplos
Exportar um componente em diferentes variantes:

```bash
# CLI (plugin/framework de terceiros) — padrão comum:
npx tokens-transformer tokens.json tokens-out.json --expandTypography
```

Configuração de tokens compartilhada (ex.: Style Dictionary):

```json
{
  "color": {
    "primary": { "value": "#2563eb", "type": "color" }
  },
  "spacing": {
    "md": { "value": "16px", "type": "dimension" }
  }
}
```

## Boas práticas
- Use Auto Layout desde o início; boxes manuais dificultam manutenção e responsividade.
- Centralize decisões em um design system com tokens e publique como library para o time.
- Nomeie layers, frames e variantes de forma consistente para o Dev Mode gerar classes úteis.
- Valide fluxos com protótipos antes de implementar, envolvendo o time de engenharia no review.
- Atualize versões das libraries com notes de changelog para comunicar alterações quebradas.

## Armadilhas comuns
- Alterar um componente da library localmente sem publicar: ninguém recebe a mudança.
- Ignorar estados (hover, disabled, erro) e depois corrigir tudo em código.
- Redimensionar frames manualmente em vez de usar Auto Layout gera layouts frágeis.
- Protótipo com interações não testadas em mobile real diverge do comportamento final.
- Exportar SVGs com cores fixas dificulta a aplicação de temas (dark mode) no código.

## Relacionadas
- [[Design]]
- [[Mobile]]