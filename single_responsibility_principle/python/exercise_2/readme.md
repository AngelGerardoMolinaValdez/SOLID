# 🛠️ Refactorización de un Sistema de Administración de Usuarios para Cumplir con el Principio de Responsabilidad Única (SRP)

## 📑 Situación Inicial

Se tiene un sistema de administración de usuarios en una aplicación web. La clase `AdministradorUsuarios` es responsable tanto de gestionar la información de los usuarios (añadir, actualizar, eliminar usuarios) como de validar la información del usuario antes de realizar operaciones en la base de datos.

## ❗ Problema Identificado

La clase `AdministradorUsuarios` viola el Principio de Responsabilidad Única (SRP), ya que tiene múltiples razones para cambiar: cambios en la lógica de gestión de usuarios y cambios en la lógica de validación de datos de usuarios.

## 🧩 Estructura Actual de la Clase

```python
class AdministradorUsuarios:
    def añadir_usuario(self, usuario):
        if self.validar_usuario(usuario):
            # Lógica para añadir usuario a la base de datos
            pass
        else:
            # Manejo del error
            pass

    def actualizar_usuario(self, usuario):
        if self.validar_usuario(usuario):
            # Lógica para actualizar usuario en la base de datos
            pass
        else:
            # Manejo del error
            pass

    def validar_usuario(self, usuario):
        # Lógica para validar la información del usuario
        return True  # Suponer validación exitosa para el ejemplo
```

## 🎯 Tarea de Refactorización

Tu tarea es refactorizar el sistema de administración de usuarios para que cumpla con el Principio de Responsabilidad Única. Debes modificar la estructura para separar la responsabilidad de validación de la información del usuario de la gestión de los usuarios en sí.

## 📝 Objetivos Específicos

1. **Separación de la Lógica de Validación:** Extraer la lógica de validación de `AdministradorUsuarios` a una clase separada dedicada exclusivamente a la validación de datos de usuarios.
2. **Cohesión dentro de `AdministradorUsuarios`:** Asegurar que `AdministradorUsuarios` se enfoque únicamente en la gestión de usuarios, delegando la validación a otra clase.
3. **Flexibilidad y Mantenibilidad:** Facilitar la extensión tanto de la lógica de gestión de usuarios como de la lógica de validación de forma independiente, mejorando la mantenibilidad del código.

## 🔍 Directrices para la Implementación

- Crear una nueva clase `ValidadorUsuarios` que contenga métodos específicos para la validación de la información del usuario.
- Modificar `AdministradorUsuarios` para que utilice una instancia de `ValidadorUsuarios` para validar los datos del usuario antes de realizar operaciones en la base de datos.
- Considerar la posibilidad de utilizar inyección de dependencias para facilitar la integración y prueba de las clases `AdministradorUsuarios` y `ValidadorUsuarios`.

Este ejercicio busca aplicar el principio de Responsabilidad Única para mejorar la estructura del sistema de administración de usuarios, promoviendo una arquitectura de software más limpia, mantenible y extensible.
