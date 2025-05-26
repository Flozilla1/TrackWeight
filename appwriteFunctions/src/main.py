def main(context):
    context.log(context.req.bodyJson)
    return context.res.json({"message": "hello world"})