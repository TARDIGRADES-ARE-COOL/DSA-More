class Foo:
    def __init__(self):
        self.lock = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.lock != 0:
            pass
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        while self.lock != 1:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        while self.lock != 2:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()