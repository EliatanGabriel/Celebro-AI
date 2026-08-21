---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Ambiente Local Laravel Vite

#area/trabalho #trabalho/ambiente-local-laravel-vite #conceito

**Resumo:** Configuração de ambiente de desenvolvimento Laravel com Vite.

## Conceitos-chave
- O Vite é o bundler front-end do Laravel moderno (substitui o Laravel Mix).
- Integração via Laravel Breeze/Jetstream ou config manual em `vite.config.js`.
- `npm run dev` serve o front-end com hot reload (HMR) apontando para a URL Laravel.

## Exemplos
```bash
# Subir o back-end (PHP)
composer install
cp .env.example .env
php artisan key:generate
php artisan migrate --seed
php artisan serve

# Subir o front-end com Vite (HMR)
npm install
npm run dev

# Build de produção
npm run build
```
```js
// vite.config.js
export default defineConfig({
  plugins: [laravel({ input: ['resources/css/app.css', 'resources/js/app.js'] })],
});
```

## Boas práticas
- Manter versões de PHP, Composer e Node compatíveis com o projeto (via `composer.json`/`package.json`).
- Rodar `npm run dev` em terminal separado do `php artisan serve`.
- Usar `.env` local e nunca versionar credenciais.
- Consultar `php artisan migrate:fresh --seed` para resetar dados de teste.

## Armadilhas comuns
- Esquecer de instalar o Vite (`npm i`) e o front não carregar.
- Porta do Vite conflitando ou `APP_URL` incorreto quebrando o HMR.
- Rodar `npm run build` e esquecer que é preciso `npm run dev` durante o desenvolvimento.
- Misturar cache antigo de assets após atualizar de Mix para Vite.

## Relacionadas
- [[Git]]
- [[Docker]]
- [[Ambiente]]