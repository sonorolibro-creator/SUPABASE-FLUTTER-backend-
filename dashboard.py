from database import supabase

def get_dashboard(cliente_rfc: str, year: int, month: int | None):

    params = {
        "p_rfc": cliente_rfc,
        "p_year": year,
        "p_month": month
    }

    res = supabase.rpc("dashboard_cfdi", params).execute()

    return res.data

