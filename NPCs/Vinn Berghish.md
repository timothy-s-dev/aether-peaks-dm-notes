#npc

> _“We don’t build to defy the mountain. We build to remind it that people still climb.”_

A middle-age dwarven woman in engineer's work-garb covered in pockets full of obscure parts and tools. She keeps her brown hair pulled back into a frizzy ponytail, and generally smells of oil and ozone from her work.
## Traits and Motivations
Vinn likes her job a great deal, and takes it very seriously. She considers the safety and convenience of the travelers on the Dimdale-Stonehollow line her personal responsibility, and is proud of how well she has maintained both.

She's smart, and knows it, but isn't a jerk about it.
## Routine
Vinn's day-to-day involves regular maintenance of the line, cable car, and winch system. She spends most of her time at her house/workshop on the Dimdale side of the line, where the winch is found, but travels regularly to the Stonehollow side to check the anchors there.

# Retainer Stats
~~~ds-statblock
type: statblock
name: Vinn Berghish
level: 1
roles:
  - Support Retainer
ancestry:
  - Dwarf
stamina: "21"
speed: 5
size: 1M
stability: 1
free_strike: 4
might: 0
agility: 1
reason: 2
intuition: 0
presence: 0
features:
  - type: feature
    feature_type: ability
    name: Snaring Shot
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
        tier1: 6 damage; pull 1
        tier2: 9 damage; pull 3
        tier3: 12 damage; pull 5
      - name: Effect
        effect: A target restrained by Vinn's allies can be force moved by this ability. This forced movement doesn't end the retrained condition unless the director determines otherwise.
  - type: feature
    feature_type: ability
    name: Deploy Climbing Line
    icon: 👤
    keywords:
      - "-"
    usage: Maneuver
    distance: Self
    target: Self
    effects:
      - name: Effect
        effect: Until the end of her turn, Vinn can climb at her full speed while moving.
~~~

![[vinn-berghish.png]]