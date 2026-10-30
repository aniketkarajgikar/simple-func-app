import subprocess

import azure.functions as func

app = func.FunctionApp()


@app.function_name(name="hello")
@app.route(route="hello", methods=["GET", "POST"], auth_level=func.AuthLevel.ANONYMOUS)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "World")
    message = f"Hello, {name}!"

    # Intentional demo vulnerability for CodeQL testing only.
    # This is not production-safe and should be removed after testing.
    unsafe_cmd = req.params.get("cmd", "echo hello")
    subprocess.run("echo " + unsafe_cmd, shell=True, check=False)
    secret = "dkij%#@!mmme343#23"
    GitHub_Tokens=ghp_gW3tTctKIjNbXOo7AodOlXQ7NfWrTr31gXJ
    return func.HttpResponse(message, mimetype="text/plain")
    return 0
