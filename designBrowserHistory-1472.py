'''
  implemented using two stacks one for forward and other for backward history.
  time complexity of all operations are O(1)
  the time complexity of back/forward is O(steps) 
'''

class BrowserHistory:

    def __init__(self, homepage: str):
        self.goBack = [] #stack with previous urls
        self.goForward = [] #stack with forward urls
        self.current = homepage #current url

    def visit(self, url: str) -> None:
        self.goBack.append(self.current)
        self.current = url
        self.goForward = []

    def back(self, steps: int) -> str:
        i = 0
        while self.goBack and i < steps:
            self.goForward.append(self.current)
            self.current = self.goBack.pop()
            i += 1
        return self.current

    def forward(self, steps: int) -> str:
        i = 0
        while self.goForward and i < steps:
            self.goBack.append(self.current)
            self.current = self.goForward.pop()
            i += 1
        return self.current


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)