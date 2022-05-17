import subprocess
import os


def get_git_revision_short_hash() -> str:
    return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode("ascii").strip()


def update_from_git():
    repo_path = os.environ.get("REPO_DESTINATION", "/opt/hydra_threefold/threefold_hydra_node")
    return (
        subprocess.check_output(
            [
                "bash",
                "-c",
                f"{repo_path}/src/update_app.sh",
            ]
        )
        .decode("ascii")
        .strip()
    )
