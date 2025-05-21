#!/bin/bash

# Set the shared repository URL
SHARED_REPO="https://github.com/clorbiecke/UI_Kit.git"  # Replace with actual repository URL
SHARED_PREFIX="shared_code"

echo "Updating shared code from repository..."

# Pull updates from the shared repository
git subtree pull --prefix=$SHARED_PREFIX $SHARED_REPO main --squash
echo "Pulled latest changes."

# # Check if there are changes to commit
# if git status --porcelain | grep "$SHARED_PREFIX"; then
#     echo "Changes detected in shared code. Committing..."
    
#     # Add changes and commit
#     git add $SHARED_PREFIX
#     git commit -m "Updated shared code"
    
#     # Push changes back to the shared repository
#     echo "Pushing changes to shared repository..."
#     git subtree push --prefix=$SHARED_PREFIX $SHARED_REPO main
#     echo "Push completed!"
# else
#     echo "No changes to push."
# fi
