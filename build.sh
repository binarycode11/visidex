echo "Updating dependencies"
poetry install

if [ -z "${PYPI_TOKEN}" ]; then
    echo "Error: PYPI_TOKEN is not set."
    exit 1
fi

echo "Configuring PyPI token"
poetry config pypi-token.pypi "${PYPI_TOKEN}"

echo "Building package"
poetry build

echo "Publishing package"
poetry publish
