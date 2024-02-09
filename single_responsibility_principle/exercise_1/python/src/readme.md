# 🛠️ Refactorización del Sistema de Notificaciones para Cumplir con el Principio de Responsabilidad Única (SRP)

## 📑 Situación Inicial

En el contexto de un sistema de gestión de notificaciones integrado en una aplicación de software empresarial, se identifica una clase denominada `ManejadorNotificaciones`. Esta clase encapsula dos comportamientos distintos: la transmisión de notificaciones a usuarios a través de múltiples canales (correo electrónico, SMS, notificaciones push) y el registro de estas actividades en un sistema de log.

## ❗ Problema Identificado

La clase `ManejadorNotificaciones` viola el Principio de Responsabilidad Única (SRP) al mezclar la lógica de envío y registro de notificaciones, dificultando el mantenimiento y escalabilidad del código.

## 🧩 Estructura Actual de la Clase

```python
class ManejadorNotificaciones:
    def enviar_notificacion(self, usuario, mensaje, tipo):
        if tipo == "email":
            # Implementación para correo electrónico
            pass
        elif tipo == "sms":
            # Implementación para SMS
            pass
        elif tipo == "app":
            # Implementación para notificaciones en app
            pass
        self.registrar_log(usuario, mensaje, tipo)

    def registrar_log(self, usuario, mensaje, tipo):
        # Implementación del registro de notificación
        pass
```

## 🎯 Tarea de Refactorización

Reestructurar la implementación para que cumpla con el Principio de Responsabilidad Única, separando las responsabilidades de envío de notificaciones y registro de logs en clases distintas.

## 📝 Objetivos Específicos

1. **Descomposición de Clases:** Separar `ManejadorNotificaciones` en clases dedicadas a una sola responsabilidad.
2. **Interfaces Claras:** Definir interfaces precisas para las nuevas clases, facilitando su integración y extensión.
3. **Minimizar Acoplamiento:** Reducir dependencias directas entre clases, utilizando patrones de diseño para gestionar relaciones.

## 🔍 Directrices para la Implementación

- Crear una clase abstracta o interfaz para el envío de notificaciones, con implementaciones específicas para cada canal.
- Diseñar una clase exclusiva para el registro de logs, considerando diferentes destinos para estos (archivo, base de datos).
- Evaluar el uso de servicios auxiliares o patrones de diseño que promuevan la inyección de dependencias y desacoplamiento.

Este ejercicio busca mejorar la calidad del código, su mantenimiento, prueba y extensión futura.

## 📑 Conclusion

Puedes encontrar el análisis y resumen en general de la solución en ./src/main.py
