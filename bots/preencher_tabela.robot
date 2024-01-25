*** Settings ***
Library           RPA.Excel

*** Variables ***
${EXCEL_FILE}     C:/Users/Keven Mota/Desktop/Desafio 2.0/banco de dados/info noticies.xlsx
${SHEET_NAME}     YourSheetName

*** Test Cases ***
Preencher Tabela Excel
    Open Excel    ${EXCEL_FILE}
    Select Worksheet    ${SHEET_NAME}
    
    ${row_data}    Create List    Valor1    Valor2    Valor3    # Substitua pelos seus valores
    Append To List    ${row_data}    NovoValor1    NovoValor2    NovoValor3    # Adicione mais valores se necessário
    
    Append To List    ${row_data}   *** Settings ***
Library           RPA.Excel
Library           OperatingSystem
Library           Collections
Library           JSON

*** Variables ***
${EXCEL_FILE}     C:/Users/Keven Mota/Desktop/Desafio 2.0/banco de dados/info noticies.xlsx
${SHEET_NAME}     YourSheetName
${JSON_FILE}      path/to/your/json/file.json

*** Test Cases ***
Preencher Tabela Excel
    Open Excel    ${EXCEL_FILE}
    Select Worksheet    ${SHEET_NAME}

    ${json_content}    Get File    ${JSON_FILE}
    ${news_list}    Evaluate    json.loads('''${json_content}''')    json

    :FOR    ${news}    IN    @{news_list["noticias"]}
    \    Write Row Values    ${news["data"]}    ${news["title"]}    ${news["author"]}    ${news["description"]}

    Save Excel    ${EXCEL_FILE}
    Close Excel
 # Adicione mais linhas se necessário
    
    Write Row Values    ${row_data}
    
    Save Excel    ${EXCEL_FILE}
    Close Excel
