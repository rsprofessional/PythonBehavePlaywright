del /q allure-results\*.json
del /q allure-results\*.txt
del /q allure-results\*.png
del /q allure-results\*.html
rmdir /s /q allure-report

timeout /t 5 /nobreak >nul

@REM behave -t @smoke --no-capture -f allure_behave.formatter:AllureFormatter -o allure-results
behave --no-capture features/development.feature -f allure_behave.formatter:AllureFormatter -o allure-results
allure generate allure-results -o allure-report --clean








