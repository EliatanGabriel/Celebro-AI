---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# PowerShell

#area/estudos #estudos/linguagens #conceito

**Resumo:** Shell e linguagem de script da Microsoft baseada em .NET, que trabalha com objetos em vez de texto, integrada ao Windows, Azure e ferramentas de automação de infraestrutura.

## Conceitos-chave
- Paradigma orientado a objetos (todo comando retorna objetos .NET, não texto).
- Tipagem dinâmica com inferência e suporte a tipos .NET fortes.
- Interpretada: executada pelo runtime do PowerShell, com acesso direto ao .NET.
- Uso principal em administração do Windows, automação de infra (IaC), Azure e Microsoft 365.
- Cmdlets seguem o padrão Verbo-Substantivo (ex.: `Get-Process`, `Set-Content`).
- Pipeline passa objetos entre comandos: `Get-Service | Where-Object { $_.Status -eq 'Running' }`.
- Particularidade: providers permitem navegar em registro, variáveis, sistema de arquivos e certificados como unidades.

## Exemplos
```powershell
# Lista processos com mais de 100 MB de memória
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB } |
    Select-Object Name, Id, @{Name='MB'; Expression={[math]::Round($_.WorkingSet64/1MB, 1)}} |
    Sort-Object MB -Descending

# Função para backup simples
function Backup-Diretorio {
    param([string]$Origem, [string]$Destino)
    Copy-Item -Path $Origem -Destination $Destino -Recurse -Force
    Write-Host "Backup concluído"
}

# Estruturas de controle
$contador = 0
while ($contador -lt 3) {
    $contador++
    Write-Host "Contador: $contador"
}
```

## Boas práticas
- Use os operadores nativos `-eq`, `-ne`, `-like`, `-match` (não `==`).
- Nomeie funções com o padrão Verbo-Substantivo aprovado (Approved Verbs).
- Prefira `Write-Output`/pipeline a `Write-Host` para retornar dados.
- Trate erros com `try`/`catch` e `-ErrorAction Stop`.
- Version scripts e siga convenções de estilo do PowerShell Gallery.

## Armadilhas comuns
- Usar `==` em vez de `-eq` — o PowerShell não compara como outras linguagens.
- Supor que variáveis não inicializadas são `null`; podem ser `$null` ou `''` dependendo do contexto.
- Pipeline de texto em vez de objetos, perdendo a flexibilidade do modelo orientado a objetos.
- Esquecer `-Recurse` em operações em diretórios e deparar-se com caminhos não encontrados.
- Política de execução bloqueando scripts (`ExecutionPolicy`); use assinatura ou política adequada.

## Relacionadas
- [[Shell]]
- [[Bash]]