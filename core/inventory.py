class Item:
    def __init__(self, name, type, description, prop, efecto=None):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop
        self.efecto = efecto

    def tiene_efecto(self):
        return self.efecto is not None
