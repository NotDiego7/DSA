class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None

"""
You have a browser of one tab where you start on the homepage.
You can visit another URL, get back in history a number of steps or move forward in history a number of steps
"""
#NOTE: 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.previous = self.curr
        self.curr.next = new_node
        self.curr = new_node
        return None


    def back(self, steps: int) -> str:
        while self.curr.previous and steps:
            self.curr = self.curr.previous
            steps -= 1
        return self.curr.val


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