from irule import IRule

class GreaterThanRule(IRule):
    def execute(self):
        print 'Hello, World 2!'

    def is_match(self):
        print 'Hello, World 2!'