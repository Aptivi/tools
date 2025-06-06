#!/bin/bash

prebuild() {
    echo "Pre-build action executed from $ROOTDIR"
}

build() {
    echo "Build action executed from $ROOTDIR"
}

postbuild() {
    echo "Post-build action executed from $ROOTDIR"
}

preclean() {
    echo "Pre-clean action executed from $ROOTDIR"
}

clean() {
    echo "clean action executed from $ROOTDIR"
}

postclean() {
    echo "Post-clean action executed from $ROOTDIR"
}

predocpack() {
    echo "Pre-docpack action executed from $ROOTDIR"
}

docpack() {
    echo "Documentation packing action executed from $ROOTDIR"
}

postdocpack() {
    echo "Post-docpack action executed from $ROOTDIR"
}

predocgenerate() {
    echo "Post-docgenerate action executed from $ROOTDIR"
}

docgenerate() {
    echo "Documentation generation action executed from $ROOTDIR"
}

postdocgenerate() {
    echo "Post-docgenerate action executed from $ROOTDIR"
}

prepackall() {
    echo "Pre-pack action executed from $ROOTDIR"
}

packall() {
    echo "Pack action executed from $ROOTDIR"
}

postpackall() {
    echo "Post-pack action executed from $ROOTDIR"
}

prepushall() {
    echo "Pre-push action executed from $ROOTDIR"
}

pushall() {
    echo "Push action executed from $ROOTDIR"
}

postpushall() {
    echo "Post-push action executed from $ROOTDIR"
}

prelocalize() {
    echo "Pre-localization action executed from $ROOTDIR"
}

localize() {
    echo "Localization action executed from $ROOTDIR"
}

postlocalize() {
    echo "Post-localization action executed from $ROOTDIR"
}

preincrement() {
    echo "Pre-increment action executed from $ROOTDIR"
}

increment() {
    echo "Increment action executed from $ROOTDIR"
}

postincrement() {
    echo "Post-increment action executed from $ROOTDIR"
}
