class PaperBook(Book):
    def __init__ (self, title, author, isbn, pages):
        super().__init__(self, title, author. isbn)
        self.pages = pages



        def display_info(self):
            base_info = super().display_info()
            return f"{base_info}, 페이지 수: {self.pages}p {단행본}"