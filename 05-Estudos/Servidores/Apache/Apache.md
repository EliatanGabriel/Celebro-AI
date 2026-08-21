---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Apache HTTP Server

#area/estudos #estudos/servidores #conceito #servidor #web

**Resumo:** Servidor web clássico e amplamente utilizado, baseado em módulos e configuração por diretórios, ideal para ambientes dinâmicos como PHP.

## Conceitos-chave
- **Virtual hosts:** servem múltiplos domínios em um único processo, cada um com seu DocumentRoot e configurações.
- **Módulos:** extensões que adicionam recursos (rewrite, SSL, proxy, cache).
- **.htaccess:** arquivos de configuração por diretório, úteis em hospedagens compartilhadas sem acesso ao config global.
- **Modelo de processo:** cada requisição é tratada por um worker/processo; por isso o consumo de memória é maior que o do Nginx.
- **HTTPS:** habilitado com o módulo mod_ssl e certificados TLS/SSL.

## Exemplos
```apache
<VirtualHost *:80>
    ServerName meu-dominio.com.br
    DocumentRoot /var/www/meu-site

    <Directory /var/www/meu-site>
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/meu-site-error.log
    CustomLog ${APACHE_LOG_DIR}/meu-site-access.log combined
</VirtualHost>
```

```bash
sudo a2enmod rewrite ssl
sudo a2ensite meu-dominio
sudo systemctl reload apache2
```

## Boas práticas
- Desabilitar `AllowOverride` quando não for necessário, pois o .htaccess é verificado a cada requisição.
- Usar sites-available + a2ensite em vez de editar o httpd.conf diretamente.
- Manter logs separados por virtual host e rotacioná-los.

## Armadilhas comuns
- Deixar `DirectoryIndex` com ordem insegura, priorizando arquivos de usuário.
- Manter o servidor exposto em HTTP sem redirecionar para HTTPS.
- Confundir a configuração por diretório do Apache com o modelo por location do Nginx.
- Habilitar muitos módulos desnecessários, inflando o consumo de memória.

## Relacionadas
- [[Nginx]]
- [[VPS]]
- [[HTTPS]]
- [[TLS]]
- [[DNS]]