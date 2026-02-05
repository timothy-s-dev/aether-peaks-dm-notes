#npc 

> *"The Fog isn't just a threat, it's a key; and I intend to be the one to turn it."*

Elara Vance is a middle-aged human woman in a practical robe, covered in small pockets and pouches containing the various ingredients and tools of her trade. She is an herbalist working in the town of [[Places/Dimdale]].  She is secretly pursuing membership with the [[Lanternbound]], hoping to avail herself of their arcane power and secret knowledge.

She has seen what the Roiling Fog can do to plant-life, and thinks it could be carefully manipulated and used to open up new avenues of research into alchemy.  She over-heard once a story about how the Lanternbound can control the Fog, and so when they appeared outside of town she seized on the opportunity.

# Retainer Stats
~~~ds-statblock
type: statblock
name: Elara Vance
level: 1
roles:
  - Hexer Retainer
ancestry:
  - Human
stamina: "21"
speed: 5
size: 1M
stability: 1
free_strike: 3
might: 0
agility: 1
reason: 2
intuition: 1
presence: 0
features:
  - type: feature
    feature_type: ability
    name: Tanglevine Bag
    icon: 🗡
    ability_type: Signature Ability
    keywords:
      - Ranged
      - Strike
      - Weapon
    usage: Main action
    distance: Ranged 5
    target: One creature or object
    effects:
      - roll: Power Roll + 2
        tier1: 5 damage; A<0 restrained (save ends)
        tier2: 7 damage; A<1 restrained (save ends)
        tier3: 9 damage; A<2 restrained (save ends)
  - type: feature
    feature_type: ability
    name: Smokescreen!
    icon: 🗡
    ability_type: Triggered action
    target: Self
    effects:
      - name: Trigger
        effect: Elara would be grabbed, prone, slowed, or weakened.
      - name: Effect
        effect: Elara deploys a smokebomb allowing her to immediately end the condition, and shift up to 2 squares. This can only be used once per encounter. 
~~~

![[elara-vance.png]]