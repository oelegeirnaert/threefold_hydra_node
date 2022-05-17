echo "Updating WebApp..."

echo ""
echo "Changing directory to: ${REPO_DESTINATION}"
echo ""

cd $REPO_DESTINATION

echo ""
echo "Getting last repo version from ${REPO_URL} ..."
echo ""

git pull

echo ""
echo "Installing requirements..."
echo "From file: ${PIP_REQUIRMENTS_FILE}"
echo ""

pip install -r $PIP_REQUIRMENTS_FILE

echo "Ready..."
