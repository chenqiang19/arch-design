# Architecture Design
**The architecture design project is to learn, summarize and document some code exercises and illustrative documents during the architecture learning process.**

## Project Structure
The project intends to manage the code in the architecture design by attaching sub-repositories to the master repository.

## Project Organization
- openstack architecture analysis
  - Paste+PasteDeploy(PPD)
  - Paste+PasteDeploy+Routes+WebOb(PPRW)
## Code Tree
```
─arch-design
│  .gitignore
│  README.md
│
└─openstack
    ├─ppd
    │  │  .gitignore
    │  │  boiler.py
    │  │  drinking.py
    │  │  hydrant.py
    │  │  main.py
    │  │  paste.ini
    │  │  purifier.py
    │  │  README.md
    │  │  shower.py
    │  │  tap.py
    │  │
    │  ├─assets
    │  │      Schematic.png
    │  │
    │  └─__pycache__
    │          boiler.cpython-38.pyc
    │          drinking.cpython-38.pyc
    │          hydrant.cpython-38.pyc
    │          purifier.cpython-38.pyc
    │          shower.cpython-38.pyc
    │          tap.cpython-38.pyc
    │
    ├─pprw
    │    │  .gitignore
    │    │  main.py
    │    │  paste.ini
    │    │  README.md
    │    │  resource_warpper.py
    │    │  server.py
    │    │
    │    └─assets
    │            nova-api-start.png
    │            routes.drawio.png
	│
    └─RBAC
        │  base.py
        │  main.py
        │  policy.py
        │  README.md
        │  request.py
        │
        ├─assets
        │      policy-flow.drawio
        │      policy-flow.drawio.png
        │
        ├─manager
        │  │  base.py
        │  │  neutron.py
        │  │  __init__.py
```