#!/bin/bash

echo "This will update this git project"

echo "adding files ..."
git add *

echo "removing useless files ..."

cd grabbo
git rm -r --cached __pycache__

cd ..
git rm -r --cached .gitignore

echo "ready to commit and push"
