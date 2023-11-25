# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 


Analyze:
    Costs:
        VMs involve higher initial costs, while App Service offers a more cost-effective solution with reduced ongoing expenses.

    Scalability:
        VMs provide manual scaling options, whereas App Service allows seamless horizontal scaling.

    Availability:
        VMs require additional configurations for high availability, while App Service includes built-in features for improved availability.

    Workflow:
        VMs demand more manual management, whereas App Service abstracts infrastructure concerns, streamlining the development workflow.
    
Choose:
    The most appropriate solution for deploying the CMS app is App Service. This choice is justified by its cost efficiency, seamless scalability, built-in high availability features, and workflow optimization.

Assess App Changes:
    To change this decision, the CMS app would need significant alterations in its architecture and requirements. If there were a shift towards a more complex infrastructure demand that requires precise control over resources (e.g., specific hardware configurations), or if there were regulatory constraints necessitating a self-managed environment, opting for VMs might become more favorable. Additionally, if the workflow requirements significantly change, demanding more hands-on infrastructure management, a shift towards VMs could be reconsidered.