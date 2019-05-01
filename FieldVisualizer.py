
import colorama

import consoleUtils

from Wall import Wall
from Money import Money
from CharacterObserver import CharacterObserver

class FieldVisualizer(CharacterObserver):

    idleCursor = (25, 70)
    offset = (3, 2)

    def __init__(self, field, character):
        consoleUtils.clearScreen()
        colorama.init()

        for x in range(0, field.width):
            for y in range(0, field.height):
                object = field.getObjectAtLocation(x, y)
                if isinstance(object, Wall):
                    consoleUtils.printAtPosition(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, 'X')
                elif isinstance(object, Money):
                    consoleUtils.printAtPosition(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, '$')

        consoleUtils.printAtPosition(FieldVisualizer.offset[1] + character.y, FieldVisualizer.offset[0] + character.x, '@')

        FieldVisualizer.resetCursor()

    def resetCursor():
        consoleUtils.setCursorPosition(FieldVisualizer.idleCursor[0], FieldVisualizer.idleCursor[1])

    def characterMoved(self, oldX, oldY, newX, newY):
        consoleUtils.printAtPosition(FieldVisualizer.offset[1] + oldY, FieldVisualizer.offset[0] + oldX, ' ')
        consoleUtils.printAtPosition(FieldVisualizer.offset[1] + newY, FieldVisualizer.offset[0] + newX, '@')

        FieldVisualizer.resetCursor()
