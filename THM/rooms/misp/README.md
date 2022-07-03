# MISP (Malware Information Sharing Platform)
- Information can be consumed by `Network Intrusion Detection Systems (NIDS)`, `SIEM` and `Log Analysis Tools`.

## UseCases

- Malware Reverse Engineering: Sharing of malware indicators to understand how different malware families function.
- Security Investigations: Searching, validating and using indicators in investigating security breaches.
- Intelligence Analysis: Gathering information about adversary groups and their capabilities.
- Law Enforcement: Using indicators to support forensic investigations.
- Risk Analysis: Researching new threats, their likelihood and occurrences.
- Fraud Analysis: Sharing of financial indicators to detect financial fraud.


## Support

- IOC database: This allows for the storage of technical and non-technical information about malware samples, incidents, attackers and intelligence.
- Automatic Correlation: Identification of relationships between attributes and indicators from malware, attack campaigns or analysis.
- Data Sharing: This allows for sharing of information using different models of distributions and among different MISP instances.
- Import & Export Features: This allows the import and export of events in different formats to integrate other systems such as NIDS, HIDS, and OpenIOC.
- Event Graph: Showcases the relationships between objects and attributes identified from events.
- API support: Supports integration with own systems to fetch and export events and intelligence.


## Terms

- Events: Collection of contextually linked information.
- Attributes: Individual data points associated with an event, such as network or system indicators.
- Objects: Custom attribute compositions.
- Object References: Relationships between different objects.
- Sightings: Time-specific occurrences of a given data point or attribute detected to provide more credibility.
- Tags: Labels attached to events/attributes.
- Taxonomies: Classification libraries are used to tag, classify and organise information.
- Galaxies: Knowledge base items used to label events/attributes.
- Indicators: Pieces of information that can detect suspicious or malicious cyber activity.

## Tagging Best Practices

** Tagging Best Practices **
*Tagging at Event level vs Attribute Level*

- Tags can be added to an event and attributes. Tags are also inheritable when set. It is recommended to set tags on the entire event and only include tags on attributes when they are an exception from what the event indicates. This will provide a more fine-grained analysis.

- The minimal subset of Tags

- The following tags can be considered a must-have to provide a well-defined event for distribution:

- **Traffic Light Protocol**: Provides a colour schema to guide how intelligence can be shared.
- **Confidence**: Provides an indication as to whether or not the data being shared is of high quality and has been vetted so that it can be trusted to be good for immediate usage.
- **Origin**: Describes the source of information and whether it was from automation or manual investigation.
- **Permissible Actions Protocol**: An advanced classification that indicates how the data can be used to search for compromises within the organisation.

## References

- [MISP Book](https://www.circl.lu/doc/misp/)
- [MISP GitHub](https://github.com/MISP/)
- [CIRCL MISP Training Module 1](https://www.youtube.com/watch?v=aM7czPsQyaI)
- [CIRCL MISP Training Module 2](https://www.youtube.com/watch?v=Jqp8CVHtNVk)
