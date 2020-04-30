#!/bin/bash
cd $1
cd templates/
mv assets/ static/
sed 's+assets/+static/+g' signup_bs.html > signup.html
