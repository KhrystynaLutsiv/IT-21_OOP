class OldPrinter:
    def print_text(self, text):
        print(f"Printing: {text}")

class NewPrinterInterface:
    def print_message(self, message):
        pass

class PrinterAdapter(NewPrinterInterface):
    def __init__(self, old_printer):
        self.old_printer = old_printer
    def print_message(self, message):
        self.old_printer.print_text(message)

def client_code(printer):
    printer.print_message("Hello, World!")


old_printer = OldPrinter()
printer_adapter = PrinterAdapter(old_printer)
client_code(printer_adapter)
