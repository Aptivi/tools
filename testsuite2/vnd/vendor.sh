#!/bin/bash

prebuild() {
    echo "Pre-build action executed from $ROOTDIR with options $@"
}

build() {
    echo "Build action executed from $ROOTDIR with options $@"
}

postbuild() {
    echo "Post-build action executed from $ROOTDIR with options $@"
}

preclean() {
    echo "Pre-clean action executed from $ROOTDIR with options $@"
}

clean() {
    echo "clean action executed from $ROOTDIR with options $@"
}

postclean() {
    echo "Post-clean action executed from $ROOTDIR with options $@"
}

predocpack() {
    echo "Pre-docpack action executed from $ROOTDIR with options $@"
}

docpack() {
    echo "Documentation packing action executed from $ROOTDIR with options $@"
}

postdocpack() {
    echo "Post-docpack action executed from $ROOTDIR with options $@"
}

predocgenerate() {
    echo "Post-docgenerate action executed from $ROOTDIR with options $@"
}

docgenerate() {
    echo "Documentation generation action executed from $ROOTDIR with options $@"
}

postdocgenerate() {
    echo "Post-docgenerate action executed from $ROOTDIR with options $@"
}

prepackall() {
    echo "Pre-pack action executed from $ROOTDIR with options $@"
}

packall() {
    echo "Pack action executed from $ROOTDIR with options $@"
}

postpackall() {
    echo "Post-pack action executed from $ROOTDIR with options $@"
}

prepushall() {
    echo "Pre-push action executed from $ROOTDIR with options $@"
}

pushall() {
    echo "Push action executed from $ROOTDIR with options $@"
}

postpushall() {
    echo "Post-push action executed from $ROOTDIR with options $@"
}

prelocalize() {
    echo "Pre-localization action executed from $ROOTDIR with options $@"
}

localize() {
    echo "Localization action executed from $ROOTDIR with options $@"
}

postlocalize() {
    echo "Post-localization action executed from $ROOTDIR with options $@"
}

preincrement() {
    echo "Pre-increment action executed from $ROOTDIR with options $@"
}

increment() {
    echo "Increment action executed from $ROOTDIR with options $@"
}

postincrement() {
    echo "Post-increment action executed from $ROOTDIR with options $@"
}
