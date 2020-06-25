#!/usr/bin/env bash


exmp = (curl -X POST "$1" -H "accept: */*" -H "Content-Type: application/json" -d "$2" | tr -d \")
def extract_uuid = new JsonSlurper().parseText(exmp).uuid
echo extract_uuid


