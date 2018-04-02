class GameState():
    def __init__(self):
      self._items = []
      self._rolls = []
      
    def set_items(self, items):
        self._items = items

    def get_items(self):
        return self._items

    def set_rolls(self, rolls):
        self._rolls = rolls

    def get_rolls(self):
        return self._rolls
