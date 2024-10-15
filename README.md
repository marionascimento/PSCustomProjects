# Python Monorepo [Professional Services]

## Project Setup

Instalar o Poetry 

```bash
cd /PSCustomProjects/projects/[cliente_folder]
poetry install
``` 

## Generate New Project

```bash
cd /PSCustomProjects/projects
poetry new {new project name}
cd {new project name}
poetry add ./../../libs/{project dependency lib module name}
```

## Execute from N8N
`./run_custom_script.sh [caminho do codigo python]`

Ex: ./run_custom_script.sh ./projects/cliente-wake-sample/app.py


## Project Structure

```
.
├── README.md
├── libs
│   ├── lib-x
│   └── logger
├── poetry.lock
├── projects
│   ├── __init__.py
│   ├── cliente-wake-sample
│   └── cliente-wake-sample2
├── run_custom_script.sh
└── pyproject.toml

```

`/projects`

Project code (Python modules) go here.  
Each project has its own dependencies.  

`/libs`

Each lib specifies its dependencies.  
Each lib has its own dependencies.  


