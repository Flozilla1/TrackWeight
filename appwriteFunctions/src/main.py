def main(context):
    context.log(context.req)
    return context.res.json({"message": "hello world"})