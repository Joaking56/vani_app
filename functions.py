from supabase_client import client

def open_wanted_file():
    response = client.table("wanted").select("item").execute()
    return [row["item"] for row in response.data]

def write_wanted_file(wanted_items):
    client.table("wanted").delete().neq("item", "").execute()
    for item in wanted_items:
        client.table("wanted").insert({"item": item}).execute()

def open_completed_file():
    response = client.table("completed").select("item").execute()
    return [row["item"] for row in response.data]

def write_completed_file(completed_items):
    client.table("completed").delete().neq("item", "").execute()
    for item in completed_items:
        client.table("completed").insert({"item": item}).execute()