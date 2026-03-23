def exibir_menu():
    print("\n" + "=" * 40)
    print("   FARMTECH SOLUTIONS - MENU PRINCIPAL   ")
    print("=" * 40)
    print("1. Entrada de dados (Novo Registro)")
    print("2. Saída de dados (Listar Registros)")
    print("3. Atualização de dados (Editar Registro)")
    print("4. Deleção de dados (Remover Registro)")
    print("5. Sair do programa")
    print("=" * 40)

def run():
    import math

    # Nosso vetor principal que armazenará os dados dos plantios
    # Cada registro será um dicionário dentro desta lista
    registros_lavoura = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            print("\n--- Entrada de Dados ---")
            print("Selecione a cultura:")
            print("1. Cana-de-açúcar (Área Retangular)")
            print("2. Milho (Pivô Central Circular)")

            tipo_cultura = input("Opção (1 ou 2): ")

            if tipo_cultura == '1':
                cultura = "Cana-de-açúcar"
                largura = float(input("Digite a largura da área (em metros): "))
                comprimento = float(input("Digite o comprimento da área (em metros): "))
                area_m2 = largura * comprimento

                # Insumo
                kg_por_hectare = float(input("Quantidade de Adubo NPK (kg) por Hectare (10.000 m²): "))
                area_hectares = area_m2 / 10000
                total_insumo = area_hectares * kg_por_hectare
                unidade = "kg"
                nome_insumo = "Adubo NPK"

            elif tipo_cultura == '2':
                cultura = "Milho"
                raio = float(input("Digite o raio do pivô central (em metros): "))
                area_m2 = math.pi * (raio ** 2)

                # Insumo
                litros_por_hectare = float(input("Quantidade de defensivo (Litros) por Hectare (10.000 m²): "))
                area_hectares = area_m2 / 10000
                total_insumo = area_hectares * litros_por_hectare
                unidade = "Litros"
                nome_insumo = "Defensivo Agrícola"

            else:
                print("Opção de cultura inválida! Operação cancelada.")
                continue

            # Salvando os dados no vetor
            novo_dado = {
                "cultura": cultura,
                "area_m2": round(area_m2, 2),
                "insumo": nome_insumo,
                "total_insumo": round(total_insumo, 2),
                "unidade": unidade
            }
            registros_lavoura.append(novo_dado)
            print("-> Dados registrados com sucesso!")

        elif opcao == '2':
            print("\n--- Saída de Dados ---")
            if len(registros_lavoura) == 0:
                print("Nenhum dado registrado ainda.")
            else:
                for i, registro in enumerate(registros_lavoura):
                    print(
                        f"Índice [{i}] | Cultura: {registro['cultura']} | Área: {registro['area_m2']} m² | {registro['insumo']}: {registro['total_insumo']} {registro['unidade']}")

        elif opcao == '3':
            print("\n--- Atualização de Dados ---")
            if len(registros_lavoura) == 0:
                print("Nenhum dado para atualizar.")
                continue

            try:
                indice = int(input("Digite o índice numérico do registro que deseja atualizar (veja na opção 2): "))
                if 0 <= indice < len(registros_lavoura):
                    print(f"Atualizando registro atual: {registros_lavoura[indice]}")

                    # Simplicando a atualização: permitindo reescrever a quantidade do insumo necessário
                    novo_total = float(input(
                        f"Digite a nova quantidade total de {registros_lavoura[indice]['insumo']} (em {registros_lavoura[indice]['unidade']}): "))
                    registros_lavoura[indice]['total_insumo'] = round(novo_total, 2)

                    print("-> Dado atualizado com sucesso!")
                else:
                    print("Índice não encontrado no vetor.")
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

        elif opcao == '4':
            print("\n--- Deleção de Dados ---")
            if len(registros_lavoura) == 0:
                print("Nenhum dado para deletar.")
                continue

            try:
                indice = int(input("Digite o índice numérico do registro que deseja deletar: "))
                if 0 <= indice < len(registros_lavoura):
                    dado_removido = registros_lavoura.pop(indice)  # Removendo do vetor
                    print(f"-> Registro da cultura '{dado_removido['cultura']}' deletado com sucesso!")
                else:
                    print("Índice não encontrado no vetor.")
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

        elif opcao == '5':
            print("\nEncerrando o sistema FarmTech Solutions. Até logo e bom plantio!")
            break

        else:
            print("\nOpção inválida. Por favor, escolha um número de 1 a 5.")


if __name__ == '__main__':
    run()

