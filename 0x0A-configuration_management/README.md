# 0x0A. Configuration management
#### DevOps SysAdmin Scripting CI/CD

## What is Configuration Management

This is a solution for turning your infrastructure administration into a codebase, describing all processes necessary for deploying a server in a set of provisioning scripts that can be versioned and easily reused.

Some common configuration management tools include:
- Puppet
- Ansible
- Salt
- Chef

For this project, Puppet was used.

## Terms used

1. **Puppet Master**: controls configuration on nodes
2. **Puppet Agent Node**: node controlled by puppet master
3. **Manifest**: file that contains a  set of instructions to be executed
4. **Resource**: portion of code that declares an element of the system and how its state should be changed. Include packages, files, users etc.
5. **Module**: a collection of manifests and other related files organized predefined to facilitate sharing and reusing parts from provisioning.
6. **Class**: classes used in programming languages to better organize the provisioning 
7. **Facts**: global variables containing information about the system
8. **Services**: used to trigger service status changes i.e restarting or stopping a service

## Manifest
Syntax used for a manifest include:

```
resourcetype { 'title':
    attribute_name => attribute_value
}
```

