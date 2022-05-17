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

echo ""
echo "Run flask on host: ${FLASK_HOST} on port ${FLASK_RUN_PORT}"
echo "Flask App: ${FLASK_APP}"
echo ""
flask run -h $FLASK_HOST

echo "Ready..."
