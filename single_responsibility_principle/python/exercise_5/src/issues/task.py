from .base import Command

class Task(Command):
    """Task command class.

    se utiliza cuando se necesita procesar una tarea por ejemplo: enviar un correo, guardar en un log, etc.
    """
    
    def execute(self) -> str:
        return "task command executed successfully"
