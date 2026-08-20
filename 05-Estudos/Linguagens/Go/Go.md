---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Go

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem compilada e concisa criada pelo Google, projetada para sistemas concorrentes, serviços de rede e infraestrutura cloud (Docker, Kubernetes).

## Conceitos-chave
- Paradigma imperativo e estrutural, com ênfase em simplicidade; sem classes e herança clássica.
- Tipagem estática e forte, com inferência de tipos via `:=`.
- Compilada para binário nativo e estático, com tempo de compilação muito rápido.
- Uso principal em backend, microserviços, ferramentas CLI, cloud e infraestrutura (Docker, Kubernetes, Terraform).
- Goroutines: execução concorrente leve; comunicação por canais (`chan`) em vez de memória compartilhada.
- Garbage collector automático e gerenciamento de memória transparente.
- Particularidade: apenas um executável de deploy (binário estático), sem dependências de runtime.

## Exemplos
```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	numeros := []int{1, 2, 3, 4, 5}

	for _, n := range numeros {
		wg.Add(1)
		go func(v int) {
			defer wg.Done()
			fmt.Println(v * v)
		}(n)
	}
	wg.Wait()
}
```

## Boas práticas
- Siga o padrão de erros explícito: verifique `err` após cada operação que pode falhar.
- Prefira goroutines coordenadas por `sync.WaitGroup` ou canais, evitando corridas de dados.
- Nomeie arquivos/pacotes em minúsculo e siga `go fmt` automaticamente.
- Use `context.Context` para propagar cancelamento e timeouts entre funções.
- Mantenha interfaces pequenas e orientadas ao comportamento do consumidor.

## Armadilhas comuns
- Copiar `sync.Mutex` por valor (acidentalmente), tornando o lock ineficaz.
- Escrever em variáveis compartilhadas entre goroutines sem `sync` — corrida de dados (data race).
- Ignorar o retorno de `err` e engolir falhas silenciosamente.
- Sombra (shadowing) de variáveis com `:=` dentro de blocos, alterando escopos.
- Uso de `interface{}` (ou `any`) excessivo, perdendo a segurança de tipos.

## Relacionadas
- [[Rust]]
- [[Backend]]