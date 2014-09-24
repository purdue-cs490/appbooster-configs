#!/bin/bash

case $1 in
    host)
        exec `dirname ${BASH_SOURCE}`/host/install.sh
        ;;
    container)
        echo "I need to be contained!!"
        ;;
    *)
        echo "??"
        ;;
esac
