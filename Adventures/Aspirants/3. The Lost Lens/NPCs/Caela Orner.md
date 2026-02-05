A friend of [[Sir Alaric Vale]], based on Navani Kholin.

An aristocrat in [[Stormcradle]], who is a big patron of the sciences.

Has some sort of exotic pet, maybe like a mini-dragon or something?

# Retainer Stats
~~~ds-statblock
type: statblock
name: Caela Orner
level: 1
roles:
  - Artillery Retainer
ancestry:
  - Human
stamina: "21"
speed: 6
size: 1M
stability: 1
free_strike: 2
might: 0
agility: 2
reason: 1
intuition: 0
presence: 1
features:
  - type: feature
    feature_type: ability
    name: Lightning Bolt
    icon: 🗡
    ability_type: Signature Ability
    keywords:
      - Ranged
      - Strike
      - Weapon
    usage: Main action
    distance: Ranged 15
    target: One creature or object
    effects:
      - roll: Power Roll + 2
        tier1: 4 damage
        tier2: 7 damage
        tier3: 10 damage
      - name: Effect
        effect: Caela can take a bane on this ability to gain +5 range.
  - type: feature
    feature_type: ability
    name: Enchanted Weave
    icon: 👤
    keywords:
      - "-"
    usage: Maneuver
    distance: Self
    target: Self
    effects:
      - name: Effect
        effect: Abilities targeting Caela that would take a bane from cover or concealment have a double bane instead.
~~~
(Note - this is a re-skinned Wode Elf Arrowswitft retainer from page 363 of the Monster book)