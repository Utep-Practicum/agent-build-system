# Agent Build System
___

## Github Practices
The following are some of the good practices we should follow so we have a better experience with this project.

* When doing some progress and want to commit, we should commit only when necessary. It is a bad practice to commit for everything. Therefore, every commit should be justified. This is done so we have a better reference and we can track better each code version.
	* **Command for commiting**:
`git commit -am "A brief comment of my work"`


* When we work on a specific feature we should create a new branch so we can track better new code additions. This way someone can easily review any new implementation.
	* **Command for creating a branch**
`git branch branch_name`
	* **Command for deleting a branch**
`git branch -D branch_name`
	* **Command for navigating another branch locally**
`git checkout branch_name`
	* **Command for creating and navigating another branch locally**
`git checkout -b branch_name`


* We should not push to `master`(now called `main`) directly. Since we would be working concurrently we should create a separate branch for any addition. One good practice is to have relevant names for branches. **Example:** `feat/causation_extractor`.


* When pushing to repository, we should push to our branch.
	* **Command for pushing**
`git push origin feat/builder`


* If for some reason we commit and we need to commit again for a little modification, we can reset our previous commit and push to repo with missed modification.
	* **Command for resetting a commit**
`git reset --soft HEAD~`
**Notes:**
 		* Each `~` means 1 commit, we can  go back in time and reset more than one commit. **Example:** `git reset --soft HEAD~~~` (For three commits).
 		* If we had already pushed to repo, we would need to force push the changes since a different version is already in the repo. **Example:** `git push origin feat/builder -f`


* When we consider a new addition is ready to be reviewed, let's create a `Pull Request` so we can review code updates. Once a review is done, we can merge to `main`. **Note:** This should be done in Github interface (Creating a Pull Request).


___
## Impotant Notes
* Every time there is an important step for setting up the project, we should update this readme.me file so we can easily reference.
* New sections should be created in this document when this project is updated and it is merited. For example: `Languages and Frameworks.`
