# Determine the user's OS

if [[ "$(uname -s)" == "Linux" ]]; then
    echo "Building for Arch Linux..."
    docker build -f Dockerfile.archLinux -t my-flask-app .
elif [[ "$(uname -s)" == "MINGW"* || "$(uname -s)" == "CYGWIN"* ]]; then
    echo "Building for Windows..."
    docker build -f Dockerfile.Windows -t my-flask-app .
else
    echo "Unsupported OS."
    exit 1
fi
