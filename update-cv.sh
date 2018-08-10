#!/bin/bash -x

cp -u ~/documents/jobsearch/0-application_materials/oney_cv_*online.org content/

source venv/bin/activate

python app.py freeze

deactivate

echo "consider:  git commit . -m 'updated cv' && git push origin master"
