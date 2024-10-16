import copy

class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Document: {self.title}\nContent: {self.content}"

if __name__ == "__main__":
    original_doc = Document("Original Title", "This is the original content.")
    print("Original Document:")
    print(original_doc)

    cloned_doc = original_doc.clone()
    cloned_doc.title = "Cloned Title"
    cloned_doc.content = "This is the cloned content."

    print("\nCloned Document:")
    print(cloned_doc)

    print("\nOriginal Document after cloning:")
    print(original_doc)
