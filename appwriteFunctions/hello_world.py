def main(req, res):
    if req.method == "POST":
        return res.json({"message": "hello world"})
    else:
        return res.json({"error": "Method Not Allowed"}, status_code=405)
