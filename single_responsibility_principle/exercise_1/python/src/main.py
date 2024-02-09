"""
Resumen de la Aplicación del Principio de Responsabilidad Única (SRP) en el Sistema de Notificaciones

La refactorización del sistema original, que encapsulaba tanto el envío como el registro de notificaciones en una única clase `ManejadorNotificaciones`, hacia una estructura modular con clases dedicadas, demuestra una aplicación efectiva del principio SRP. Se ha logrado separar las responsabilidades de manera clara y coherente, asignando a cada clase una única razón para cambiar.

Cambios Realizados:
- Se dividió la lógica de `ManejadorNotificaciones` en clases específicas dentro de la carpeta `notifications` para manejar los diferentes tipos de notificaciones (Email, SMS, App), cada una extendiendo de una clase base o implementando una interfaz común `Notification`.
- Se introdujo una separación similar para el registro de logs, con la creación de clases específicas en la carpeta `recorders`, permitiendo diferentes estrategias de registro (Base de Datos, Archivo) y abstrayéndolas a través de una interfaz o clase base `Recorder`.
- Se mantuvo la cohesión dentro de las clases de notificación y registro, asegurando que cada una se enfoca en una tarea específica sin sobrecargarlas con múltiples responsabilidades.

Por Qué Está Bien Aplicado:
- **Separación de Concerns:** Cada componente del sistema se concentra en una sola responsabilidad, lo que facilita el mantenimiento, la extensión y la prueba del código.
- **Flexibilidad:** La arquitectura permite añadir fácilmente nuevos tipos de notificaciones o métodos de registro sin alterar el funcionamiento de los componentes existentes.
- **Cohesión:** Las clases son cohesivas, agrupando funcionalidades relacionadas y mejorando la legibilidad y gestión del código.
"""
from handler_notifications import HandlerNotifications
from notifications.sms_notification import SMSNotification
from log_recorder import LogRecorder
from recorders.database_recorder import DataBaseRecorder

if __name__ == "__main__":
    sms = SMSNotification(123456789)
    db = DataBaseRecorder("connection_string")
    handler = HandlerNotifications()
    log = LogRecorder()

    handler.send(sms, "Hello")
    log.record(db, {"data": "Hello"})
