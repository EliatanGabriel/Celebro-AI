---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Mobile

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Desenvolvimento de aplicativos para smartphones e tablets (Android e iOS), abrangendo nativo, multiplataforma, responsividade, notificações push e publicação em app stores.

## Conceitos-chave
- **Nativo**: Android (Kotlin/Java, Android Studio) e iOS (Swift, Xcode); maior acesso a APIs do dispositivo e performance.
- **Multiplataforma**: Flutter (Dart), React Native (JS/TS) e Kotlin Multiplatform — um código para ambos os sistemas, com acesso via bridges/FFI.
- **Componentes de UI**: View/Activity (Android), SwiftUI/UIKit (iOS); layouts responsivos por densidade e tamanho de tela.
- **Notificações push**: FCM (Firebase Cloud Messaging) para Android e APNs para iOS; exigem serviço de backend para envio.
- **App stores**: Play Store (revisão automatizada, .aab) e App Store (revisão manual, .ipa); exigem assinatura e versionamento.
- **Deploy e CI**: assinaturas, keystores/provisioning profiles e pipelines para gerar builds assinadas.

## Exemplos
Criar app mínimo com Flutter:

```dart
import 'package:flutter/material.dart';

void main() => runApp(const App());

class App extends StatelessWidget {
  const App({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(child: Text('Olá, mobile')),
      ),
    );
  }
}
```

Build e teste:

```bash
flutter create meu_app
flutter test
flutter build apk --release
adb install build/app/outputs/flutter-apk/app-release.apk
```

## Boas práticas
- Teste em múltiplas densidades de tela e telas pequenas/landscape desde o início.
- Garanta contraste e alvos de toque de pelo menos 44x44dp para acessibilidade.
- Use CI para rodar testes e gerar builds assinadas; nunca commite keystores ou secrets.
- Otimize para bateria/rede: cache de imagens, lazy loading e chamadas de rede agrupadas.
- Siga as diretrizes de review das stores para evitar rejeições (permissões, políticas de privacidade).

## Armadilhas comuns
- Testar só no emulador com as mesmas configurações não reflete dispositivos reais de baixo custo.
- Notificações push que não funcionam por falta de registro de token ou permissão negada.
- Tratar versões do iOS/Android como iguais: APIs e permissões mudam entre versões.
- Assinatura errada/keystore perdido impede atualização na store (a chave não pode ser trocada facilmente).
- UI responsiva implementada só para um tamanho quebra em telas diferentes.

## Relacionadas
- [[Ferramentas]]
- [[Design]]
- [[Figma]]
- [[IntelliJ]]