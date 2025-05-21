# Physics
Contains files for implementing physics.

# Necessary Files
- [colors.py](https://github.com/clorbiecke/UI_Kit)

## physics_objects.py:
Defines the PhysicsObject class and child classes, like Circle, Polygon, Wall, UniformPolygon, and UniformCircle.
The PhysicsObject base class includes properties and methods for basics physics, including position, velocity, force, and their angular counterparts.

## contact.py:
Defines the Contact class and contains function for generating and resolving contacts between PhysicsObject objects.
- Each PhysicsObject should have a contact_type property for use in this file. 

## forces.py
Defines some force base classes and child classes for use with PhysicsObject objects.
Base classes: SingleForce, PairForce, BondForce
Child classes: Gravity(SingleForce), LennardJones(PairForce), HarmonicBonds(BondForce), SpringForce(BondForce), DragForce(SingleForce), Friction(SingleForce)

## effects.py
Defines a ParticleEffect class for spawning particles.
- A ParticleEffect object contains a deque which holds every particle the object spawns.
- The object will update its particles inside its own update() method. 

testing...