# 🛠️ # Refactorización de la Clase "ContentManager" para cumplir con el Principio de Abierto/Cerrado (OCP)

## 📑 Situación Inicial

En un sistema de gestión de contenido digital, existe una clase llamada `ContentManager` que maneja la visualización de diferentes tipos de contenido como texto, imagen, y video. Actualmente, esta clase utiliza múltiples condicionales para determinar cómo manejar y mostrar cada tipo de contenido.

## ❗ Problema Identificado

La clase `ContentManager` no cumple con el Principio de Abierto/Cerrado (OCP), ya que cualquier adición de un nuevo tipo de contenido requiere la modificación directa de esta clase, añadiendo nuevos condicionales y lógica de manejo.

## 🧩 Estructura Actual de la Clase

```python
class ContentManager:
    def display_content(self, content):
        if content.type == "text":
            print(f"Displaying text: {content.data}")
        elif content.type == "image":
            print(f"Displaying image from: {content.data}")
        elif content.type == "video":
            print(f"Playing video from: {content.data}")
```

## 🚀 Contexto de Uso

Supongamos que deseamos mostrar diferentes tipos de contenido usando la clase `ContentManager`. En el estado actual del código, cada vez que se añade un nuevo tipo de contenido, necesitamos añadir una nueva condición en el método `display_content`. Aquí un ejemplo de cómo se utiliza este enfoque:

```python
content_text = {"type": "text", "data": "Hello, World!"}
content_image = {"type": "image", "data": "path/to/image.png"}
content_video = {"type": "video", "data": "path/to/video.mp4"}

content_manager = ContentManager()
content_manager.display_content(content_text)
content_manager.display_content(content_image)
content_manager.display_content(content_video)
```

## 🎯 Tarea de Refactorización

Refactoriza la implementación para que `ContentManager` se adhiera al Principio de Abierto/Cerrado. Esto significa que la clase debe estar abierta para la extensión pero cerrada para la modificación.

## 📝 Objetivos Específicos

1. **Uso de Polimorfismo**: Implementa clases específicas para cada tipo de contenido que extiendan una clase base o interfaz común que define cómo se debe manejar y mostrar el contenido.

2. **Reducción de Condicionales**: Elimina los condicionales de la clase `ContentManager` utilizando un enfoque basado en polimorfismo.

## 🔍 Directrices para la Implementación

- Crea una clase abstracta o interfaz `Content` con un método `display()`.
- Desarrolla subclases concretas como `TextContent`, `ImageContent`, y `VideoContent` que implementen el método `display()`.
- Modifica `ContentManager` para que utilice el método `display()` de los objetos de contenido, independientemente de su tipo específico.
