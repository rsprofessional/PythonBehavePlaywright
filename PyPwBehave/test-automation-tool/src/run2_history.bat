@echo off

REM ===============================
REM Copiar histórico (se existir) do report para o results
REM ===============================
if exist allure-report\history (
    xcopy /E /I /Y allure-report\history allure-results\history
)

REM ===============================
REM Limpar resultados antigos
REM ===============================
del /q allure-results\*.json 2>nul
REM recria o executor.json
echo {^
  "name":"Execução Local",^
  "type":"local",^
  "buildName":"Behave Run"^
} > allure-results\executor.json
del /q allure-results\*.txt 2>nul
del /q allure-results\*.png 2>nul
del /q allure-results\*.html 2>nul

REM ===============================
REM Executar testes features/development.feature
REM ===============================
behave --no-capture  ^
  -f allure_behave.formatter:AllureFormatter ^
  -o allure-results

REM ===============================
REM Gerar report
REM ===============================
allure generate allure-results -o allure-report --clean