def main(context):
    context.log(context.req.body_json)
    return context.res.json({"message": "hello world"})