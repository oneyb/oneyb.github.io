#!/usr/bin/env bash

git clone https://github.com/BlackrockDigital/startbootstrap-freelancer

cp -r startbootstrap-freelancer/*/ static/

cp startbootstrap-freelancer/index.html templates/bs_index.html

sed -ri 's:src="([^"]+)":src="{{ url_for("static", filename="\1") }}":' templates/bs_index.html

sed -ri 's:href="([^h#])([^"]+)":href="{{ url_for("static", filename="\1\2") }}":' templates/bs_index.html

echo -e "\nAdditional licenses for including 'startbootstrap-freelancer':\n" >> LICENSE
cat startbootstrap-freelancer/LICENSE >> LICENSE
