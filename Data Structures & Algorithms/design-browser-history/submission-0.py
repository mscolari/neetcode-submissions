class Page:

    def __init__(self, url, prev):
        self.url = url
        self.prev = prev
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr_page = Page(homepage, None)

    def visit(self, url: str) -> None:
        new_page = Page(url, self.curr_page)
        self.curr_page.next = new_page
        self.curr_page = new_page

    def back(self, steps: int) -> str:
        count = 0
        curr = self.curr_page

        while curr.prev and count < steps:
            curr = curr.prev
            count += 1

        self.curr_page = curr
        
        return self.curr_page.url

    def forward(self, steps: int) -> str:
        count = 0
        curr = self.curr_page

        while curr.next and count < steps:
            curr = curr.next
            count += 1

        self.curr_page = curr
        return self.curr_page.url

