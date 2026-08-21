---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Wget

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Ferramenta de linha de comando (GNU) para download de arquivos e espelhamento de sites via HTTP/HTTPS e FTP; destaca-se pelo suporte recursivo, retomada de downloads (`-c`) e espelhamento completo com `--mirror`.

## Conceitos-chave
- **Download básico**: `wget URL` salva no diretório atual; `-O` define nome de arquivo, `-P` define diretório.
- **Recursão**: `-r` segue links de páginas; `-l N` limita profundidade, `-np` evita subir de diretório.
- **Mirror/espelhamento**: `--mirror` combina recursão com preservação de timestamp para replicar sites.
- **Retomada e robustez**: `-c` continua downloads interrompidos; `--tries`, `--timeout` e `--wait` controlam tentativas e pausas.
- **Autenticação/headers**: `--user`/`--password`, `--header`, `--load-cookies` para sites que exigem sessão.
- **Limites**: `-A`/`-R` filtram por extensão, `-X` exclui diretórios, `-nd` desativa a criação de árvore de diretórios.

## Exemplos
Download simples:

```bash
wget https://exemplo.com/arquivo.tar.gz
wget -O instalar.sh https://exemplo.com/install
wget -P /tmp/downloads https://exemplo.com/foto.png
```

Espelhamento de um site:

```bash
wget --mirror --page-requisites --adjust-extension \
  --convert-links --no-parent https://exemplo.com/docs/
```

Retomar download interrompido com pausa:

```bash
wget -c --tries=5 --timeout=30 --wait=3 https://exemplo.com/grande.iso
```

Baixar arquivos listados em um arquivo:

```bash
wget -i urls.txt
```

## Boas práticas
- Use `-c` para grandes downloads e defina `--tries`/`--timeout` para ambientes instáveis.
- Ao espelhar sites, combine `--page-requisites` e `--convert-links` para que páginas offline funcionem.
- Respeite o servidor: use `--wait`/`--limit-rate` para não sobrecarregar ou ser bloqueado.
- Prefira `curl` para APIs/upload e `wget` para downloads recursivos e espelhamento.
- Em scripts, use `--no-clobber` (`-nc`) ou diretórios separados para não sobrescrever arquivos.

## Armadilhas comuns
- Espelhamento recursivo sem limites (`-l inf`) que baixa sites inteiros por engano.
- Downloads seguindo redirecionamentos HTML que salvam a página em vez do arquivo (`--page-requisites` ajuda).
- Servidores que exigem User-Agent/cookies bloqueiam o wget padrão; adicione `--header`.
- `-c` com arquivos já completos pode causar erros; use `-nc` quando a lógica é "não sobrescrever".
- Baixar conteúdo de fontes não confiáveis sem checar checksums (use `--checksum` ou compare sha256).

## Relacionadas
- [[Curl]]
- [[Terminal]]
- [[Scripts]]
- [[Ferramentas-CLI]]