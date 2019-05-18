
from Game.Objects import Object

class Character(Object):

    def __init__(self, field, x, y):
        self.field = field
        self.x = x
        self.y = y

        self.field.addObject(x, y, self)

    def getVisibilityPriority(self):
        return 100000;

    def isTransparent(self):
        return True

    def actUp(self):
        self.act(self.x, self.y, self.x, self.y - 1)

    def actDown(self):
        self.act(self.x, self.y, self.x, self.y + 1)

    def actLeft(self):
        self.act(self.x, self.y, self.x - 1, self.y)

    def actRight(self):
        self.act(self.x, self.y, self.x + 1, self.y)

    def act(self, fromX, fromY, x, y):
        if self.field.canMoveTo(x, y, self):
            if not self.crackingVaultDoor is None:
                self.stopCrackingVaultDoor()
            self.field.moveTo(self, x, y)
            self.notifyMovement(fromX, fromY)
        elif self.field.canBeInteractedWith(x, y, self):
            self.field.interact(x, y, self)
