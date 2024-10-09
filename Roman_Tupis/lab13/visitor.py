"""Visitor (Відвідувач)
Для чого він використовується? Патерн Visitor дозволяє додавати нові операції до об’єктів без зміни їх класів. Він розділяє алгоритми від структури об’єктів. Це особливо корисно, коли маємо багато різних класів об’єктів і хочемо виконувати різні дії над ними.

Як він працює?

Спочатку визначається інтерфейс відвідувача, який містить методи для кожного класу об’єктів, які ми хочемо відвідати.
Кожен клас об’єктів реалізує метод accept(visitor), який передає відвідувача.
Відвідувач викликає відповідний метод для об’єкта, який він відвідує.
Приклад використання: Давай уявимо, що ми розробляємо систему обробки документів. У нас є різні типи документів: текстові файли, PDF-документи, електронні таблиці тощо. Ми хочемо додати можливість виконувати різні дії над цими документами (наприклад, підрахунок слів у текстовому файлі, відображення таблиці у вигляді графіку у PDF тощо). Використання патерну Visitor дозволить нам додавати нові операції без зміни класів документів."""

#у нас є класи для різних типів документів

class TextDocument:
    def accept(self, visitor):
        visitor.visit_text_document(self)

class PdfDocument:
    def accept(self, visitor):
        visitor.visit_pdf_document(self)

class SpreadsheetDocument:
    def accept(self, visitor):
        visitor.visit_spreadsheet_document(self)
#visitor
class DocumentVisitor:
    def visit_text_document(self, text_document):
        print("Обробка текстового документа")

    def visit_pdf_document(self, pdf_document):
        print("Обробка PDF-документа")

    def visit_spreadsheet_document(self, spreadsheet_document):
        print("Обробка електронної таблиці")

text_doc = TextDocument()
pdf_doc = PdfDocument()
spreadsheet_doc = SpreadsheetDocument()

visitor = DocumentVisitor()
text_doc.accept(visitor)
pdf_doc.accept(visitor)
spreadsheet_doc.accept(visitor)
