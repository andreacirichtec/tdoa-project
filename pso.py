import math
import random

class Point:
    def __init__(self,x, y, z):
        self.x = x     
        self.y = y
        self.z = z

    def __str__(self):
        return f"({round(self.x,2)},{round(self.y,2)},{round(self.z,2)})"

    def distance(self,P):
        return math.dist((self.x,self.y,self.z),(P.x,P.y,P.z))

class Particle:
    def __init__(self,x0):
        self.position = []              # particle position
        self.velocity = []              # particle velocity
        self.personal_best = []         # best position individual
        self.err_best_personal = -1     # best error individual
        self.err = -1                   # error individual

        for i in range(0,num_dimensions):
            self.velocity.append(random.uniform(-1,1))
            self.position.append(x0[i])

    # evaluate current fitness
    def evaluate(self,costFunc):
        self.err=costFunc(self.position)

        # check to see if the current position is an individual best
        if (self.err < self.err_best_personal) or (self.err_best_personal == -1):
            self.personal_best = self.position
            self.err_best_personal = self.err

    # update new particle velocity
    def update_velocity(self,global_best):
        w = 0.729         # constant inertia weight (how much to weigh the previous velocity)
        c1 = 1.494        # cognative constant
        c2 = 1.494        # social constant

        for i in range(0,num_dimensions):
            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)

            vel_cognitive = c1 * r1 * (self.personal_best[i] - self.position[i])
            vel_social = c2 * r2 * (global_best[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + vel_cognitive + vel_social

    # update the particle position based off new velocity updates
    def update_position(self,bounds):
        for i in range(0,num_dimensions):
            self.position[i] = self.position[i] + self.velocity[i]

            # adjust maximum position if necessary
            if (self.position[i] > bounds[i][1]):
                self.position[i] = bounds[i][1]

            # adjust minimum position if neseccary
            if (self.position[i] < bounds[i][0]):
                self.position[i] = bounds[i][0]


def PSO(costFunc,x0,bounds,num_particles,maxiter):
    global num_dimensions

    num_dimensions  = len(x0)
    err_best_global = -1                   # best error for group
    global_best     = []                   # best position for group

    # establish the swarm
    swarm = []
    for i in range(0,num_particles):
        swarm.append(Particle(x0))

    # begin optimization loop
    i = 0
    while i < maxiter:
        # cycle through particles in swarm and evaluate fitness
        for j in range(0,num_particles):
            swarm[j].evaluate(costFunc)

            # determine if current particle is the best (globally)
            if (swarm[j].err < err_best_global) or (err_best_global == -1):
                global_best = list(swarm[j].position)
                err_best_global = float(swarm[j].err)

        # cycle through swarm and update velocities and position
        for j in range(0,num_particles):
            swarm[j].update_velocity(global_best)
            swarm[j].update_position(bounds)
        i+=1

    return global_best, err_best_global
