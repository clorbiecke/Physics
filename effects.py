from physics_objects import Particle
from pygame.math import Vector2
import colors
import forces
import pygame
import random
from collections import deque

# FIXME: 
# - Does ltime even do anything? Remove it? 
# - 'effects', 'ltime', and 'update_all()' should be made into instance variables/methods rather than class vars/methods. 
# - A ParticleEffect object will add all of the particles it spawns to its own deque
#   and update them as part of its own update() method. 
class ParticleEffect:
    effects = deque()
    ltime = pygame.time.get_ticks()
    @classmethod
    def update_all(cls, dt):
        while cls.effects and cls.effects[0].duration < 0:
            cls.effects.popleft()
        for effect in cls.effects:
            effect.update(dt)
        # print(f"num particles: {len(Particle.particles)}")
        # print(f"dt: {pygame.time.get_ticks() - Particle.ltime}")
        cls.ltime = pygame.time.get_ticks()
    def __init__(self, duration:float=0, num_particles:int=100):
        self.num_particles = num_particles
        self.duration = duration
        ParticleEffect.effects.append(self)
    
    def update(self, dt=0):
        # print("update called on Particle_Effect")
        if self.duration < 0: del self
        else:
            if dt < self.duration:
                n=int((dt/self.duration)*self.num_particles)
            else:
                n=self.num_particles
            
            self.spawn_particles(n)
            self.duration -= dt
            
    def spawn_particles(self, n:int): 
        pass


def impact_effect(impact_normal:Vector2, impact_pos, impact_strength, **kwargs):
    # print("impact_effect called!")
    Impact_Effect(impact_normal=impact_normal, impact_pos=impact_pos, impact_strength=impact_strength, **kwargs)
# shoots out particles to both sides of a given direction
class Impact_Effect(ParticleEffect):
    def __init__(self, impact_normal:Vector2, impact_pos, impact_strength, duration=0, num_particles=50, color=colors.white, to_color=colors.alpha(colors.black, 128)):
        super().__init__(duration, num_particles)
        # print("Impact_Effect created!")
        self.spawn_normal:Vector2 = Vector2(impact_normal.y, -impact_normal.x)
        self.impact_normal:Vector2 = impact_normal
        self.pos:Vector2 = impact_pos
        self.strength:float = impact_strength
        self.k:float = 1 # coefficient for changing direction of particle velocity
        self.color = color
        self.to_color = to_color
    def __del__(self):
        pass# print("Impact_Effect is being deleted")
    def spawn_particles(self, n:int):
        # print("spawning particles...")
        for i in range(n):
            self.k *= -1
            size = random.uniform(2,10)
            mass = 0.0000001 * size
            spd = self.k * self.strength * random.gauss(0.5,0.12)
            pos = self.pos
            ortho = random.gauss(0,0.25) * self.impact_normal
            vel = spd * (self.spawn_normal + ortho)
            # print(f"spawning particle at pos {pos}, vel: {vel}, mag: {vel.magnitude()}, str: {self.strength}")
            Particle(size=size, color=self.color, lifetime=250, to_color=self.to_color, mass=mass, pos=pos, vel=vel)

