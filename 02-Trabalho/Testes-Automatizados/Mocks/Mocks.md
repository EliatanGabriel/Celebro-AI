---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Mocks

#area/trabalho #trabalho/testes-automatizados #conceito

**Resumo:** Objetos simulados que imitam dependências reais em testes.

## Conceitos-chave
- Objetos simulados que imitam dependências reais (API, banco, relógio, módulos).
- Stubs: retornam respostas fixas para isolar o código testado.
- Spies: registram chamadas, argumentos e retornos para verificação.
- Podem simular timers, aleatoriedade e efeitos colaterais.
- Têm papel central no unit testing para garantir determinismo.

## Exemplos
```
import { buscarUsuario } from './api';

jest.mock('./api');

test('salva o nome do usuário', async () => {
  buscarUsuario.mockResolvedValue({ nome: 'QA' });

  const resultado = await salvarPerfil(1);

  expect(resultado).toBe('Perfil de QA salvo');
  expect(buscarUsuario).toHaveBeenCalledWith(1);
});
```

## Boas práticas
- Mockar apenas fronteiras: rede, banco, arquivos, relógio.
- Manter o comportamento do mock realista em relação ao real.
- Verificar chamadas relevantes ao cenário testado.
- Restaurar mocks no teardown (afterEach) para não vazar entre testes.
- Usar mocks no nível correto: unidade simula, integração evita.

## Armadilhas comuns
- Mockar demais e testar a implementação do mock, não a do código.
- Comportamento do mock divergente da realidade, gerando falsos positivos.
- Esquecer de restaurar mocks e contaminar os demais testes.
- Acoplar a verificação ao nome exato da função interna.
- Mocks de módulo quebrados por mudança de imports.

## Relacionadas
- [[Fixtures]]
- [[Unit-testing]]
- [[Integration-testing]]
- [[Test-frameworks]]