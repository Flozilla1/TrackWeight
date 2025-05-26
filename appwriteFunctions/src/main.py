def main(context):
    return context.res.json({"message": "hello world", "req": context.req})