---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Composer

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Gerenciador de dependências do PHP, similar ao npm para JavaScript: resolve, instala e autoload de pacotes a partir do Packagist, gravando as versões em `composer.lock`.

## Conceitos-chave
- **Packagist**: repositório público padrão de pacotes PHP; pacotes são referenciados como `vendor/pacote`.
- **composer.json**: declara as dependências diretas com restrições de versão (`^`, `~`, `*`) e outros metadados do projeto.
- **composer.lock**: registra as versões exatas resolvidas; garante builds reproduzíveis.
- **vendor/**: diretório onde os pacotes são instalados; não deve ser versionado no Git.
- **Autoload**: o Composer gera o autoloader PSR-4/PSR-0 que carrega classes sob demanda, sem `require` manual.
- **Scripts**: hooks (`post-install-cmd`, `post-update-cmd`) executam comandos após eventos do ciclo de vida.

## Exemplos
Criar um projeto e instalar dependências:

```bash
composer init                 # cria o composer.json interativo
composer require guzzlehttp/guzzle   # adiciona e instala pacote
composer install              # instala a partir do composer.lock
composer update               # resolve novamente e atualiza o lock
```

Configuração de autoload PSR-4 no composer.json:

```json
{
  "require": {
    "php": "^8.1",
    "guzzlehttp/guzzle": "^7.8"
  },
  "autoload": {
    "psr-4": { "App\\": "src/" }
  },
  "scripts": {
    "post-install-cmd": ["@php artisan migrate"]
  }
}
```

Regenerar o autoloader após alterar o autoload:

```bash
composer dump-autoload -o   # -o gera otimizado (classmap)
```

## Boas práticas
- Versionar `composer.lock` em aplicações e usar `composer install` em deploy; só atualize o lock conscientemente.
- Usar restrições conservadoras (`^7.8`) e revisar `composer outdated` periodicamente.
- Rodar `composer validate` para checar a sintaxe do composer.json.
- Manter a versão mínima do PHP declarada e testar em CI com matrizes de versões.
- Não commitar `vendor/`; adicione ao `.gitignore`.

## Armadilhas comuns
- Rodar `composer update` no servidor sem necessidade: quebra reprodução e pode instalar versões incompatíveis.
- Confundir `install` (usa lock) com `update` (re-resolve e regrava o lock).
- Ignorar conflitos de versão entre pacotes que exigem versões distintas do PHP ou de extensões.
- Esquecer de regenerar o autoloader após criar novas classes com PSR-4 não otimizado.
- Baixar `composer.phar` de fontes não oficiais ou de versões desatualizadas com falhas de segurança.

## Relacionadas
- [[Ferramentas]]
- [[Terminal]]