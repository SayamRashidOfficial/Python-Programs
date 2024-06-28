class Bird:
    def chirp(self):
        return "Chirp chirp!"

class Fly:
    def fly(self):
        return "Flying high!"

class FlyingBird(Bird, Fly):
    pass

bird = FlyingBird()

print(bird.chirp()) 
print(bird.fly())   
