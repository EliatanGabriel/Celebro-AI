---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Spring

#area/estudos #estudos/backend #conceito

**Resumo:** Ecossistema do Java (com destaque para Spring Boot) para construir aplicações enterprise robustas, com injeção de dependência, segurança e suporte a microsserviços.

## Conceitos-chave
- **O que é:** framework com IoC/DI, módulos para web, segurança, dados, mensageria, cloud e testes.
- **Spring Boot:** inicialização rápida com autoconfiguração e servidor embutido (Tomcat), sem deploy externo.
- **Quando usar:** sistemas corporativos, APIs REST, microsserviços e aplicações que exigem maturidade e manutenção de longo prazo.
- **Estrutura básica:** `@SpringBootApplication` + controllers `@RestController` + serviços `@Service` + repositories.
- **Injeção de dependência:** container gerencia beans e resolve dependências via anotações.
- **Spring Security:** autenticação/autorização com filtros, JWT e OAuth integrados.
- **Spring Data JPA:** camada de persistência com repositories e mapeamento ORM.
- **Diferenças-chave:** comparado a Django/Flask (Python) e NestJS (TS), é o padrão enterprise do Java, com mais robustez e também mais cerimônia.

## Exemplos
```java
// Application.java
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

```java
// UsuarioController.java
@RestController
@RequestMapping("/usuarios")
public class UsuarioController {

    private final UsuarioService service;

    public UsuarioController(UsuarioService service) {
        this.service = service; // injeção por construtor
    }

    @GetMapping("/{id}")
    public Usuario getUsuario(@PathVariable Long id) {
        return service.buscar(id);
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public Usuario criar(@RequestBody @Valid UsuarioDto dto) {
        return service.criar(dto);
    }
}
```

```java
// UsuarioRepository.java
public interface UsuarioRepository extends JpaRepository<Usuario, Long> {
    Optional<Usuario> findByEmail(String email);
}
```

## Boas práticas
- Usar injeção por construtor e beans pequenos com responsabilidade única.
- Validar DTOs com Bean Validation (`@Valid`, `@NotNull`).
- Configurar perfis de ambiente (`application-dev.yml`, `application-prod.yml`).
- Proteger endpoints com Spring Security e tokens (JWT/OAuth).
- Escrever testes com Spring Boot Test e camadas isoladas (MockMvc, @DataJpaTest).

## Armadilhas comuns
- Anotar classes com `@Component` desnecessariamente, dificultando a leitura do container.
- Lazy loading em controllers sem transação → `LazyInitializationException`.
- Esquecer de fechar recursos/threads e deixar conexões vazando.
- Confiar só em `@Autowired` de campo, dificultando testes (preferir construtor).
- Subir um único bean gigante que acopla banco, regras e HTTP.

## Relacionadas
- [[Java]]
- [[Backend]]
- [[JWT]]
- [[Auth]]
- [[Microservicos]]