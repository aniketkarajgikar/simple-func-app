import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="hello")
@app.route(route="hello", methods=["GET", "POST"], auth_level=func.AuthLevel.ANONYMOUS)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "World")
    message = f"Hello, {name}!"
    return func.HttpResponse(message, mimetype="text/plain")