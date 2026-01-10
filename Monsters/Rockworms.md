One of the species native to the Aether Peaks before the arrival of the Roiling Fog, Rockworms live on a diet of mostly mineral-rich rock, periodically supplemented by whatever wanders into the tunnels they create as they eat.

The minerals from the rocks they eat are used to build up armor that gets thicker the larger the Rockworm grows. Sometimes parts of this armor are scraped off by cave walls or broken off in combat - these pieces can be used for several crafting projects, if the PCs have the right recipes.

* Bastion Belt (DSH p. 324) - Can use Rockworm armor in place of the giant's tooth.
* Catapult Dust (DSH p. 316) - Can crush up Rockworm armor into dust to use in place of the witherite crystal (enough for a Bastion Belt could instead make 4 catapult dust)

~~~ds-statblock
type: statblock
name: Rockworm Larva
level: 1
roles:
  - Minion Brute
ancestry:
  - Animal
ev: "3 for four minions"
stamina: "5"
speed: 5
size: 1S
stability: 1
free_strike: 2
might: 2
agility: -1
reason: -1
intuition: 0
presence: -1
movement: burrowing
features:
  - type: feature
    feature_type: ability
    name: Slam
    icon: 🗡
    ability_type: Signature Ability
    keywords:
      - Charge
      - Melee
      - Strike
      - Weapon
    usage: Main action
    distance: Melee 1
    target: One creature or object per minion
    effects:
      - roll: Power Roll + 2
        tier1: 1 damage
        tier2: 2 damage
        tier3: 3 damage
~~~
^rockworm-larva-statblock

~~~ds-statblock
type: statblock
name: Rockworm
level: 1
roles:
  - Elite Brute
ancestry:
  - Animal
ev: "12"
stamina: "60"
speed: 6
size: 1M
stability: 2
free_strike: 4
might: 2
agility: -1
reason: -1
intuition: 0
presence: -1
movement: burrowing
features:
  - type: feature
    feature_type: ability
    name: Slam
    icon: 🗡
    ability_type: Signature Ability
    keywords:
      - Charge
      - Melee
      - Strike
      - Weapon
    usage: Main action
    distance: Melee 1
    target: Two creatures or objects
    effects:
      - roll: Power Roll + 2
        tier1: 6 damage
        tier2: 9 damage
        tier3: 12 damage
      - name: Effect
        effect: The animal shifts up to 2 squares between strikes.
  - type: feature
    feature_type: ability
    name: Lithic Carapace
    icon: ⭐️
    ability_type: 1 Malice
    usage: Triggered action
    distance: Self
    target: self
    trigger: The rockworm takes damage
    effects:
      - effect: The rockworm halves the damage, and has damage weakness 3 and a +3 bonus to speed until the end of the encounter. This damage weakness increases by 3 each time the rockworm uses this ability in the same encounter.
~~~
^rockworm-statblock

~~~ds-statblock
type: statblock
name: Rockworm Alpha
level: 3
roles:
  - Elite Brute
ancestry:
  - Animal
ev: "20"
stamina: "132"
speed: 5
size: 2
stability: 2
free_strike: 6
might: 2
agility: -1
reason: 0
intuition: 1
presence: 2
movement: burrowing
features:
  - type: feature
    feature_type: ability
    name: Slam
    icon: 🗡
    ability_type: Signature Ability
    keywords:
      - Melee
      - Strike
      - Weapon
    usage: Main action
    distance: Melee 2
    target: Two creatures or objects
    effects:
      - roll: Power Roll + 2
        tier1: 8 damage
        tier2: 12 damage; M<1 restrained (save ends)
        tier3: 15 damage; M<2 restrained (save ends)
      - name: Effect
        effect: The target's space is difficult terrain
  - type: feature
    feature_type: ability
    name: Extrude Armor
    usage: Maneuver
    distance: Self
    target: Self
    effects:
      - name: Effect
        effect: Until the start of the Rockworm's next turn, any melee strike made against it takes a bane if it doesn't already have a bane or double bane.
      - name: 3 Malice
        effect: Until the end of the encounter, the Rockworm grows a thicker carapace of stone. They have a +3 bonus to stability and gain 15 temporary stamina. If they have gained damage weakness from Lithic Carapace, they lose 3 of that weakness instead of gaining the temporary hitpoints.
  - type: feature
    feature_type: ability
    name: Lithic Carapace
    icon: ⭐️
    ability_type: 1 Malice
    usage: Triggered action
    distance: Self
    target: self
    trigger: The rockworm takes damage
    effects:
      - effect: The rockworm halves the damage, and has damage weakness 3 and a +3 bonus to speed until the end of the encounter. This damage weakness increases by 3 each time the rockworm uses this ability in the same encounter.
  - type: feature
    feature_type: trait
    name: Sturdy and Grounded
    icon: ⭐️
    effects:
      - effect: The rockworm cannot be restrained, slowed, or knocked prone, and ignores difficult terrain.
  - type: feature
    feature_type: trait
    name: Primodrial Strength
    icon: ⭐️
    effects:
      - effect: The rockworm's strikes gain a +6 damage bonus against objects.
~~~
^rockworm-alpha-statblock