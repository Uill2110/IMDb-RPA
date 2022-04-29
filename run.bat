@echo off
echo starting...
set argFile=%1
IF EXIST venv\Scripts\activate (
    echo activating virtual environment
    venv\Scripts\activate
    IF errorlevel 1 (
        echo virtual environment not found
        echo creating virtual environment
        python -m venv venv & venv\Scripts\activate
        echo upgrading pip
        python -m pip install --upgrade pip
    )
    echo starting application
    python %argFile%
    
) ELSE (
    echo virtual environment not found
    echo creating virtual environment
    python -m venv venv
    venv\Scripts\activate
    echo upgrading pip
    python -m pip install --upgrade pip
    echo installing libraries
    pip install -r requirements.txt
    IF errorlevel 1 (
        pause
    )
    echo starting application
    python %argFile%
    deactivate
)
@pause
