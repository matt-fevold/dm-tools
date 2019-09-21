# dm tools

### virtual env on windows:
`pip install virtualenv`
` virtualenv venv `
(my execution policy is restricted to not let scripts run) set execution policy to unrestricted to run the activation script - then change back afterwards)
`Set-ExecutionPolicy Unrestricted`
` .\venv\Scripts\activate `
`Set-ExecutionPolicy  Default`

now you have a virtual env and need to install dependencies

`pip install -r .\requirements.txt`

### Running the tool



go to random_encounters_tool directory

 `pip install --editable .\`

 run from same directory
 `dmtools` will now output a single random encounter 

 example output:

 `(venv) PS .\random_encounters_tool> dmtools                                                                     10
A small army of orc mercenaries is camped outside of town. They're working for the local ruler, but if they don't see battle soon they may get bored and start pillaging the countryside in search of something to do.`
