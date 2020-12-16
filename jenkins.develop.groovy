def build_app(){
  powershell 'C:/Users/Daija/AppData/Local/Programs/Python/Python39/python.exe -m pip install -r requirements.txt'
}

def test_app(){
  powershell 'C:/Users/Daija/AppData/Local/Programs/Python/Python39/python.exe test_app.py'
}

def down_app(){
  
}

def release_app(){
  echo 'branch into release'
}

def live_app(){
}

return this
