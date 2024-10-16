class parent:
    def __init__(self,eyes,hair):
        self.eyes=eyes
        self.hair=hair


class child(parent):
    def __init__(self,parent):
      super(). __init__(parent.eyes,parent.hair)


father=parent("brown","black")
son=child(father)


print(son.eyes)
print(son.hair)