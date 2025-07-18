---
author: Martin Bustos
title: True Ballistics
showTitle: false
date: 0
description: A physically-accurate ballistics that provides realistic bullet trajectories, ricochets, penetration, ...
tags: ["unity", "store", "FPS", "ballistic", "bullet", "weapon", "physics", "shooter", "first person", "bullets"]
metadata: none
showImage: false
thumbnail:
  url: img/true-ballistics.jpg
---
{{< asset-header youtube="44zTW3yJL-Y" store="" demo="" >}}

A comprehensive, **physically-accurate** ballistics simulation system for Unity that provides **realistic trajectories**, **ricochets**, **penetration** mechanics, and advanced ballistic effects for games requiring authentic projectile behavior.

- **Physically Accurate**: Implements real-world ballistics physics including gravity, air resistance, drag models (G1, G2, G5, G6, G7, G8), and environmental effects.
- **High Performance**: Built on a custom lightweight Entity Component System (ECS) architecture with Unity Jobs and Burst compilation for optimal performance, capable of handling hundreds of simultaneous projectiles.
- **Realistic Ricochets**: Physically-based bullet deflection with angle-dependent probability and energy retention based on material properties.
- **Advanced Penetration Mechanics**: Energy-based projectile penetration through materials with realistic entry/exit behavior and stuck projectile handling.
- **Comprehensive Material System**: Extensive surface interaction properties with material-specific ballistic characteristics for different surfaces.
- **Advanced Effects**: Coriolis effect, spin drift, weather simulation, and atmospheric conditions.
- **Visual Feedback**: Built-in tracer system and comprehensive debug visualization tools.
- **Extensive Weapons Database**: 380+ real-world weapons with authentic ballistic data including pistols, rifles, shotguns, machine guns, and sniper rifles.
- **Educational FPS Demo**: Complete SimpleFPS demo system showcasing all features with clean, documented code.

#### What Can Be Used For

✅ **Realistic Ballistics Simulation**: Accurate trajectories with proper physics for FPS, military, hunting, ...
✅ **Material Penetration**: Realistic projectile behavior through different materials (wood, metal, concrete, etc).
✅ **Ricochet Effects**: Physically-based bullet deflection off surfaces .
✅ **Long-Range Shooting**: Precision ballistics for sniper games with environmental factors.
✅ **Performance-Critical Games**: Optimized for handling thousands of simultaneous projectiles.

#### What Is NOT

❌ **FPS Controller**: While it includes a `SimpleFPS` system, it's designed for ballistics simulation, **not as a FPS character controller**.
❌ **Visual Effects System**: Focuses on physics simulation rather than muzzle flashes, explosions, or other visual effects.
❌ **Weapon Animation System**: Doesn't handle weapon animations, reloading animations, or complex weapon mechanics.
❌ **Audio System**: Doesn't provide comprehensive audio management beyond basic demo sounds.
❌ **Networking Solution**: Designed for single-player simulations, not multiplayer networking.
❌ **Energy Weapons or Propelled Projectiles**: Designed for ballistic projectiles only, doesn't support laser weapons, plasma guns, or self-propelled projectiles like rockets and missiles.

### Requirements

* Unity 6000.0 LTS or newer.

### Installation

1. Download and import the `True Ballistics` asset from the Unity Asset Store into your Unity project.
3. No additional setup is required. The asset is ready to use out of the box!

### How to Use

The `BallisticsManager` component is the central hub of the ballistics system. It manages the lightweight ECS, handles projectile spawning, and coordinates all ballistic systems.

Create an empty GameObject and add the `BallisticsManager` component (Fronkon Games → True Ballistics → Ballistics Manager)

{{< image src="inspector_0.jpg" wrapper="col-9 mx-auto">}}

###### Add systems

Systems are modules that take care of a task. You can add as many as you want in `Systems`, this way you will only use the ones you need.

They are [ScriptableObjects](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html) and therefore files. You can create them from the `Project` window (Fronkon Games → True Ballistics → Systems)

{{< image src="inspector_1.jpg" wrapper="col-9 mx-auto">}}

All the systems included are discussed in more detail below. The minimum recommended systems are:

- **Physics System**: without this system the projectiles would not move.
- **Lifecycle System**: is in charge of _recycling_ projectiles. Without this system the projectiles would never be destroyed and when reaching the maximum number (5000 by default), no new ones would be created.
- **Collision System**: the one in charge of reporting collisions with projectiles.

Once these three systems are added, you can fire a projectile in this way:

```csharp
// Get the manager instance
BallisticsManager manager = FindFirstObjectByType<BallisticsManager>();

// Spawn a projectile
int projectileEntity = manager.SpawnProjectile(
    weaponData,          // WeaponData ScriptableObject
    transform.position,  // Spawn position
    transform.rotation,  // Spawn rotation
    1.0f,                // Dispersion multiplier
    true,                // Can jam
    1.0f                 // Velocity multiplier
);

// Spawn pellets (for shotguns)
List<int> pellets = manager.SpawnPellets(
    weaponData,          // WeaponData ScriptableObject
    shellData,           // ShellData ScriptableObject
    transform.position,  // Spawn position
    transform.rotation   // Spawn rotation
);
```

`weaponData` is another ScriptableObject (a file) with all the relevant data of a weapon model. You have more than 380 in the `FronkonGames/TrueBallistics/Data/Weapons` folder.

{{< image src="inspector_2.jpg" wrapper="col-9 mx-auto">}}

In the case of shotguns, in addition to the corresponding `weaponData`, you must add `shellData`, the type of cartridge you want to use. You can find several in `FronkonGames/TrueBallistics/Data/Ammo`.

You can create new weapons (and shells) from the `Project` window (Fronkon Games → True Ballistics → Weapon Data / Fronkon Games → True Ballistics → Shell Data).

{{< image src="inspector_3.jpg" wrapper="col-9 mx-auto">}}

### Systems

`True Ballistics` uses a custom lightweight ECS architecture optimized for ballistics simulation:

* **Entities**: Simple integer IDs representing projectiles (max 5000 concurrent).
* **Components**: Data structures (PhysicsComponent, DragComponent, etc).
* **Systems**: Logic processors that operate on entities with specific components.

#### Physics System

{{< image src="inspector_4.jpg" wrapper="col-9 mx-auto">}}

Handles core ballistics physics including gravity, drag, and atmospheric effects. Without this system the projectiles **would not move**.

**Features**:
- Configurable gravity vector (supports other planets).
- Air density simulation with altitude effects.
- Multiple drag models (G1, G2, G5, G6, G7, G8).
- Wind effects and atmospheric conditions.
- Burst-compiled jobs for performance.

**Configuration**:
- `Gravity`: Gravity vector (default: Earth's 9.81 m/s²).
  - Moon: 1.62 m/s².
  - Mars: 3.71 m/s².
  - Jupiter: 24.79 m/s².
  - Saturn: 10.44 m/s².
  - Uranus: 8.87 m/s².
  - Neptune: 11.15 m/s².
  - Pluto: 0.62 m/s².
  - Sun: 274.0 m/s².
  - Venus: 8.87 m/s².
  - Mercury: 3.70 m/s².
  - Io: 1.796 m/s².
  - Europa: 1.315 m/s².
  - Ganymede: 1.428 m/s².
  - Callisto: 1.235 m/s².
- `Air Density`: Air density in kg/m³ (default value is 1.225 kg/m³ at sea level).
  - 0.001225 kg/m³ at 10,000 meters.
  - 0.0001225 kg/m³ at 20,000 meters.
  - 0.00001225 kg/m³ at 30,000 meters.
  - 0.000001225 kg/m³ at 40,000 meters.
  - 0.0000001225 kg/m³ at 50,000 meters.
- `Speed Of Sound`: Speed of sound for [Mach](https://en.wikipedia.org/wiki/Mach_number) calculations (default value is 343 m/s at sea level).
  - 295 m/s at 10,000 meters.
  - 235 m/s at 20,000 meters.
  - 196 m/s at 30,000 meters.
  - 167 m/s at 40,000 meters.
  - 145 m/s at 50,000 meters.
- `Max Speed`: Maximum projectile velocity in m/s (default value is 299,792,458 m/s, the speed of light in vacuum).

#### Lifecycle System

{{< image src="inspector_5.jpg" wrapper="col-9 mx-auto">}}

Manages projectile lifecycle with configurable termination rules. **It is essential to add this system**, since it is in charge of _recycling_ projectiles. Without this system, when the maximum number of projectiles is reached (5000 by default), no more can be created.

If any of the following (active) rules are met, the projectile is deactivated.

##### Max Lifetime Rule

Deactivates the projectile if its lifetime has exceeded a certain limit.

##### Min Speed Percentage Rule

Deactivates the projectile if its speed is below a certain percentage.

##### Min Bounds Rule

Deactivates the projectile if its coordinates are less than a certain limit.

##### Max Bounds Rule

Deactivates the projectile if its coordinates are greater than a certain limit.

##### Stationary Rule

Deactivates the projectile if it has been stationary for a certain amount of time.

##### Max Distance Rule

Deactivates the projectile if it has traveled a certain linear distance from its point of origin.

##### One Collision Rule

Deactivates the projectile after its first collision.

If you use the `Ricochet System`, a bouncing projectile **does not count for this rule**.

##### Ricochet Rule

Deactivates the projectile if a ricochet occurred with an angle lower than a certain limit.

##### Ricochet Failed Rule

If true, projectiles are deactivated upon any impact that does not result in a ricochet. This overrides `One Collision Rule` if both are true.

#### Collision System

{{< image src="inspector_6.jpg" wrapper="col-9 mx-auto">}}

Efficient collision detection with adaptive algorithms. Remember that for a projectile to collide with an object on the stage, this object must have some kind of [Collider](https://docs.unity3d.com/Manual/collision-section.html).

**Features**:
- Raycast for high-speed projectiles.
- Batched SphereCasts for regular projectiles.
- Configurable layer masks.
- Automatic material detection.

**Configuration**:
- `Layer Mask`: Collision layers.
- `High Speed Threshold`: Percentage of the speed of light (default 10%) at which RayCast is used instead of SphereCast (the projectile is considered instantaneous).

Once added to the systems, you can subscribe to the `OnProjectileHit` events to receive information on each impact.

```csharp
// Cache all colliders on this object and its children for efficient hit detection
colliders = this.GetComponentsInChildren<Collider>();

// Get the manager instance
BallisticsManager manager = FindFirstObjectByType<BallisticsManager>();

// Subscribe to projectile hit event (don't forget to unsubscribe)
ballisticsManager.OnProjectileHit += OnProjectileHitHandler;

...

private void OnProjectileHitHandler(CollisionInfo info)
{
  // Skip processing if collision info is invalid
  if (info.collider == null)
    return;

  // Check if the hit collider belongs to this object (or any of its children)
  foreach (Collider c in colliders)
  {
    if (c != null && info.collider == c)
    {
      // Doing something
      break;
    }
  }
}
```

Check these classes in `FronkonGames/TrueBallistics/Demos/Scripts` for more examples:
* **Coin**: A coin that oscillates and disappears upon impact.
* **DestroyOnHit**: The object is destroyed on impact.
* **NonKinematicOnHit**: Changes a Kinematic object to Non Kinematic on impact.

Objects with Colliders and physics ([RigidBody](https://docs.unity3d.com/Manual/rigidbody-physics-section.html)) **do not receive any physical impulse** when hitting a projectile (it is not the goal of this library). However you can consult the `RigidBodyManager` class to see an example of how to do it.

Neither create bullet marks or particles at the point of impact, although you can see how this is done in the demo in the `HolesManager` and `SparksManager` classes. Both solutions are quite rudimentary (enough for the purposes of the demo) so **I do not recommend** using them in production environments.

#### Ricochet System

{{< image src="inspector_7.jpg" wrapper="col-9 mx-auto">}}

Realistic ricochet simulation based on impact angle and material properties.

**Features**:
- Probability-based ricochet calculation.
- Physically-based velocity changes.
- Material-specific restitution.
- Energy retention modeling.

Once added to the systems, you can subscribe to the `OnProjectileRicochet` events to receive information on each ricochet.

#### Penetration System

{{< image src="inspector_8.jpg" wrapper="col-9 mx-auto">}}

Advanced penetration mechanics with energy-based calculations.

**Features**:
- Entry/exit point calculation.
- Energy consumption modeling.
- Path deflection on entry.
- Stuck projectile handling.

**Configuration**:
- `energyScale`: Energy scaling factor.
- `maxEntryDeflectionAngleDegrees`: Maximum entry deflection.

{{< alert color="warning" >}}
SECTION UNDER CONSTRUCTION
{{< /alert >}}

#### Tracer System

{{< image src="inspector_9.jpg" wrapper="col-9 mx-auto">}}

GPU-accelerated visual tracer rendering. 

**Features**:
- Compute shader-based geometry generation.
- Per-weapon-type configuration.
- Brightness based on velocity.
- Separate head/tail materials.

{{< alert color="warning" >}}
SECTION UNDER CONSTRUCTION
{{< /alert >}}

#### Weather System

{{< image src="inspector_10.jpg" wrapper="col-9 mx-auto">}}

Environmental effects simulation using ICAO Standard Atmosphere.

**Features**:
- Altitude-based air density.
- Temperature effects.
- Wind simulation.
- Precipitation effects.

**Configuration**:
- `altitude`: Altitude in meters.
- `temperature`: Temperature in Celsius.
- `wind`: Wind vector in m/s.
- `precipitation`: Precipitation intensity (0-1).

{{< alert color="warning" >}}
SECTION UNDER CONSTRUCTION
{{< /alert >}}

#### Coriolis System

{{< image src="inspector_11.jpg" wrapper="col-9 mx-auto">}}

Coriolis effect simulation for long-range ballistics.

**Features**:
- Configurable planetary parameters.
- Latitude-based calculations.
- Realistic deflection patterns.

**Configuration**:
- `planetAngularVelocity`: Planet rotation rate.
- `latitude`: Observer latitude.

{{< alert color="warning" >}}
SECTION UNDER CONSTRUCTION
{{< /alert >}}

#### Spin Drift System

{{< image src="inspector_12.jpg" wrapper="col-9 mx-auto">}}

Spin-induced projectile drift for long-range simulation.

**Features**:
- Magnus effect calculation.
- Twist rate considerations.
- Barrel length effects.

**Configuration**:
- `driftFactor`: Overall drift scaling.

{{< alert color="warning" >}}
SECTION UNDER CONSTRUCTION
{{< /alert >}}

#### Debug System

{{< image src="inspector_13.jpg" wrapper="col-9 mx-auto">}}

{{< alert color="warning" >}}
This system uses Debug.DrawLine and can affect performance **only** in the Editor (in builds it has no effect).
{{< /alert >}}

Comprehensive debug visualization (Editor only).

**Features**:
- Trajectory visualization with speed coloring
- Force vector display
- Impact point markers
- Ricochet and penetration visualization
- Configurable retention time

{{< alert color="warning" >}}
SECTION UNDER CONSTRUCTION
{{< /alert >}}

### Customs Systems

Creating a custom system involves inheriting from `SystemBase` and implementing the required methods:

```csharp
[CreateAssetMenu(fileName = "CustomSystem", menuName = "My Game/Custom System")]
public class CustomSystem : SystemBase
{
  // Execution order (lower = earlier)
  public override int ExecutionOrder => 1500;
    
  // System initialization
  public override void Initialize(BallisticsManager manager)
  {
      base.Initialize(manager);
      // Setup system resources
  }
    
  // Called before physics update
  public override void PreTick(float deltaTime)
  {
      if (!active) return;
      // Pre-physics logic
  }
    
  // Main system update
  public override void Tick(float deltaTime)
  {
      if (!active) return;
      // Main system logic
  }
    
  // Called after physics update
  public override void PostTick(float deltaTime)
  {
      if (!active) return;
      // Post-physics logic
  }
    
  // System cleanup
  public override void DeInitialize()
  {
      // Cleanup resources
      base.DeInitialize();
  }
}
```

**Example: Simple Gravity Well System**

```csharp
[CreateAssetMenu(fileName = "GravityWellSystem", menuName = "My Game/Gravity Well System")]
public class GravityWellSystem : SystemBase
{
    [Header("Gravity Well Settings")]
    public Transform gravityWellCenter;
    public float gravityWellStrength = 10f;
    public float gravityWellRadius = 50f;
    
    public override int ExecutionOrder => SystemExecution.Physics + 50; // After PhysicsSystem
    
    public override void PostTick(float deltaTime)
    {
        if (!active || gravityWellCenter == null) return;
        
        // Get component arrays
        var physicsComponents = manager.GetComponentArray<PhysicsComponent>();
        
        // Process all entities with physics components
        for (int i = 0; i < BallisticsManager.MaxEntities; i++)
        {
            if (!manager.entities[i]) continue;
            
            ref var physics = ref physicsComponents[i];
            
            // Calculate distance to gravity well
            Vector3 toWell = gravityWellCenter.position - physics.position;
            float distance = toWell.magnitude;
            
            // Apply gravity well force if within radius
            if (distance < gravityWellRadius && distance > 0.1f)
            {
                float force = gravityWellStrength / (distance * distance);
                Vector3 gravityForce = toWell.normalized * force * physics.mass;
                
                // Apply force
                physics.velocity += gravityForce * deltaTime / physics.mass;
            }
        }
    }
}
```

{{< alert color="warning" >}}
SECTION UNDER CONSTRUCTION
{{< /alert >}}

### Simple FPS

`SimpleFPS` is an educational first-person controller demo that showcases `True Ballistics` integration. **It's designed for learning and prototyping, not production use.**

#### Purpose

- **Educational**: Demonstrates best practices for ballistics integration
- **Prototyping**: Rapid testing of weapon configurations
- **Reference**: Clean, documented code for learning
- **Decoupled**: Event-driven architecture for easy modification

#### Architecture

- **Event-Driven**: Uses `SimpleFPSEvents` for decoupled communication
- **Auto-Wired**: `SimpleFPSDependencyContainer` automatically subscribes methods
- **Modular**: Each component handles a specific responsibility

#### Key Components

- **SimpleFPSInput**: Keyboard/mouse input handling
- **SimpleFPSMovement**: Character movement with physics
- **SimpleFPSCamera**: Mouse look with pitch/yaw
- **SimpleFPSWeapon**: Weapon handling and ballistics integration
- **SimpleFPSInventory**: Weapon switching and ammo management
- **SimpleFPSAudio**: Centralized audio management
- **SimpleFPSPlayer**: Physics and collision handling

#### Features

- **Movement**: Walking, sprinting, jumping, crouching
- **Camera**: Smooth mouse look with configurable sensitivity
- **Weapons**: 7-slot weapon system with realistic ballistics
- **Audio**: Footsteps, weapon sounds, and environmental audio
- **Effects**: Head bob, weapon sway, and recoil
- **Ballistics**: Full integration with True Ballistics system

#### Usage Guidelines

✅ **Use for**: Learning, prototyping, testing weapon configurations
❌ **Don't use for**: Production games, complex gameplay systems

{{< alert color="warning" >}}
**⚠️ Support Notice**: SimpleFPS is provided as-is for educational purposes only. No support is provided for implementation, customization or troubleshooting.
{{< /alert >}}

{{< alert color="warning" >}}
SECTION UNDER CONSTRUCTION
{{< /alert >}}

---
#
## Support

Do you have any problem or any suggestions? Send me an email to **fronkongames@gmail.com** and I'll be happy to help you.

Remember that if you want to inform me of an error, it would help me if you sent to me the [log file](https://docs.unity3d.com/Manual/LogFiles.html).

{{< rawhtml >}}
<br><center><h4>
{{< /rawhtml >}}

{{< alert color="warning" >}}
If you are happy with this asset, consider write a review in the store

❤️ thanks! ❤️
{{< /alert >}}

{{< rawhtml >}}
</center></h4>
{{< /rawhtml >}}
