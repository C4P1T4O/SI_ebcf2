# The "Food" class

class Food():

    def __init__(self, x, y, vel):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 6
        self.maxspeed = 1.0
        self.maxforce = 0.01
        self.contado = 0

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def fPosition(self):
        return self.position
    
    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)
        
    def contado(self):
        contado = contador + 1 
        return self.contador

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading()# + PI / 2
        fill(127)
        stroke(0)
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            rect(0, 0, self.r, self.r)
