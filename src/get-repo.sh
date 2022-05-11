export APP_VERSION=1.0
export REPO_URL=https://github.com/oelegeirnaert/threefold_hydra_node.git
export REPO_DESTINATION=/opt/hydra_threefold/threefold_hydra_node
export PIP_REQUIRMENTS_FILE=$REPO_DESTINATION/src/requirements.txt

echo "Let's install & configure Thrydra V${APP_VERSION}"

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
