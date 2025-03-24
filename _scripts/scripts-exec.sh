# First make all scripts executable
chmod +x _scripts/*.sh

# Run scripts in background by adding & at the end
nohup _scripts/chrome-start.sh > /dev/null 2>&1 &