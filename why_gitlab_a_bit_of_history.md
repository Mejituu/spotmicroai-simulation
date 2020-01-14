A bit of history:

On 14th of January of 2020 we migrated from Github.com to Gitlab based in the following.
Github applied a hard limit of 1GB for big files, and the .step file in the original repo had 68MB, after very short time, all users trying to pull or push to the repo were hitting the 1GB bottle neck, and the repo was basically "lock for use".

The specific error was:
C:\Users\fran\projects\SpotMicroAI>git reset --hard 4164031a883e1bdf3d5df8cc26e2bbc2255d8906
Downloading Hardware/CORE/Assembly.step (68 MB)
Error downloading object: Hardware/CORE/Assembly.step (2b3dff1): Smudge error: Error downloading Hardware/CORE/Assembly.step (2b3dff104839eda26c59a3f31ad103e6830c7998a0120136b575fe20017a6484): batch response: This repository is over its data quota. Account responsible for LFS bandwidth should purchase more data packs to restore access.

Github.com
	Space limitation: 1GB
	Transfer limitation: 1GB x month
	Source: https://help.github.com/en/github/setting-up-and-managing-billing-and-payments-on-github/about-billing-for-git-large-file-storage

Gitlab.com
	Space limitation: 10GB
	Transfer limitation: None
	"Public and private repositories on GitLab.com are unlimited, don't have a transfer limit and they include unlimited collaborators."	
	https://about.gitlab.com/blog/2015/04/08/gitlab-dot-com-storage-limit-raised-to-10gb-per-repo/

Bitbucket.com
	Space limitation: 1Gb soft limit, 2GB hard limit.
	Transfer limitation: 5000 requests per hour, max file size 2GB
	https://confluence.atlassian.com/bitbucket/what-kind-of-limits-do-you-have-on-repository-file-size-273877699.html