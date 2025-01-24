#!/bin/bash

if grep -q docker /proc/1/cgroup; then
  echo "Running inside a Docker container."
elif grep -q kubepods /proc/1/cgroup; then
  echo "Running inside a Kubernetes pod."
else
  echo "Not running inside a container."
fi
