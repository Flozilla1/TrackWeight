def main(context):
    try:
        context.log(context.req.body_json)
        return context.res.json({"message": "hello world"})
    except Exception as error:
        return context.res.json({"errorType": type(error).__name__,"error": error})