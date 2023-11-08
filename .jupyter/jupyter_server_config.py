# Run `jupyter server --generate-config`

# mypy: ignore-errors
c = get_config() # noqa: F821  # pyright: ignore[reportUndefinedVariable]


# Isolate user's workspace from the configs at $HOME
c.SingleUserNotebookApp.root_dir = "work"
c.ServerApp.root_dir = "work"


# Allow the server to serve hidden files
# Displaying hidden files is another thing: "View" -> "Show Hidden Files"
# https://jupyterlab.readthedocs.io/en/latest/user/files.html#displaying-hidden-files
# [NOTE] jupyter-fs requires this setting.
c.ContentsManager.allow_hidden = True

# Enable deleting non-empty directories
c.FileContentsManager.always_delete_dir = True


# Triton LSP
c.LanguageServerManager.language_servers = {
    "triton-lsp": {
    "version": 2,
    "argv": [
        "/srv/conda/envs/notebook/bin/node",
        "/srv/conda/envs/notebook/etc/jupyter/node_modules/.bin/triton-lsp",
        "--stdio"
    ],
    "languages": [
        "bash",
        "sh"
    ],
    "mime_types": [
        "text/x-sh",
        "application/x-sh"
    ],
    "display_name": "triton-lsp"
    }
}
