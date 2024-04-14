from .base import Command

class Error(Command):
    """Error command class.

    se utiliza cuando se necesita procesar un error por ejemplo: enviar un correo, guardar en un log, etc.
    """
    
    def execute(self) -> str:
        return "error command executed successfully"
