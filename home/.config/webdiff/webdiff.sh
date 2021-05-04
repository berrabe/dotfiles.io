#!/bin/bash
# This Is Not Config File, But Custom Script
# Look at {test.sh,testing.cfg} on https://github.com/danvk/webdiff
export WEBDIFF_CONFIG=$HOME/.config/webdiff/berrabe.cfg
export WEBDIFF_PORT=9000
$(which git-webdiff) $*