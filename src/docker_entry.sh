echo "** Let's install & configure Thydra V${APP_VERSION} **"

echo ""
echo "Getting Repo from ${REPO_URL} ..."
echo "Saving repository to: ${REPO_DESTINATION}."
echo ""

git clone $REPO_URL $REPO_DESTINATION


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
while true; do sleep 30; done;
