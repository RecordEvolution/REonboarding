# Conda & Anaconda
Environemnt and package manager for Python


## Conda CLI
the Conda CLI allows to create capsulated Python and Spark environments.

 ### Environments

2. **List environment**
name the environment `MyTest` and install `Python 3.7`
 ```
conda env list
 ``` 

2. **Create or clone a new environment**
name the environment `MyTest` and install `Python 3.7`
 ```
# new
conda create --name MyTest python=3.7
# clone
conda create --clone MyTest --name MyTest-2
 ```

3. **Activate/deactivate environment**
 ```
conda activate MyTest
conda deactivate
 ```




