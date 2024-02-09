# Introducción al Principio de Responsabilidad Única (SRP) 🎯

Bienvenido al segmento dedicado al Principio de Responsabilidad Única (SRP), el primero de los cinco principios SOLID fundamentales para el diseño y desarrollo de software orientado a objetos. Este README tiene como objetivo proporcionarte una comprensión profunda del SRP, ejemplificar su aplicación en diferentes lenguajes de programación y escenarios, y demostrar cómo puede mejorar significativamente la calidad del software.

## Objetivos del Segmento 🎯

Este segmento busca profundizar en el Principio de Responsabilidad Única a través de ejemplos detallados, ejercicios prácticos y discusiones sobre su impacto en el desarrollo de software. Exploraremos su aplicación en distintos lenguajes de programación y cómo puede ayudarte a crear código más limpio, mantenible y escalable.

## ¿Qué es el Principio de Responsabilidad Única? ✔️

El Principio de Responsabilidad Única afirma que **"una clase debe tener una, y solo una, razón para cambiar"**. En términos más simples, significa que una clase debe encargarse de una sola parte de la funcionalidad proporcionada por el software, y esta responsabilidad debe estar totalmente encapsulada por la clase.

### Historia y Fundamento 📚

Introducido por Robert C. Martin en sus primeras discusiones sobre los principios SOLID, el SRP es crucial para entender cómo diseñar sistemas de manera que sean mantenibles, comprensibles y flexibles ante cambios futuros. La motivación detrás del SRP es reducir la complejidad de los módulos de software, facilitar su comprensión, y hacer más sencillo el mantenimiento y la refactorización del código.

### Ejemplos de Aplicación 🖥

Para ilustrar el SRP, consideremos un sistema de gestión de pedidos en el que una clase `Pedido` tiene métodos tanto para calcular el total del pedido como para guardar el pedido en una base de datos. Según el SRP, estas responsabilidades deberían separarse en diferentes clases, porque los cambios en los requisitos de cálculo del total del pedido (una razón para cambiar) no deberían afectar la lógica de almacenamiento del pedido (otra razón para cambiar).

```python
# Antes: Violación del SRP
class Pedido:
    def calcular_total(self):
        pass
    def guardar_pedido(self):
        pass

# Después: Cumplimiento del SRP
class Pedido:
    def calcular_total(self):
        pass

class AlmacenamientoPedido:
    def guardar_pedido(self, pedido):
        pass
```

### Beneficios del SRP 🌟

- **Mejora la Cohesión:** Al mantener las responsabilidades bien definidas y separadas, las clases se vuelven más cohesivas.
- **Facilita la Mantenibilidad:** Es más fácil mantener y actualizar el código, ya que los cambios en una parte del sistema tienen menos probabilidades de afectar otras partes.
- **Mejora la Testabilidad:** Las clases con una sola responsabilidad son más fáciles de testear debido a su menor complejidad.
