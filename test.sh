#!/bin/bash

PYTHONPATH=../:$PYTHONPATH
nosetests test/lib
