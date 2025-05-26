def main(context):
    if context.req.method == "POST":
        return context.res.json({"message": "hello world", "req": context.req})
    else:
        return context.res.json({"error": "Method Not Allowed"}, status_code=405)
