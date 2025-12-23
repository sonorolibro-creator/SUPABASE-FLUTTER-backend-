from database import supabase

def get_dashboard(cliente_rfc: str, year: int, month: int | None):

    if month:
        start = f"{year}-{month:02d}-01"
        end = f"{year}-{month:02d}-31"
    else:
        start = f"{year}-01-01"
        end = f"{year}-12-31"

    def count(filters: dict):
        query = (
            supabase
            .from_("cfdi_xml")
            .select("id", count="exact")
            .gte("fecha", start)
            .lte("fecha", end)
        )

        for k, v in filters.items():
            query = query.eq(k, v)

        return query.execute().count

    def count_by_tipo(rfc_column):
        res = (
            supabase
            .from_("cfdi_xml")
            .select("tipo_cfdi, estado_sat")
            .eq(rfc_column, cliente_rfc)
            .gte("fecha", start)
            .lte("fecha", end)
            .execute()
        )

        output = {}

        for row in res.data:
            tipo = row["tipo_cfdi"] or "SIN_TIPO"
            estado = row["estado_sat"] or "DESCONOCIDO"

            output.setdefault(tipo, {"VIGENTE": 0, "CANCELADO": 0})
            output[tipo][estado] += 1

        return output

    return {
        "emitidos": {
            "total": count({"rfc_emisor": cliente_rfc}),
            "vigentes": count({
                "rfc_emisor": cliente_rfc,
                "estado_sat": "VIGENTE"
            }),
            "cancelados": count({
                "rfc_emisor": cliente_rfc,
                "estado_sat": "CANCELADO"
            }),
            "por_tipo": count_by_tipo("rfc_emisor")
        },
        "recibidos": {
            "total": count({"rfc_receptor": cliente_rfc}),
            "vigentes": count({
                "rfc_receptor": cliente_rfc,
                "estado_sat": "VIGENTE"
            }),
            "cancelados": count({
                "rfc_receptor": cliente_rfc,
                "estado_sat": "CANCELADO"
            }),
            "por_tipo": count_by_tipo("rfc_receptor")
        }
    }
