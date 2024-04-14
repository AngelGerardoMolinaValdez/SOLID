# 🛠️ Refactorización de la Clase "Centro de Servicio al Cliente" para Cumplir con el Principio de Responsabilidad Única (SRP)

## 📑 Situación Inicial

En una plataforma de comercio electrónico, existe una clase llamada `CentroServicioCliente` que maneja tanto la recepción de consultas de clientes como la resolución de problemas y la redirección de llamadas. Esta clase combina la lógica de atención inicial, procesamiento de problemas específicos y comunicación posterior con el cliente.

## ❗ Problema Identificado

La clase `CentroServicioCliente` rompe el Principio de Responsabilidad Única (SRP) al integrar múltiples responsabilidades: recepción de consultas, resolución de problemas y comunicaciones de seguimiento. Esto complica la mantenibilidad y escalabilidad del código.

## 🧩 Estructura Actual de la Clase

```python
class CustomerServiceCenter:
    def receive_call(self, customer):
        # Identificar el tipo de consulta
        print(f"Receiving call from {customer.name}")
        issue_type = self.identify_issue(customer.issue)
        self.resolve_issue(issue_type, customer)
        self.follow_up(customer)

    def identify_issue(self, issue):
        # Determinar el tipo de problema basado en la descripción
        return "tipo_de_problema"

    def resolve_issue(self, issue_type, customer):
        # Resolver el problema específico
        print(f"Resolving {issue_type} for {customer.name}")

    def follow_up(self, customer):
        # Enviar comunicación de seguimiento
        print(f"Following up with {customer.name}")
```

## 🎯 Tarea de Refactorización

Reestructurar la implementación para que cumpla con el Principio de Responsabilidad Única, separando las responsabilidades de recepción de llamadas, resolución de problemas y seguimiento en clases distintas.

## 📝 Objetivos Específicos

1. **Descomposición de Clases**: Crear clases independientes para la recepción de consultas, la resolución de problemas y las comunicaciones de seguimiento.
2. **Interfaces Claras**: Definir interfaces bien delimitadas para las nuevas clases, permitiendo una mejor integración y manejo.
3. **Minimizar Acoplamiento**: Implementar patrones de diseño que reduzcan la interdependencia entre las clases para una mayor flexibilidad y modularidad.

## 🔍 Directrices para la Implementación

- Desarrollar una clase abstracta o interfaz para la recepción de consultas con métodos específicos que puedan ser extendidos según el tipo de cliente o problema.
- Implementar clases separadas para la resolución de problemas, permitiendo diferentes estrategias de resolución según el tipo de problema.
- Crear una clase para el seguimiento post-resolución, que pueda adaptarse a diferentes canales de comunicación (correo electrónico, llamada telefónica, mensaje de texto).
