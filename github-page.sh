set -eu

sh build.sh
cp -pR $(pwd)/honkit/_book/* $(pwd)/docs