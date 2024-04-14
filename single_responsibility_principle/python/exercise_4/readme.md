# 🛠️ Refactorización de la Clase "Gestor de Pagos" para Cumplir con el Principio de Responsabilidad Única (SRP)

## 📑 Situación Inicial

En una aplicación de comercio electrónico, se encuentra una clase llamada `GestorPagos` que maneja tanto el procesamiento de transacciones de pago como la generación de informes de transacciones. Esta clase combina la lógica de procesamiento de pagos y la generación de informes financieros.

## ❗ Problema Identificado

La clase `GestorPagos` rompe el Principio de Responsabilidad Única (SRP) al integrar la lógica de procesamiento de pagos y generación de informes en una sola entidad, complicando las pruebas y mantenimiento del código.

## 🧩 Estructura Actual de la Clase

```python
class PaymentManager:
    def process_payment(self, user_id, payment_details):
        # Lógica para procesar el pago
        print(f"Processing payment for user {user_id}")
        # Supuesto procesamiento del pago
        self.log_transaction(user_id, payment_details)

    def log_transaction(self, user_id, payment_details):
        # Lógica para registrar la transacción en un informe
        print(f"Logging transaction for user {user_id}: {payment_details}")
```

## 🎯 Tarea de Refactorización

Reestructurar la implementación para que cumpla con el Principio de Responsabilidad Única, separando las responsabilidades de procesamiento de pagos y generación de informes de transacciones en clases distintas.

## 📝 Objetivos Específicos

1. **Descomposición de Clases:** Crear clases independientes para el procesamiento de pagos y la generación de informes.
2. **Interfaces Claras:** Definir interfaces bien delimitadas para las nuevas clases, permitiendo una mejor integración y manejo.
3. **Minimizar Acoplamiento:** Implementar patrones de diseño que reduzcan la interdependencia entre las clases para una mayor flexibilidad y modularidad.

## 🔍 Directrices para la Implementación

- Desarrollar una clase abstracta o interfaz para el procesamiento de pagos con métodos específicos que puedan ser extendidos según el tipo de pago.
- Implementar una clase separada para la generación de informes de transacciones, permitiendo diferentes formatos y detalles en los informes (PDF, HTML, texto plano).
- Considerar el uso de inyección de dependencias para facilitar la prueba y extensión de las clases.
