@ECHO OFF
SET text_value=%1
Set output_folder=%2
Set output_file=%3
if "%~1"=="" (
echo "Invalid input"
pause
exit 0
)
if "%~2"=="" (
echo "Invalid input"
pause
exit 0
)
if "%~3"=="" (
echo "Invalid input"
pause
exit 0
)
IF EXIST %output_folder% (
GOTO AFTERDIRECTORY
)
MKDIR %output_folder%
:AFTERDIRECTORY
CD %output_folder%
attrib -r %output_file%
ECHO %text_value% > %output_file%
attrib +r %output_file%
CD..