Fog skimmers are large, ray-like flying predators that haunt the upper reaches of mountains and ruined towers near the edge of the Roiling Fog. Their bodies are broad and thin, with membranous wings that ripple rather than flap, allowing them to glide for long stretches with minimal effort. At a distance they resemble drifting shadows or low clouds catching on the stone.

They are **tidebound** creatures. Fog skimmers do not follow day or night cycles, instead waking during the latter half of a rising fog tide. As the fog climbs the mountainside, skimmers leave their roosts and circle just above the encroaching mist, watching for animals and travelers fleeing uphill ahead of it. They rarely pursue prey for long distances, preferring to strike once exhaustion has already taken hold, using their venom to compound on their victims' exhaustion.  

![[fog-skimmer.png]]


~~~ds-statblock
type: statblock
name: Adult Fogskimmer
level: 1
roles:
  - Elite Harrier
ancestry:
  - Animal
ev: "12"
stamina: "60"
speed: 6
size: 1M
stability: 0
free_strike: 4
might: 0
agility: 2
reason: -2
intuition: 1
presence: -2
movement: flight
features:
  - type: feature
    feature_type: ability
    name: Stinging Tail
    icon: 🗡
    ability_type: Signature Ability
    keywords:
      - Melee
      - Strike
      - Weapon
    usage: Main action
    distance: Melee 1
    target: Two creatures or objects
    effects:
      - roll: Power Roll + 2
        tier1: 6 damage, +2 poison damage; M < 1 Weakened (save ends)
        tier2: 9 damage, +2 poison damage; M < 1 Weakened (save ends)
        tier3: 12 damage, +2 poison damage; M < 1 Weakened (save ends)
      - name: Effect
        effect: The animal shifts up to 2 squares between strikes.
  - type: feature
    feature_type: ability
    name: Rush
    icon: 👤
    keywords:
      - "-"
    usage: Maneuver
    distance: Self
    target: Self
    effects:
      - name: Effect
        effect: The animal moves up to their speed.
  - type: feature
    feature_type: trait
    name: Ambush Metabolism
    icon: ⭐️
    effects:
      - effect: For the first two rounds of combat, a fog skimmer can negate a bane on their abilities, or turn a double bane into a bane. From round 4 on they take a bane on all abilities.
  - type: feature
    feature_type: trait
    name: Hunter
    icon: 🏹
    effects:
        - effect: The fog skimmer ignores concealment.
~~~
^adult-tideskimmer-statblock

~~~ds-statblock
type: statblock
name: Fledgling Fogskimmer Swarm
level: 1
roles:
  - Elite Hexer
ancestry:
  - Animal
ev: "12"
stamina: "40"
speed: 5
size: 2
stability: 0
free_strike: 4
might: -2
agility: 1
reason: -3
intuition: 2
presence: -3
movement: flight
features:
  - type: feature
    feature_type: ability
    name: Flurry
    icon: 🗡
    ability_type: Signature Ability
    keywords:
      - Melee
      - Strike
      - Weapon
    usage: Main action
    distance: Melee 1
    target: Two creatures or objects
    effects:
      - roll: Power Roll + 2
        tier1: 6 damage; +2 poison damage; M < 1 Weakened (save ends)
        tier2: 9 damage; +2 poison damage; pull 1; M < 1 Weakened (save ends)
        tier3: 12 damage; +2 poison damage; pull 2; M < 1 Weakened (save ends)
      - name: Effect
        effect: If the target is pulled into the animal swarm, that forced movement deals damage only at the Director's determination.
  - type: feature
    feature_type: trait
    name: Swarm
    icon: ⭐
    keywords:
      - "-"
    usage: Maneuver
    distance: Self
    target: Self
    effects:
      - name: Effect
        effect: The fogskimmer swarm can move through spaces as if they were a size 1M creature, and can occupy other creatures’ spaces. At the start of each of the animal swarm’s turns, they can make a free strike against each creature whose space they share.
  - type: feature
    feature_type: trait
    name: Impede
    icon: ⬇️
    keywords:
      - "Area"
    usage: Maneuver
    distance: 1 aura
    target: Special
    effects:
      - name: Effect
        effect: The area is difficult terrain for enemies until the start of the swarm’s next turn.
  - type: feature
    feature_type: trait
    name: Ambush Metabolism
    icon: ⭐️
    effects:
      - effect: For the first two rounds of combat, a fog skimmer can negate a bane on their abilities, or turn a double bane into a bane. From round 4 on they take a bane on all abilities.
  - type: feature
    feature_type: trait
    name: Hunter
    icon: 🏹
    effects:
        - effect: The fog skimmer ignores concealment.
~~~
^fledgling-fogskimmer-swarm-statblock

~~~ds-statblock
type: statblock
name: Fog Skimmer Alpha
level: 1
roles:
  - Elite Brute
ancestry:
  - Animal
ev: "22"
stamina: "100"
speed: 5
size: 2
stability: 0
free_strike: 5
might: 1
agility: 2
reason: -2
intuition: 1
presence: 1
movement: flight
features:
  - type: feature
    feature_type: ability
    name: Stinging Tail
    icon: 🗡
    ability_type: Signature Ability
    keywords:
      - Melee
      - Strike
      - Weapon
    usage: Main action
    distance: Melee 3
    target: Two creatures or objects
    effects:
      - roll: Power Roll + 2
        tier1: 7 damage, +2 poison damage; M < 1 Weakened (save ends)
        tier2: 10 damage, +2 poison damage; M < 1 Prone & Weakened (save ends)
        tier3: 13 damage, +2 poison damage; M < 1 Prone & Weakened (save ends)
  - type: feature
    feature_type: ability
    name: Quick Strike
    icon: 🗡
    ability_type: Triggered action
    keywords:
      - Melee
      - Strike
      - Weapon
    usage: Main action
    distance: Melee 1
    target: The triggering creature or object
    effects:
      - name: Trigger
        effect: A creature or object comes within distance.
      - name: Effect
        effect: The predator makes a free strike against the target. If the predator was hidden from the target, the strike deals an extra 3 damage.
  - type: feature
    feature_type: ability
    name: Ready to Strike
    icon: 👤
    keywords:
      - "-"
    usage: Maneuver
    distance: Self
    target: Self
    effects:
      - name: Effect
        effect: The alpha assesses their environment and gains an edge on their next strike.
  - type: feature
    feature_type: ability
    name: Screech
    icon: 👤
    keywords:
      - "-"
    usage: Maneuver
    distance: Self
    target: Self
    effects:
      - name: Effect
        effect: Each enemy within 2 squares of the alpha with I < 1 must shift 3 squares in a striaght line away from it.
  - type: feature
    feature_type: trait
    name: Ambush Metabolism
    icon: ⭐️
    effects:
      - effect: For the first two rounds of combat, a fog skimmer can negate a bane on their abilities, or turn a double bane into a bane. From round 4 on they take a bane on all abilities.
  - type: feature
    feature_type: trait
    name: Hunter
    icon: 🏹
    effects:
        - effect: The fog skimmer ignores concealment.
~~~
^alpha-fogskimmer-statblock

## Notes
Adult Fogskimmer is an Animal with Flight, Venom, and Hunter
The swarm is an Animal Swarm with Flight, Venom, and Hunter
The Alpha is Predator A with Flight, Venom, Hunter, Reach, Fearsome, and Thick Hide x2

All have the usual "Nature's Spirit" ability replaced by the "Ambush Metabolism" ability