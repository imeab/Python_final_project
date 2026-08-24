from .base_book import Book


class PaperBook(Book):
    def __init__ (self, title, author, isbn, pages):
        super().__init__(self, title, author, isbn)
        self.pages = pages



        def display_info(self):
            base_info = super().display_info()
            return f"{base_info}, 페이지 수: {self.pages}p {단행본}"


class EBook(Book):
    def __init__ (self, title, author, isbn, file_size):
        super().__init__(self, title, author, isbn)
        self.file_size = file_size

        def displat_info(self):
            base_info = super().display_info()
            return f"{base_info}, 파일 크기: {self.file_size}MB {전자도서}"