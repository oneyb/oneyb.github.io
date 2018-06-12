#!/bin/bash -x

cp -u ~/documents/jobsearch/application_materials/oney_cv_*.org content/

source venv/bin/activate

python app.py freeze

deactivate

echo "consider:  git commit . -m 'updated cv' && git push origin master"
