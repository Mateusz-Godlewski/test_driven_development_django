from selenium import webdriver

geckodriver_path = r"C:\Program Files\Mozilla Firefox\geckodriver.exe"
browser = webdriver.Firefox(executable_path=geckodriver_path)
browser.get("http://localhost:8000")

assert "install" in browser.title