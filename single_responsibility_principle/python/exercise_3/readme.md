# 🛠️ Refactorización de la Clase "Gestor de Reportes" para Cumplir con el Principio de Responsabilidad Única (SRP)

## 📑 Situación Inicial

En una aplicación de análisis de datos, existe una clase llamada `GestorReportes` que maneja tanto la generación de reportes de datos como su visualización. Esta clase combina la lógica de procesamiento de datos y la presentación de los mismos en una única entidad.

## ❗ Problema Identificado

La clase `GestorReportes` rompe el Principio de Responsabilidad Única (SRP) al integrar la lógica de generación y visualización de reportes, lo cual complica las pruebas, el mantenimiento y la extensión del código.

## 🧩 Estructura Actual de la Clase

```python
class ReportManager:
    def generate_report(self, data):
        # Logic to process and generate the report
        report = f"Report processed with {len(data)} elements"
        return report

    def display_report(self, report):
        # Logic to display the report
        print(f"Displaying report: {report}")
```

## 🎯 Tarea de Refactorización

Reestructurar la implementación para que cumpla con el Principio de Responsabilidad Única, separando las responsabilidades de generación de reportes y su visualización en clases distintas.

## 📝 Objetivos Específicos

1. **Descomposición de Clases:** Crear clases independientes para la generación y la visualización de reportes.
2. **Interfaces Claras:** Definir interfaces bien delimitadas para las nuevas clases, permitiendo una mejor integración y manejo.
3. **Minimizar Acoplamiento:** Implementar patrones de diseño que reduzcan la interdependencia entre las clases para una mayor flexibilidad y modularidad.

## 🔍 Directrices para la Implementación

- Desarrollar una clase abstracta o interfaz para la generación de reportes con métodos específicos que puedan ser extendidos según el tipo de datos.
- Implementar una clase separada para la visualización de reportes, permitiendo diferentes formatos y medios de visualización (consola, interfaz gráfica, etc.).
- Considerar el uso de inyección de dependencias para facilitar la prueba y extensión de las clases.
