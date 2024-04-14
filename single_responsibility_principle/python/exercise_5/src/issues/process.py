from .base import Command

class Process(Command):
    """Process command class.

    se utiliza cuando se necesita procesar un comando por ejemplo: procesar un pago, procesar un reporte, etc.
    """
    
    def execute(self) -> str:
        return "process command executed successfully"
