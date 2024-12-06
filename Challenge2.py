# Santa Claus 🎅 wants to frame the names of the good children to decorate his workshop 🖼️, but the frame must follow specific rules. Your task is to help the elves generate this magical frame.

# Rules:

# Given an array of names, you must create a rectangular frame that contains all of them.
# Each name must be on a line, aligned to the left.
# The frame is built with * and has a border one line thick.
# The width of the frame automatically adapts to the longest name plus a margin of 1 space on each side.

names = ["midu", "bb", "ccc", "dddd"]


def createFrame(names):

    a = max(len(lst) for lst in names)
    border = '*' * (a + 4) 
    middle =  "\n".join([f"* {name} {' ' * (a-len(name))}" + "*" for name in names]) 
    result = border + middle + "\n" + border
    return result
