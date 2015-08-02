if __name__ == "__main__":
    import subprocess
    cmd_api = "sphinx-apidoc -f -o docs/apis project_doc_sample"
    cmd_doc = "sphinx-build -b html docs/ docs/_build"
    
    for cmd in [cmd_api, cmd_doc]:
        result = subprocess.check_output(cmd, universal_newlines=True)
        print(result)
