#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

for i in photos/*
do
  ./run.sh photos/original.jpg $i >> test.md
done

exit O
