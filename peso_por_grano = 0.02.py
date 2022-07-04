peso_por_grano = 0.02
padding = {
    "casilla": 2,
    "unit": 20,
    "weight": 25
}
msg = {
    "unit": "granos",
    "weight": "gramos",
    "t_weight": "toneladas",
}


def build_box(content=None):
    table = "┌────┬─────────────────────┬───────────────────────────┐\n"
    table += f'|  # | {str(msg["unit"]).center(padding["unit"])}'
    table += f'| {str(msg["weight"]).center(padding["weight"])} |\n'
    table += "├────┼─────────────────────┼───────────────────────────┤\n"
    if content:
        table += content
    table += "└────┴─────────────────────┴───────────────────────────┘"

    return table


def build_content():
    granos_contabilizados = 0
    content = ""

    for exponente in range(64):
        granos_por_casilla = 2 ** exponente
        peso_por_casilla = peso_por_grano * granos_por_casilla

        ui_exponente = str(exponente).ljust(padding["casilla"])
        ui_granos_por_casilla = str(granos_por_casilla).center(padding["unit"])
        ui_peso_por_casilla = str(peso_por_casilla).center(padding["weight"])

        content += f"│ {ui_exponente} "
        content += f"│ {ui_granos_por_casilla}"
        content += f"│ {ui_peso_por_casilla} │"

        content += "\n"

    granos_contabilizados = granos_contabilizados + granos_por_casilla

    result = {
        "total_number": granos_contabilizados,
        "total_weight": peso_por_grano * granos_contabilizados,
        "content": content
    }

    return result


data = build_content()

print(build_box())
print(f"  {data['content'] }")
print(f"  · Granos totales: {data['total_number']}")
print(f"  · Peso total = {data['total_weight'] / 1000000} { msg['t_weight'] }")