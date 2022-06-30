# MITRE

**From Mitre.org: "At MITRE, we solve problems for a safer world. Through our federally funded R&D centers and public-private partnerships, we work across government to tackle challenges to the safety, stability, and well-being of our nation."**

## MITRE Projects

MITRE has created the following projects 
- ATT&CK® (Adversarial Tactics, Techniques, and Common Knowledge) Framework
- CAR (Cyber Analytics Repository) Knowledge Base
- SHIELD (sorry, not a fancy acronym) Active Defense
- AEP (ATT&CK Emulation Plans)

## Advanced Persistent Threat

- APT is an acronym for Advanced Persistent Threat. 
- This can be considered a team/group (threat group), or even country (nation-state group), that engages in long-term attacks against organizations and/or countries. 
- The term 'advanced' can be misleading as it will tend to cause us to believe that each APT group all have some super-weapon, e.i. a zero-day exploit, that they use. That is not the case. As we will see a bit later, the techniques these APT groups use are quite common and can be detected with the right implementations in place. You can view FireEye's current list of APT groups [here](https://www.mandiant.com/resources/apt-groups)

## MITRE ATT&CK
- MITRE ATT&CK is advanced tactics, techniques and common knowledge gathered from real world obserations
- In 2013, MITRE began to address the need to record and document common TTPs (Tactics, Techniques, and Procedures) that APT (Advanced Persistent Threat) groups used against enterprise Windows networks. This started with an internal project known as FMX (Fort Meade Experiment). Within this project, selected security professionals were tasked to emulated adversarial TTPs against a network, and data was collected from the attacks on this network. The gathered data helped construct the beginning pieces of what we know today as the ATT&CK® framework.
- Security researchers and threat intelligence groups contribute to the framework
- This is a tool for blue teamers but it is also very useful for red teamers.

## CAR (Cyber Analytics Repository)
- CAR is based on MITRE Attack adversary model

## Mitre Engenuity and Emulation Plans
- https://ctid.mitre-engenuity.org/
- https://medium.com/mitre-engenuity/introducing-the-all-new-adversary-emulation-plan-library-234b1d543f6b
- https://attack.mitre.org/docs/APT3_Adversary_Emulation_Plan.pdf


## Conclusion
- In this room, we explored tools/resources that MITRE has provided to the security community. The room's goal was to expose you to these resources and give you a foundational knowledge of their uses. Many vendors of security products and security teams across the globe consider these contributions from MITRE invaluable in the day-to-day efforts to thwart evil. The more information we have as defenders, the better we are equipped to fight back. Some of you might be looking to transition to become a SOC analyst, detection engineer, cyber threat analyst, etc. these tools/resources are a must to know.

- As mentioned before, though, this is not only for defenders. As red teamers, these tools/resources are useful as well. Your objective is to mimic the adversary and attempt to bypass all the controls in place within the environment. With these resources, as the red teamer, you can effectively mimic a true adversary and communicate your findings in a common language that both sides can understand. In a nutshell, this is known as purple teaming.  

## References
- [MITRE Navigator](https://mitre-attack.github.io/attack-navigator//#layerURL=https%3A%2F%2Fattack.mitre.org%2Fgroups%2FG0008%2FG0008-enterprise-layer.json)
