class Node:
    def __init__(self, val, previous=None, next=None):
        self.val = val
        self.previous = previous
        self.next = next

"""
You have a browser of one tab where you start on the homepage.
You can visit another URL, get back in history a number of steps or move forward in history a number of steps
"""
#NOTE: 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    # O(1)
    def visit(self, url: str) -> None:
        new_node = Node(url, previous= self.curr)
        self.curr.next = new_node
        self.curr = new_node
        return None

    # O(n)
    def back(self, steps: int) -> str:
        while self.curr.previous and steps:
            self.curr = self.curr.previous
            steps -= 1
        return self.curr.val

    # O(n)
    def forward(self, steps: int) -> str:
        while self.curr.next and steps:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
