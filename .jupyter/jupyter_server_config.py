# Run `jupyter server --generate-config`

# mypy: ignore-errors
c = get_config() # noqa: F821  # pyright: ignore[reportUndefinedVariable]


# jupyter-fs configs
c.SingleUserNotebookApp.root_dir = "work"
c.SingleUserNotebookApp.contents_manager_class = "jupyterfs.metamanager.MetaManager"
c.SingleUserNotebookApp.jpserver_extensions = {
    "jupyterfs.extension": True
}

c.ServerApp.root_dir = "work"
c.ServerApp.contents_manager_class = "jupyterfs.metamanager.MetaManager"
c.ServerApp.jpserver_extensions = {
    "jupyterfs.extension": True
}


# Enable deleting non-empty directories
c.ContentsManager.allow_hidden = True
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
