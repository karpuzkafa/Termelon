#Copyright 2025 Hasan Agit Ünal

import argparse
from dulwich import porcelain

def git_remote(repo_path, add=False, remove=False, remote_name=None, remote_url=None):
    """Manage remotes for a repository."""
    try:
        repo = porcelain.open_repo(repo_path)
        if add:
            if remote_name and remote_url:
                porcelain.remote_add(repo, remote_name.encode(), remote_url.encode())
                print(f"✅ Remote {remote_name} added with URL {remote_url}")
            else:
                print("❗ Please specify both remote_name and remote_url.")
        elif remove:
            if remote_name:
                porcelain.remote_remove(repo, remote_name.encode())
                print(f"❌ Remote {remote_name} removed.")
            else:
                print("❗ Please specify the remote_name to remove.")
        else:
            remotes = porcelain.remotes(repo)
            print("🔗 Remote repositories:")
            for name, url in remotes:
                print(f"  - {name.decode()}: {url.decode()}")
    except Exception as e:
        print(f"❌ Error: \n{e}")
        

def git_fetch(repo_path):
    """Fetch changes from the remote repository."""
    try:
        repo = porcelain.open_repo(repo_path)
        porcelain.fetch(repo)
        print("🔄 Changes fetched from remote repository.")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_pull(repo_path):
    """Pull changes from the remote repository and merge."""
    try:
        repo = porcelain.open_repo(repo_path)
        porcelain.pull(repo)
        print("📥 Changes pulled and merged from remote repository.")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_merge(repo_path, branch_name):
    """Merge a branch into the current branch."""
    try:
        repo = porcelain.open_repo(repo_path)
        porcelain.merge(repo, branch_name.encode())
        print(f"🔀 Merged branch {branch_name} into current branch.")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_tag(repo_path, tag_name):
    """Tag a commit."""
    try:
        repo = porcelain.open_repo(repo_path)
        porcelain.tag(repo, tag_name)
        print(f"🏷 Tagged with {tag_name}.")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_log(repo_path):
    """Show commit logs."""
    try:
        repo = porcelain.open_repo(repo_path)
        logs = porcelain.log(repo)
        print("📜 Commit Logs:")
        for commit in logs:
            print(f"  💬 {commit.message.decode()} - {commit.committer} on {commit.commit_time}")
    except Exception as e:
        print(f"❌ Error: \n{e}")
        

def git_clone(repo_url, target_dir):
    try:
        print(f"📥 Repository Cloning: {repo_url} → {target_dir} ...")
        porcelain.clone(repo_url, target_dir)
        print(f"✅ Repository Cloned: {target_dir}")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_commit(repo_path, message):
    try:
        repo = porcelain.open_repo(repo_path)
        porcelain.add(repo, ".")
        porcelain.commit(repo, message.encode("utf-8"))
        print(f"📌 Committed: {message}")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_remove(repo_path, file_path, keep_local):
    try:
        repo = porcelain.open_repo(repo_path)
        if keep_local:
            porcelain.rm(repo, [file_path], cached=True)
            print(f"🗑 {file_path} Removed from Repository (Kept Locally)")
        else:
            porcelain.rm(repo, [file_path])
            print(f"🗑 {file_path} Removed from Local && Repository")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_status(repo_path):
    try:
        repo = porcelain.open_repo(repo_path)
        status = porcelain.status(repo)
        print("🔍 Changes:")
        for file in status.staged["add"]:
            print(f"  ➕ Added: {file}")
        for file in status.staged["modify"]:
            print(f"  ✏️  Modified: {file}")
        for file in status.staged["delete"]:
            print(f"  ❌ Deleted: {file}")
        print("\n🚀 Untracked files:")
        for file in status.untracked:
            print(f"  🆕 {file}")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_branch(repo_path, list_branches=False, create=None, delete=None):
    try:
        repo = porcelain.open_repo(repo_path)
        if list_branches:
            branches = porcelain.branch_list(repo)
            print("🌿 Branches:")
            for branch in branches:
                print(f"  - {branch.decode()}")
        elif create:
            porcelain.branch_create(repo, create)
            print(f"✅ Branch Created: {create}")
        elif delete:
            porcelain.branch_delete(repo, delete)
            print(f"❌ Branch Deleted: {delete}")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_init(repo_path):
    try:
        porcelain.init(repo_path)
        print(f"✅ Repository Initialized: {repo_path}")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_add(repo_path, file_path):
    try:
        repo = porcelain.open_repo(repo_path)
        porcelain.add(repo, file_path)
        print(f"✅ Staged: {file_path}")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_checkout(repo_path, branch_name, create_new=False):
    """Switch to another branch or create a new one."""
    try:
        repo = porcelain.open_repo(repo_path)
        if create_new:
            porcelain.branch_create(repo, branch_name)
            print(f"🌿 Created and switched to new branch: {branch_name}")
        repo.refs.set_symbolic_ref(b"HEAD", f"refs/heads/{branch_name}".encode())
        print(f"🔀 Switched to branch: {branch_name}")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_reset(repo_path, hard=False, soft=False):
    try:
        repo = porcelain.open_repo(repo_path)
        if hard:
            porcelain.reset(repo, mode="hard")
            print("⏪ Hard reset performed.")
        elif soft:
            porcelain.reset(repo, mode="soft")
            print("⏪ Soft reset performed.")
        else:
            print("❗ Please specify either --hard or --soft.")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_revert(repo_path, commit_hash, no_commit=False):
    """Revert a specific commit."""
    try:
        repo = porcelain.open_repo(repo_path)
        porcelain.revert(repo, commit_hash.encode(), no_commit=no_commit)
        if no_commit:
            print(f"🔄 Commit {commit_hash} reverted but not committed.")
        else:
            print(f"🔄 Commit {commit_hash} reverted and committed.")
    except Exception as e:
        print(f"❌ Error: \n{e}")

def git_push(repo_path, remote_name="origin", branch_name="master"):
    """Push changes to a remote repository."""
    try:
        repo = porcelain.open_repo(repo_path)
        # Push the current branch to the remote
        porcelain.push(repo, remote_name, branch_name)
        print(f"🚀 Pushed changes to {remote_name}/{branch_name}")
    except Exception as e:
        print(f"❌ Error: \n{e}")
        
def show_examples():
    examples = """
📌 Examples:
  # Clone a repository from a remote URL
  # git clone <repo_url> <target_dir>
  tgit clone https://github.com/user/repo.git my_repo
  
  # Add a remote repository
  # git remote --add <remote_name> <remote_url>
  tgit remote my_repo --add -n origin -u https://github.com/user/repo.git

  # Remove a remote repository
  # git remote --remove <remote_name>
  tgit remote my_repo --remove -n origin

  # Show the remotes of a repository
  # git remote
  tgit remote my_repo
  
  # Commit changes with a message
  # git commit -m <message>
  tgit commit my_repo -m "first commit"
  
  # Remove a file from the repository (keep it locally if --keep-local is used)
  # git rm <file_path>
  tgit rm my_repo file.py
  
  # Show the current status of the repository (added, modified, deleted files)
  # git status
  tgit status my_repo
  
  # Create a new branch in the repository
  # git branch <branch_name>
  tgit branch-create my_repo my-branch
  
  # Delete a branch from the repository
  # git branch -d <branch_name>
  tgit branch-delete my_repo my-branch
  
  # Initialize a new repository
  # git init
  tgit init my_repo
  
  # Stage a file for commit
  # git add <file_path>
  tgit add my_repo file.py
  
  # Switch to another branch (or create a new branch with --create)
  # git switch <branch_name> or git checkout -b <branch_name>
  tgit checkout my_repo my-branch
  
  # Reset the repository to the last commit (use --hard for a hard reset)
  # git reset --hard
  tgit reset my_repo --hard
  
  # Revert a specific commit by its hash
  # git revert <commit_hash>
  tgit revert my_repo commit_hash
  
  # Push changes to the remote repository
  # git push
  tgit push my_repo
  
  # Fetch updates from the remote repository
  # git fetch
  tgit fetch my_repo
  
  # Pull updates from the remote repository
  # git pull
  tgit pull my_repo
  
  # Merge a branch into the current branch
  # git merge <branch_name>
  tgit merge my_repo my-branch
  
  # Create a new tag for a specific commit
  # git tag <tag_name> <commit_hash>
  tgit tag my_repo commit_hash v1.0
  
  # Show the commit history in a compact format
  # git log --oneline
  tgit log my_repo --oneline
    """
    print(examples)

def main():
    parser = argparse.ArgumentParser(
        description="🔧 Tgit | Termelon Git Tool: A Git Tool For Pydroid3",
        epilog="""
  """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "--examples", 
        action="store_true", 
        help="Show command examples"
    )
    

    subparsers = parser.add_subparsers(dest="command", metavar="")

    clone_parser = subparsers.add_parser("clone", help="📥 Clone Repository")
    clone_parser.add_argument("repo_url", type=str, help="🔗 Repository URL")
    clone_parser.add_argument("target_dir", type=str, help="📂 Target directory")

    commit_parser = subparsers.add_parser("commit", help="📌 Commit Changes")
    commit_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    commit_parser.add_argument("-m", "--message", type=str, required=True, help="✏️ Commit message")

    # Remote
    remote_parser = subparsers.add_parser("remote", help="🔗 Manage Remote Repositories")
    remote_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    remote_parser.add_argument("--add", action="store_true", help="📥 Add a remote")
    remote_parser.add_argument("--remove", action="store_true", help="🗑 Remove a remote")
    remote_parser.add_argument("-n", "--name", type=str, help="🔗 Remote name")
    remote_parser.add_argument("-u", "--url", type=str, help="🔗 Remote URL")

    push_parser = subparsers.add_parser("push", help="🚀 Push changes to remote repository")
    push_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    push_parser.add_argument("-r", "--remote", type=str, default="origin", help="🔗 Remote name (default: origin)")
    push_parser.add_argument("-b", "--branch", type=str, default="master", help="🌿 Branch name (default: master)")

    remove_parser = subparsers.add_parser("rm", help="🗑 Remove File")
    remove_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    remove_parser.add_argument("file_path", type=str, help="🗑 File to remove")
    remove_parser.add_argument("--keep-local", action="store_true", help="📌 Keep file locally")

    status_parser = subparsers.add_parser("status", help="🔍 Show Status")
    status_parser.add_argument("repo_path", type=str, help="📂 Repository path")

    branch_parser = subparsers.add_parser("branch", help="🌿 Manage branches")
    branch_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    branch_parser.add_argument("--list", action="store_true", help="📜 List branches")
    branch_parser.add_argument("--create", type=str, help="🌱 Create new branch")
    branch_parser.add_argument("--delete", type=str, help="🗑 Delete branch")

    init_parser = subparsers.add_parser("init", help="📂 Initialize a new repository")
    init_parser.add_argument("repo_path", type=str, help="📂 Repository path")

    add_parser = subparsers.add_parser("add", help="➕ Stage files for commit")
    add_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    add_parser.add_argument("file_path", type=str, help="📄 File to stage")

    checkout_parser = subparsers.add_parser("checkout", help="🔀 Switch branches")
    checkout_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    checkout_parser.add_argument("branch_name", type=str, help="🌿 Branch name")
    checkout_parser.add_argument("--create", action="store_true", help="🌱 Create new branch")

    reset_parser = subparsers.add_parser("reset", help="⏪ Reset repository")
    reset_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    reset_parser.add_argument("--hard", action="store_true", help="🔥 Hard reset")
    reset_parser.add_argument("--soft", action="store_true", help="📌 Soft reset")

    revert_parser = subparsers.add_parser("revert", help="🔄 Revert a commit")
    revert_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    revert_parser.add_argument("commit_hash", type=str, help="🔢 Commit hash to revert")
    revert_parser.add_argument("--no-commit", action="store_true", help="Do not automatically commit revert")
    
    # Fetch
    fetch_parser = subparsers.add_parser("fetch", help="📥 Fetch Changes from Remote Repository")
    fetch_parser.add_argument("repo_path", type=str, help="📂 Repository path")

    # Pull
    pull_parser = subparsers.add_parser("pull", help="⬇️ Pull Changes from Remote and Merge")
    pull_parser.add_argument("repo_path", type=str, help="📂 Repository path")

    # Merge
    merge_parser = subparsers.add_parser("merge", help="🔀 Merge a Branch into Current Branch")
    merge_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    merge_parser.add_argument("branch_name", type=str, help="🌿 Branch name to merge")

    # Tag
    tag_parser = subparsers.add_parser("tag", help="🏷 Tag a Commit")
    tag_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    tag_parser.add_argument("commit_hash", type=str, help="🔢 Commit hash to tag")
    tag_parser.add_argument("tag_name", type=str, help="🏷 Tag name")

    # Log
    log_parser = subparsers.add_parser("log", help="📜 Show Commit History")
    log_parser.add_argument("repo_path", type=str, help="📂 Repository path")
    log_parser.add_argument("--oneline", action="store_true", help="Show commit history in a single line")
    
    
    
    
    args = parser.parse_args()
    
    
    if args.examples:
        show_examples()
    elif not args.command:
        parser.print_help()
    elif args.command == "clone":
        git_clone(args.repo_url, args.target_dir)
    elif args.command == "commit":
        git_commit(args.repo_path, args.message)
    elif args.command == "rm":
        git_remove(args.repo_path, args.file_path, args.keep_local)
    elif args.command == "status":
        git_status(args.repo_path)
    elif args.command == "branch":
        git_branch(args.repo_path, args.list, args.create, args.delete)
    elif args.command == "init":
        git_init(args.repo_path)
    elif args.command == "add":
        git_add(args.repo_path, args.file_path)
    elif args.command == "checkout":
        git_checkout(args.repo_path, args.branch_name, args.create)
    elif args.command == "reset":
        git_reset(args.repo_path, args.hard)
    elif args.command == "revert":
        git_revert(args.repo_path, args.commit_hash)
    elif args.command == "push":
        git_push(args.repo_path, args.remote, args.branch)
    elif args.command == "fetch":
        git_fetch(args.repo_path)
    elif args.command == "pull":
        git_pull(args.repo_path)
    elif args.command == "merge":
        git_merge(args.repo_path, args.branch_name)
    elif args.command == "tag":
        git_tag(args.repo_path, args.commit_hash, args.tag_name)
    elif args.command == "log":
        git_log(args.repo_path, args.oneline)
    elif args.command == "remote":
        git_remote(args.repo_path, args.add, args.remove, args.name, args.url)
    
if __name__ == "__main__":
    main()
