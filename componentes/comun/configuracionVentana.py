class ConfiguracionVentana():
    def __init__(self, root):
        self.root = root

    def configurar(self):
        self.root.title("BattleShip")
        self.root.geometry("1366x768")
        self.root.configure(bg="#292D2B")
