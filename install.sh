#!/bin/bash

case $1 in
    brain)
        exec `dirname ${BASH_SOURCE}`/brain/install.sh
        ;;
    zombine)
        echo "I want brains!!"
        ;;
    *)
        echo "??"
        ;;
esac
