#!/usr/bin/python3
# qubes-task-gui.py
import os

unman_key_content = """-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: SKS 1.1.6
Comment: Hostname: pgp.mit.edu

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
1OSQxcOZiBnE0amRjD1rIHLuVDwd4ctJQW4=
=QpWg
-----END PGP PUBLIC KEY BLOCK-----
"""

tasks_repo_content = """[3isec-dom0-current]
name = 3isec Qubes Dom0 Repository (updates)
baseurl = https://qubes.3isec.org/rpm/r$releasever/current/dom0/fc32
skip_if_unavailable=False
enabled = 1
metadata_expire = 6h
gpgcheck = 1
gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-unman"""

templates_repo_content = """[3isec-templates]
name = 3isec Qubes Templates Repository (updates)
baseurl = https://qubes.3isec.org/rpm/r$releasever/templates
skip_if_unavailable = False
enabled = 1
metadata_expire = 6h
gpgcheck = 1
gpgkey = file:////etc/qubes/repo-templates/keys/RPM-GPG-KEY-unman"""

tasks_repo_path = "/etc/yum.repos.d/3isec-dom0.repo"
templates_repo_path = "/etc/qubes/repo-templates/3isec-templates.repo"
tasks_key_path = "/etc/pki/rpm-gpg/RPM-GPG-KEY-unman"
templates_key_path = "/etc/qubes/repo-templates/keys/RPM-GPG-KEY-unman"

task_instructions = """

            [3isec-dom0-current]
            name = 3isec Qubes Dom0 Repository (updates)
            baseurl = https://qubes.3isec.org/rpm/r$releasever/current/dom0/fc32
            skip_if_unavailable=False
            enabled = 1
            metadata_expire = 6h
            gpgcheck = 1
            gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-unman

            Create a file in dom0 with this content at /etc/yum.repos.d/3isec-dom0.repo

            All packages are signed with my Qubes OS Signing key.
            You'll need to get this from a keyserver, or two, to make sure all is fine:
            keyserver.ubuntu.com or pgp.mit.edu

            You can also check the Qubes users mailing list or look on github.

            Once you have copies of the key, check the fingerprint:

            gpg -n --import --import-options import-show unman.pub

            replacing unman.pub with the path to the key.
            The output should look similar to this:

            pub   rsa4096 2016-06-25 [SC]
                  4B1F 400D F256 51B5 3C41  41B3 8B3F 30F9 C8C0 C2EF
            uid           [ unknown] unman (Qubes OS signing key) 
            sub   rsa4096 2016-06-27 [S] [expires: 2024-06-30]
            sub   rsa4096 2016-06-25 [E]

            In particular, check that the output from your command contains the fingerprint 4B1F 400D F256 51B5 3C41 41B3 8B3F 30F9 C8C0 C2EF

            When you are happy, copy the key in to dom0:

            qvm-run -p QUBE_WHERE_YOU_DOWNLOADED_KEY 'cat PATH_TO_KEY' > RPM-GPG-KEY-unman
            sudo mv RPM-GPG-KEY-unman /etc/pki/rpm-gpg/
            """

templates_instructions = """

             All templates are signed with my Qubes OS Signing key:

             pub   rsa4096 2016-06-25 [SC]
                   4B1F 400D F256 51B5 3C41  41B3 8B3F 30F9 C8C0 C2EF
             uid           [ unknown] unman (Qubes OS signing key) 
             sub   rsa4096 2016-06-27 [S] [expires: 2024-06-30]
             sub   rsa4096 2016-06-25 [E]
             
             
             You can read about how to get a copy of the key, and how to validate it here.
             You will need to copy the key in to dom0:
             qvm-run -p qube 'cat PATH_TO_KEY ' > RPM-GPG-KEY-unman
             and then move it into place:
             sudo mv RPM-GPG-KEY-unman /etc/pki/rpm-gpg/RPM-GPG-KEY-unman
             
             Download the template you want to use, and copy it into dom0:
             qvm-run -p QUBE 'cat PATH_TO_DOWNLOADED_TEMPLATE ' > TEMPLATE_PACKAGE_NAME
             replacing TEMPLATE_PACKAGE_NAME with a name of your choice.
             Then check the signature by (e.g):
             rpm -K TEMPLATE_PACKAGE_NAME
             
             Install the template using qvm-template:
             qvm-template install --keyring /etc/pki/rpm-gpg/RPM-GPG-KEY-unman FULL_PATH_TO_DOWNLOADED_TEMPLATE 
             """


class RepoInstallation:
    def __init__(self, reponame, instructions, key_path, key_content, repo_path, repo_content):
        self.reponame = reponame
        self.instructions = instructions
        self.key_path = key_path
        self.key_content = key_content
        self.repo_path = repo_path
        self.repo_content = repo_content

    def is_installed(self):
        return os.path.isfile(self.key_path) and os.path.isfile(self.repo_path)

    def get_script(self):
        command = f"""
_3isec_repo_path = "{self.repo_path}"
_3isec_repo = \"""{self.repo_content}\"""
with open(_3isec_repo_path, "w") as f:
    f.write(_3isec_repo)

unman_public_key_path = "{self.key_path}"
unman_public_key = \"""{self.key_content}\"""
with open(unman_public_key_path, "w") as f:
    f.write(unman_public_key)

print("I3SEC_REPO_INSTALLED")
"""
        return command


tasks_repo = RepoInstallation(
    "tasks",
    task_instructions,
    tasks_key_path,
    unman_key_content,
    tasks_repo_path,
    tasks_repo_content)

templates_repo = RepoInstallation(
    "templates",
    templates_instructions,
    templates_key_path,
    unman_key_content,
    templates_repo_path,
    templates_repo_content)
