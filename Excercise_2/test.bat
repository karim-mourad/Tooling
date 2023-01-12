
@ECHO OFF
SETLOCAL EnableDelayedExpansion
set inf= %~1
set tf= "Text Files"
set sf= "Source Files"
set hf= "Header Files"
if not exist %tf% ( mkdir %tf% )
if not exist %sf% ( mkdir %sf% )
if not exist %hf% ( mkdir %hf% )
for /f "tokens=1-4 delims= " %%a in (%inf%) do (
if not exist %%a (
mkdir %%a
)
cd %%a
if not exist %%b (
echo 0 >%%b
) else (
SET /P count=<%%b
SET /A count=count+1
ECHO !count! > %%b
)
if not exist %%c (
echo 0 >%%c
) else (
SET /P count=<%%c
SET /A count=count+1
ECHO !count! > %%c
)
if not exist %%d (
echo 0 >%%d
) else (
SET /P count=<%%d
SET /A count=count+1
ECHO !count! > %%d
)
cd ..
COPY /Y %%a\*.txt %tf% >NUL
COPY /Y %%a\*.c %sf% >NUL
COPY /Y %%a\*.h %hf% >NUL
)