---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Windows

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Família de sistemas operacionais da Microsoft para desktops e servidores, com interface gráfica, gerenciamento de arquivos, processos e administração via ferramentas próprias.

## Conceitos-chave
- **GUI e shell:** interface gráfica (explorador de arquivos, área de trabalho) e shells de linha de comando (Prompt, PowerShell).
- **Registro (Registry):** banco de dados hierárquico que armazena configurações do sistema e de aplicações.
- **Sistema de arquivos:** NTFS é o padrão, com permissões (ACLs), journaling, criptografia (EFS/BitLocker) e quotas.
- **Gerenciamento de processos:** Gerenciador de Tarefas, serviços do Windows (SCM) e ferramentas como `tasklist` e `Get-Process`.
- **PowerShell:** shell e linguagem de automação baseada em objetos (.NET), essencial para administração e scripting.
- **Active Directory:** serviço de diretório para gerenciar usuários, grupos e políticas em redes corporativas.
- **Segurança:** contas de usuário, UAC (controle de acesso), políticas de grupo e atualizações (Windows Update).

## Exemplos
```powershell
# PowerShell: listar processos e parar um serviço
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
Get-Service | Where-Object { $_.Status -eq 'Running' }
Stop-Service -Name "wuauserv" -Force

# Ver uso de disco e espaço
Get-PSDrive C
```

```text
// Atalhos e comandos úteis
Win + R         // Executar
taskmgr         // Gerenciador de Tarefas
services.msc    // Gerenciar serviços
regedit         // Editor do Registro
cmd / ipconfig  // informações de rede
```

```text
// Estrutura de diretórios principais
C:\Windows        // sistema operacional
C:\Users\<nome>   // perfis de usuário
C:\Program Files  // aplicações (64 bits)
C:\Program Files (x86)  // aplicações (32 bits)
```

## Boas práticas
- Usar PowerShell para automação e tarefas administrativas repetitivas.
- Fazer backup do Registro antes de edições manuais.
- Separar contas de administrador das contas de uso diário (princípio do menor privilégio).
- Manter o sistema atualizado para reduzir vulnerabilidades.
- Usar NTFS com permissões adequadas em ambientes compartilhados.

## Armadilhas comuns
- Editar o Registro sem backup, podendo tornar o sistema instável.
- Executar comandos de administração sem entender o impacto (desligar serviços críticos).
- Confundir usuário Administrador com UAC; a elevação não é sempre ativa.
- Ignorar permissões NTFS e ACLs ao compartilhar arquivos.
- Tratar caminhos com `\` e confundir com a notação de outras plataformas (`/`).

## Relacionadas
- [[Sistemas]]
- [[Performance]]
- [[Debug]]
- [[Memoria]]