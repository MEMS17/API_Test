class Voiture: 

# Constructeur de la classe Voiture 

    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

 

    def avancer(self): 
        self.x += 1
        print(f"La voiture est à la position {self.x}, {self.y}") 
        return self.x, self.y 

 

    def reculer(self): 
        self.x -= 1 
        print(f"La voiture est à la position {self.x}, {self.y}") 
        return self.x, self.y 

 

    def tourner(self, direction): 
        if direction == "droite": 
            self.y -= 1 
            print(f"La voiture est à la position {self.x}, {self.y}") 

        if direction == "gauche": 
            self.y += 1 
            print(f"La voiture est à la position {self.x}, {self.y}") 

        else: 
            print(f"La voiture est à la position {self.x}, {self.y}") 
            return direction 

 

# Créer une instance de la classe Voiture 

voiture = Voiture(0, 0) 

voiture.avancer() 

voiture.tourner("gauche") 