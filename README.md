# cnnClass
## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml



Config
secret
param
entity
config
compo
pipeline
main
dvc



##

tensorbaord to watch model information
tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/
This will open in port 6060

dvc 
dvc init -- for intialization
dvc repro that will run all the steps in pipeline

python app.py  - flask app running in 8080
