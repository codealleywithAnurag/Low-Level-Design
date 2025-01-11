class Document:
    def __init__(self, title, content, style):
        self.title = title
        self.content = content
        self.style = style

def main():
    doc1 = Document("Report", "Annual financial report", "Formal")

    doc2 = Document(doc1.title, doc1.content, doc1.style)
    doc2.title = "Summary Report"

    print(f"Document 1: Title={doc1.title}, Content={doc1.content}, Style={doc1.style}")
    print(f"Document 2: Title={doc2.title}, Content={doc2.content}, Style={doc2.style}")

if __name__ == "__main__":
    main()
