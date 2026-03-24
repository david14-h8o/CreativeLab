from router import route_query

def handle_query(user_input: str) -> str:
    try:
        return route_query(user_input)
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
