#!/bin/bash#

rclone copy stc-src:bk-trietnguyen-stc/ubuntu-24.04.1-desktop-amd64.iso stc-dest:des-tnguyen547-stc --multi-thread-chunk-size 512Mi --multi-thread-streams 32 --multi-thread-write-buffer-size 1024Ki -P --log-file rclone.log --log-level INFO --transfers 16 --checkers 64 --buffer-size 512Mi